#!/usr/bin/env python3
"""Copy the RoutineFlow template catalog from the Xcode project into routineflow/templates.json.

The app is the single source of truth (RoutineFlow/Templates/Templates.swift for steps,
icons and durations, Localizable.xcstrings for English and French names). Run this after
changing the catalog in the app, then `python3 build.py`.

    python3 sync_routineflow_templates.py [path/to/RoutineFlow]   # default: ../RoutineFlow
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
APP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "..", "RoutineFlow")
SWIFT = os.path.join(APP, "RoutineFlow", "Templates", "Templates.swift")
STRINGS = os.path.join(APP, "RoutineFlow", "Localizable.xcstrings")
OUT = os.path.join(ROOT, "routineflow", "templates.json")


def translations(strings, key):
    loc = strings[key]["localizations"]
    return {lang: loc[lang]["stringUnit"]["value"] for lang in ("en", "fr")}


def main():
    with open(SWIFT, encoding="utf-8") as f:
        swift = f.read()
    with open(STRINGS, encoding="utf-8") as f:
        strings = json.load(f)["strings"]

    templates = []
    for body in re.findall(r"RoutineTemplate\((.*?)\]\)", swift, re.S):
        field = lambda key: re.search(rf'{key}: "([^"]+)"', body).group(1)
        tid = field("id")
        steps = []
        for kind, key, icon, minutes in re.findall(
                r'\.(timed|ownPace)\("([^"]+)", "([^"]+)"(?:, minutes: ([\d.]+))?\)', body):
            timed = kind == "timed"
            steps.append({
                "name": translations(strings, key),
                "icon": icon,
                "seconds": int(float(minutes) * 60) if timed else 60,
                "timed": timed,
            })
        category = re.search(r"category: \.(\w+)", body).group(1)
        templates.append({
            "id": tid,
            "category": category,
            "category_name": translations(strings, f"template.category.{category}"),
            "icon": field("icon"),
            "color": field("colorHex"),
            "premium": "isPremium: true" in body,
            "name": translations(strings, f"template.{tid}.name"),
            "pitch": translations(strings, f"template.{tid}.pitch"),
            "steps": steps,
        })

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(templates, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"  ✓ routineflow/templates.json ({len(templates)} templates)")


if __name__ == "__main__":
    main()
