#!/usr/bin/env python3
"""Build dist/intake-output.html from src/tracker.html.

The only difference between the two is Chart.js: the source loads it from a CDN
so the file stays small and readable in diffs, and the build inlines it so the
distributed file works with no internet connection at all.

    python3 build/build.py            # build
    python3 build/build.py --check    # verify dist matches src, change nothing

Chart.js is fetched from npm the first time and cached in build/vendor/.
"""
import argparse
import pathlib
import subprocess
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "tracker.html"
DIST = ROOT / "dist" / "intake-output.html"
VENDOR = ROOT / "build" / "vendor" / "chart.umd.js"

CHART_VERSION = "4.4.1"
CDN_TAG = (
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/'
    f'{CHART_VERSION}/chart.umd.min.js"></script>'
)
BANNER = (
    f"<!-- Chart.js {CHART_VERSION} (MIT), inlined so this file works "
    "with no internet connection -->"
)


def chart_source() -> str:
    """The Chart.js UMD bundle, from the local cache or npm."""
    if VENDOR.exists():
        return VENDOR.read_text(encoding="utf-8")

    VENDOR.parent.mkdir(parents=True, exist_ok=True)
    url = f"https://cdn.jsdelivr.net/npm/chart.js@{CHART_VERSION}/dist/chart.umd.js"
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            text = r.read().decode("utf-8")
    except Exception:
        # no direct network: fall back to npm, which most environments allow
        subprocess.run(
            ["npm", "pack", f"chart.js@{CHART_VERSION}", "--quiet"],
            cwd=VENDOR.parent, check=True,
        )
        tgz = next(VENDOR.parent.glob("chart.js-*.tgz"))
        subprocess.run(["tar", "-xzf", tgz.name], cwd=VENDOR.parent, check=True)
        text = (VENDOR.parent / "package" / "dist" / "chart.umd.js").read_text(encoding="utf-8")

    VENDOR.write_text(text, encoding="utf-8")
    return text


def build() -> str:
    src = SRC.read_text(encoding="utf-8")
    if src.count(CDN_TAG) != 1:
        sys.exit(f"expected exactly one Chart.js script tag in {SRC}")

    lib = chart_source()
    if "</script" in lib.lower():
        sys.exit("the library contains a closing script tag and cannot be inlined as is")

    return src.replace(CDN_TAG, f"{BANNER}\n<script>{lib}\n</script>")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if dist is out of date; write nothing")
    args = ap.parse_args()

    out = build()

    if args.check:
        current = DIST.read_text(encoding="utf-8") if DIST.exists() else ""
        if current != out:
            sys.exit("dist/intake-output.html is out of date: run python3 build/build.py")
        print("dist is up to date")
        return

    DIST.parent.mkdir(parents=True, exist_ok=True)
    DIST.write_text(out, encoding="utf-8")
    print(f"wrote {DIST.relative_to(ROOT)} ({len(out):,} bytes)")


if __name__ == "__main__":
    main()
