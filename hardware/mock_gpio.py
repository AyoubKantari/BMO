BCM = "BCM"
IN = "IN"
OUT = "OUT"
RISING = "RISING"
FALLING = "FALLING"
BOTH = "BOTH"


def setmode(mode):
    print(f"[Mock GPIO] setmode: {mode}")


def setup(pin, mode):
    print(f"[Mock GPIO] setup Pin {pin} als {mode}")


def input(pin):
    return 0


def add_event_detect(pin, trigger, callback=None):
    print(f"[Mock GPIO] Interrupt registriert auf Pin {pin} ({trigger})")


def cleanup():
    print("[Mock GPIO] cleanup")
