#!/usr/bin/env python3
"""Download hero and content images from Unsplash (Unsplash License)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

CUSTOM_IMAGES: frozenset[str] = frozenset({
    "hero-cozumel.png",
    "cozumel-intro.png",
    "best-cozumel-excursions.png",
    "one-day-cozumel.png",
    "best-of-cozumel.png",
    "cozumel-beaches.png",
    "cozumel-beach-day.png",
    "cozumel-beach-crystal.png",
    "cozumel-snorkeling.png",
    "cozumel-scuba.png",
    "chankanaab-park.png",
    "mr-sanchos.png",
    "cozumel-catamaran.png",
    "cozumel-private-island.png",
    "cozumel-cruise-port.png",
    "cozumel-cruise-port-arrival.png",
    "el-cielo-sandbar.png",
})

DOWNLOADS: list[tuple[str, str, int]] = [
    ("cozumel-jeep-tour.png", "bHavJvvmcAU", 1920),
    ("cozumel-mayan-ruins.png", "PsgyWVeJjOA", 1920),
    ("cozumel-atv.png", "bHavJvvmcAU", 1920),
    ("cozumel-tequila.png", "PsgyWVeJjOA", 1920),
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
