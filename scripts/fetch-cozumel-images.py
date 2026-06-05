#!/usr/bin/env python3
"""Download hero and content images from Unsplash (Unsplash License)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

CUSTOM_IMAGES: frozenset[str] = frozenset()

DOWNLOADS: list[tuple[str, str, int]] = [
    ("hero-cozumel.png", "vYXrNeIpm3w", 1920),
    ("cozumel-cruise-port.png", "WOyBhxyB8KI", 1920),
    ("best-cozumel-excursions.png", "vYXrNeIpm3w", 1920),
    ("one-day-cozumel.png", "YZ8Jc6TiH2A", 1920),
    ("cozumel-intro.png", "vYXrNeIpm3w", 1920),
    ("cozumel-beaches.png", "WOyBhxyB8KI", 1920),
    ("best-of-cozumel.png", "vYXrNeIpm3w", 1920),
    ("cozumel-beach-day.png", "WOyBhxyB8KI", 1920),
    ("cozumel-snorkeling.png", "Q0HR_nrDkB8", 1920),
    ("chankanaab-park.png", "vYXrNeIpm3w", 1920),
    ("mr-sanchos.png", "WOyBhxyB8KI", 1920),
    ("cozumel-jeep-tour.png", "bHavJvvmcAU", 1920),
    ("cozumel-mayan-ruins.png", "PsgyWVeJjOA", 1920),
    ("cozumel-catamaran.png", "vYXrNeIpm3w", 1920),
    ("cozumel-atv.png", "bHavJvvmcAU", 1920),
    ("cozumel-tequila.png", "PsgyWVeJjOA", 1920),
    ("cozumel-private-island.png", "WOyBhxyB8KI", 1920),
    ("cozumel-scuba.png", "Q0HR_nrDkB8", 1920),
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
    IMAGES.mkdir(parents=True, exist_ok=True)
    print("Downloading Cozumel images from Unsplash…")
    failed = 0
    for filename, slug, width in DOWNLOADS:
        if filename in CUSTOM_IMAGES:
            continue
        if not download(filename, slug, width):
            failed += 1
    if failed:
        raise SystemExit(f"{failed} download(s) failed.")
    print("Done.")


if __name__ == "__main__":
    main()
