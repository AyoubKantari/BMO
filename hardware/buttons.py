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

    GPIO.setup(BUTTON_A, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUTTON_B, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(BUTTON_A, GPIO.RISING, callback=lambda x: stimmung.wechsle(Zustand.DENKT), bouncetime=200)
    GPIO.add_event_detect(BUTTON_B, GPIO.RISING, callback=lambda x: stimmung.unterbrechen(), bouncetime=200)


def cleanup():
    GPIO.cleanup()
