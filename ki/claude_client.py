import anthropic
from config import API_KEY, CLAUDE_MODELL, MAX_TOKENS

# BMO's Persönlichkeit
SYSTEM_PROMPT = """Du bist BMO, ein freundlicher kleiner Roboter aus der Serie Adventure Time.
Du sprichst kurz, niedlich und hilfreich. Antworte immer auf Deutsch."""


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
            antwort_text = antwort.content[0].text
            self.history.append({"role": "assistant", "content": antwort_text})
            return antwort_text

        except Exception as e:
            print(f"[Claude API Fehler] {e}")
            return None

    def reset(self):
        self.history = []
