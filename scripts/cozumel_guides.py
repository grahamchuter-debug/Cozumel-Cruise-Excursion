"""Guide and home page content for Cozumel Cruise Excursion."""
from cozumel_config import (
    BEACHES_IMG, BEACHES_ALT, BEST_IMG, BEST_ALT, CHANKANAAB_IMG, CHANKANAAB_ALT,
    INTRO_IMG, INTRO_ALT, MR_SANCHOS_IMG, MR_SANCHOS_ALT, PORT_IMG, PORT_ALT,
    SNORKEL_IMG, SNORKEL_ALT,
)
from cozumel_helpers import (
    card_grid, comparison_section, internal_links, snapshot_default,
)


def content_home() -> str:
    featured = card_grid([
        (SNORKEL_IMG, SNORKEL_ALT, "Cozumel Snorkeling", "Palancar Reef, El Cielo sandbar and Colombia Reef with gear and guides.", "cozumel-snorkeling-tour.html", "Snorkeling"),
        (CHANKANAAB_IMG, CHANKANAAB_ALT, "Chankanaab Park", "Reef snorkel, beach, dolphins and botanical gardens near the port.", "chankanaab-park-tour.html", "Chankanaab"),
        (MR_SANCHOS_IMG, MR_SANCHOS_ALT, "Mr Sanchos Beach Club", "All-inclusive west-coast beach day with pool and open bar.", "mr-sanchos-beach-club.html", "Mr Sanchos"),
        (SNORKEL_IMG, SNORKEL_ALT, "Catamaran Sail &amp; Snorkel", "Sailing, reef snorkel and El Cielo on a spacious catamaran.", "cozumel-catamaran-sail-and-snorkel.html", "Catamaran"),
    ])
    best_cards = card_grid([
        (SNORKEL_IMG, SNORKEL_ALT, "Snorkeling Tour", "World-class reef sites on the Mesoamerican Barrier Reef.", "cozumel-snorkeling-tour.html", "Reef Tours"),
        (BEACHES_IMG, BEACHES_ALT, "Beach Day", "Loungers, calm water and all-inclusive beach clubs.", "cozumel-beach-day.html", "Beach Day"),
        (CHANKANAAB_IMG, CHANKANAAB_ALT, "Chankanaab Park", "One-stop snorkel, beach and family activities.", "chankanaab-park-tour.html", "Park Tour"),
        (SNORKEL_IMG, SNORKEL_ALT, "Best of Cozumel", "Island highlights, culture and tequila in one tour.", "best-of-cozumel.html", "Best of Cozumel"),
    ])
    snap = snapshot_default()
    return f"""<section class="pt-8 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-10">
    <div class="section-label mx-auto">Best Excursions</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-4">Best Cozumel Cruise Excursions</h2>
    <p class="text-gray-600 text-sm max-w-2xl mx-auto">Ranked for cruise schedules — reef snorkeling, beach clubs, Chankanaab, jeep adventures and Mayan ruins across Cozumel, Mexico.</p>
  </div>
  {best_cards}
  <p class="text-center mt-8"><a href="best-cozumel-shore-excursions.html" class="text-ocean-600 font-semibold text-sm">See full comparison →</a></p>
</div></section>
<section class="pt-4 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <div class="inline-flex items-center gap-2 text-ocean-600 text-xs font-semibold tracking-widest uppercase mb-3"><div class="w-8 h-px bg-ocean-400"></div>Cozumel Cruise Port</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-5">Why Cruise Passengers<br/><span class="text-ocean-600">Choose Cozumel</span></h2>
    <p class="text-gray-600 leading-relaxed mb-5">Cozumel pairs world-class reef snorkeling with relaxed beach clubs and easy downtown shopping — Palancar Reef, El Cielo, Chankanaab and Mr Sanchos fit a typical <strong>6–10 hour</strong> port call. USD is widely accepted; Mexican pesos are the official currency.</p>
    <a href="cozumel-port-guide.html" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Port Guide</a>
  </div>
  <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
    <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-16 bg-amber-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-12"><h2 class="text-3xl font-display font-bold text-gray-900">Featured Excursions</h2>
  <p class="text-gray-600 text-sm mt-3 max-w-xl mx-auto">Most-booked shore excursions for Cozumel cruise passengers.</p></div>
  {featured}
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 text-center mb-10">Top Things To Do in Cozumel</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Reef Snorkeling</h3><p class="text-gray-600">Palancar, Colombia Reef and El Cielo sandbar — among the Caribbean's clearest water.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Chankanaab Park</h3><p class="text-gray-600">Marine park with house reef snorkel, beach and optional dolphin encounters.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Beach Club Day</h3><p class="text-gray-600">Mr Sanchos and west-coast clubs offer all-inclusive lounging 20 minutes from port.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">San Gervasio Ruins</h3><p class="text-gray-600">Mayan archaeological site dedicated to goddess Ixchel in the island interior.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Downtown San Miguel</h3><p class="text-gray-600">Walkable from Punta Langosta pier — shops, cafés and waterfront malecón.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Jeep &amp; ATV Adventures</h3><p class="text-gray-600">Jungle trails, cenotes and reef snorkel combos for active port days.</p></div>
  </div>
</div></section>
<section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BEACHES_IMG}" alt="{BEACHES_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best Beaches For Cruise Passengers</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Cozumel's west coast faces the protected Caribbean — calm water, soft sand and beach clubs with food, drinks and snorkel access. Mr Sanchos, Chankanaab and all-inclusive day passes are the top picks for cruise guests who want a hassle-free beach day.</p>
    <p class="text-gray-600 leading-relaxed mb-5">East-coast beaches face open ocean with stronger surf — most cruise excursions stay on the leeward side. See our <a href="best-cozumel-beaches-for-cruise-passengers.html" class="text-ocean-600 font-medium">beach guide</a> for pier distances and taxi tips.</p>
    <a href="mr-sanchos-beach-club.html" class="text-ocean-600 font-semibold text-sm">Mr Sanchos Beach Club →</a>
  </div>
</div></div></section>
<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Snorkeling In Cozumel</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Cozumel, Mexico sits on the Mesoamerican Reef — cruise passengers snorkel dramatic coral walls at Palancar, shallow gardens at Colombia Reef and the famous El Cielo sandbar where starfish rest in gin-clear shallows.</p>
    <p class="text-gray-600 leading-relaxed mb-5">Morning seas are typically calmer. Catamaran and boat tours include gear; reef-safe sunscreen protects the ecosystem. Certified divers can add a <a href="cozumel-scuba-diving-tour.html" class="text-ocean-600 font-medium">scuba dive</a> at Chankanaab.</p>
    <a href="cozumel-snorkeling-tour.html" class="text-ocean-600 font-semibold text-sm">Snorkeling tours →</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{SNORKEL_IMG}" alt="{SNORKEL_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
{comparison_section()}
{home_faq_section()}
<section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-white mb-4">Plan Your Cozumel Port Day</h2>
  <p class="text-white/85 text-sm mb-6">Compare excursions, read the port guide and build your itinerary before you dock in Cozumel, Mexico.</p>
  <div class="flex flex-col sm:flex-row gap-4 justify-center">
    <a href="best-cozumel-shore-excursions.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Compare Excursions</a>
    <a href="cozumel-port-guide.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Port Guide</a>
  </div>
</div></section>"""


def home_faq_section() -> str:
    return """<section class="py-16 bg-white"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-3xl font-display font-bold text-gray-900 text-center mb-8">Cozumel Shore Excursions FAQ</h2>
  <div class="space-y-4">
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do cruise ships stay in Cozumel?</summary>
      <p class="mt-4 text-sm text-gray-500">Most Cozumel port calls are 6 to 10 hours. A half-day snorkel or beach club fits comfortably; full-day catamaran trips need a longer call with return buffer.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Which Cozumel cruise pier will my ship use?</summary>
      <p class="mt-4 text-sm text-gray-500">Ships dock at Punta Langosta (downtown), International Pier or Puerta Maya (south). Your cruise line assigns the pier — check your itinerary and our <a href="cozumel-port-guide.html" class="text-ocean-600">port guide</a>.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What currency is used in Cozumel?</summary>
      <p class="mt-4 text-sm text-gray-500">Mexican pesos (MXN) are official. USD is widely accepted in tourist areas — carry small bills for taxis and tips.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Beach day or snorkeling for a Cozumel port day?</summary>
      <p class="mt-4 text-sm text-gray-500">Snorkeling for reef lovers; beach clubs like Mr Sanchos for relaxed lounging. Chankanaab combines both. First-timers often choose Best of Cozumel or Chankanaab.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Ship excursion or book independently in Cozumel?</summary>
      <p class="mt-4 text-sm text-gray-500">Ship tours guarantee the vessel waits if the operator is late. Reputable Cozumel operators plan returns with buffer — confirm policies before booking ashore.</p></details>
  </div>
</div></section>"""


def home_faq_data() -> list[tuple[str, str]]:
    return [
        ("How long do cruise ships stay in Cozumel?", "Most Cozumel port calls are 6 to 10 hours."),
        ("Which Cozumel cruise pier will my ship use?", "Punta Langosta, International Pier or Puerta Maya — check your cruise itinerary."),
        ("What currency is used in Cozumel?", "Mexican pesos official; USD widely accepted in tourist areas."),
        ("Beach day or snorkeling for a Cozumel port day?", "Snorkeling for reefs; beach clubs for relaxing; Chankanaab combines both."),
        ("Ship excursion or book independently in Cozumel?", "Ship tours guarantee wait-if-late; reputable locals plan buffer returns."),
    ]


def content_best_excursions() -> str:
    snap = snapshot_default(best_for="Comparing all excursion types", popular="See comparison table below")
    rankings = """<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Excursions by Traveler Type</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Families</h3><p class="text-gray-600 mb-3">Chankanaab Park, beach day passes and gentle snorkel catamarans suit mixed ages.</p><a href="chankanaab-park-tour.html" class="text-ocean-600 font-semibold">Chankanaab →</a></div>
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Couples</h3><p class="text-gray-600 mb-3">Mr Sanchos all-inclusive, private catamaran and tequila tasting tours.</p><a href="mr-sanchos-beach-club.html" class="text-ocean-600 font-semibold">Mr Sanchos →</a></div>
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
  <p class="text-gray-600 leading-relaxed text-sm">Ships dock at <strong>Cozumel cruise port</strong> piers with reef snorkeling, beach clubs and San Miguel downtown on a typical <strong>6–10 hour</strong> call in Quintana Roo, Mexico.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Where Ships Arrive</h2>
  <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
    <img src="{PORT_IMG}" alt="{PORT_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
  </div>
  <div class="grid lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Punta Langosta</h3><p class="text-gray-600">Downtown pier — walk to San Miguel shops, waterfront malecón and cafés in minutes. Taxis to south-side attractions.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">International Pier</h3><p class="text-gray-600">South of downtown — tour pickups at terminal. 10–15 minute taxi to San Miguel; 15–20 minutes to Chankanaab.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Puerta Maya</h3><p class="text-gray-600">Carnival Corporation pier south of town — organised excursions meet inside terminal. Taxi plaza outside for independent trips.</p></div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Practical Port Day Info</h2>
  <div class="grid sm:grid-cols-3 gap-6 text-sm">
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">Mexican pesos (MXN) official. <strong>USD</strong> accepted at tourist businesses — carry small bills for taxis.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Taxis</strong><p class="mt-2 text-gray-600">Official taxis at all piers — agree fare before departing. No rideshare; fixed-route vans serve popular beaches.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Return Timing</strong><p class="mt-2 text-gray-600">Allow 60–90 minutes before all aboard. Organised tours build buffer; independent guests track ship time carefully.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Safety</strong><p class="mt-2 text-gray-600">Cozumel is heavily touristed. See our <a href="is-cozumel-safe-for-cruise-passengers.html" class="text-ocean-600 font-medium">safety guide</a> for practical tips.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Weather &amp; Seas</strong><p class="mt-2 text-gray-600">Tropical year-round. Rainy season June–October. Morning snorkel seas are typically calmer on the west coast.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Distances</strong><p class="mt-2 text-gray-600">Chankanaab 15–20 min south. Mr Sanchos ~20 min. San Gervasio ruins ~45 min across island.</p></div>
  </div>
  <p class="text-center mt-8"><a href="cozumel-cruise-port-map.html" class="text-ocean-600 font-semibold text-sm">Port map →</a> · <a href="one-day-in-cozumel-from-a-cruise-ship.html" class="text-ocean-600 font-semibold text-sm">One-day itinerary →</a></p>
  <div class="mt-10 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>"""


def content_one_day() -> str:
    snap = snapshot_default(best_for="Morning snorkel + afternoon beach or downtown")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <p class="text-gray-600 text-sm">Sample timeline for a <strong>6–10 hour</strong> Cozumel call. Adjust for your ship's actual times.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Classic Cozumel Port Day</h2>
  <ol class="space-y-4 text-sm">
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">08:00</span><div><strong>Depart pier</strong><p class="text-gray-600 mt-1">Meet snorkel catamaran or transfer to Chankanaab — morning reef visibility is best.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">09:30</span><div><strong>El Cielo or Chankanaab snorkel</strong><p class="text-gray-600 mt-1">Reef sites with guide; float in crystal shallows at El Cielo sandbar.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">12:00</span><div><strong>Lunch &amp; beach</strong><p class="text-gray-600 mt-1">Beach club buffet or tacos at Kuza — relax before afternoon heat peaks.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">14:00</span><div><strong>Downtown or second activity</strong><p class="text-gray-600 mt-1">Shopping in San Miguel from Punta Langosta pier, or extend beach time at Mr Sanchos.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">16:30</span><div><strong>Return toward ship</strong><p class="text-gray-600 mt-1">Taxi or tour transfer to your pier — allow margin before all aboard.</p></div></li>
  </ol>
  <div class="mt-8 bg-white rounded-2xl p-6 border border-pr-100">
    <h3 class="font-display font-bold text-lg mb-3">Suggested Excursions</h3>
    <ul class="space-y-2 text-sm text-gray-600">
      <li><a href="cozumel-snorkeling-tour.html" class="text-ocean-600 font-medium">Snorkeling Tour</a> — best single water excursion</li>
      <li><a href="chankanaab-park-tour.html" class="text-ocean-600 font-medium">Chankanaab Park</a> — snorkel and beach in one stop</li>
      <li><a href="best-of-cozumel.html" class="text-ocean-600 font-medium">Best of Cozumel</a> — culture and highlights for first-timers</li>
    </ul>
  </div>
  <div class="mt-10">{internal_links()}</div>
</div></section>"""


def content_beaches_guide() -> str:
    snap = snapshot_default(best_for="Choosing a west-coast beach club", popular="Mr Sanchos, Chankanaab, day passes")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">Cozumel's cruise-friendly beaches sit on the protected west coast — calm turquoise water, soft sand and clubs with loungers, food and open bars. East-coast beaches face open ocean with stronger surf and are rarely included on shore excursions.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Mr Sanchos</strong> — all-inclusive favourite, ~20 min from port. <a href="mr-sanchos-cozumel-guide.html" class="text-ocean-600">Guide →</a></li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Chankanaab</strong> — park with reef snorkel and beach, 15–20 min south.</li>
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
    <div class="bg-white rounded-2xl p-5 border border-pr-100"><strong class="text-gray-900">Chankanaab Park</strong><p class="mt-2 text-gray-600">~8 km / 15–20 min south of downtown piers.</p></div>
    <div class="bg-white rounded-2xl p-5 border border-pr-100"><strong class="text-gray-900">Mr Sanchos</strong><p class="mt-2 text-gray-600">~10 km / ~20 min west-coast road from port area.</p></div>
    <div class="bg-white rounded-2xl p-5 border border-pr-100"><strong class="text-gray-900">San Gervasio Ruins</strong><p class="mt-2 text-gray-600">~20 km / ~45 min across island interior.</p></div>
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
    <p class="text-gray-600 leading-relaxed mb-6">Chankanaab National Marine Park is 15–20 minutes south of Cozumel cruise piers — a protected lagoon, beach, house reef snorkel, sea lion and dolphin programs, botanical gardens and restaurants in one ticketed destination.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Organised tours include transport and timed return to ship.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>House reef snorkel suitable for beginners with rental gear on site.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Discover scuba and one-tank dives available inside the park.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Lockers, showers and multiple food outlets inside the park.</li>
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
    <p class="text-gray-600 leading-relaxed mb-6">Mr Sanchos Beach Club on Cozumel's west coast is a top cruise passenger pick — all-inclusive food and drinks, freshwater pool, beach loungers and calm Caribbean swimming about 20 minutes from the port by taxi or organised transfer.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Pay-one-price packages simplify budgeting for groups.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Pool, beach volleyball and water trampoline activities.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Reserve ahead on busy multi-ship days.</li>
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
    return {
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
    }
