from pathlib import Path

from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


OUT = Path(__file__).parents[1] / "gdpr" / "koterovska4" / "strezeno-koterovska4.pdf"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
pdfmetrics.registerFont(TTFont("DejaVu", FONT))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", FONT_BOLD))

PAGE_W, PAGE_H = landscape(A4)


def fit_size(text, max_width, preferred=14, minimum=9):
    size = preferred
    while size > minimum and pdfmetrics.stringWidth(text, "DejaVu", size) > max_width:
        size -= 0.25
    return size


def label(c, x, y):
    # x/y are the lower-left coordinates of a label area.
    width = 390
    center = x + width / 2
    c.setFillColorRGB(0, 0, 0)
    c.setFont("DejaVu-Bold", 36)
    c.drawCentredString(center, y + 236, "Střeženo")
    c.drawCentredString(center, y + 195, "kamerami se")
    c.drawCentredString(center, y + 154, "záznamem")

    c.setFont("DejaVu", 13)
    c.drawString(x, y + 127, "Účel zpracování: ochrana majetku a osob")
    supervisor = "Správce: Společenství vlastníků Koterovská 93/4, Plzeň"
    c.setFont("DejaVu", fit_size(supervisor, width, 13, 10))
    c.drawString(x, y + 102, supervisor)
    c.setFont("DejaVu", 13)
    c.drawString(x, y + 77, "Kontakt: info@sbdps.cz")
    c.drawString(x, y + 51, "Podrobné informace o zpracování osobních údajů")
    c.drawString(x, y + 31, "najdete u správce domu SBD Plzeň - sever nebo na")
    c.setFont("DejaVu", fit_size("www.kamery-plzen.cz/gdpr/koterovska4", width, 13, 9))
    c.drawString(x, y + 11, "www.kamery-plzen.cz/gdpr/koterovska4")


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT), pagesize=landscape(A4))
    label(c, 12, 30)
    label(c, 432, 30)
    label(c, 12, -253)
    label(c, 432, -253)
    c.save()


if __name__ == "__main__":
    main()
