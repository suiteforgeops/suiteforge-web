#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract each app's real 1024x1024 App Store icon from its Xcode project,
encode it as 256x256 WebP at quality 90 (lowering by 4 until < 40 KB),
and write it to suiteforge-web/<app>/icon.webp.

Source Assets.xcassets are read-only. We never write inside the app projects.
Idempotent: re-running overwrites the WebP outputs.
"""
import os, sys, glob
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
APPS_ROOT = "/Users/nicolasdojcilovic/Desktop/Business/Applications/SuiteForgeApps"

# slug -> (absolute source PNG path)
SOURCES = {
    "fastclear":   f"{APPS_ROOT}/2.FastClear/Code/FastClear/Assets.xcassets/AppIcon.appiconset/AppIcon.png",
    "routineflow": f"{APPS_ROOT}/3.RoutineFlow/Code/RoutineFlow/Assets.xcassets/AppIcon.appiconset/AppIcon-Light.png",
    "walkquest":   f"{APPS_ROOT}/4.WalkQuest/Code/WalkQuest/Assets.xcassets/AppIcon.appiconset/AppIcon.png",
    "keepcontact": f"{APPS_ROOT}/1.KeepContact/Code/KeepContact/Assets.xcassets/AppIcon.appiconset/AppIcon_1024.png",
}

TARGET_SIDE = 256
TARGET_BYTES = 40 * 1024  # < 40 KB
START_Q = 90
MIN_Q = 60
STEP_Q = 4


def encode(src, out):
    im = Image.open(src)
    src_w, src_h = im.size
    # Keep the square crop, in case any source is non-square (Apple requires 1024x1024 though).
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        # Apple icons must be fully opaque per HIG, so we flatten on white
        # — but use sentinel pixel check: if there is no transparency anyway,
        # converting to RGB is identical. Flatten to be safe.
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    # Downscale to TARGET_SIDE x TARGET_SIDE (square)
    im = im.resize((TARGET_SIDE, TARGET_SIDE), Image.LANCZOS)
    q = START_Q
    while True:
        im.save(out, "WEBP", quality=q, method=6)
        size = os.path.getsize(out)
        if size <= TARGET_BYTES or q <= MIN_Q:
            return (src_w, src_h, size, q)
        q -= STEP_Q


def main():
    print(f"{'App':<14} {'src WxH':>10} {'KB':>7} {'q':>3}  source basename")
    print("-" * 78)
    grand = 0
    for slug, src in SOURCES.items():
        if not os.path.isfile(src):
            print(f"{slug:<14} (source not found: {src})")
            continue
        out = os.path.join(ROOT, slug, "icon.webp")
        sw, sh, size, q = encode(src, out)
        grand += size
        print(f"{slug:<14} {sw}x{sh:<6} {size/1024:>7.1f} {q:>3}  {os.path.basename(src)}")
    print("-" * 78)
    print(f"GRAND TOTAL: {grand/1024:.1f} KB")


if __name__ == "__main__":
    main()
