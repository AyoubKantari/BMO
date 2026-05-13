# BMO – AI-Powered Voice Assistant on Raspberry Pi

> *"BMO, what's it like to be alive?"*

BMO is a voice-controlled AI assistant running on a Raspberry Pi, inspired by the character from Adventure Time. It listens, thinks, and talks — powered by the Claude AI API and Google Speech Recognition.

---

## What it does

BMO wakes up in **idle mode** and waits. When activated, it:

1. Listens to your voice via microphone (German language, Google Speech API)
2. Sends your question to **Claude Haiku** (Anthropic API)
3. Displays an animated face on a TFT display showing its current state
4. Responds out loud using text-to-speech (pyttsx3)

The assistant has four visible states shown on the display: `idle`, `listens`, `thinks`, and `speaks`.

---

## Hardware

| Component | Details |
|---|---|
| **Microcontroller** | Raspberry Pi |
| **Display** | ILI9341 TFT, 240×320px, SPI (24 MHz) |
| **Buttons** | 3× physical push buttons (GPIO 17, 27, 22) |
| **Audio** | USB microphone + speaker/headphone jack |

**GPIO Wiring (Display):**
- DC → Pin 18 (GPIO 24)
- RESET → Pin 22 (GPIO 25)
- CS → Pin 24 / CE0 (GPIO 8)

---

## Tech Stack

- **Python 3**
- **Anthropic Claude API** (`claude-haiku`) — AI responses
- **SpeechRecognition** + Google Speech API — voice input (German)
- **pyttsx3** — text-to-speech output
- **Pygame / PIL** — display rendering
- **RPi.GPIO** — hardware button control

---

## Project Structure

```
BMO/
├── main.py              # Entry point — main loop & state machine
├── config.py            # Hardware pins, API keys, constants
├── bmo/
│   ├── gesicht.py       # Face rendering (idle, thinks, speaks, ...)
│   └── stimmung.py      # State machine (Zustand: IDLE, DENKT, SPRICHT)
├── hardware/
│   ├── display.py       # ILI9341 TFT display driver
│   └── buttons.py       # GPIO button setup & callbacks
├── ki/
│   └── claude_client.py # Anthropic API client wrapper
├── assets/
│   └── sounds/          # Audio assets
└── phase_2/             # Next iteration (in progress)
```

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/AyoubKantari/BMO.git
cd BMO
```

**2. Install dependencies**
```bash
pip install anthropic speechrecognition pyttsx3 python-dotenv RPi.GPIO pygame pillow
sudo apt-get install python3-pyaudio flac
```

**3. Set your API key**

Create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=your_api_key_here
```

**4. Run**
```bash
python main.py
```

---

## Configuration

All hardware pins, display settings, colors, and API parameters are defined in `config.py`. No hardcoded values in the main logic.

---

## Status

Working prototype — Phase 1 complete.  
Phase 2 (`/phase_2`) is in active development.

---

## Author

**Ayoub Kantari** — [github.com/AyoubKantari](https://github.com/AyoubKantari)
