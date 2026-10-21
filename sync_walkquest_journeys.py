#!/usr/bin/env python3
"""Copy the WalkQuest journey catalog from the Xcode project into walkquest/journeys.json.

The app is the single source of truth (WalkQuest/Journeys/Journey.swift for routes and
stages, Localizable.xcstrings for English and French names). Run this after changing the
catalog in the app, then `python3 build.py`.

    python3 sync_walkquest_journeys.py [path/to/WalkQuest]   # default: ../WalkQuest
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
APP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "..", "WalkQuest")
SWIFT = os.path.join(APP, "WalkQuest", "Journeys", "Journey.swift")
STRINGS = os.path.join(APP, "WalkQuest", "Resources", "Localizable.xcstrings")
OUT = os.path.join(ROOT, "walkquest", "journeys.json")


def translations(strings, key):
    loc = strings[key]["localizations"]
    return {lang: loc[lang]["stringUnit"]["value"] for lang in ("en", "fr")}


def main():
    with open(SWIFT, encoding="utf-8") as f:
        swift = f.read()
    with open(STRINGS, encoding="utf-8") as f:
        strings = json.load(f)["strings"]

    blocks = dict(re.findall(r"static let (\w+) = Journey\((.*?)\n    \)\n", swift, re.S))
    order = re.search(r"static let all: \[Journey\] = \[(.*?)\]", swift, re.S).group(1)
    journeys = []
    for name in re.findall(r"\w+", order):
        body = blocks[name]
        field = lambda key: re.search(rf'{key}: "([^"]+)"', body).group(1)
        points = [[float(a), float(b)] for a, b in re.findall(r"GeoPoint\((-?[\d.]+), (-?[\d.]+)\)", body)]
        stages = [{"name": translations(strings, key), "point": int(i)}
                  for key, i in re.findall(r'\.init\(name: "([^"]+)", pointIndex: (\d+)\)', body)]
        journeys.append({
            "id": field("id"),
            "title": translations(strings, field("title")),
            "region": translations(strings, field("region")),
            "premium": "isPremium: true" in body,
            "points": points,
            "stages": stages,
        })

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(journeys, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"  ✓ walkquest/journeys.json ({len(journeys)} journeys)")


if __name__ == "__main__":
    main()
