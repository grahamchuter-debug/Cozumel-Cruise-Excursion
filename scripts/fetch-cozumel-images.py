#!/usr/bin/env python3
"""Download Unsplash assets still managed by this script.

Wikimedia remediations for tequila/ATV/catamaran/beach assets are documented in
images/ATTRIBUTION.md and are not overwritten here.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

DOWNLOADS: list[tuple[str, str, int]] = [
    ("cozumel-jeep-tour.png", "bHavJvvmcAU", 1920),
    ("cozumel-mayan-ruins.png", "PsgyWVeJjOA", 1920),
]


def download(filename: str, slug: str, width: int) -> bool:
    dest = IMAGES / filename
    url = f"https://unsplash.com/photos/{slug}/download?force=true&w={width}"
    print(f"  {filename} <- {slug}")
    result = subprocess.run(
        ["curl", "-fsSL", "-o", str(dest), url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"    FAILED: {result.stderr.strip()}", file=sys.stderr)
        return False
    size = dest.stat().st_size
    if size < 10_000:
        print(f"    WARNING: small file ({size} bytes)", file=sys.stderr)
    print(f"    OK ({size // 1024} KB)")
    return True


def main() -> None:
    IMAGES.mkdir(exist_ok=True)
    print("Downloading Unsplash images for Cozumel…")
    failed = 0
    for filename, slug, width in DOWNLOADS:
        if not download(filename, slug, width):
            failed += 1
    if failed:
        raise SystemExit(f"{failed} download(s) failed.")
    print("Done. See images/ATTRIBUTION.md for Wikimedia assets.")


if __name__ == "__main__":
    main()
