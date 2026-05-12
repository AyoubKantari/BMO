import pygame
from PIL import Image

BREITE = 320
HOEHE  = 240


class Display:
    def __init__(self):
        pygame.init()
        self.fenster = pygame.display.set_mode((BREITE, HOEHE))
        pygame.display.set_caption("BMO")

    def zeige(self, bild: Image.Image) -> None:
        # PIL Image → pygame Surface
        pygame_bild = pygame.image.fromstring(bild.tobytes(), bild.size, bild.mode)
        self.fenster.blit(pygame_bild, (0, 0))
        pygame.display.flip()

    def events_verarbeiten(self, stimmung=None) -> bool:
        # gibt False zurück wenn Fenster geschlossen wird
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and stimmung:
                from bmo.stimmung import Zustand
                if event.key == pygame.K_SPACE:
                    stimmung.wechsle(Zustand.DENKT)
                if event.key == pygame.K_ESCAPE:
                    stimmung.unterbrechen()
        return True

    def schliessen(self) -> None:
        pygame.quit()
