#!/usr/bin/env python3
"""Generate Cozumel Cruise Excursion static site files."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cozumel_config import (
    ACCENT,
    ALL_IMAGES,
    BEST_IMG,
    BEST_ALT,
    BEST_OF_IMG,
    BEST_OF_ALT,
    BEACH_DAY_IMG,
    BEACH_DAY_ALT,
    BEACHES_IMG,
    BEACHES_ALT,
    CATAMARAN_IMG,
    CATAMARAN_ALT,
    CHANKANAAB_IMG,
    CHANKANAAB_ALT,
    DATE,
    DOMAIN,
    HERO_GRADIENT,
    HOME_HERO,
    HOME_HERO_ALT,
    JEEP_IMG,
    JEEP_ALT,
    MR_SANCHOS_IMG,
    MR_SANCHOS_ALT,
    ONE_DAY_IMG,
    ONE_DAY_ALT,
    PLACEHOLDER_PNG,
    PORT_IMG,
    PORT_ALT,
    PRIVATE_ISLAND_IMG,
    PRIVATE_ISLAND_ALT,
    ROOT,
    RUINS_IMG,
    RUINS_ALT,
    SCUBA_IMG,
    SCUBA_ALT,
    SITE,
    SITEMAP_PAGES,
    SNORKEL_IMG,
    SNORKEL_ALT,
    ATV_IMG,
    ATV_ALT,
    TEQUILA_IMG,
    TEQUILA_ALT,
)
from cozumel_guides import all_guide_content, home_faq_data
from cozumel_helpers import hero_inner, hero_wave, home_schema, page_shell, tourist_trip_schema
from cozumel_tours import all_tour_content


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  wrote {path}")


def hero_home() -> str:
    return f"""  <section class="site-hero">
    <div class="absolute inset-0 hero-bg" style="background-image: {HERO_GRADIENT}, url('{HOME_HERO}');" role="img" aria-label="{HOME_HERO_ALT}"></div>
    <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
          <span class="w-2 h-2 rounded-full bg-pr-400"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">Cozumel · Mexico cruise port</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          Cozumel Shore<br/><span class="{ACCENT}">Excursions</span>
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Plan your Cozumel port day around your ship, your terminal and the kind of day you actually want — reef, beach club, ruins or something easy.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="best-cozumel-shore-excursions.html" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Explore shore excursions</a>
          <a href="ship-schedule/" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Find your ship schedule</a>
        </div>
      </div>
    </div>
    {hero_wave()}
  </section>"""


HERO_DEFS = {
    "hero-home.html": hero_home(),
    "hero-excursions.html": hero_inner(
        "Cozumel · Mexico", f"Best Cozumel<br/><span class=\"{ACCENT}\">Shore Excursions</span>",
        "Compare reef snorkeling, beach clubs, Chankanaab, jeep tours, Mayan ruins and catamaran sails for your ship schedule.",
        BEST_IMG, BEST_ALT, breadcrumb="Best Excursions",
    ),
    "hero-port-guide.html": hero_inner(
        "Cruise Passenger Guide", f"Cozumel<br/><span class=\"{ACCENT}\">Cruise Port Guide</span>",
        "Punta Langosta, International Pier, Puerta Maya, taxis, currency, distances and how to plan shore time in Cozumel, Mexico.",
        PORT_IMG, PORT_ALT, breadcrumb="Port Guide",
        cta=("best-cozumel-shore-excursions.html", "View Shore Excursions →"),
        tags=["🚢 Cruise Port", "🏖️ Beaches", "💵 MXN & USD", "🤿 Snorkeling"],
    ),
    "hero-one-day.html": hero_inner(
        "Port Day Timeline", f"One Day in<br/><span class=\"{ACCENT}\">Cozumel</span>",
        "Hour-by-hour plan from gangway to departure — snorkel, beach and downtown with return-to-ship buffer.",
        ONE_DAY_IMG, ONE_DAY_ALT, breadcrumb="One Day in Cozumel",
    ),
    "hero-beaches.html": hero_inner(
        "West-Coast Beaches", f"Best Cozumel<br/><span class=\"{ACCENT}\">Beaches</span>",
        "Mr Sanchos, Chankanaab and beach clubs — calm Caribbean water for cruise passenger beach days.",
        BEACHES_IMG, BEACHES_ALT, breadcrumb="Best Beaches",
    ),
    "hero-safety.html": hero_inner(
        "Cruise Passenger Safety", f"Is Cozumel<br/><span class=\"{ACCENT}\">Safe</span>?",
        "Practical safety advice for cruise guests — port zones, excursions, water conditions and travel tips in Cozumel, Mexico.",
        PORT_IMG, PORT_ALT, breadcrumb="Safety Guide",
    ),
    "hero-without-excursion.html": hero_inner(
        "Independent Exploring", f"Explore Cozumel<br/><span class=\"{ACCENT}\">Without an Excursion</span>",
        "Walk downtown from Punta Langosta, take taxis to beaches and plan short port calls without a tour booking.",
        PORT_IMG, PORT_ALT, breadcrumb="Without Excursion",
    ),
    "hero-port-map.html": hero_inner(
        "Port Orientation", f"Cozumel<br/><span class=\"{ACCENT}\">Cruise Port Map</span>",
        "Pier locations, distances to Chankanaab, Mr Sanchos, San Gervasio and reef departure points.",
        PORT_IMG, PORT_ALT, breadcrumb="Port Map",
    ),
    "hero-chankanaab-guide.html": hero_inner(
        "Marine Park", f"Chankanaab<br/><span class=\"{ACCENT}\">Park Guide</span>",
        "Reef snorkel, beach, dolphins and botanical gardens — Cozumel's top marine park for cruise passengers.",
        CHANKANAAB_IMG, CHANKANAAB_ALT, breadcrumb="Chankanaab Guide",
    ),
    "hero-mr-sanchos-guide.html": hero_inner(
        "Beach Club", f"Mr Sanchos<br/><span class=\"{ACCENT}\">Cozumel Guide</span>",
        "West-coast beach club day — loungers and a slower pace; transfer time depends on pier and traffic.",
        MR_SANCHOS_IMG, MR_SANCHOS_ALT, breadcrumb="Mr Sanchos Guide",
    ),
    "hero-best-of-cozumel.html": hero_inner(
        "Island Highlights", f"Best of<br/><span class=\"{ACCENT}\">Cozumel Tour</span>",
        "Beaches, Mayan heritage, tequila tasting and downtown — the essential Cozumel shore excursion for first-time visitors.",
        BEST_OF_IMG, BEST_OF_ALT, breadcrumb="Best of Cozumel",
    ),
    "hero-beach-day.html": hero_inner(
        "Beach · Caribbean", f"Cozumel<br/><span class=\"{ACCENT}\">Beach Day</span>",
        "Loungers and calm west-coast water — confirm club inclusions for your date.",
        BEACH_DAY_IMG, BEACH_DAY_ALT, breadcrumb="Beach Day",
    ),
    "hero-snorkeling.html": hero_inner(
        "Mesoamerican Reef", f"Cozumel<br/><span class=\"{ACCENT}\">Snorkeling Tour</span>",
        "Palancar Reef, Colombia Reef and El Cielo sandbar — world-class snorkel sites for cruise passengers.",
        SNORKEL_IMG, SNORKEL_ALT, breadcrumb="Snorkeling Tour",
    ),
    "hero-chankanaab-tour.html": hero_inner(
        "Marine Park Tour", f"Chankanaab<br/><span class=\"{ACCENT}\">Park Tour</span>",
        "House reef snorkel, beach and park facilities a short transfer from many cruise piers.",
        CHANKANAAB_IMG, CHANKANAAB_ALT, breadcrumb="Chankanaab Tour",
    ),
    "hero-mr-sanchos.html": hero_inner(
        "All-Inclusive Beach", f"Mr Sanchos<br/><span class=\"{ACCENT}\">Beach Club</span>",
        "Pool, open bar and west-coast beach lounging — a cruise passenger favourite in Cozumel, Mexico.",
        MR_SANCHOS_IMG, MR_SANCHOS_ALT, breadcrumb="Mr Sanchos",
    ),
    "hero-jeep.html": hero_inner(
        "Island Adventure", f"Cozumel<br/><span class=\"{ACCENT}\">Jeep Tour</span>",
        "Jungle trails, Mayan caverns, cenote swim and reef snorkel in open-top jeeps across Cozumel.",
        JEEP_IMG, JEEP_ALT, breadcrumb="Jeep Tour",
    ),
    "hero-ruins.html": hero_inner(
        "Mayan History", f"Cozumel<br/><span class=\"{ACCENT}\">Mayan Ruins Tour</span>",
        "San Gervasio archaeological site and island Mayan culture on a cruise-timed shore excursion.",
        RUINS_IMG, RUINS_ALT, breadcrumb="Mayan Ruins",
    ),
    "hero-catamaran.html": hero_inner(
        "Sail &amp; Snorkel", f"Cozumel<br/><span class=\"{ACCENT}\">Catamaran Tour</span>",
        "Sailing, reef snorkel and El Cielo sandbar on a spacious Caribbean catamaran from Cozumel.",
        CATAMARAN_IMG, CATAMARAN_ALT, breadcrumb="Catamaran Tour",
    ),
    "hero-atv.html": hero_inner(
        "Adventure · Jungle", f"Cozumel<br/><span class=\"{ACCENT}\">ATV Adventure</span>",
        "High-energy jungle trail riding across Cozumel island for active cruise passengers.",
        ATV_IMG, ATV_ALT, breadcrumb="ATV Adventure",
    ),
    "hero-tequila.html": hero_inner(
        "Mexican Culture", f"Cozumel<br/><span class=\"{ACCENT}\">Tequila Tasting</span>",
        "Agave education, guided tastings and island sightseeing on a Cozumel cultural shore excursion.",
        TEQUILA_IMG, TEQUILA_ALT, breadcrumb="Tequila Tour",
    ),
    "hero-private-island.html": hero_inner(
        "Private Escape", f"Cozumel<br/><span class=\"{ACCENT}\">Private Island Tour</span>",
        "Secluded sandbars, private boats and exclusive beach time away from cruise crowds in Cozumel, Mexico.",
        PRIVATE_ISLAND_IMG, PRIVATE_ISLAND_ALT, breadcrumb="Private Island",
    ),
    "hero-scuba.html": hero_inner(
        "Reef Diving", f"Cozumel<br/><span class=\"{ACCENT}\">Scuba Diving</span>",
        "Discover scuba and one-tank reef dives at Chankanaab for cruise passengers in Cozumel, Mexico.",
        SCUBA_IMG, SCUBA_ALT, breadcrumb="Scuba Diving",
    ),
}

PAGE_META = [
    dict(file="index.html", title=f"{SITE} | Shore Excursions &amp; Port-Day Planning",
         description="Plan your Cozumel cruise port day — reef snorkelling, beach clubs, terminals, island vs mainland and ship schedule for 2026–2027.",
         keywords="Cozumel shore excursions, Cozumel cruise port, Cozumel ship schedule, Cozumel snorkelling, Cozumel beach day",
         path="", data_page="home", hero="partials/hero-home.html", content="home.html", schema=home_schema(home_faq_data())),
    dict(file="best-cozumel-shore-excursions.html", title="Best Cozumel Shore Excursions | Compare Mexico Cruise Tours",
         description="Compare the best Cozumel shore excursions — snorkeling, beach clubs, Chankanaab, jeep tours, catamaran and Mayan ruins with cruise timing.",
         keywords="best Cozumel shore excursions, Cozumel cruise port tours, compare Cozumel excursions, Mexico shore trips",
         path="best-cozumel-shore-excursions.html", data_page="excursions", hero="partials/hero-excursions.html",
         content="best-cozumel-shore-excursions.html", preload=BEST_IMG,
         schema={"@context": "https://schema.org", "@type": "WebPage", "name": "Best Cozumel Shore Excursions", "url": f"{DOMAIN}/best-cozumel-shore-excursions.html"}),
    dict(file="cozumel-port-guide.html", title="Cozumel Cruise Port Guide | Mexico for Cruise Passengers",
         description="Cozumel cruise port guide — Punta Langosta, International Pier, Puerta Maya, taxis, currency, distances and top shore excursions.",
         keywords="Cozumel cruise port guide, Cozumel port day, cruise passenger guide Cozumel, Cozumel from cruise ship",
         path="cozumel-port-guide.html", data_page="port", hero="partials/hero-port-guide.html",
         content="cozumel-port-guide.html", preload=PORT_IMG,
         schema={"@context": "https://schema.org", "@type": "Article", "headline": "Cozumel Cruise Port Guide", "url": f"{DOMAIN}/cozumel-port-guide.html"}),
    dict(file="one-day-in-cozumel-from-a-cruise-ship.html", title="One Day in Cozumel from a Cruise Ship | Port Itinerary",
         description="How to spend one day in Cozumel on a cruise stop — morning snorkel, beach lunch and afternoon downtown with return-to-ship buffer.",
         keywords="one day in Cozumel cruise, Cozumel port day itinerary, cruise stop Cozumel planning",
         path="one-day-in-cozumel-from-a-cruise-ship.html", data_page="oneday", hero="partials/hero-one-day.html",
         content="one-day-in-cozumel-from-a-cruise-ship.html", preload=ONE_DAY_IMG),
    dict(file="best-cozumel-beaches-for-cruise-passengers.html", title="Best Cozumel Beaches for Cruise Passengers | Beach Club Guide",
         description="Best Cozumel beaches for cruise passengers — Mr Sanchos, Chankanaab, west-coast clubs, pier distances and taxi tips.",
         keywords="best Cozumel beaches cruise, Mr Sanchos cruise, Cozumel beach day cruise passengers",
         path="best-cozumel-beaches-for-cruise-passengers.html", data_page="beaches", hero="partials/hero-beaches.html",
         content="best-cozumel-beaches-for-cruise-passengers.html", preload=BEACHES_IMG),
    dict(file="is-cozumel-safe-for-cruise-passengers.html", title="Is Cozumel Safe for Cruise Passengers? | Port Safety Guide",
         description="Is Cozumel safe for cruise passengers? Practical safety tips for port zones, excursions, water activities and independent exploring in Cozumel, Mexico.",
         keywords="is Cozumel safe cruise, Cozumel safety cruise passengers, safe Cozumel shore excursions",
         path="is-cozumel-safe-for-cruise-passengers.html", data_page="port", hero="partials/hero-safety.html",
         content="is-cozumel-safe-for-cruise-passengers.html", preload=PORT_IMG),
    dict(file="can-you-explore-cozumel-without-an-excursion.html", title="Can You Explore Cozumel Without an Excursion? | Cruise Guide",
         description="Explore Cozumel without a booked excursion — downtown walking from Punta Langosta, taxis to beaches and tips for short port calls.",
         keywords="Cozumel without excursion, explore Cozumel cruise ship, self guided Cozumel port day",
         path="can-you-explore-cozumel-without-an-excursion.html", data_page="port", hero="partials/hero-without-excursion.html",
         content="can-you-explore-cozumel-without-an-excursion.html", preload=PORT_IMG),
    dict(file="cozumel-cruise-port-map.html", title="Cozumel Cruise Port Map | Pier Locations &amp; Distances",
         description="Cozumel cruise port map — Punta Langosta, International Pier, Puerta Maya and distances to Chankanaab, Mr Sanchos and San Gervasio.",
         keywords="Cozumel cruise port map, Cozumel pier map, Punta Langosta pier, Puerta Maya Cozumel",
         path="cozumel-cruise-port-map.html", data_page="port", hero="partials/hero-port-map.html",
         content="cozumel-cruise-port-map.html", preload=PORT_IMG),
    dict(file="chankanaab-park-guide.html", title="Chankanaab Park Guide | Cozumel Cruise Passenger Guide",
         description="Chankanaab National Marine Park guide for cruise passengers — snorkel reef, beach, dolphins, distances from port and tour options.",
         keywords="Chankanaab park guide, Chankanaab Cozumel cruise, Chankanaab snorkel cruise excursion",
         path="chankanaab-park-guide.html", data_page="chankanaab", hero="partials/hero-chankanaab-guide.html",
         content="chankanaab-park-guide.html", preload=CHANKANAAB_IMG),
    dict(file="mr-sanchos-cozumel-guide.html", title="Mr Sanchos Cozumel Guide | Beach Club for Cruise Passengers",
         description="Mr Sanchos Beach Club guide for Cozumel cruise passengers — beach-club day planning, transfer considerations and what to confirm with operators.",
         keywords="Mr Sanchos Cozumel guide, Mr Sanchos cruise excursion, Mr Sanchos beach club Cozumel",
         path="mr-sanchos-cozumel-guide.html", data_page="beaches", hero="partials/hero-mr-sanchos-guide.html",
         content="mr-sanchos-cozumel-guide.html", preload=MR_SANCHOS_IMG),
    dict(file="best-of-cozumel.html", title="Best of Cozumel Tour | Cozumel Cruise Shore Excursion",
         description="Best of Cozumel shore excursion for cruise passengers — beaches, Mayan heritage, tequila tasting and downtown exploration with cruise-friendly returns.",
         keywords="best of Cozumel tour, Cozumel highlights cruise excursion, first time Cozumel tour",
         path="best-of-cozumel.html", data_page="tours", hero="partials/hero-best-of-cozumel.html",
         content="best-of-cozumel.html", preload=BEST_OF_IMG,
         schema=tourist_trip_schema("Best of Cozumel Tour", "Island highlights and culture for Cozumel cruise passengers.")),
    dict(file="cozumel-beach-day.html", title="Cozumel Beach Day | Cruise Shore Excursion Guide",
         description="Cozumel beach day excursions for cruise passengers — west-coast clubs, loungers and planning around your ship schedule.",
         keywords="Cozumel beach day cruise, Cozumel beach excursion, beach club Cozumel cruise port",
         path="cozumel-beach-day.html", data_page="beaches", hero="partials/hero-beach-day.html",
         content="cozumel-beach-day.html", preload=BEACH_DAY_IMG,
         schema=tourist_trip_schema("Cozumel Beach Day", "Beach club day excursion for Cozumel cruise passengers.")),
    dict(file="cozumel-snorkeling-tour.html", title="Cozumel Snorkeling Tour | Reef Cruise Excursion",
         description="Cozumel snorkeling tours for cruise passengers — Palancar Reef, El Cielo sandbar and Colombia Reef with gear, guides and ship-timed returns.",
         keywords="Cozumel snorkeling tour, El Cielo cruise excursion, Palancar Reef snorkel Cozumel",
         path="cozumel-snorkeling-tour.html", data_page="snorkel", hero="partials/hero-snorkeling.html",
         content="cozumel-snorkeling-tour.html", preload=SNORKEL_IMG,
         schema=tourist_trip_schema("Cozumel Snorkeling Tour", "Reef snorkeling shore excursion from Cozumel cruise port.")),
    dict(file="chankanaab-park-tour.html", title="Chankanaab Park Tour | Cozumel Cruise Excursion",
         description="Chankanaab Park tour for cruise passengers — house reef snorkel, beach, dolphins and marine park activities near Cozumel port.",
         keywords="Chankanaab park tour, Chankanaab cruise excursion Cozumel, Chankanaab snorkel tour",
         path="chankanaab-park-tour.html", data_page="chankanaab", hero="partials/hero-chankanaab-tour.html",
         content="chankanaab-park-tour.html", preload=CHANKANAAB_IMG,
         schema=tourist_trip_schema("Chankanaab Park Tour", "Marine park shore excursion for Cozumel cruise passengers.")),
    dict(file="mr-sanchos-beach-club.html", title="Mr Sanchos Beach Club | Cozumel Cruise Excursion",
         description="Mr Sanchos Beach Club excursion for Cozumel cruise passengers — beach-club day planning with port transfers; confirm inclusions with the operator.",
         keywords="Mr Sanchos beach club, Mr Sanchos Cozumel cruise excursion, all inclusive beach Cozumel",
         path="mr-sanchos-beach-club.html", data_page="beaches", hero="partials/hero-mr-sanchos.html",
         content="mr-sanchos-beach-club.html", preload=MR_SANCHOS_IMG,
         schema=tourist_trip_schema("Mr Sanchos Beach Club", "All-inclusive beach club excursion in Cozumel.")),
    dict(file="cozumel-jeep-tour.html", title="Cozumel Jeep Tour | Jungle Cruise Shore Excursion",
         description="Cozumel jeep tour for cruise passengers — jungle trails, Mayan caverns, cenote swim and Dzul-Ha reef snorkel with cruise-timed returns.",
         keywords="Cozumel jeep tour, jungle jeep Cozumel cruise, Cozumel adventure excursion",
         path="cozumel-jeep-tour.html", data_page="adventure", hero="partials/hero-jeep.html",
         content="cozumel-jeep-tour.html", preload=JEEP_IMG,
         schema=tourist_trip_schema("Cozumel Jeep Tour", "Jungle jeep adventure shore excursion in Cozumel.")),
    dict(file="cozumel-mayan-ruins-tour.html", title="Cozumel Mayan Ruins Tour | San Gervasio Cruise Excursion",
         description="Cozumel Mayan ruins tour — San Gervasio archaeological site and island Mayan culture for cruise passengers with beach extension options.",
         keywords="Cozumel Mayan ruins tour, San Gervasio cruise excursion, Mayan ruins Cozumel cruise",
         path="cozumel-mayan-ruins-tour.html", data_page="tours", hero="partials/hero-ruins.html",
         content="cozumel-mayan-ruins-tour.html", preload=RUINS_IMG,
         schema=tourist_trip_schema("Cozumel Mayan Ruins Tour", "San Gervasio Mayan ruins excursion for cruise passengers.")),
    dict(file="cozumel-catamaran-sail-and-snorkel.html", title="Cozumel Catamaran Sail and Snorkel | Cruise Excursion",
         description="Cozumel catamaran sail and snorkel for cruise passengers — El Cielo sandbar, Colombia Reef and lunch with cruise-friendly timing.",
         keywords="Cozumel catamaran snorkel, El Cielo catamaran cruise, catamaran sail Cozumel excursion",
         path="cozumel-catamaran-sail-and-snorkel.html", data_page="snorkel", hero="partials/hero-catamaran.html",
         content="cozumel-catamaran-sail-and-snorkel.html", preload=CATAMARAN_IMG,
         schema=tourist_trip_schema("Cozumel Catamaran Sail and Snorkel", "Catamaran sailing and reef snorkel from Cozumel.")),
    dict(file="cozumel-atv-adventure.html", title="Cozumel ATV Adventure | Cruise Shore Excursion",
         description="Cozumel ATV adventure for cruise passengers — jungle trail riding with safety briefing, helmets and cruise-timed returns.",
         keywords="Cozumel ATV tour, ATV adventure Cozumel cruise, Cozumel jungle ATV excursion",
         path="cozumel-atv-adventure.html", data_page="adventure", hero="partials/hero-atv.html",
         content="cozumel-atv-adventure.html", preload=ATV_IMG,
         schema=tourist_trip_schema("Cozumel ATV Adventure", "ATV jungle trail excursion for Cozumel cruise passengers.")),
    dict(file="cozumel-tequila-tasting-tour.html", title="Cozumel Tequila Tasting Tour | Cultural Cruise Excursion",
         description="Cozumel tequila tasting tour for cruise passengers — agave education, guided tastings and island sightseeing with optional adventure combos.",
         keywords="Cozumel tequila tasting tour, tequila excursion Cozumel cruise, Mexican tequila Cozumel shore excursion",
         path="cozumel-tequila-tasting-tour.html", data_page="tours", hero="partials/hero-tequila.html",
         content="cozumel-tequila-tasting-tour.html", preload=TEQUILA_IMG,
         schema=tourist_trip_schema("Cozumel Tequila Tasting Tour", "Tequila tasting cultural excursion in Cozumel.")),
    dict(file="cozumel-private-island-tour.html", title="Cozumel Private Island Tour | Private Cruise Excursion",
         description="Cozumel private island and secluded beach tours for cruise passengers — private boats, sandbars and custom small-group charters.",
         keywords="Cozumel private island tour, private catamaran Cozumel cruise, El Cielo private boat Cozumel",
         path="cozumel-private-island-tour.html", data_page="private", hero="partials/hero-private-island.html",
         content="cozumel-private-island-tour.html", preload=PRIVATE_ISLAND_IMG,
         schema=tourist_trip_schema("Cozumel Private Island Tour", "Private island beach excursion for Cozumel cruise passengers.")),
    dict(file="cozumel-scuba-diving-tour.html", title="Cozumel Scuba Diving Tour | Reef Dive Cruise Excursion",
         description="Cozumel scuba diving tours for cruise passengers — discover scuba and one-tank reef dives at Chankanaab with certified instructors.",
         keywords="Cozumel scuba diving tour, discover scuba Cozumel cruise, Chankanaab dive excursion",
         path="cozumel-scuba-diving-tour.html", data_page="snorkel", hero="partials/hero-scuba.html",
         content="cozumel-scuba-diving-tour.html", preload=SCUBA_IMG,
         schema=tourist_trip_schema("Cozumel Scuba Diving Tour", "Reef scuba diving excursion for Cozumel cruise passengers.")),
    dict(file="cozumel-island-vs-mainland.html", title="Cozumel Island vs Mainland | Cruise Port Day Decision",
         description="Should you stay on Cozumel or ferry to the mainland? Practical trade-offs for cruise passengers — time, buffer, ruins and flexibility.",
         keywords="Cozumel island vs mainland, Cozumel ferry Playa del Carmen, Cozumel mainland excursion cruise",
         path="cozumel-island-vs-mainland.html", data_page="port", hero="partials/hero-port-guide.html",
         content="cozumel-island-vs-mainland.html", preload=PORT_IMG),
    dict(file="cozumel-reef-vs-beach.html", title="Cozumel Reef vs Beach Club | Cruise Passenger Decision",
         description="Reef snorkel or beach club in Cozumel? Compare boat reef days with west-coast beach clubs for your cruise call.",
         keywords="Cozumel reef vs beach, Cozumel snorkel or beach club, Cozumel cruise water day",
         path="cozumel-reef-vs-beach.html", data_page="excursions", hero="partials/hero-snorkeling.html",
         content="cozumel-reef-vs-beach.html", preload=SNORKEL_IMG),
    dict(file="about.html", title="About Cozumel Cruise Excursion | Independent Port Planning",
         description="About Cozumel Cruise Excursion — independent cruise-port planning for Cozumel, Mexico. Not a cruise line or ticket marketplace.",
         keywords="about Cozumel Cruise Excursion, Cozumel cruise planning guide",
         path="about.html", data_page="contact", hero="partials/hero-port-guide.html",
         content="about.html", preload=PORT_IMG),
    dict(file="contact.html", title="Contact Cozumel Cruise Excursion | Port Day Concierge",
         description="Contact Cozumel Cruise Excursion for help planning your Cozumel cruise port day. Concierge email activates at launch.",
         keywords="contact Cozumel Cruise Excursion, Cozumel shore excursion help",
         path="contact.html", data_page="contact", hero="partials/hero-port-guide.html",
         content="contact.html", preload=PORT_IMG),
    dict(file="privacy.html", title="Privacy | Cozumel Cruise Excursion",
         description="Privacy information for Cozumel Cruise Excursion — static planning site without booking passenger databases in this phase.",
         keywords="privacy Cozumel Cruise Excursion",
         path="privacy.html", data_page="contact", hero="partials/hero-port-guide.html",
         content="privacy.html", preload=PORT_IMG),
    dict(file="terms.html", title="Terms of Use | Cozumel Cruise Excursion",
         description="Terms of use for Cozumel Cruise Excursion planning content — schedules and excursion details can change.",
         keywords="terms Cozumel Cruise Excursion",
         path="terms.html", data_page="contact", hero="partials/hero-port-guide.html",
         content="terms.html", preload=PORT_IMG),
    dict(file="methodology.html", title="How We Assess Cozumel Excursions | Methodology",
         description="How Cozumel Cruise Excursion assesses shore options — cruise timing, honest claims and authority schedule integrity.",
         keywords="Cozumel excursion methodology, how we choose Cozumel tours",
         path="methodology.html", data_page="contact", hero="partials/hero-port-guide.html",
         content="methodology.html", preload=PORT_IMG),
]


def nav_html() -> str:
    return f"""<nav class="fixed top-0 left-0 right-0 z-50 bg-white/90 border-b border-pr-100 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-14">
      <a href="index.html" class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-full btn-ocean flex items-center justify-center" aria-hidden="true">
          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/></svg>
        </div>
        <span class="font-display font-semibold text-ocean-800 text-base leading-tight">Cozumel<br/><span class="text-[10px] font-body font-normal text-pr-600 tracking-widest uppercase">Cruise Excursion</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-5 text-sm font-medium">
        <a href="index.html" data-nav="home" class="text-gray-600 hover:text-ocean-600 transition-colors">Home</a>
        <a href="best-cozumel-shore-excursions.html" data-nav="excursions" class="text-gray-600 hover:text-ocean-600 transition-colors">Excursions</a>
        <a href="cozumel-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
        <a href="ship-schedule/" data-nav="schedule" class="text-gray-600 hover:text-ocean-600 transition-colors">Ship Schedule</a>
        <a href="one-day-in-cozumel-from-a-cruise-ship.html" data-nav="oneday" class="text-gray-600 hover:text-ocean-600 transition-colors">One Day</a>
        <a href="contact.html" data-nav="contact" class="text-gray-600 hover:text-ocean-600 transition-colors">Contact</a>
      </div>
      <a href="ship-schedule/" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">Find your ship</a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sand-50" aria-label="Open menu" aria-expanded="false" data-nav-toggle>
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
    <div class="mobile-nav-panel lg:hidden" data-nav-panel hidden>
      <a href="index.html" data-nav="home">Home</a>
      <a href="best-cozumel-shore-excursions.html" data-nav="excursions">Excursions</a>
      <a href="cozumel-port-guide.html" data-nav="port">Port Guide</a>
      <a href="ship-schedule/" data-nav="schedule">Ship Schedule</a>
      <a href="one-day-in-cozumel-from-a-cruise-ship.html" data-nav="oneday">One Day</a>
      <a href="contact.html" data-nav="contact">Contact</a>
    </div>
  </div>
</nav>
"""


def footer_html() -> str:
    return f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="index.html" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Independent planning guide for cruise visitors to Cozumel, Mexico. Not affiliated with any cruise line.</p>
          <p class="mt-3 text-xs leading-relaxed">Regional context: <a href="https://caribbeanshoreexcursion.com/" class="hover:text-white transition-colors">Caribbean Shore Excursions</a></p>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Excursions</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="best-cozumel-shore-excursions.html" class="hover:text-white transition-colors">Best excursions</a></li>
            <li><a href="cozumel-snorkeling-tour.html" class="hover:text-white transition-colors">Snorkelling</a></li>
            <li><a href="cozumel-beach-day.html" class="hover:text-white transition-colors">Beach day</a></li>
            <li><a href="chankanaab-park-tour.html" class="hover:text-white transition-colors">Chankanaab</a></li>
            <li><a href="mr-sanchos-beach-club.html" class="hover:text-white transition-colors">Mr Sanchos</a></li>
            <li><a href="cozumel-mayan-ruins-tour.html" class="hover:text-white transition-colors">Mayan ruins</a></li>
            <li><a href="cozumel-island-vs-mainland.html" class="hover:text-white transition-colors">Island vs mainland</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Plan</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="cozumel-port-guide.html" class="hover:text-white transition-colors">Port guide</a></li>
            <li><a href="ship-schedule/" class="hover:text-white transition-colors">Ship schedule</a></li>
            <li><a href="one-day-in-cozumel-from-a-cruise-ship.html" class="hover:text-white transition-colors">One day in Cozumel</a></li>
            <li><a href="cozumel-reef-vs-beach.html" class="hover:text-white transition-colors">Reef vs beach</a></li>
            <li><a href="methodology.html" class="hover:text-white transition-colors">Methodology</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Site</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="about.html" class="hover:text-white transition-colors">About</a></li>
            <li><a href="contact.html" class="hover:text-white transition-colors">Contact</a></li>
            <li><a href="privacy.html" class="hover:text-white transition-colors">Privacy</a></li>
            <li><a href="terms.html" class="hover:text-white transition-colors">Terms</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Schedules and excursion details can change — confirm with your cruise line and operators.</p>
      </div>
    </div>
  </footer>
"""


def trust_strip_html() -> str:
    return """<section class="trust-strip" aria-label="Cozumel planning highlights">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="trust-strip__list">
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Cruise-specific planning</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Terminal guidance</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Authority ship schedule</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Honest, non-booking CTAs</li>
    </ul>
  </div>
</section>
"""


def main() -> None:
    print("Building Cozumel Cruise Excursion site…")

    write("partials/nav.html", nav_html())
    write("partials/footer.html", footer_html())
    write("partials/trust-strip.html", trust_strip_html())

    for name, html in HERO_DEFS.items():
        write(f"partials/{name}", html)

    for name, html in all_guide_content().items():
        write(f"content/{name}", html)

    for name, html in all_tour_content().items():
        write(f"content/{name}", html)

    for p in PAGE_META:
        write(
            p["file"],
            page_shell(
                title=p["title"],
                description=p["description"],
                keywords=p["keywords"],
                canonical_path=p["path"],
                data_page=p["data_page"],
                hero=p["hero"],
                content=p["content"],
                preload=p.get("preload", HOME_HERO),
                schema=p.get("schema"),
            ),
        )

    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

    # Schedule pages (requires prior npm run sync:schedules)
    schedule_entries = []
    try:
        from generate_schedule_pages import main as gen_schedules
        schedule_entries = gen_schedules()
    except SystemExit as e:
        print(f"  schedule generation skipped/failed: {e}")
    except Exception as e:
        print(f"  schedule generation error: {e}")

    extra_pages = [
        ("cozumel-island-vs-mainland.html", "0.8", "monthly"),
        ("cozumel-reef-vs-beach.html", "0.8", "monthly"),
        ("about.html", "0.5", "yearly"),
        ("contact.html", "0.6", "yearly"),
        ("privacy.html", "0.3", "yearly"),
        ("terms.html", "0.3", "yearly"),
        ("methodology.html", "0.5", "yearly"),
    ]
    all_sitemap = list(SITEMAP_PAGES) + extra_pages + list(schedule_entries)

    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, priority, freq in all_sitemap:
        url = f"{DOMAIN}/{loc}" if loc else f"{DOMAIN}/"
        lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{DATE}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines) + "\n")

    write("package.json", """{
  "name": "cozumel-cruise-excursion",
  "private": true,
  "scripts": {
    "sync:schedules": "node scripts/sync-schedules.mjs",
    "qa:schedules": "node scripts/qa-schedules.mjs",
    "build": "python3 scripts/build-cozumel-site.py",
    "build:all": "npm run sync:schedules && npm run qa:schedules && npm run build",
    "images": "python3 scripts/fetch-cozumel-images.py",
    "deploy": "wrangler deploy",
    "preview": "python3 -m http.server 8905"
  },
  "devDependencies": {
    "wrangler": "^4.94.0"
  }
}
""")

    write("wrangler.jsonc", """{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "cozumel-cruise-excursion",
  "compatibility_date": "2026-06-05",
  "observability": { "enabled": true },
  "assets": { "directory": "." },
  "routes": [
    {
      "pattern": "cozumelcruiseexcursion.com",
      "custom_domain": true
    }
  ]
}
""")

    write("deploy.sh", f"""#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

echo "Deploying {SITE} to Cloudflare..."
npx wrangler deploy

echo "Done. Check {DOMAIN}/ shortly."
""")

    (ROOT / "deploy.sh").chmod(0o755)

    images_dir = ROOT / "images"
    images_dir.mkdir(exist_ok=True)
    for img in ALL_IMAGES:
        p = ROOT / img
        if p.exists() and p.stat().st_size > 5000:
            continue
        p.write_bytes(PLACEHOLDER_PNG)

    # Do not overwrite images/ATTRIBUTION.md — provenance is maintained separately.

    print("Done.")


if __name__ == "__main__":
    main()
