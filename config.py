
import os
from dotenv import load_dotenv

load_dotenv()

# --- Claude API ---
API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
CLAUDE_MODELL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 1024

# --- Display (ILI9341 240x320) ---
DISPLAY_BREITE = 320
DISPLAY_HOEHE  = 240
DISPLAY_SPI_GESCHWINDIGKEIT = 24000000  # 24 MHz

# --- GPIO Pins: Display ---
DISPLAY_DC    = 24   # Pin 18
DISPLAY_RESET = 25   # Pin 22
DISPLAY_CS    = 8    # Pin 24 (CE0)

# --- GPIO Pins: Buttons ---
BUTTON_A = 17   # Pin 11
BUTTON_B = 27   # Pin 13
BUTTON_C = 22   # Pin 15

# --- BMO Farben (RGB) ---
BMO_GRUEN      = (0, 168, 107)
BMO_HELLGRUEN  = (100, 200, 150)
WEISS          = (255, 255, 255)
SCHWARZ        = (0, 0, 0)
GELB           = (255, 255, 0)
ROT            = (255, 50, 50)

# --- BMO Zustände ---
ZUSTAND_IDLE     = "idle"
ZUSTAND_HORCHT   = "horcht"
ZUSTAND_DENKT    = "denkt"
ZUSTAND_SPRICHT  = "spricht"
ZUSTAND_HAPPY    = "happy"

# --- Audio ---
AUDIO_LAUTSTAERKE = 80   # Prozent 0-100
TTS_SPRACHE       = "de" # Deutsch