#!/usr/bin/env python3
"""Tell IndexNow (Bing, Yandex, Seznam, Naver) which pages changed, after a push is live.

Usage (from this folder, once GitHub Pages has published the push):
  python3 indexnow.py              pages whose sitemap <lastmod> is today
  python3 indexnow.py 2026-11-12   pages changed on that day
  python3 indexnow.py --all        every page of the sitemap (first submission)
  python3 indexnow.py --dry-run …  list the URLs without sending them

Google does not use IndexNow: new pages still need "Request indexing" in Search Console.
"""
import datetime, json, os, re, sys, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.abspath(__file__))
HOST = "suiteforge.app"
ENDPOINT = "https://api.indexnow.org/indexnow"


def key():
    m = re.search(r'INDEXNOW_KEY = "([0-9a-f]+)"', open(os.path.join(ROOT, "build.py"), encoding="utf-8").read())
    return m.group(1)


def sitemap_urls():
    xml = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    return re.findall(r"<url><loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", xml)


def main(argv):
    dry = "--dry-run" in argv
    args = [a for a in argv if a != "--dry-run"]
    urls = sitemap_urls()
    if args and args[0] == "--all":
        chosen = [u for u, _ in urls]
    else:
        day = args[0] if args else datetime.date.today().isoformat()
        chosen = [u for u, d in urls if d == day]
    if not chosen:
        print("No page changed on that day: nothing to send.")
        return 0
    print(f"{len(chosen)} URL(s)")
    if dry:
        print("\n".join(chosen))
        return 0
    k = key()
    body = json.dumps({"host": HOST, "key": k, "keyLocation": f"https://{HOST}/{k}.txt", "urlList": chosen}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"IndexNow: HTTP {resp.status} (200 or 202 = accepted)")
            return 0
    except urllib.error.HTTPError as e:
        print(f"IndexNow: HTTP {e.code} {e.read().decode('utf-8', 'replace')[:300]}")
        print("403 = key file not reachable yet (wait for GitHub Pages); 422 = URL outside the host or bad key.")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
