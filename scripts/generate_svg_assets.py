#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Writes all marketing SVGs as UTF-8 (Kyrgyz + Latin)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "assets"

FONT_IMPORT = """@import url("https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&display=swap");"""

STYLE_T = """.t { font-family: Manrope, "DejaVu Sans", Arial, sans-serif; }"""


def w(name: str, body: str) -> None:
    p = ROOT / name
    p.write_text(body.strip() + "\n", encoding="utf-8")
    print("wrote", p)


def svg_wrap(title: str, inner: str, wvb: str, width: int, height: int) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="{wvb}" role="img" aria-labelledby="t">
  <title id="t">{title}</title>
  {inner}
</svg>"""


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)

    logo = svg_wrap(
        "Mega Kids logo",
        f"""<defs><style type="text/css"><![CDATA[
{FONT_IMPORT}
{STYLE_T}
]]></style></defs>
  <rect x="4" y="8" width="56" height="56" rx="14" fill="#e85d4c"/>
  <text x="32" y="49" text-anchor="middle" class="t" fill="#ffffff" font-weight="800" font-size="28">M</text>
  <text x="76" y="50" class="t" font-weight="800" font-size="34" fill="#0f1419">Mega</text>
  <text x="178" y="50" class="t" font-weight="800" font-size="34" fill="#e85d4c">Kids</text>""",
        "0 0 300 72",
        300,
        72,
    )
    w("mega-kids-logo.svg", logo)

    mono_b = svg_wrap(
        "Mega Kids logo mono black",
        f"""<defs><style type="text/css"><![CDATA[
{FONT_IMPORT}
{STYLE_T}
]]></style></defs>
  <rect x="4" y="8" width="56" height="56" rx="14" fill="#0f1419"/>
  <text x="32" y="49" text-anchor="middle" class="t" fill="#ffffff" font-weight="800" font-size="28">M</text>
  <text x="76" y="50" class="t" font-weight="800" font-size="34" fill="#0f1419">Mega</text>
  <text x="178" y="50" class="t" font-weight="800" font-size="34" fill="#0f1419">Kids</text>""",
        "0 0 300 72",
        300,
        72,
    )
    w("mega-kids-logo-mono-black.svg", mono_b)

    mono_w = svg_wrap(
        "Mega Kids logo mono white on dark",
        f"""<defs><style type="text/css"><![CDATA[
{FONT_IMPORT}
{STYLE_T}
]]></style></defs>
  <rect width="300" height="72" fill="#0f1419"/>
  <rect x="4" y="8" width="56" height="56" rx="14" fill="#ffffff"/>
  <text x="32" y="49" text-anchor="middle" class="t" fill="#0f1419" font-weight="800" font-size="28">M</text>
  <text x="76" y="50" class="t" font-weight="800" font-size="34" fill="#ffffff">Mega</text>
  <text x="178" y="50" class="t" font-weight="800" font-size="34" fill="#ffffff">Kids</text>""",
        "0 0 300 72",
        300,
        72,
    )
    w("mega-kids-logo-mono-white.svg", mono_w)

    banner = svg_wrap(
        "Mega Kids outdoor banner",
        f"""<defs>
    <style type="text/css"><![CDATA[
{FONT_IMPORT}
{STYLE_T}
      .h1 {{ font-weight: 800; font-size: 128px; }}
      .h2 {{ font-weight: 700; font-size: 46px; fill: #4a5568; }}
      .box {{ font-weight: 600; font-size: 40px; fill: #0f1419; }}
      .accent {{ fill: #e85d4c; font-weight: 800; }}
    ]]></style>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#faf8f5"/>
      <stop offset="1" stop-color="#ebe4d9"/>
    </linearGradient>
  </defs>
  <rect width="3600" height="1200" fill="url(#g)"/>
  <rect x="0" y="0" width="28" height="1200" fill="#e85d4c"/>
  <text x="100" y="220" class="t h1" fill="#0f1419">Mega</text>
  <text x="420" y="220" class="t h1 accent">Kids</text>
  <text x="100" y="320" class="t h2">0\u201312 жашка чейинки балдар үчүн кийим жана аксессуарлар</text>
  <text x="100" y="400" class="t h2">\u00abМега\u00bb имаратындагы балдар кийими \u00b7 Баткен</text>
  <text x="100" y="500" class="t h1 accent">Ачылды!</text>
  <rect x="2200" y="140" width="1280" height="920" rx="28" fill="#ffffff" stroke="#e8e3db" stroke-width="4"/>
  <text x="2340" y="280" class="t box">23:00 чейин ачык</text>
  <text x="2340" y="380" class="t box">Самат Садыков к., 50</text>
  <text x="2340" y="480" class="t box">\u00abМега\u00bb имараты</text>
  <text x="2340" y="620" class="t box accent">@mega_kids_batken</text>
  <text x="2340" y="720" class="t box">+996 776 66 85 80</text>""",
        "0 0 3600 1200",
        3600,
        1200,
    )
    w("banner-outdoor.svg", banner)

    ig1350 = svg_wrap(
        "Instagram post 1080x1350",
        f"""<defs>
    <style type="text/css"><![CDATA[
{FONT_IMPORT}
{STYLE_T}
    ]]></style>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#faf8f5"/>
      <stop offset="1" stop-color="#f0ebe3"/>
    </linearGradient>
  </defs>
  <rect width="1080" height="1350" fill="url(#bg)"/>
  <rect width="1080" height="240" fill="#e85d4c"/>
  <text x="540" y="125" text-anchor="middle" class="t" fill="#fff" font-weight="800" font-size="72">Mega Kids</text>
  <text x="540" y="195" text-anchor="middle" class="t" fill="#fff" font-weight="600" font-size="32">Баткен \u00b7 \u00abМега\u00bb имараты</text>
  <rect x="120" y="300" width="840" height="120" rx="20" fill="#e85d4c"/>
  <text x="540" y="385" text-anchor="middle" class="t" fill="#fff" font-weight="800" font-size="52">Ачылды!</text>
  <text x="540" y="520" text-anchor="middle" class="t" fill="#0f1419" font-weight="700" font-size="36">0\u201312 жашка чейинки балдар үчүн</text>
  <text x="540" y="580" text-anchor="middle" class="t" fill="#0f1419" font-weight="700" font-size="36">кийим жана аксессуарлар</text>
  <text x="540" y="700" text-anchor="middle" class="t" fill="#4a5568" font-weight="600" font-size="32">Самат Садыков к., 50</text>
  <text x="540" y="760" text-anchor="middle" class="t" fill="#4a5568" font-weight="600" font-size="32">\u00abМега\u00bb имараты \u00b7 23:00 чейин ачык</text>
  <text x="540" y="920" text-anchor="middle" class="t" fill="#e85d4c" font-weight="800" font-size="38">@mega_kids_batken</text>
  <text x="540" y="990" text-anchor="middle" class="t" fill="#0f1419" font-weight="700" font-size="34">+996 776 66 85 80</text>
  <text x="540" y="1180" text-anchor="middle" class="t" fill="#a0aec0" font-size="26">#MegaKids #Баткен #БалдарКийими</text>""",
        "0 0 1080 1350",
        1080,
        1350,
    )
    w("instagram-1080x1350.svg", ig1350)

    ig1080 = svg_wrap(
        "Instagram square 1080",
        f"""<defs><style type="text/css"><![CDATA[
{FONT_IMPORT}
{STYLE_T}
    ]]></style></defs>
  <rect width="1080" height="1080" fill="#faf8f5"/>
  <circle cx="540" cy="380" r="160" fill="#e85d4c"/>
  <text x="540" y="405" text-anchor="middle" class="t" fill="#fff" font-weight="800" font-size="120">M</text>
  <text x="540" y="620" text-anchor="middle" class="t" fill="#0f1419" font-weight="800" font-size="68">Mega Kids</text>
  <text x="540" y="700" text-anchor="middle" class="t" fill="#4a5568" font-weight="600" font-size="34">0\u201312 жаш \u00b7 кийим жана аксессуарлар</text>
  <text x="540" y="780" text-anchor="middle" class="t" fill="#4a5568" font-weight="600" font-size="30">\u00abМега\u00bb \u00b7 Самат Садыков 50, Баткен</text>
  <text x="540" y="860" text-anchor="middle" class="t" fill="#e85d4c" font-weight="800" font-size="36">@mega_kids_batken</text>
  <text x="540" y="920" text-anchor="middle" class="t" fill="#0f1419" font-weight="700" font-size="32">23:00 чейин \u00b7 +996 776 66 85 80</text>""",
        "0 0 1080 1080",
        1080,
        1080,
    )
    w("instagram-1080x1080.svg", ig1080)

    story = svg_wrap(
        "Instagram story 1080x1920",
        f"""<defs>
    <style type="text/css"><![CDATA[
{FONT_IMPORT}
{STYLE_T}
    ]]></style>
    <linearGradient id="sg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0f1419"/>
      <stop offset="0.45" stop-color="#1a2332"/>
      <stop offset="1" stop-color="#e85d4c"/>
    </linearGradient>
  </defs>
  <rect width="1080" height="1920" fill="url(#sg)"/>
  <text x="540" y="520" text-anchor="middle" class="t" fill="#fff" font-weight="800" font-size="80">Mega Kids</text>
  <text x="540" y="620" text-anchor="middle" class="t" fill="#fbd5cf" font-weight="600" font-size="36">Баткен \u00b7 \u00abМега\u00bb</text>
  <text x="540" y="900" text-anchor="middle" class="t" fill="#fff" font-weight="800" font-size="96">Ачылды!</text>
  <text x="540" y="1040" text-anchor="middle" class="t" fill="#fff" font-weight="600" font-size="38">0\u201312 жаш \u00b7 кийим жана аксессуарлар</text>
  <text x="540" y="1180" text-anchor="middle" class="t" fill="#fff" font-weight="600" font-size="34">Самат Садыков 50 \u00b7 23:00 чейин</text>
  <text x="540" y="1380" text-anchor="middle" class="t" fill="#fff" font-weight="800" font-size="42">@mega_kids_batken</text>
  <text x="540" y="1480" text-anchor="middle" class="t" fill="#fff" font-weight="700" font-size="36">+996 776 66 85 80</text>
  <text x="540" y="1750" text-anchor="middle" class="t" fill="#ffffff" font-weight="600" font-size="28" opacity="0.85">Stories: төмөн/үстүн боштук</text>""",
        "0 0 1080 1920",
        1080,
        1920,
    )
    w("instagram-1080x1920-story.svg", story)

    sticker = svg_wrap(
        "Door hours sticker",
        f"""<defs><style type="text/css"><![CDATA[
{FONT_IMPORT}
{STYLE_T}
    ]]></style></defs>
  <rect width="800" height="360" rx="24" fill="#0f1419"/>
  <text x="400" y="200" text-anchor="middle" class="t" fill="#fff" font-weight="800" font-size="110">23:00</text>
  <text x="400" y="280" text-anchor="middle" class="t" fill="#e85d4c" font-weight="700" font-size="44">чейин ачык</text>
  <text x="400" y="330" text-anchor="middle" class="t" fill="#a0aec0" font-weight="600" font-size="26">Mega Kids \u00b7 Баткен</text>""",
        "0 0 800 360",
        800,
        360,
    )
    w("sticker-hours.svg", sticker)

    tag = svg_wrap(
        "Shelf label template",
        f"""<defs><style type="text/css"><![CDATA[
{FONT_IMPORT}
{STYLE_T}
    ]]></style></defs>
  <rect width="480" height="200" rx="16" fill="#ffffff" stroke="#e85d4c" stroke-width="6"/>
  <text x="240" y="95" text-anchor="middle" class="t" fill="#0f1419" font-weight="800" font-size="36">Жаңы коллекция</text>
  <text x="240" y="155" text-anchor="middle" class="t" fill="#718096" font-weight="700" font-size="28">0\u201312 жаш \u00b7 Mega Kids</text>""",
        "0 0 480 200",
        480,
        200,
    )
    w("price-tag-generic.svg", tag)


if __name__ == "__main__":
    main()
