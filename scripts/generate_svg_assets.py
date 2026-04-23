#!/usr/bin/env python3
"""Writes marketing SVGs as UTF-8. Kyrgyz strings load from ky_strings.json (ASCII \\u escapes)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "assets"
KY = json.loads((Path(__file__).parent / "ky_strings.json").read_text(encoding="utf-8"))

FONT_IMPORT = """@import url("https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&display=swap");"""
STYLE_T = """.t { font-family: Manrope, "DejaVu Sans", Arial, sans-serif; }"""


def w(name: str, body: str) -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
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
    k = KY

    logo = svg_wrap(
        "Mega Kids logo",
        f"""<defs><style type="text/css"><![CDATA[
{FONT_IMPORT}
{STYLE_T}
]]></style></defs>
  <rect x="6" y="12" width="408" height="70" rx="24" fill="#12365d" stroke="#8fb4dc" stroke-width="3"/>
  <rect x="140" y="74" width="140" height="34" rx="12" fill="#12365d" stroke="#8fb4dc" stroke-width="3"/>
  <text x="52" y="58" class="t" font-weight="800" font-size="50" fill="#9de8da">MEGA</text>
  <text x="222" y="58" class="t" font-weight="800" font-size="50" fill="#ff7a5f">KIDS</text>
  <text x="210" y="100" text-anchor="middle" class="t" font-weight="800" font-size="34" fill="#ffffff">БАТКЕН</text>
  <text x="192" y="30" class="t" font-size="18" font-weight="700" fill="#98ebe0">★</text>
  <text x="255" y="30" class="t" font-size="18" font-weight="700" fill="#ff7a5f">❤</text>""",
        "0 0 420 120",
        420,
        120,
    )
    w("mega-kids-logo.svg", logo)

    mono_b = svg_wrap(
        "Mega Kids logo mono black",
        f"""<defs><style type="text/css"><![CDATA[
{FONT_IMPORT}
{STYLE_T}
]]></style></defs>
  <rect x="6" y="12" width="408" height="70" rx="24" fill="#0f1419" stroke="#0f1419" stroke-width="3"/>
  <rect x="140" y="74" width="140" height="34" rx="12" fill="#0f1419" stroke="#0f1419" stroke-width="3"/>
  <text x="52" y="58" class="t" font-weight="800" font-size="50" fill="#0f1419">MEGA</text>
  <text x="222" y="58" class="t" font-weight="800" font-size="50" fill="#0f1419">KIDS</text>
  <text x="210" y="100" text-anchor="middle" class="t" font-weight="800" font-size="34" fill="#0f1419">БАТКЕН</text>
  <text x="192" y="30" class="t" font-size="18" font-weight="700" fill="#0f1419">★</text>
  <text x="255" y="30" class="t" font-size="18" font-weight="700" fill="#0f1419">❤</text>""",
        "0 0 420 120",
        420,
        120,
    )
    w("mega-kids-logo-mono-black.svg", mono_b)

    mono_w = svg_wrap(
        "Mega Kids logo mono white on dark",
        f"""<defs><style type="text/css"><![CDATA[
{FONT_IMPORT}
{STYLE_T}
]]></style></defs>
  <rect width="420" height="120" fill="#0f1419"/>
  <rect x="6" y="12" width="408" height="70" rx="24" fill="none" stroke="#ffffff" stroke-width="3"/>
  <rect x="140" y="74" width="140" height="34" rx="12" fill="none" stroke="#ffffff" stroke-width="3"/>
  <text x="52" y="58" class="t" font-weight="800" font-size="50" fill="#ffffff">MEGA</text>
  <text x="222" y="58" class="t" font-weight="800" font-size="50" fill="#ffffff">KIDS</text>
  <text x="210" y="100" text-anchor="middle" class="t" font-weight="800" font-size="34" fill="#ffffff">БАТКЕН</text>
  <text x="192" y="30" class="t" font-size="18" font-weight="700" fill="#ffffff">★</text>
  <text x="255" y="30" class="t" font-size="18" font-weight="700" fill="#ffffff">❤</text>""",
        "0 0 420 120",
        420,
        120,
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
  <text x="100" y="320" class="t h2">{k["banner_sub"]}</text>
  <text x="100" y="400" class="t h2">{k["mega_line_long"]}</text>
  <text x="100" y="500" class="t h1 accent">{k["open_exc"]}</text>
  <rect x="2200" y="140" width="1280" height="920" rx="28" fill="#ffffff" stroke="#e8e3db" stroke-width="4"/>
  <text x="2340" y="280" class="t box">{k["hours_open"]}</text>
  <text x="2340" y="380" class="t box">{k["samat_addr"]}</text>
  <text x="2340" y="480" class="t box">{k["mega_building"]}</text>
  <text x="2340" y="620" class="t box accent">@megabatken</text>
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
  <text x="540" y="195" text-anchor="middle" class="t" fill="#fff" font-weight="600" font-size="32">{k["mega_building_caption"]}</text>
  <rect x="120" y="300" width="840" height="120" rx="20" fill="#e85d4c"/>
  <text x="540" y="385" text-anchor="middle" class="t" fill="#fff" font-weight="800" font-size="52">{k["open_exc"]}</text>
  <text x="540" y="520" text-anchor="middle" class="t" fill="#0f1419" font-weight="700" font-size="36">{k["age_line"]}</text>
  <text x="540" y="580" text-anchor="middle" class="t" fill="#0f1419" font-weight="700" font-size="36">{k["clothing_line"]}</text>
  <text x="540" y="700" text-anchor="middle" class="t" fill="#4a5568" font-weight="600" font-size="32">{k["samat_addr"]}</text>
  <text x="540" y="760" text-anchor="middle" class="t" fill="#4a5568" font-weight="600" font-size="32">{k["mega_hours_line"]}</text>
  <text x="540" y="920" text-anchor="middle" class="t" fill="#e85d4c" font-weight="800" font-size="38">@megabatken</text>
  <text x="540" y="990" text-anchor="middle" class="t" fill="#0f1419" font-weight="700" font-size="34">+996 776 66 85 80</text>
  <text x="540" y="1180" text-anchor="middle" class="t" fill="#a0aec0" font-size="26">{k["hashtags"]}</text>""",
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
  <text x="540" y="700" text-anchor="middle" class="t" fill="#4a5568" font-weight="600" font-size="34">{k["square_age"]}</text>
  <text x="540" y="780" text-anchor="middle" class="t" fill="#4a5568" font-weight="600" font-size="30">{k["square_addr"]}</text>
  <text x="540" y="860" text-anchor="middle" class="t" fill="#e85d4c" font-weight="800" font-size="36">@megabatken</text>
  <text x="540" y="920" text-anchor="middle" class="t" fill="#0f1419" font-weight="700" font-size="32">{k["square_hours_phone"]}</text>""",
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
  <text x="540" y="620" text-anchor="middle" class="t" fill="#fbd5cf" font-weight="600" font-size="36">{k["story_sub"]}</text>
  <text x="540" y="900" text-anchor="middle" class="t" fill="#fff" font-weight="800" font-size="96">{k["open_exc"]}</text>
  <text x="540" y="1040" text-anchor="middle" class="t" fill="#fff" font-weight="600" font-size="38">{k["story_mid"]}</text>
  <text x="540" y="1180" text-anchor="middle" class="t" fill="#fff" font-weight="600" font-size="34">{k["story_addr"]}</text>
  <text x="540" y="1380" text-anchor="middle" class="t" fill="#fff" font-weight="800" font-size="42">@megabatken</text>
  <text x="540" y="1480" text-anchor="middle" class="t" fill="#fff" font-weight="700" font-size="36">+996 776 66 85 80</text>
  <text x="540" y="1750" text-anchor="middle" class="t" fill="#ffffff" font-weight="600" font-size="28" opacity="0.85">{k["story_footer"]}</text>""",
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
  <text x="400" y="280" text-anchor="middle" class="t" fill="#e85d4c" font-weight="700" font-size="44">{k["hours_until"]}</text>
  <text x="400" y="330" text-anchor="middle" class="t" fill="#a0aec0" font-weight="600" font-size="26">{k["sticker_footer"]}</text>""",
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
  <text x="240" y="95" text-anchor="middle" class="t" fill="#0f1419" font-weight="800" font-size="36">{k["price_new"]}</text>
  <text x="240" y="155" text-anchor="middle" class="t" fill="#718096" font-weight="700" font-size="28">{k["price_sub"]}</text>""",
        "0 0 480 200",
        480,
        200,
    )
    w("price-tag-generic.svg", tag)

    facebook = svg_wrap(
        "Facebook / link preview 1200x630",
        f"""<defs>
    <style type="text/css"><![CDATA[
{FONT_IMPORT}
{STYLE_T}
      .xl {{ font-weight: 800; font-size: 88px; }}
      .md {{ font-weight: 700; font-size: 34px; fill: #4a5568; }}
      .sm {{ font-weight: 600; font-size: 28px; fill: #0f1419; }}
      .acc {{ fill: #e85d4c; font-weight: 800; }}
    ]]></style>
    <linearGradient id="fb" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#faf8f5"/>
      <stop offset="1" stop-color="#ebe4d9"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="630" fill="url(#fb)"/>
  <rect x="0" y="0" width="20" height="630" fill="#e85d4c"/>
  <text x="60" y="160" class="t xl" fill="#0f1419">Mega</text>
  <text x="280" y="160" class="t xl acc">Kids</text>
  <text x="60" y="240" class="t md">{k["banner_sub"]}</text>
  <text x="60" y="310" class="t sm">{k["mega_building_caption"]}</text>
  <text x="60" y="380" class="t sm acc">{k["open_exc"]}</text>
  <text x="60" y="460" class="t sm">{k["samat_addr"]} \u00b7 {k["hours_open"]}</text>
  <text x="60" y="520" class="t sm acc">@megabatken</text>
  <text x="60" y="575" class="t sm">+996 776 66 85 80</text>""",
        "0 0 1200 630",
        1200,
        630,
    )
    w("facebook-1200x630.svg", facebook)


if __name__ == "__main__":
    main()
