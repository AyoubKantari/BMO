from gpiozero import Button
from bmo.stimmung import Zustand

BUTTON_A_PIN = 17
BUTTON_B_PIN = 27

# Globale Referenzen halten — sonst wird Garbage Collection ausgeloest
_btn_a = None
_btn_b = None


def setup(stimmung):
    global _btn_a, _btn_b
    # pull_up=False weil 10kOhm Pull-down Widerstand verbaut ist
    _btn_a = Button(BUTTON_A_PIN, pull_up=False, bounce_time=0.2)
    _btn_b = Button(BUTTON_B_PIN, pull_up=False, bounce_time=0.2)

    _btn_a.when_pressed = lambda: stimmung.wechsle(Zustand.DENKT)
    _btn_b.when_pressed = lambda: stimmung.unterbrechen()


def cleanup():
    global _btn_a, _btn_b
    if _btn_a:
        _btn_a.close()
    if _btn_b:
        _btn_b.close()
    _btn_a = None
    _btn_b = None
