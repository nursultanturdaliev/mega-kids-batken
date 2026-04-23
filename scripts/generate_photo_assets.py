#!/usr/bin/env python3
"""Generate photo-style ad creatives from reference image (Kyrgyz text).
Run manually: python3 scripts/generate_photo_assets.py
Requires: pip install pillow
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
SRC = ASSETS / "reference-source.png"

FONT_REG = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
if not Path(FONT_REG).exists():
    FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
if not Path(FONT_BOLD).exists():
    FONT_BOLD = FONT_REG


def fnt(size: int, bold: bool = False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size=size)


def rr(draw, box, r, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def kids_strip(base: Image.Image, target_w: int) -> Image.Image:
    crop = base.crop((230, 175, 1080, 670))
    return ImageOps.contain(crop, (target_w, int(target_w * 0.55)))


def add_brand(draw: ImageDraw.ImageDraw, width: int):
    rr(draw, (width // 2 - 260, 36, width // 2 + 260, 170), 34, (17, 45, 78, 235), (220, 235, 255, 220), 4)
    draw.text((width // 2 - 160, 68), "MEGA", font=fnt(66, True), fill=(126, 238, 210))
    draw.text((width // 2 + 20, 68), "KIDS", font=fnt(66, True), fill=(255, 120, 94))
    draw.text((width // 2 - 60, 130), "БАТКЕН", font=fnt(48, True), fill=(240, 250, 255))


def footer(draw: ImageDraw.ImageDraw, w: int, h: int, small: bool = False):
    fs = 34 if not small else 24
    y = h - 84 if not small else h - 62
    txt = "Баткен | Самат Садыков 50   |   +996 776 66 85 80   |   @mega_kids_batken"
    tw = draw.textlength(txt, font=fnt(fs, True))
    draw.text(((w - tw) / 2, y), txt, font=fnt(fs, True), fill=(239, 247, 255))


def main():
    if not SRC.exists():
        raise SystemExit(f"Reference image missing: {SRC}")

    base = Image.open(SRC).convert("RGBA")

    # Banner 1920x1080
    w, h = 1920, 1080
    can = Image.new("RGBA", (w, h), (26, 63, 105, 255))
    d = ImageDraw.Draw(can)
    add_brand(d, w)
    d.text((w // 2 - 430, 220), "БАЛДАР МОДАСЫ ЖАНА СТИЛЬ", font=fnt(68, True), fill=(245, 250, 255))
    d.text((w // 2 - 425, 290), "КИЧИНЕКЕЙЛЕР ҮЧҮН МЫКТЫ ТАНДОО", font=fnt(52, True), fill=(245, 250, 255))
    rr(d, (80, 410, 600, 560), 38, (232, 244, 255, 235), (214, 230, 244), 4)
    rr(d, (1320, 410, 1840, 560), 38, (232, 244, 255, 235), (214, 230, 244), 4)
    d.text((145, 455), "КИЙИМ | БУТ КИЙИМ", font=fnt(44, True), fill=(17, 46, 74))
    d.text((200, 505), "АКСЕССУАРЛАР", font=fnt(44, True), fill=(17, 46, 74))
    d.text((1405, 455), "СТИЛДҮҮ", font=fnt(44, True), fill=(17, 46, 74))
    d.text((1365, 505), "КОЛЛЕКЦИЯЛАР", font=fnt(44, True), fill=(17, 46, 74))
    strip = kids_strip(base, 980)
    can.alpha_composite(strip, (w // 2 - strip.width // 2, 465))
    footer(d, w, h)
    can.convert("RGB").save(ASSETS / "photo-banner-kg-1920x1080.png", quality=95)

    # IG portrait 1080x1350
    w, h = 1080, 1350
    can = Image.new("RGBA", (w, h), (28, 63, 104, 255))
    d = ImageDraw.Draw(can)
    add_brand(d, w)
    rr(d, (70, 220, 1010, 370), 32, (232, 244, 255, 235), (214, 230, 244), 4)
    d.text((220, 272), "АЧЫЛДЫ!", font=fnt(74, True), fill=(228, 78, 55))
    d.text((130, 395), "0–12 жашка чейин кийим жана аксессуарлар", font=fnt(40, True), fill=(243, 250, 255))
    strip = kids_strip(base, 820)
    can.alpha_composite(strip, (130, 575))
    footer(d, w, h, small=True)
    can.convert("RGB").save(ASSETS / "photo-instagram-1080x1350.png", quality=95)

    # IG square
    w = h = 1080
    can = Image.new("RGBA", (w, h), (28, 63, 104, 255))
    d = ImageDraw.Draw(can)
    add_brand(d, w)
    d.text((145, 220), "АЧЫЛДЫ! 0–12 жаш", font=fnt(64, True), fill=(255, 235, 232))
    strip = kids_strip(base, 780)
    can.alpha_composite(strip, (150, 360))
    rr(d, (90, 860, 990, 1030), 30, (232, 244, 255, 235), (214, 230, 244), 3)
    d.text((145, 905), "Самат Садыков 50  |  @mega_kids_batken", font=fnt(32, True), fill=(24, 58, 92))
    d.text((270, 950), "+996 776 66 85 80  |  23:00 чейин", font=fnt(30, True), fill=(24, 58, 92))
    can.convert("RGB").save(ASSETS / "photo-instagram-1080x1080.png", quality=95)

    # Story
    w, h = 1080, 1920
    can = Image.new("RGBA", (w, h), (20, 42, 72, 255))
    d = ImageDraw.Draw(can)
    add_brand(d, w)
    d.text((160, 240), "Mega Kids Баткен", font=fnt(70, True), fill=(237, 246, 255))
    d.text((130, 330), "Балдар мода жана стиль", font=fnt(52, True), fill=(237, 246, 255))
    strip = kids_strip(base, 950)
    can.alpha_composite(strip, (65, 760))
    rr(d, (80, 1460, 1000, 1740), 34, (232, 244, 255, 235), (214, 230, 244), 4)
    d.text((170, 1515), "КИЙИМ • БУТ КИЙИМ • АКСЕССУАР", font=fnt(36, True), fill=(21, 54, 87))
    d.text((165, 1570), "Самат Садыков 50", font=fnt(40, True), fill=(21, 54, 87))
    d.text((165, 1625), "+996 776 66 85 80", font=fnt(40, True), fill=(21, 54, 87))
    d.text((165, 1680), "@mega_kids_batken • 23:00 чейин", font=fnt(36, True), fill=(21, 54, 87))
    can.convert("RGB").save(ASSETS / "photo-story-1080x1920.png", quality=95)

    # Facebook 1200x630
    w, h = 1200, 630
    can = Image.new("RGBA", (w, h), (29, 64, 106, 255))
    d = ImageDraw.Draw(can)
    add_brand(d, w)
    d.text((130, 220), "АЧЫЛДЫ! Балдар кийими 0–12", font=fnt(56, True), fill=(243, 251, 255))
    strip = kids_strip(base, 600)
    can.alpha_composite(strip, (560, 250))
    d.text((110, 315), "Самат Садыков 50, «Мега»", font=fnt(38, True), fill=(243, 251, 255))
    d.text((110, 370), "+996 776 66 85 80", font=fnt(38, True), fill=(243, 251, 255))
    d.text((110, 425), "@mega_kids_batken", font=fnt(38, True), fill=(255, 139, 119))
    can.convert("RGB").save(ASSETS / "photo-facebook-1200x630.png", quality=95)

    print("Photo-style assets updated")


if __name__ == "__main__":
    main()
