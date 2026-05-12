"""
Minimaler ILI9341-Test.
Zeigt nacheinander Rot, Gruen, Blau auf dem Display.
"""

import time
import board
import digitalio
from PIL import Image
from adafruit_rgb_display import ili9341

# Pins (Physical Pin in Klammern)
CS_PIN    = digitalio.DigitalInOut(board.CE0)   # GPIO8  (Pin 24)
DC_PIN    = digitalio.DigitalInOut(board.D24)   # GPIO24 (Pin 18)
RESET_PIN = digitalio.DigitalInOut(board.D25)   # GPIO25 (Pin 22)

# SPI mit 24 MHz starten
spi = board.SPI()
display = ili9341.ILI9341(
    spi,
    rotation=270,           # Querformat 320x240
    cs=CS_PIN,
    dc=DC_PIN,
    rst=RESET_PIN,
    baudrate=24000000,
)

# Bei rotation=270 dreht sich width/height automatisch
print(f"Display Groesse: {display.width} x {display.height}")

# Bild muss im Querformat (320x240) übergeben werden —
# die Library dreht es intern auf 240x320 für den Chip (rotation=270)
BREITE, HOEHE = 320, 240

farben = [
    ("Rot",   (255, 0,   0)),
    ("Gruen", (0,   255, 0)),
    ("Blau",  (0,   0,   255)),
]

for name, rgb in farben:
    print(f"Zeige {name}")
    bild = Image.new("RGB", (BREITE, HOEHE), rgb)
    display.image(bild)
    time.sleep(1)

print("Test fertig")
