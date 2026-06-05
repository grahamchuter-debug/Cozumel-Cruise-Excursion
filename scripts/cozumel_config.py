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
    "Turquoise Caribbean water along a Cozumel beach with a cruise ship visible "
    "near the Cozumel Mexico cruise port"
)
PORT_IMG = "images/cozumel-cruise-port.png"
PORT_ALT = (
    "Cozumel Mexico cruise port with passenger ship docked at pier and "
    "turquoise Caribbean water along the waterfront"
)
BEST_IMG = "images/best-cozumel-excursions.png"
BEST_ALT = (
    "Best Cozumel shore excursions for cruise passengers including snorkeling, "
    "beach clubs and Mayan ruins tours"
)
ONE_DAY_IMG = "images/one-day-cozumel.png"
ONE_DAY_ALT = (
    "One day Cozumel cruise port itinerary with beach, snorkeling and downtown "
    "shopping for cruise passengers"
)
INTRO_IMG = "images/cozumel-intro.png"
INTRO_ALT = (
    "Cozumel Mexico overview for cruise passengers with reef snorkeling, "
    "beach clubs and San Miguel downtown"
)
BEACHES_IMG = "images/cozumel-beaches.png"
BEACHES_ALT = (
    "Cozumel beach club with clear turquoise water, loungers and palm trees "
    "for cruise passenger beach day excursions"
)

BEST_OF_IMG = "images/best-of-cozumel.png"
BEST_OF_ALT = (
    "Best of Cozumel shore excursion combining beaches, Mayan heritage and "
    "downtown Cozumel for cruise passengers"
)
BEACH_DAY_IMG = "images/cozumel-beach-day.png"
BEACH_DAY_ALT = (
    "Cruise passengers relaxing on a Cozumel beach day excursion with "
    "crystal clear Caribbean water and loungers"
)
SNORKEL_IMG = "images/cozumel-snorkeling.png"
SNORKEL_ALT = (
    "Snorkelers exploring colorful coral reef and tropical fish in clear "
    "Cozumel Mexico waters on a cruise shore excursion"
)
CHANKANAAB_IMG = "images/chankanaab-park.png"
CHANKANAAB_ALT = (
    "Chankanaab National Marine Park lagoon and beach in Cozumel Mexico "
    "popular with cruise passengers"
)
MR_SANCHOS_IMG = "images/mr-sanchos.png"
MR_SANCHOS_ALT = (
    "Mr Sanchos Beach Club pool and loungers on the west coast of Cozumel "
    "Mexico for cruise passenger beach days"
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
    "Catamaran sailing across turquoise Caribbean water off Cozumel Mexico "
    "with snorkel excursion guests aboard"
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
    "Private island beach escape near Cozumel Mexico with white sand and "
    "turquoise water for cruise passengers"
)
SCUBA_IMG = "images/cozumel-scuba.png"
SCUBA_ALT = (
    "Scuba diver exploring coral reef underwater near Cozumel Mexico on a "
    "cruise passenger diving excursion"
)

ALL_IMAGES = [
    HOME_HERO, PORT_IMG, BEST_IMG, ONE_DAY_IMG, INTRO_IMG, BEACHES_IMG,
    BEST_OF_IMG, BEACH_DAY_IMG, SNORKEL_IMG, CHANKANAAB_IMG, MR_SANCHOS_IMG,
    JEEP_IMG, RUINS_IMG, CATAMARAN_IMG, ATV_IMG, TEQUILA_IMG,
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
