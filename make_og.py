#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate per-app social share images (Open Graph / Twitter), 1200x630 PNG.

Output: <slug>/og.png — picked up automatically by build.py when present —
plus assets/og-suiteforge.png for the home page (all four icons, no phone).
Inputs: <slug>/screenshots/source/en/<hero> and the app icons from Xcode
(same sources as optimize_icons.py). Font: SF Pro Rounded (macOS system font).
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from optimize_icons import SOURCES as ICONS

ROOT = os.path.dirname(os.path.abspath(__file__))
APPS_ROOT = "/Users/nicolasdojcilovic/Desktop/Business/Applications/SuiteForgeApps"
FONT = "/System/Library/Fonts/SFNSRounded.ttf"

W, H = 1200, 630

OG = {
    "keepcontact": {
        "bg": (107, 63, 212),          # #6B3FD4 — icon violet
        "glow": (255, 122, 89),        # #FF7A59 — coral
        "soft": (226, 214, 250),       # light violet for secondary text
        "shot": "screenshots/source/en/01 Home.png",
        "name": "KeepContact",
        "title": ["Stay close to the", "people who matter."],
        "sub": "Private personal CRM for iPhone",
        "chips": ["On-device AI", "No account", "100% offline"],
    },
    "fastclear": {
        "bg": (21, 122, 66),           # #157A42 — deep icon green (white text stays legible)
        "glow": (52, 199, 89),         # #34C759 — icon green
        "soft": (205, 238, 216),
        "shot": "screenshots/source/en/1_home_en.png",
        "name": "FastClear",
        "title": ["A calm timer for", "intermittent fasting."],
        "sub": "Private fasting tracker for iPhone",
        "chips": ["16:8 · 18:6 · OMAD", "No account", "No tracking"],
    },
    "routineflow": {
        "bg": (28, 28, 30),            # #1C1C1E — icon background
        "glow": (232, 130, 30),        # #E8821E — icon orange
        "soft": (214, 210, 204),
        "shot": "screenshots/source/en/01_home_en.png",
        "name": "RoutineFlow",
        "title": ["A morning routine", "that actually sticks."],
        "sub": "One calm step at a time, on iPhone",
        "chips": ["Step by step", "No account", "No tracking"],
    },
    "walkquest": {
        "bg": (26, 46, 75),            # #1A2E4B — icon navy
        "glow": (255, 189, 26),        # #FFBD1A — icon gold
        "soft": (208, 218, 233),
        "shot": "screenshots/source/en/1. Today EN.png",
        "name": "WalkQuest",
        "title": ["Turn your daily steps", "into a quiet quest."],
        "sub": "Private step challenges for iPhone",
        "chips": ["Apple Health steps", "No account", "No tracking"],
    },
}

# Home page: the house brand (sage) and the four app icons
HOUSE = {
    "bg": (60, 86, 72),                # #3C5648 — site accent-deep
    "glow": (127, 168, 145),
    "soft": (220, 232, 224),
    "apps": ["keepcontact", "fastclear", "routineflow", "walkquest"],
    "name": "SuiteForge",
    "title": ["Apps for a calmer,", "quieter life."],
    "sub": "Privacy-first iPhone apps",
    "chips": ["No accounts", "No tracking", "On your device"],
}


def font(size, weight="Bold"):
    f = ImageFont.truetype(FONT, size)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass
    return f


def rounded(im, radius):
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, *im.size), radius, fill=255)
    out = Image.new("RGBA", im.size, (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    return out


def build(slug, c):
    img = Image.new("RGBA", (W, H), c["bg"] + (255,))

    # Soft coral glow behind the phone
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((760, 120, 1260, 620), fill=c["glow"] + (150,))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(110)))

    # Phone: real Home screenshot in a dark bezel, bleeding off the bottom edge
    shot = Image.open(os.path.join(ROOT, slug, c["shot"])).convert("RGB")
    sw = 360
    shot = shot.resize((sw, round(shot.height * sw / shot.width)), Image.LANCZOS)
    bezel = 14
    phone = Image.new("RGBA", (sw + 2 * bezel, shot.height + 2 * bezel), (24, 18, 38, 255))
    phone = rounded(phone, 62)
    phone.alpha_composite(rounded(shot.convert("RGBA"), 50), (bezel, bezel))
    px, py = 790, 70
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle(
        (px + 10, py + 24, px + phone.width + 10, py + phone.height + 24), 62, fill=(20, 8, 50, 120))
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(26)))
    img.alpha_composite(phone, (px, py))

    icon = rounded(Image.open(ICONS[slug]).convert("RGBA").resize((96, 96), Image.LANCZOS), 22)
    text_block(img, c, icon)
    save(img, os.path.join(ROOT, slug, "og.png"))


def text_block(img, c, icon=None):
    """Left column: icon + name, two-line headline, subtitle, chips."""
    d = ImageDraw.Draw(img)
    x = 72

    if icon is not None:
        ring = rounded(Image.new("RGBA", (104, 104), (255, 255, 255, 70)), 26)
        img.alpha_composite(ring, (x - 4, 76))
        img.alpha_composite(icon, (x, 80))
        d.text((x + 120, 128), c["name"], font=font(46), fill="white", anchor="lm")
    else:
        d.text((x, 128), c["name"], font=font(46), fill="white", anchor="lm")

    # Headline
    y = 236
    for line in c["title"]:
        d.text((x, y), line, font=font(68), fill="white")
        y += 80

    d.text((x, y + 20), c["sub"], font=font(32, "Medium"), fill=c["soft"])

    # Chips
    cx, cy = x, y + 86
    f = font(24, "Semibold")
    # Translucent pills must be composited, not drawn straight onto the RGBA canvas
    pills = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pd = ImageDraw.Draw(pills)
    for chip in c["chips"]:
        tw = d.textlength(chip, font=f)
        pd.rounded_rectangle((cx, cy, cx + tw + 36, cy + 46), 23, fill=(255, 255, 255, 38),
                             outline=(255, 255, 255, 110), width=2)
        pd.text((cx + 18, cy + 23), chip, font=f, fill="white", anchor="lm")
        cx += tw + 36 + 12
    img.alpha_composite(pills)


def save(img, out):
    img.convert("RGB").save(out, "PNG", optimize=True)
    print(f"  ✓ {os.path.relpath(out, ROOT)}  {os.path.getsize(out) / 1024:.0f} KB")


def build_house(c):
    img = Image.new("RGBA", (W, H), c["bg"] + (255,))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((720, 80, 1240, 600), fill=c["glow"] + (140,))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(110)))

    # 2x2 grid of app icons with soft shadows
    size, gap = 170, 36
    gx, gy = 1200 - 72 - 2 * size - gap, (H - 2 * size - gap) // 2
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    for i, slug in enumerate(c["apps"]):
        x, y = gx + (i % 2) * (size + gap), gy + (i // 2) * (size + gap)
        sd.rounded_rectangle((x + 4, y + 14, x + size + 4, y + size + 14), 40, fill=(10, 20, 15, 110))
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(18)))
    for i, slug in enumerate(c["apps"]):
        x, y = gx + (i % 2) * (size + gap), gy + (i // 2) * (size + gap)
        icon = Image.open(ICONS[slug]).convert("RGBA").resize((size, size), Image.LANCZOS)
        img.alpha_composite(rounded(icon, 40), (x, y))

    text_block(img, c)
    save(img, os.path.join(ROOT, "assets", "og-suiteforge.png"))


if __name__ == "__main__":
    for slug, cfg in OG.items():
        build(slug, cfg)
    build_house(HOUSE)
