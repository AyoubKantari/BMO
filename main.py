from bmo.stimmung import Stimmung, Zustand
from bmo.gesicht import zeichne_gesicht
from hardware.buttons import setup, cleanup


def main():
    bmo = Stimmung()
    setup(bmo)

    try:
        while True:
            zustand = bmo.get_zustand()

            if zustand == Zustand.IDLE:
                zeichne_gesicht("idle")

            elif zustand == Zustand.DENKT:
                zeichne_gesicht("denkt")
                # TODO: Claude API aufrufen
                # TODO: Antwort an TTS weitergeben
                bmo.wechsle(Zustand.SPRICHT)

            elif zustand == Zustand.SPRICHT:
                zeichne_gesicht("spricht")
                # TODO: TTS abspielen
                bmo.wechsle(Zustand.IDLE)

    except KeyboardInterrupt:
        cleanup()


if __name__ == "__main__":
    main()
