try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    import hardware.mock_gpio as GPIO
from bmo.stimmung import Zustand

# Pin-Nummern
BUTTON_A = 17
BUTTON_B = 27


def setup(stimmung):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(BUTTON_A, GPIO.IN)
    GPIO.setup(BUTTON_B, GPIO.IN)

    GPIO.add_event_detect(BUTTON_A, GPIO.RISING, callback=lambda x: stimmung.wechsle(Zustand.DENKT))
    GPIO.add_event_detect(BUTTON_B, GPIO.RISING, callback=lambda x: stimmung.unterbrechen())


def cleanup():
    GPIO.cleanup()
