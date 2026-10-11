#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate per-app social share images (Open Graph / Twitter), 1200x630 PNG.

Output: <slug>/og.png — picked up automatically by build.py when present.
Inputs: <slug>/screenshots/source/en/<hero> and the app icon from Xcode
(same source as optimize_icons.py). Fonts: SF Pro Rounded (macOS system font).
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.abspath(__file__))
APPS_ROOT = "/Users/nicolasdojcilovic/Desktop/Business/Applications/SuiteForgeApps"
FONT = "/System/Library/Fonts/SFNSRounded.ttf"

W, H = 1200, 630

OG = {
    "keepcontact": {
        "bg": (107, 63, 212),          # #6B3FD4 — icon violet
        "glow": (255, 122, 89),        # #FF7A59 — coral
        "soft": (226, 214, 250),       # light violet for secondary text
        "icon": f"{APPS_ROOT}/1.KeepContact/Code/KeepContact/Assets.xcassets/AppIcon.appiconset/AppIcon_1024.png",
        "shot": "screenshots/source/en/01 Home.png",
        "name": "KeepContact",
        "title": ["Stay close to the", "people who matter."],
        "sub": "Private personal CRM for iPhone",
        "chips": ["On-device AI", "No account", "100% offline"],
    },
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

    d = ImageDraw.Draw(img)
    x = 72

    # Icon + app name
    icon = Image.open(c["icon"]).convert("RGBA").resize((96, 96), Image.LANCZOS)
    icon = rounded(icon, 22)
    ring = rounded(Image.new("RGBA", (104, 104), (255, 255, 255, 70)), 26)
    img.alpha_composite(ring, (x - 4, 76))
    img.alpha_composite(icon, (x, 80))
    d.text((x + 120, 128), c["name"], font=font(46), fill="white", anchor="lm")

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

    out = os.path.join(ROOT, slug, "og.png")
    img.convert("RGB").save(out, "PNG", optimize=True)
    print(f"  ✓ {slug}/og.png  {os.path.getsize(out) / 1024:.0f} KB")


if __name__ == "__main__":
    for slug, cfg in OG.items():
        build(slug, cfg)
