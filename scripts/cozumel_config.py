"""Cozumel Cruise Excursion site configuration."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://cozumelcruiseexcursion.com"
SITE = "Cozumel Cruise Excursion"
DATE = "2026-06-05"
FONTS = (
    "https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700"
    "&family=Source+Sans+3:wght@400;500;600;700&display=swap"
)
HERO_GRADIENT = (
    "linear-gradient(135deg, rgba(37, 99, 235, 0.75) 0%, "
    "rgba(249, 115, 22, 0.65) 50%, rgba(30, 58, 138, 0.55) 100%)"
)
ACCENT = "text-pr-300"

HOME_HERO = "images/hero-cozumel.png"
HOME_HERO_ALT = (
    "Cozumel Mexico beach signpost with colorful destination arrows and turquoise "
    "Caribbean water along the white sand shoreline"
)
PORT_IMG = "images/cozumel-cruise-port.png"
PORT_ALT = (
    "Colorful Cozumel Mexico cruise port sign with Royal Caribbean ship docked "
    "at the pier for cruise passenger shore excursions"
)
PORT_ARRIVAL_IMG = "images/cozumel-cruise-port-arrival.png"
PORT_ARRIVAL_ALT = (
    "Royal Caribbean cruise ship docked at Cozumel Mexico cruise port pier with "
    "turquoise Caribbean water and tropical shoreline for cruise passengers"
)
BEST_IMG = "images/best-cozumel-excursions.png"
BEST_ALT = (
    "Cozumel Mexico beach signpost with turquoise Caribbean water representing "
    "best shore excursions for cruise passengers"
)
ONE_DAY_IMG = "images/one-day-cozumel.png"
ONE_DAY_ALT = (
    "Cozumel Mexico beach signpost overlooking turquoise Caribbean water for "
    "cruise passenger one-day port itineraries"
)
INTRO_IMG = "images/cozumel-intro.png"
INTRO_ALT = (
    "Iconic Cozumel Mexico beach signpost with turquoise Caribbean water and "
    "white sand for cruise passenger shore excursion planning"
)
BEACHES_IMG = "images/cozumel-beaches.png"
BEACHES_ALT = (
    "Sunny Cozumel Mexico beach with palm trees, wooden lounge chairs and "
    "turquoise Caribbean water for cruise passenger beach days"
)
CRYSTAL_IMG = "images/cozumel-beach-crystal.png"
CRYSTAL_ALT = (
    "Crystal clear shallow turquoise water with white sandy seafloor in Cozumel "
    "Mexico ideal for cruise passenger beach and snorkel excursions"
)

BEST_OF_IMG = "images/best-of-cozumel.png"
BEST_OF_ALT = (
    "Colorful Cozumel Mexico cruise port sign with Royal Caribbean ship docked "
    "at the pier on a best-of Cozumel shore excursion for cruise passengers"
)
BEACH_DAY_IMG = "images/cozumel-beach-day.png"
BEACH_DAY_ALT = (
    "Sunny white sand beach in Cozumel Mexico with palm trees, wooden lounge "
    "chairs and turquoise Caribbean water on a cruise beach day excursion"
)
SNORKEL_IMG = "images/cozumel-snorkeling.png"
SNORKEL_ALT = (
    "Cruise passengers snorkeling in crystal-clear Cozumel Mexico water surrounded "
    "by a school of colorful tropical fish on a reef shore excursion"
)
CHANKANAAB_IMG = "images/chankanaab-park.png"
CHANKANAAB_ALT = (
    "Welcome to Chankanaab Park entrance booth with thatched palapa roof, "
    "tropical palm trees and paved roadway for Cozumel Mexico cruise passengers"
)
MR_SANCHOS_IMG = "images/mr-sanchos.png"
MR_SANCHOS_ALT = (
    "Tropical beach club setting in Cozumel Mexico with palm trees, loungers and "
    "turquoise Caribbean water for Mr Sanchos-style cruise beach days"
)
JEEP_IMG = "images/cozumel-jeep-tour.png"
JEEP_ALT = (
    "Open-top jeep driving a coastal road on Cozumel Mexico island adventure "
    "tour for cruise passengers"
)
RUINS_IMG = "images/cozumel-mayan-ruins.png"
RUINS_ALT = (
    "San Gervasio Mayan ruins archaeological site in Cozumel Mexico on a "
    "cruise shore excursion tour"
)
CATAMARAN_IMG = "images/cozumel-catamaran.png"
CATAMARAN_ALT = (
    "Crystal clear turquoise Caribbean water off Cozumel Mexico for catamaran "
    "sail and snorkel cruise shore excursions"
)
EL_CIELO_IMG = "images/el-cielo-sandbar.png"
EL_CIELO_ALT = (
    "Starfish on white sand at El Cielo sandbar in Cozumel Mexico shallow "
    "turquoise water on a cruise passenger snorkel excursion"
)
ATV_IMG = "images/cozumel-atv.png"
ATV_ALT = (
    "ATV adventure tour through jungle trails on Cozumel Mexico island for "
    "cruise passenger shore excursions"
)
TEQUILA_IMG = "images/cozumel-tequila.png"
TEQUILA_ALT = (
    "Tequila tasting setup with agave spirits at a Cozumel Mexico hacienda "
    "on a cruise passenger cultural tour"
)
PRIVATE_ISLAND_IMG = "images/cozumel-private-island.png"
PRIVATE_ISLAND_ALT = (
    "Crystal clear shallow turquoise water near Cozumel Mexico for private "
    "island and sandbar cruise shore excursions"
)
SCUBA_IMG = "images/cozumel-scuba.png"
SCUBA_ALT = (
    "Underwater coral reef dive site in Cozumel Mexico with tropical fish and "
    "sunlit clear water on a cruise scuba excursion"
)

ALL_IMAGES = [
    HOME_HERO, PORT_IMG, PORT_ARRIVAL_IMG, BEST_IMG, ONE_DAY_IMG, INTRO_IMG, BEACHES_IMG,
    CRYSTAL_IMG, BEST_OF_IMG, BEACH_DAY_IMG, SNORKEL_IMG, CHANKANAAB_IMG,
    MR_SANCHOS_IMG, JEEP_IMG, RUINS_IMG, CATAMARAN_IMG, EL_CIELO_IMG, ATV_IMG, TEQUILA_IMG,
    PRIVATE_ISLAND_IMG, SCUBA_IMG,
]

SITEMAP_PAGES = [
    ("", "1.0", "weekly"),
    ("best-cozumel-shore-excursions.html", "0.9", "monthly"),
    ("cozumel-port-guide.html", "0.8", "monthly"),
    ("one-day-in-cozumel-from-a-cruise-ship.html", "0.8", "monthly"),
    ("best-cozumel-beaches-for-cruise-passengers.html", "0.8", "monthly"),
    ("is-cozumel-safe-for-cruise-passengers.html", "0.8", "monthly"),
    ("can-you-explore-cozumel-without-an-excursion.html", "0.8", "monthly"),
    ("cozumel-cruise-port-map.html", "0.8", "monthly"),
    ("chankanaab-park-guide.html", "0.8", "monthly"),
    ("mr-sanchos-cozumel-guide.html", "0.8", "monthly"),
    ("best-of-cozumel.html", "0.9", "monthly"),
    ("cozumel-beach-day.html", "0.9", "monthly"),
    ("cozumel-snorkeling-tour.html", "0.9", "monthly"),
    ("chankanaab-park-tour.html", "0.9", "monthly"),
    ("mr-sanchos-beach-club.html", "0.9", "monthly"),
    ("cozumel-jeep-tour.html", "0.9", "monthly"),
    ("cozumel-mayan-ruins-tour.html", "0.9", "monthly"),
    ("cozumel-catamaran-sail-and-snorkel.html", "0.9", "monthly"),
    ("cozumel-atv-adventure.html", "0.9", "monthly"),
    ("cozumel-tequila-tasting-tour.html", "0.9", "monthly"),
    ("cozumel-private-island-tour.html", "0.9", "monthly"),
    ("cozumel-scuba-diving-tour.html", "0.9", "monthly"),
]

SHIP_ICON = (
    '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">'
    '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" '
    'd="M3 17h18M5 17l2-8h10l2 8M9 9l1-4h4l1 4"/></svg>'
)

PLACEHOLDER_PNG = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
    b"\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
    b"\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n"
    b"\xdb\x00\x00\x00\x00IEND\xaeB`\x82"
)

TOUR_PAGES = [
    "best-of-cozumel",
    "cozumel-beach-day",
    "cozumel-snorkeling-tour",
    "chankanaab-park-tour",
    "mr-sanchos-beach-club",
    "cozumel-jeep-tour",
    "cozumel-mayan-ruins-tour",
    "cozumel-catamaran-sail-and-snorkel",
    "cozumel-atv-adventure",
    "cozumel-tequila-tasting-tour",
    "cozumel-private-island-tour",
    "cozumel-scuba-diving-tour",
]

GUIDE_PAGES = [
    "cozumel-port-guide",
    "one-day-in-cozumel-from-a-cruise-ship",
    "best-cozumel-shore-excursions",
    "best-cozumel-beaches-for-cruise-passengers",
    "is-cozumel-safe-for-cruise-passengers",
    "can-you-explore-cozumel-without-an-excursion",
    "cozumel-cruise-port-map",
    "chankanaab-park-guide",
    "mr-sanchos-cozumel-guide",
]
