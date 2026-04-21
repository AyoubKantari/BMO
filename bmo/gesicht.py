"""
gesicht.py — BMO Gesichter mit Pillow zeichnen
Zustände: idle, happy, denkt, spricht
Display: ILI9341, 320x240px (Querformat)
"""

from PIL import Image, ImageDraw

# --- Bildgröße (Querformat) ---
BREITE = 320
HOEHE  = 240

# --- BMO Farbpalette ---
MINTGRUEN_DUNKEL = (155, 225, 185)   # Hintergrund: idle / denkt / spricht
MINTGRUEN_HELL   = (195, 235, 205)   # Hintergrund: happy
SCHWARZ          = (18,  18,  18)    # Augen
GRUEN_DUNKEL     = (35,  105, 65)    # Mund Hauptfarbe + Rand
GRUEN_RAND       = (20,   65, 40)    # Mund Außenrand
GRUEN_HELL       = (95,  175, 110)   # Mund Unterlippe (happy)
WEISS            = (238, 238, 230)   # Zähne (happy)


# ─────────────────────────────────────────────
# Öffentliche API
# ─────────────────────────────────────────────

def gesicht_erstellen(zustand: str, mund_offen: bool = True,
                      blinzeln: bool = False) -> Image.Image:
    """
    Erstellt ein BMO-Gesicht als PIL-Image.
    zustand:   'idle' | 'happy' | 'denkt' | 'spricht'
    blinzeln:  True → Augen kurz geschlossen (Animation)
    """
    bild = Image.new("RGB", (BREITE, HOEHE))
    draw = ImageDraw.Draw(bild)

    zeichner = {
        "idle":    lambda d: _zeichne_idle(d, blinzeln),
        "happy":   lambda d: _zeichne_happy(d, blinzeln),
        "denkt":   _zeichne_denkt,
        "spricht": lambda d: _zeichne_spricht(d, mund_offen, blinzeln),
    }
    zeichner.get(zustand, _zeichne_idle)(draw)
    return bild


# ─────────────────────────────────────────────
# Hilfsfunktionen — Grundbausteine
# ─────────────────────────────────────────────

def _hintergrund(draw: ImageDraw.Draw, farbe: tuple) -> None:
    """Füllt den gesamten Hintergrund mit einer Farbe."""
    draw.rectangle([0, 0, BREITE, HOEHE], fill=farbe)


def _auge(draw: ImageDraw.Draw, mx: int, hg: tuple,
          rx: int = 7, ry: int = 7) -> None:
    """
    Zeichnet ein einzelnes Auge als schwarzes Oval.
    mx: horizontale Mittelposition des Auges
    """
    ay = int(HOEHE * 0.38)
    draw.ellipse([mx - rx, ay - ry, mx + rx, ay + ry], fill=SCHWARZ)


def _augen_paar(draw: ImageDraw.Draw, hg: tuple,
                rx: int = 7, ry: int = 7, blinzeln: bool = False) -> None:
    """Zeichnet beide Augen — offen als Punkte, blinzeln als flache Bögen."""
    cx   = BREITE // 2
    abst = int(BREITE * 0.185)
    ay   = int(HOEHE * 0.38)
    if blinzeln:
        for mx in [cx - abst, cx + abst]:
            draw.arc([mx - 14, ay - 3, mx + 14, ay + 9],
                     start=200, end=340, fill=SCHWARZ, width=3)
    else:
        _auge(draw, cx - abst, hg, rx, ry)
        _auge(draw, cx + abst, hg, rx, ry)



# ─────────────────────────────────────────────
# Gesichter
# ─────────────────────────────────────────────

def _zeichne_idle(draw: ImageDraw.Draw, blinzeln: bool = False) -> None:
    """Idle: Punkt-Augen, dünnes Lächeln."""
    hg = MINTGRUEN_DUNKEL
    _hintergrund(draw, hg)
    _augen_paar(draw, hg, blinzeln=blinzeln)

    cx = BREITE // 2
    my = int(HOEHE * 0.67)
    draw.arc([cx - 45, my - 20, cx + 45, my + 20], start=0, end=180, fill=SCHWARZ, width=3)


def _zeichne_happy(draw: ImageDraw.Draw, blinzeln: bool = False) -> None:
    """Happy: Punkt-Augen, gefüllter grüner Mund."""
    hg = MINTGRUEN_HELL
    _hintergrund(draw, hg)
    _augen_paar(draw, hg, blinzeln=blinzeln)

    cx = BREITE // 2
    my = int(HOEHE * 0.67)
    draw.chord([cx - 55, my - 25, cx + 55, my + 30],
               start=0, end=180, fill=GRUEN_DUNKEL, outline=GRUEN_RAND)


def _zeichne_denkt(draw: ImageDraw.Draw) -> None:
    """
    Denkt: geschlossene Bogen-Augen (^-Form) + kleines Lächeln.
    """
    hg = MINTGRUEN_DUNKEL
    _hintergrund(draw, hg)

    cx   = BREITE // 2
    abst = int(BREITE * 0.185)
    ay   = int(HOEHE * 0.38)

    # Geschlossene Augen als obere Bögen (^ Form)
    draw.arc([cx - abst - 18, ay - 10, cx - abst + 18, ay + 14],
             start=200, end=340, fill=SCHWARZ, width=3)
    draw.arc([cx + abst - 18, ay - 10, cx + abst + 18, ay + 14],
             start=200, end=340, fill=SCHWARZ, width=3)

    # Kleines Lächeln
    my = int(HOEHE * 0.67)
    draw.arc([cx - 40, my - 18, cx + 40, my + 18],
             start=0, end=180, fill=SCHWARZ, width=3)


def _zeichne_spricht(draw: ImageDraw.Draw, mund_offen: bool,
                     blinzeln: bool = False) -> None:
    """Spricht: Punkt-Augen, Mund wechselt offen/zu für Animation."""
    hg = MINTGRUEN_DUNKEL
    _hintergrund(draw, hg)
    _augen_paar(draw, hg, blinzeln=blinzeln)

    cx = BREITE // 2
    my = int(HOEHE * 0.67)

    if mund_offen:
        draw.ellipse([cx - 38, my - 22, cx + 38, my + 22],
                     fill=GRUEN_DUNKEL, outline=GRUEN_RAND, width=3)
    else:
        draw.arc([cx - 45, my - 20, cx + 45, my + 20],
                 start=0, end=180, fill=SCHWARZ, width=3)


# ─────────────────────────────────────────────
# Lokaler Test (nur auf dem PC / Pi direkt)
# ─────────────────────────────────────────────

if __name__ == "__main__":
    for zustand in ["idle", "happy", "denkt", "spricht"]:
        bild = gesicht_erstellen(zustand)
        dateiname = f"test_{zustand}.png"
        bild.save(dateiname)
        bild.show()   
        print(f"Gespeichert: {dateiname}")