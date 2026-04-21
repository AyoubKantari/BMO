from enum import Enum


class Zustand(Enum):
    IDLE = 1
    DENKT = 2
    SPRICHT = 3


class Stimmung:

    def __init__(self):
        self.aktueller_zustand = Zustand.IDLE

    def wechsle(self, nächster):
        self.aktueller_zustand = nächster

    def unterbrechen(self):
        self.aktueller_zustand = Zustand.IDLE

    def get_zustand(self):
        return self.aktueller_zustand
