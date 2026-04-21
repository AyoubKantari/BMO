"""
animation.py — BMO Gesichts-Animation
Erzeugt Frames pro Zustand und übergibt sie an eine Display-Funktion.
"""

import time
from PIL import Image
from bmo.gesicht import gesicht_erstellen

FPS = 12


def tick(zustand: str, frame_nr: int) -> Image.Image:
    """Berechnet den aktuellen Frame basierend auf Zustand und Frame-Nummer."""
    blinzeln   = _soll_blinzeln(frame_nr)
    mund_offen = _mund_offen(frame_nr)
    return gesicht_erstellen(zustand, mund_offen=mund_offen, blinzeln=blinzeln)


def loop(get_zustand, display_fn) -> None:
    """
    Hauptloop — läuft bis KeyboardInterrupt.
    get_zustand: Funktion die den aktuellen Zustand zurückgibt
    display_fn:  Funktion die ein PIL-Image ans Display schickt
    """
    frame_nr  = 0
    intervall = 1.0 / FPS

    while True:
        start   = time.monotonic()
        zustand = get_zustand()
        bild    = tick(zustand, frame_nr)
        display_fn(bild)
        frame_nr += 1

        vergangen = time.monotonic() - start
        restzeit  = intervall - vergangen
        if restzeit > 0:
            time.sleep(restzeit)


# ─────────────────────────────────────────────
# Interne Animationslogik
# ─────────────────────────────────────────────

def _soll_blinzeln(frame_nr: int) -> bool:
    """Alle 3 Sekunden für 2 Frames blinzeln."""
    return (frame_nr % (FPS * 3)) < 2


def _mund_offen(frame_nr: int) -> bool:
    """Mund wechselt alle 3 Frames offen/zu (für spricht-Zustand)."""
    return (frame_nr // 3) % 2 == 0


# ─────────────────────────────────────────────
# PC-Test mit tkinter Fenster
# ─────────────────────────────────────────────

if __name__ == "__main__":
    import tkinter as tk
    from PIL import ImageTk

    ZUSTAENDE     = ["idle", "happy", "denkt", "spricht"]
    zustand_index = [0]
    frame_nr      = [0]

    root  = tk.Tk()
    root.title("BMO Animation Test")
    label = tk.Label(root)
    label.pack()
    info  = tk.Label(root, text="Zustand: idle  |  Leertaste = wechseln")
    info.pack()

    def naechster_frame():
        zustand = ZUSTAENDE[zustand_index[0]]
        bild    = tick(zustand, frame_nr[0])
        photo   = ImageTk.PhotoImage(bild)
        label.config(image=photo)
        label.image = photo
        frame_nr[0] += 1
        root.after(int(1000 / FPS), naechster_frame)

    def zustand_wechseln(event):
        zustand_index[0] = (zustand_index[0] + 1) % len(ZUSTAENDE)
        info.config(text=f"Zustand: {ZUSTAENDE[zustand_index[0]]}  |  Leertaste = wechseln")

    root.bind("<space>", zustand_wechseln)
    naechster_frame()
    root.mainloop()
