import board
import digitalio
from adafruit_rgb_display import ili9341
from PIL import Image

BREITE = 320
HOEHE  = 240


class Display:
    def __init__(self):
        cs_pin    = digitalio.DigitalInOut(board.CE0)   # GPIO8  (Pin 24)
        dc_pin    = digitalio.DigitalInOut(board.D24)   # GPIO24 (Pin 18)
        reset_pin = digitalio.DigitalInOut(board.D25)   # GPIO25 (Pin 22)

        spi = board.SPI()
        self._display = ili9341.ILI9341(
            spi,
            rotation=270,        # Querformat 320x240
            cs=cs_pin,
            dc=dc_pin,
            rst=reset_pin,
            baudrate=24000000,
        )

    def zeige(self, bild: Image.Image) -> None:
        # Bild muss 320x240 sein — Library dreht intern auf 240x320 fuer den Chip
        self._display.image(bild)

    def events_verarbeiten(self, stimmung=None) -> bool:
        # Auf dem Pi uebernehmen GPIO-Interrupts (buttons.py) die Eingaben
        return True

    def schliessen(self) -> None:
        pass
