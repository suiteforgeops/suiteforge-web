#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Optimize App Store screenshots into web-friendly WebPs.

For each app:
  1. Find the "home" screen (filename contains 'home' or 'today',
     case-insensitive; 'home' wins if both exist).
     -> encode as hero-home.webp (~680 px wide, q=84, target < 120 KB).
  2. Take the first 5 sorted EN sources, drop the home if present,
     keep up to 5 -> encode each as shot-N.webp
     (~620 px wide, q=82, target < 90 KB).

Skips an app silently if its source/en/ folder is empty.
Idempotent: re-running overwrites outputs and cleans stale shot-*.webp.
Never touches source/ files.
"""
import os, glob, re, sys
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
APPS = ["fastclear", "routineflow", "walkquest", "keepcontact", "jezko"]

CAROUSEL = dict(max_width=620, target_bytes=90 * 1024, start_q=82, min_q=50, step=4, max_count=5)
# Per-app carousel size override (sources sorted; the home screen is removed)
MAX_COUNT = {"keepcontact": 6, "jezko": 9}
HERO     = dict(max_width=680, target_bytes=120 * 1024, start_q=84, min_q=50, step=4)


def sorted_sources(app):
    p = os.path.join(ROOT, app, "screenshots", "source", "en")
    if not os.path.isdir(p):
        return []
    files = []
    for ext in ("png", "PNG", "jpg", "jpeg", "JPG", "JPEG"):
        files.extend(glob.glob(os.path.join(p, f"*.{ext}")))
    return sorted(set(files), key=lambda f: os.path.basename(f).lower())


def pick_home(srcs):
    """Return the home/today source, preferring 'home' over 'today' if both exist."""
    home = [f for f in srcs if re.search(r"home", os.path.basename(f), re.I)]
    if home:
        return home[0]
    today = [f for f in srcs if re.search(r"today", os.path.basename(f), re.I)]
    return today[0] if today else None


def encode(src_path, out_path, cfg):
    im = Image.open(src_path)
    if im.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGB", im.size, (255, 255, 255))
        im = im.convert("RGBA")
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    w, h = im.size
    if w > cfg["max_width"]:
        new_h = round(h * cfg["max_width"] / w)
        im = im.resize((cfg["max_width"], new_h), Image.LANCZOS)
        w, h = im.size
    q = cfg["start_q"]
    while True:
        im.save(out_path, "WEBP", quality=q, method=6)
        size = os.path.getsize(out_path)
        if size <= cfg["target_bytes"] or q <= cfg["min_q"]:
            return (w, h, size, q)
        q -= cfg["step"]


def main():
    print(f"{'App':<14} {'Role':<10} {'#':>2} {'WxH':>11} {'KB':>7} {'q':>3}  source")
    print("-" * 96)
    summary = {}
    for slug in sys.argv[1:] or APPS:  # optional: only the apps named on the command line
        srcs = sorted_sources(slug)
        if not srcs:
            print(f"{slug:<14} (no sources)")
            continue
        out_dir = os.path.join(ROOT, slug, "screenshots")
        # Clean previous outputs (preserve source/)
        for old in glob.glob(os.path.join(out_dir, "shot-*.webp")):
            os.remove(old)
        for old in glob.glob(os.path.join(out_dir, "hero-home.webp")):
            os.remove(old)

        # 1. Hero
        hero_src = pick_home(srcs)
        if hero_src:
            out = os.path.join(out_dir, "hero-home.webp")
            w, h, size, q = encode(hero_src, out, HERO)
            print(f"{slug:<14} {'HERO':<10}  - {w}x{h:<7} {size/1024:>7.1f} {q:>3}  {os.path.basename(hero_src)}")
            summary.setdefault(slug, {})["hero"] = (w, h, size, os.path.basename(hero_src))

        # 2. Carrousel: first 5 sorted, minus the home
        candidates = srcs[: MAX_COUNT.get(slug, CAROUSEL["max_count"])]
        if hero_src and hero_src in candidates:
            candidates = [c for c in candidates if c != hero_src]
        carousel_total = 0
        carousel_items = []
        for i, src in enumerate(candidates, 1):
            out = os.path.join(out_dir, f"shot-{i}.webp")
            w, h, size, q = encode(src, out, CAROUSEL)
            carousel_total += size
            carousel_items.append((i, w, h, size, os.path.basename(src)))
            print(f"{slug:<14} {'shot':<10} {i:>2} {w}x{h:<7} {size/1024:>7.1f} {q:>3}  {os.path.basename(src)}")
        summary.setdefault(slug, {})["carousel"] = carousel_items
        summary[slug]["carousel_kb"] = carousel_total / 1024

    print("-" * 96)
    print("SUMMARY")
    grand = 0
    for slug, data in summary.items():
        hero = data.get("hero")
        car_kb = data.get("carousel_kb", 0)
        n_shots = len(data.get("carousel", []))
        if hero:
            hw, hh, hb, hname = hero
            grand += hb
            print(f"  {slug:<14} hero={hb/1024:>6.1f} KB ({hw}x{hh}, {hname}) + {n_shots} shots={car_kb:.1f} KB")
        else:
            print(f"  {slug:<14} (no hero) + {n_shots} shots={car_kb:.1f} KB")
        grand += car_kb * 1024
    print(f"  GRAND TOTAL: {grand/1024:.1f} KB")


if __name__ == "__main__":
    main()
