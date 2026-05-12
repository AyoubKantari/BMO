import threading
import speech_recognition as sr
import pyttsx3
from hardware.display import Display
from hardware.buttons import setup, cleanup
from bmo.gesicht import gesicht_erstellen
from bmo.stimmung import Stimmung, Zustand
from ki.claude_client import ClaudeClient


def sprich(text: str) -> threading.Thread:
    # Eigene Engine pro Aufruf — umgeht den pyttsx3-Bug, dass runAndWait nur einmal funktioniert
    def _sprechen():
        engine = pyttsx3.init()
        for stimme in engine.getProperty("voices"):
            if "german" in stimme.name.lower() or "de" in stimme.id.lower():
                engine.setProperty("voice", stimme.id)
                break
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)
        engine.say(text)
        engine.runAndWait()
        engine.stop()

    thread = threading.Thread(target=_sprechen, daemon=True)
    thread.start()
    return thread


def main():
    bmo      = Stimmung()
    display  = Display()
    claude   = ClaudeClient()
    mikrofon = sr.Recognizer()

    setup(bmo)

    try:
        while display.events_verarbeiten(bmo):
            zustand = bmo.get_zustand()

            if zustand == Zustand.IDLE:
                display.zeige(gesicht_erstellen("idle"))

            elif zustand == Zustand.DENKT:
                display.zeige(gesicht_erstellen("denkt"))

                text = ""
                try:
                    with sr.Microphone() as quelle:
                        print("[BMO] Ich höre zu...")
                        mikrofon.adjust_for_ambient_noise(quelle, duration=0.5)
                        audio = mikrofon.listen(quelle, timeout=5, phrase_time_limit=8)
                    text = mikrofon.recognize_google(audio, language="de-DE")
                    print(f"[Du] {text}")
                except sr.WaitTimeoutError:
                    print("[BMO] Nichts gehört — zurück zu IDLE")
                except sr.UnknownValueError:
                    print("[BMO] Sprache nicht erkannt")
                except Exception as e:
                    print(f"[Fehler] {e}")

                if text:
                    antwort = claude.sende(text)
                    if antwort:
                        print(f"[BMO] {antwort}")
                        bmo.wechsle(Zustand.SPRICHT)
                        display.zeige(gesicht_erstellen("spricht"))
                        sprich(antwort).join()

                bmo.wechsle(Zustand.IDLE)

    except KeyboardInterrupt:
        pass
    finally:
        cleanup()
        display.schliessen()


if __name__ == "__main__":
    main()
