"""Guide and home page content for Cozumel Cruise Excursion."""
from cozumel_config import (
    BEACHES_IMG, BEACHES_ALT, CHANKANAAB_IMG, CHANKANAAB_ALT,
    INTRO_IMG, INTRO_ALT, MR_SANCHOS_IMG, MR_SANCHOS_ALT,
    PORT_ARRIVAL_ALT, PORT_ARRIVAL_IMG, PORT_IMG, PORT_ALT,
    SNORKEL_IMG, SNORKEL_ALT,
)
from cozumel_helpers import (
    card_grid, comparison_section, concierge_panel, internal_links, snapshot_default,
)


def content_home() -> str:
    featured = card_grid([
        (SNORKEL_IMG, SNORKEL_ALT, "Cozumel snorkelling", "Palancar, El Cielo and Columbia Reef boat days timed for cruise calls.", "cozumel-snorkeling-tour.html", "Explore snorkelling"),
        (CHANKANAAB_IMG, CHANKANAAB_ALT, "Chankanaab Park", "House reef, beach and park facilities a short drive from the piers.", "chankanaab-park-tour.html", "Explore Chankanaab"),
        (MR_SANCHOS_IMG, MR_SANCHOS_ALT, "Mr Sanchos beach club", "West-coast loungers and a slower port day when you want easy.", "mr-sanchos-beach-club.html", "Explore beach club"),
        (SNORKEL_IMG, SNORKEL_ALT, "Catamaran sail &amp; snorkel", "Sailing plus reef stops when you want time on the water.", "cozumel-catamaran-sail-and-snorkel.html", "Explore catamaran"),
    ])
    snap = snapshot_default()
    return f"""<section class="pt-8 pb-6 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
  <p class="section-label mx-auto">Cruise passenger orientation</p>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">You are arriving in Cozumel by ship</h2>
  <p class="text-gray-600 text-sm sm:text-base leading-relaxed">Three cruise terminals serve the island. Your realistic choices are reef time, a beach club, island sightseeing, San Gervasio, or a longer mainland day via the Playa del Carmen ferry. Start with the kind of day you want, then check your ship date.</p>
</div></section>
<section class="pb-10 bg-white"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="decision-grid">
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Reef / snorkel</h3><p>Boat days toward Palancar, Columbia or El Cielo when water is the priority.</p><a href="cozumel-snorkeling-tour.html" class="text-ocean-600 font-semibold text-sm">Snorkelling →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Beach club</h3><p>Loungers and a calmer pace — compare Mr Sanchos, Chankanaab and other west-coast days.</p><a href="cozumel-beach-day.html" class="text-ocean-600 font-semibold text-sm">Beach day →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Mayan history</h3><p>San Gervasio on-island, or a more complex mainland ruins day if your call supports it.</p><a href="cozumel-mayan-ruins-tour.html" class="text-ocean-600 font-semibold text-sm">Ruins options →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Island vs mainland</h3><p>Stay put for flexibility, or ferry across knowing the day gets longer.</p><a href="cozumel-island-vs-mainland.html" class="text-ocean-600 font-semibold text-sm">Compare →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Easy / low-effort</h3><p>Downtown from Punta Langosta, a short beach taxi, or a park pass with simple logistics.</p><a href="can-you-explore-cozumel-without-an-excursion.html" class="text-ocean-600 font-semibold text-sm">Easy day ideas →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Find your ship</h3><p>Search Cozumel call dates for 2026 and 2027, then plan buffer around all aboard.</p><a href="ship-schedule/" class="text-ocean-600 font-semibold text-sm">Ship schedule →</a></div>
  </div>
</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-10">
    <p class="section-label mx-auto">Excursion choices</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-3">Major ways to spend the port day</h2>
    <p class="text-gray-600 text-sm max-w-2xl mx-auto">Editorial guides for cruise timing — not a booking marketplace. Explore details, then decide what fits your call.</p>
  </div>
  {featured}
  <p class="text-center mt-8"><a href="best-cozumel-shore-excursions.html" class="text-ocean-600 font-semibold text-sm">Full comparison →</a></p>
</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <p class="section-label">Terminals</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Puerta Maya, International Pier &amp; Punta Langosta</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Which pier you use changes downtown walking distance, taxi orientation and meeting logistics. Ship-to-terminal assignments can vary — check your cruise information rather than assuming a fixed berth.</p>
    <a href="cozumel-port-guide.html" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Port guide</a>
  </div>
  <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
    <img src="{PORT_ARRIVAL_IMG}" alt="{PORT_ARRIVAL_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg order-2 lg:order-1">
    <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
  <div class="order-1 lg:order-2">
    <p class="section-label">Ship planning</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Plan around your actual call</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Browse Cozumel arrivals by month, search your ship, then build a day that leaves a sensible return buffer. Schedules can change — treat times as planning aids.</p>
    <a href="ship-schedule/" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm">Find your ship schedule</a>
  </div>
</div></div></section>
<section class="pb-4 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Snorkelling on the Mesoamerican Reef</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Cozumel’s leeward reef is the island’s genuine differentiator. Conditions and sightings vary — go for the reef experience, not a wildlife guarantee. Morning departures are often calmer.</p>
    <a href="cozumel-snorkeling-tour.html" class="text-ocean-600 font-semibold text-sm">Snorkelling guide →</a>
    <span class="text-gray-300 mx-2">·</span>
    <a href="cozumel-reef-vs-beach.html" class="text-ocean-600 font-semibold text-sm">Reef vs beach →</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{SNORKEL_IMG}" alt="{SNORKEL_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BEACHES_IMG}" alt="{BEACHES_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Beach clubs without the brochure gloss</h2>
    <p class="text-gray-600 leading-relaxed mb-4">West-coast clubs suit passengers who want shade, swimming and a simple day. Inclusions and atmosphere differ — compare Mr Sanchos, Chankanaab and other beach days before you commit.</p>
    <a href="best-cozumel-beaches-for-cruise-passengers.html" class="text-ocean-600 font-semibold text-sm">Beach guide →</a>
  </div>
</div></div></section>
{comparison_section()}
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-gray-900 text-center mb-8">Useful guides</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 text-sm">
    <a href="one-day-in-cozumel-from-a-cruise-ship.html" class="decision-card hover:border-ocean-200"><h3 class="font-display font-bold">One day in Cozumel</h3><p>Paths for easy, reef, beach, culture and mainland-minded days.</p></a>
    <a href="cozumel-island-vs-mainland.html" class="decision-card hover:border-ocean-200"><h3 class="font-display font-bold">Island vs mainland</h3><p>Ferry and buffer trade-offs without scare language.</p></a>
    <a href="methodology.html" class="decision-card hover:border-ocean-200"><h3 class="font-display font-bold">How we assess options</h3><p>Cruise timing, honest claims and schedule integrity.</p></a>
  </div>
</div></section>
{home_faq_section()}
{concierge_panel()}
<section class="py-14 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-white mb-4">Ready to shape your Cozumel day?</h2>
  <p class="text-white/85 text-sm mb-6">Compare excursions, check terminals, then look up your ship.</p>
  <div class="flex flex-col sm:flex-row gap-4 justify-center">
    <a href="best-cozumel-shore-excursions.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Explore shore excursions</a>
    <a href="ship-schedule/" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Find your ship schedule</a>
  </div>
</div></section>"""


def home_faq_section() -> str:
    return """<section class="py-16 bg-white"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-3xl font-display font-bold text-gray-900 text-center mb-8">Cozumel shore excursions FAQ</h2>
  <div class="space-y-4">
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do cruise ships stay in Cozumel?</summary>
      <p class="mt-4 text-sm text-gray-500">Many Cozumel calls last roughly 6 to 10 hours, but your ship’s timetable is what matters. Check arrival, departure and all-aboard on your cruise documents, then leave a return buffer.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Which Cozumel cruise terminal will I use?</summary>
      <p class="mt-4 text-sm text-gray-500">Ships use Puerta Maya, International Pier or Punta Langosta. Assignments can change — confirm with your cruise line. See the <a href="cozumel-port-guide.html" class="text-ocean-600">port guide</a> for how each pier affects downtown and transfers.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Should I stay on Cozumel or go to the mainland?</summary>
      <p class="mt-4 text-sm text-gray-500">Island days are usually more flexible. Mainland days via the Playa del Carmen ferry unlock larger ruins and Riviera Maya scenery but consume more of the call. Read <a href="cozumel-island-vs-mainland.html" class="text-ocean-600">island vs mainland</a>.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Beach day or snorkelling?</summary>
      <p class="mt-4 text-sm text-gray-500">Choose snorkelling for reef structure and boat time; choose a beach club for lounging and a slower pace. Chankanaab combines park facilities with a house reef. Compare in <a href="cozumel-reef-vs-beach.html" class="text-ocean-600">reef vs beach</a>.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Ship excursion or independent operator?</summary>
      <p class="mt-4 text-sm text-gray-500">Ship tours often include the cruise line’s return policies. Independent operators can be excellent when they plan buffer and communicate meeting points clearly — verify policies before you book. This site does not sell tickets.</p></details>
  </div>
</div></section>"""


def home_faq_data() -> list[tuple[str, str]]:
    return [
        ("How long do cruise ships stay in Cozumel?", "Many Cozumel calls last roughly 6 to 10 hours; confirm your ship’s timetable and leave a return buffer."),
        ("Which Cozumel cruise terminal will I use?", "Puerta Maya, International Pier or Punta Langosta — assignments can change; check your cruise information."),
        ("Should I stay on Cozumel or go to the mainland?", "Island days are more flexible; mainland days via ferry take more of the call and need careful buffering."),
        ("Beach day or snorkelling?", "Snorkelling for reef time; beach clubs for a slower day; Chankanaab combines park and house reef."),
        ("Ship excursion or independent operator?", "Compare return policies and meeting logistics; this site is a planning guide, not a ticket seller."),
    ]


def content_best_excursions() -> str:
    snap = snapshot_default(best_for="Comparing all excursion types", popular="See comparison table below")
    rankings = """<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Excursions by Traveler Type</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Families</h3><p class="text-gray-600 mb-3">Chankanaab Park, beach day passes and gentle snorkel catamarans suit mixed ages.</p><a href="chankanaab-park-tour.html" class="text-ocean-600 font-semibold">Chankanaab →</a></div>
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Couples</h3><p class="text-gray-600 mb-3">Beach-club days, private catamaran charters and tequila tasting outings.</p><a href="mr-sanchos-beach-club.html" class="text-ocean-600 font-semibold">Mr Sanchos →</a></div>
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">First Timers</h3><p class="text-gray-600 mb-3">Best of Cozumel and Chankanaab cover island highlights in one trip.</p><a href="best-of-cozumel.html" class="text-ocean-600 font-semibold">Best of Cozumel →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Adventure</h3><p class="text-gray-600 mb-3">Jeep jungle tours, ATV trails and cenote snorkel combos.</p><a href="cozumel-jeep-tour.html" class="text-ocean-600 font-semibold">Jeep Tour →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Reef Lovers</h3><p class="text-gray-600 mb-3">Snorkel El Cielo, Palancar Reef and scuba dives at Chankanaab.</p><a href="cozumel-snorkeling-tour.html" class="text-ocean-600 font-semibold">Snorkeling →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Short Port Calls</h3><p class="text-gray-600 mb-3">Downtown shopping from Punta Langosta or half-day Chankanaab pass.</p><a href="can-you-explore-cozumel-without-an-excursion.html" class="text-ocean-600 font-semibold">Without Excursion →</a></div>
  </div>
</div></section>"""
    cards = card_grid([
        (SNORKEL_IMG, SNORKEL_ALT, "Snorkeling Tour", "El Cielo, Palancar and Colombia Reef on guided boat trips.", "cozumel-snorkeling-tour.html", "Snorkel"),
        (CHANKANAAB_IMG, CHANKANAAB_ALT, "Chankanaab Park", "Reef snorkel, beach and family activities near port.", "chankanaab-park-tour.html", "Chankanaab"),
        (MR_SANCHOS_IMG, MR_SANCHOS_ALT, "Mr Sanchos", "All-inclusive west-coast beach club day pass.", "mr-sanchos-beach-club.html", "Beach Club"),
        (SNORKEL_IMG, SNORKEL_ALT, "Best of Cozumel", "Island culture, beaches and tequila tasting combo.", "best-of-cozumel.html", "Best of Cozumel"),
    ])
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best Cozumel Shore Excursions</h2>
  <p class="text-gray-600 leading-relaxed text-sm">Operators meet at <strong>Cozumel cruise terminals</strong> — Punta Langosta, International Pier and Puerta Maya — and plan returns with buffer before all aboard.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
{comparison_section()}
{rankings}
<section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Excursion Guides</h2>
  {cards}
  <div class="mt-12 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>"""


def content_port_guide() -> str:
    snap = snapshot_default(activity_level="Low at terminal; moderate on tours", popular="Taxis, tour pickups, downtown walk")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <p class="text-gray-600 leading-relaxed text-sm">Cozumel’s cruise piers put reef, beach clubs and San Miguel within reach of a typical call — if you match the day to your terminal and all-aboard time.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-3">The three cruise terminals</h2>
  <p class="text-center text-sm text-gray-600 max-w-2xl mx-auto mb-8">Terminal location changes downtown access, taxi plazas and meeting logistics. Do not treat ship-to-pier pairings as permanent; confirm on your cruise documents.</p>
  <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
    <img src="{PORT_ARRIVAL_IMG}" alt="{PORT_ARRIVAL_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
  </div>
  <div class="grid lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Punta Langosta</h3><p class="text-gray-600 mb-3">Closest to downtown San Miguel — shops, malecón and cafés are walkable for many passengers. Handy for an easy, low-transfer day.</p><p class="text-gray-500 text-xs">South-side parks and beach clubs still need a taxi or organised transfer.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">International Pier</h3><p class="text-gray-600 mb-3">South of downtown. Tour desks and taxi plazas serve the terminal. Downtown is a short taxi rather than a casual stroll for most guests.</p><p class="text-gray-500 text-xs">Convenient orientation for many organised west-coast and park transfers.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Puerta Maya</h3><p class="text-gray-600 mb-3">Large southern complex used by many ships. Organised excursions commonly meet inside the terminal; independent guests use the taxi plaza outside.</p><p class="text-gray-500 text-xs">Plan meeting points carefully — the complex is bigger than a single downtown pier.</p></div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Practical port-day notes</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">Mexican pesos (MXN) are official. USD is widely accepted in tourist areas — small notes help for taxis and tips. We do not publish fixed fare tables.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Transport</strong><p class="mt-2 text-gray-600">Official taxis operate at the piers. Agree the fare or route before you leave. Rideshare is not the local default for most cruise guests.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Return planning</strong><p class="mt-2 text-gray-600">Build your own buffer before all aboard. Organised tours should communicate return timing; independent days need tighter self-management.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Independent vs organised</strong><p class="mt-2 text-gray-600">Downtown walking and a simple beach taxi can work alone. Reef boats, El Cielo and many ruins days are simpler with an operator who owns the logistics.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Ferry / mainland</strong><p class="mt-2 text-gray-600">Crossing to Playa del Carmen adds ferry and road time. See <a href="cozumel-island-vs-mainland.html" class="text-ocean-600 font-medium">island vs mainland</a> before committing.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Heat &amp; mobility</strong><p class="mt-2 text-gray-600">Expect strong sun. Prefer shaded beach or park days if mobility is limited; confirm walking surfaces for ruins and adventure tours.</p></div>
  </div>
  <p class="text-center mt-8 text-sm"><a href="cozumel-cruise-port-map.html" class="text-ocean-600 font-semibold">Port map →</a> · <a href="ship-schedule/" class="text-ocean-600 font-semibold">Ship schedule →</a> · <a href="one-day-in-cozumel-from-a-cruise-ship.html" class="text-ocean-600 font-semibold">One-day itinerary →</a></p>
  <div class="mt-10 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>
{concierge_panel()}"""


def content_one_day() -> str:
    snap = snapshot_default(best_for="Matching a day path to your call length")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <p class="text-gray-600 text-sm">Use these as planning sketches, not rigid clocks. Anchor everything to your ship’s arrival, departure and all-aboard time.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-5xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Port-day paths</h2>
  <div class="decision-grid mb-10">
    <div class="decision-card"><h3 class="font-display font-bold">Easy day</h3><p>Downtown from Punta Langosta, or a short taxi to a beach club with a clear return plan.</p><a href="can-you-explore-cozumel-without-an-excursion.html" class="text-ocean-600 font-semibold text-sm">Independent ideas →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold">Beach / water day</h3><p>West-coast club or Chankanaab when you want swimming, shade and fewer moving parts.</p><a href="cozumel-beach-day.html" class="text-ocean-600 font-semibold text-sm">Beach day →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold">Active reef day</h3><p>Boat snorkel or catamaran toward Palancar, Columbia or El Cielo — leave buffer for seas and queues.</p><a href="cozumel-snorkeling-tour.html" class="text-ocean-600 font-semibold text-sm">Snorkelling →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold">History / culture</h3><p>San Gervasio or a Best of Cozumel style mix without a ferry crossing.</p><a href="cozumel-mayan-ruins-tour.html" class="text-ocean-600 font-semibold text-sm">Ruins →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold">Mainland full-day</h3><p>Only when the call truly supports ferry + road time. Read the trade-offs first.</p><a href="cozumel-island-vs-mainland.html" class="text-ocean-600 font-semibold text-sm">Island vs mainland →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold">Family mix</h3><p>Chankanaab or a gentle beach club often beats a packed multi-stop adventure.</p><a href="chankanaab-park-tour.html" class="text-ocean-600 font-semibold text-sm">Chankanaab →</a></div>
  </div>
  <h2 class="text-xl font-display font-bold text-center mb-6">Sample island reef + beach sketch</h2>
  <ol class="space-y-4 text-sm max-w-3xl mx-auto">
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">Morning</span><div><strong>Leave the pier with purpose</strong><p class="text-gray-600 mt-1">Meet a snorkel boat or transfer to Chankanaab while energy and light are good.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">Midday</span><div><strong>Water time, then shade</strong><p class="text-gray-600 mt-1">Reef stop or park snorkel, then lunch and a pause before heat peaks.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">Afternoon</span><div><strong>Second activity or downtown</strong><p class="text-gray-600 mt-1">Extend beach time, or shop near Punta Langosta if that is your terminal.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">Return</span><div><strong>Move early enough</strong><p class="text-gray-600 mt-1">Taxi or tour transfer with margin. Confirm your pier — Puerta Maya, International or Punta Langosta.</p></div></li>
  </ol>
  <p class="text-center mt-8 text-sm"><a href="ship-schedule/" class="text-ocean-600 font-semibold">Check your ship date →</a></p>
  <div class="mt-10 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>
{concierge_panel()}"""


def content_beaches_guide() -> str:
    snap = snapshot_default(best_for="Choosing a west-coast beach club", popular="Mr Sanchos, Chankanaab, day passes")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">Cozumel's cruise-friendly beaches sit on the protected west coast — calm turquoise water, soft sand and clubs with loungers, food and open bars. East-coast beaches face open ocean with stronger surf and are rarely included on shore excursions.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Mr Sanchos</strong> — popular beach-club style day; transfer time depends on pier and traffic. <a href="mr-sanchos-cozumel-guide.html" class="text-ocean-600">Guide →</a></li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Chankanaab</strong> — park with house reef and beach a short drive south for many ships.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Money Bar / Dzul-Ha</strong> — reef snorkel from shore with day pass.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Kuza Beach Park</strong> — often paired with El Cielo snorkel catamarans.</li>
    </ul>
    <a href="cozumel-beach-day.html" class="text-ocean-600 font-semibold text-sm">Beach day excursions →</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BEACHES_IMG}" alt="{BEACHES_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{internal_links([("mr-sanchos-beach-club.html", "Mr Sanchos")])}</div></section>"""


def content_safety() -> str:
    snap = snapshot_default(best_for="Understanding Cozumel safety for tourists", activity_level="N/A")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4">
  <p class="text-gray-600 leading-relaxed text-sm mb-6">Cozumel, Mexico is one of the Caribbean's most visited cruise ports and is heavily oriented toward tourism. Cruise passengers generally report safe, welcoming experiences when staying in tourist zones and using licensed operators.</p>
  <div class="space-y-4 text-sm">
    <div class="bg-sand-50 rounded-2xl p-5 border border-pr-100"><h3 class="font-display font-bold mb-2">Port &amp; Downtown</h3><p class="text-gray-600">Pier areas and San Miguel downtown are busy and patrolled. Use normal city awareness; avoid unlicensed transport offers.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-5 border border-ocean-100"><h3 class="font-display font-bold mb-2">Excursions</h3><p class="text-gray-600">Book through reputable operators with cruise return policies. Verify meeting points inside official terminals.</p></div>
    <div class="bg-sand-50 rounded-2xl p-5 border border-pr-100"><h3 class="font-display font-bold mb-2">Water Safety</h3><p class="text-gray-600">Follow snorkel guides; check conditions before boat trips. East-coast beaches have strong currents — stick to excursion beaches.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-5 border border-ocean-100"><h3 class="font-display font-bold mb-2">Health</h3><p class="text-gray-600">Drink bottled water if sensitive; use reef-safe sunscreen. Travel insurance recommended for diving and adventure tours.</p></div>
  </div>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{internal_links()}</div></section>"""


def content_without_excursion() -> str:
    snap = snapshot_default(best_for="Self-guided downtown and short visits", activity_level="Low — walking and taxis")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4">
  <p class="text-gray-600 leading-relaxed text-sm mb-6">Yes — cruise passengers can explore Cozumel without a booked excursion, especially from <strong>Punta Langosta</strong> pier where San Miguel downtown is walkable. Shopping, cafés, the waterfront malecón and taxis to nearby beaches are all independent options.</p>
  <div class="space-y-4 text-sm">
    <div class="bg-sand-50 rounded-2xl p-5 border border-pr-100"><h3 class="font-display font-bold mb-2">Few Hours Only</h3><p class="text-gray-600">Walk downtown, browse shops on Avenida Rafael Melgar, grab lunch and return — ideal for short port calls or mobility concerns.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-5 border border-ocean-100"><h3 class="font-display font-bold mb-2">Taxi to Beach</h3><p class="text-gray-600">Negotiate round-trip taxi to Mr Sanchos or Chankanaab — confirm return pickup time with driver before all aboard.</p></div>
    <div class="bg-sand-50 rounded-2xl p-5 border border-pr-100"><h3 class="font-display font-bold mb-2">When Book a Tour</h3><p class="text-gray-600">Reef snorkel, El Cielo and San Gervasio need boats or island transport — organised tours handle timing and gear.</p></div>
  </div>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{internal_links()}</div></section>"""


def content_port_map() -> str:
    snap = snapshot_default(best_for="Orienting to piers and attractions", popular="Pier map, taxi routes")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-6">Cozumel Cruise Port Map Overview</h2>
  <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
    <img src="{PORT_IMG}" alt="{PORT_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
  </div>
  <div class="grid sm:grid-cols-2 gap-6 text-sm max-w-4xl mx-auto">
    <div class="bg-white rounded-2xl p-5 border border-pr-100"><strong class="text-gray-900">San Miguel Downtown</strong><p class="mt-2 text-gray-600">Walk from Punta Langosta — shops, restaurants, waterfront.</p></div>
    <div class="bg-white rounded-2xl p-5 border border-pr-100"><strong class="text-gray-900">Chankanaab Park</strong><p class="mt-2 text-gray-600">A short drive south of the downtown pier area for many ships — allow for traffic.</p></div>
    <div class="bg-white rounded-2xl p-5 border border-pr-100"><strong class="text-gray-900">Mr Sanchos area</strong><p class="mt-2 text-gray-600">West-coast road from the port zone; journey time depends on pier and traffic.</p></div>
    <div class="bg-white rounded-2xl p-5 border border-pr-100"><strong class="text-gray-900">San Gervasio Ruins</strong><p class="mt-2 text-gray-600">Across the island interior — plan a longer transfer than a beach club hop.</p></div>
    <div class="bg-white rounded-2xl p-5 border border-pr-100"><strong class="text-gray-900">Palancar Reef</strong><p class="mt-2 text-gray-600">Southwest coast — boat access from marina zones.</p></div>
    <div class="bg-white rounded-2xl p-5 border border-pr-100"><strong class="text-gray-900">El Cielo Sandbar</strong><p class="mt-2 text-gray-600">Off southwest coast — reachable only by boat.</p></div>
  </div>
  <p class="text-center mt-8"><a href="cozumel-port-guide.html" class="text-ocean-600 font-semibold text-sm">Full port guide →</a></p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{internal_links()}</div></section>"""


def content_chankanaab_guide() -> str:
    snap = snapshot_default(best_for="Chankanaab park planning", popular="Park pass, snorkel, dolphins")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">Chankanaab National Marine Park sits south of the main cruise piers — lagoon and beach areas, a house reef snorkel zone, optional animal programs where offered, gardens and food outlets in one ticketed destination. Allow for transfer time that varies with pier and traffic.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Organised tours often include transport and a timed return plan — confirm details.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>House reef snorkel is commonly available; rental gear policies vary.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Introductory scuba may be offered inside or near the park depending on operator.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Lockers, showers and food outlets are typically available on site.</li>
    </ul>
    <a href="chankanaab-park-tour.html" class="btn-ocean inline-flex items-center text-white font-semibold px-6 py-3 rounded-full text-sm">Chankanaab Tour</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{CHANKANAAB_IMG}" alt="{CHANKANAAB_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{internal_links([("cozumel-scuba-diving-tour.html", "Scuba Diving")])}</div></section>"""


def content_mr_sanchos_guide() -> str:
    snap = snapshot_default(best_for="Mr Sanchos beach club visit", popular="Day pass, open bar, pool")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">Mr Sanchos on Cozumel’s west coast is a well-known beach-club style option for cruise passengers who want loungers, a pool and a social atmosphere away from the pier. Food, drink and amenity inclusions vary by package and date — confirm what you are buying rather than assuming a fixed “all-inclusive” list. Transfer time depends on which terminal you use and traffic.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Day-pass style packages can simplify budgeting when inclusions are clear.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Pool and beach facilities are part of the usual club atmosphere — check current amenities.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Reserve ahead on busy multi-ship days when possible.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Compare with <a href="cozumel-beach-day.html" class="text-ocean-600">other beach day</a> options.</li>
    </ul>
    <a href="mr-sanchos-beach-club.html" class="btn-ocean inline-flex items-center text-white font-semibold px-6 py-3 rounded-full text-sm">Mr Sanchos Excursion</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{MR_SANCHOS_IMG}" alt="{MR_SANCHOS_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{internal_links([("best-cozumel-beaches-for-cruise-passengers.html", "All Beaches")])}</div></section>"""


def all_guide_content() -> dict[str, str]:
    from cozumel_decisions import content_decision_reef_vs_beach, content_island_vs_mainland
    from cozumel_legal import all_legal_content

    guides = {
        "home.html": content_home(),
        "best-cozumel-shore-excursions.html": content_best_excursions(),
        "cozumel-port-guide.html": content_port_guide(),
        "one-day-in-cozumel-from-a-cruise-ship.html": content_one_day(),
        "best-cozumel-beaches-for-cruise-passengers.html": content_beaches_guide(),
        "is-cozumel-safe-for-cruise-passengers.html": content_safety(),
        "can-you-explore-cozumel-without-an-excursion.html": content_without_excursion(),
        "cozumel-cruise-port-map.html": content_port_map(),
        "chankanaab-park-guide.html": content_chankanaab_guide(),
        "mr-sanchos-cozumel-guide.html": content_mr_sanchos_guide(),
        "cozumel-island-vs-mainland.html": content_island_vs_mainland(),
        "cozumel-reef-vs-beach.html": content_decision_reef_vs_beach(),
    }
    guides.update(all_legal_content())
    return guides
