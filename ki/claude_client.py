import re
import anthropic
from config import API_KEY, CLAUDE_MODELL, MAX_TOKENS

# BMO's Persönlichkeit
SYSTEM_PROMPT = """Du bist BMO, ein freundlicher kleiner Roboter aus der Serie Adventure Time.
Du sprichst kurz, niedlich und hilfreich. Antworte immer auf Deutsch.
Benutze keine Emojis und keine Sonderzeichen — deine Antworten werden von einer Sprachausgabe vorgelesen."""

# Emoji-Filter (Sicherheitsnetz, falls das Modell trotzdem Emojis schickt)
_EMOJI_REGEX = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # Emoticons
    "\U0001F300-\U0001F5FF"  # Symbole & Piktogramme
    "\U0001F680-\U0001F6FF"  # Transport & Karten
    "\U0001F1E0-\U0001F1FF"  # Flaggen
    "\U00002700-\U000027BF"  # Dingbats
    "\U0001F900-\U0001F9FF"  # zusätzliche Symbole
    "\U00002600-\U000026FF"  # Misc Symbole
    "]+",
    flags=re.UNICODE,
)


def _emojis_entfernen(text: str) -> str:
    return _EMOJI_REGEX.sub("", text).strip()


class ClaudeClient:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=API_KEY)
        self.history = []

    def sende(self, nachricht):
        self.history.append({"role": "user", "content": nachricht})

        try:
            antwort = self.client.messages.create(
                model=CLAUDE_MODELL,
                max_tokens=MAX_TOKENS,
                system=SYSTEM_PROMPT,
                messages=self.history
            )
            antwort_text = _emojis_entfernen(antwort.content[0].text)
            self.history.append({"role": "assistant", "content": antwort_text})
            return antwort_text

        except Exception as e:
            print(f"[Claude API Fehler] {e}")
            return None

    def reset(self):
        self.history = []
