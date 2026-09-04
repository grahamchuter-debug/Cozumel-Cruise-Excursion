"""Island vs mainland and related decision content for Cozumel."""
from cozumel_config import (
    BEACHES_IMG, BEACHES_ALT, PORT_IMG, PORT_ALT, SNORKEL_IMG, SNORKEL_ALT,
)
from cozumel_helpers import concierge_panel, internal_links, snapshot_default


def content_island_vs_mainland() -> str:
    snap = snapshot_default(
        best_for="Choosing island day vs mainland day trip",
        activity_level="Mainland days are longer and less flexible",
        popular="Island reef/beach vs Playa/Tulum-style mainland days",
        return_ship="Mainland days need the most buffer — plan carefully",
    )
    return f"""<section class="pt-8 pb-6 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <p class="text-gray-600 leading-relaxed mb-4">One of the biggest Cozumel decisions is whether to stay on the island or cross to the mainland. Both can be excellent. They are not interchangeable on a typical cruise call.</p>
  <p class="text-gray-600 leading-relaxed">Staying on Cozumel keeps transfers shorter and leaves more room for weather, queues and a calm return to the pier. A mainland day opens larger archaeological sites and Riviera Maya scenery, but it spends more of your port day on ferries and roads.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-gray-900 text-center mb-8">Island day vs mainland day</h2>
  <div class="grid md:grid-cols-2 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-pr-100">
      <h3 class="font-display font-bold text-lg mb-3">Stay on Cozumel</h3>
      <ul class="space-y-2 text-gray-600">
        <li>Reef snorkelling, beach clubs, Chankanaab, San Gervasio and downtown San Miguel</li>
        <li>Shorter transfers from Puerta Maya, International Pier or Punta Langosta</li>
        <li>More flexibility if seas, heat or queues slow you down</li>
        <li>Better fit for short or medium calls</li>
      </ul>
      <p class="mt-4"><a href="cozumel-snorkeling-tour.html" class="text-ocean-600 font-semibold">Reef options →</a> · <a href="cozumel-beach-day.html" class="text-ocean-600 font-semibold">Beach day →</a></p>
    </div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100">
      <h3 class="font-display font-bold text-lg mb-3">Mainland day trip</h3>
      <ul class="space-y-2 text-gray-600">
        <li>Ferry to Playa del Carmen, then road transfers onward (for example toward major ruins)</li>
        <li>Longer door-to-door day with less spare time</li>
        <li>Ferry and road conditions can vary — build buffer, do not cut it fine</li>
        <li>Best only when your ship’s call and all-aboard time truly support it</li>
      </ul>
      <p class="mt-4 text-gray-600">We do not publish fixed “always takes X hours” claims. Ask operators for current ferry and transfer plans for your date.</p>
    </div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="grid lg:grid-cols-2 gap-10 items-center mb-12">
    <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
      <img src="{SNORKEL_IMG}" alt="{SNORKEL_ALT}" width="600" height="450" loading="lazy" decoding="async" />
    </div>
    <div>
      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">San Gervasio is not Tulum</h2>
      <p class="text-gray-600 leading-relaxed mb-3">San Gervasio on Cozumel is a meaningful Mayan site with a lighter logistics load than major mainland ruins. It suits passengers who want history without a ferry-and-highway day.</p>
      <p class="text-gray-600 leading-relaxed">If your priority is a flagship mainland archaeological complex, you are choosing a fuller, less flexible port day. Compare that honestly against reef or beach time on the island.</p>
      <p class="mt-4"><a href="cozumel-mayan-ruins-tour.html" class="text-ocean-600 font-semibold">San Gervasio / island ruins →</a></p>
    </div>
  </div>
  <div class="grid lg:grid-cols-2 gap-10 items-center">
    <div>
      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Terminals still matter</h2>
      <p class="text-gray-600 leading-relaxed mb-3">Meeting points, taxi plazas and downtown walking distance change depending on whether you use Puerta Maya, International Pier or Punta Langosta. Assignments can vary — check your cruise information rather than assuming a ship always uses the same pier.</p>
      <p class="mt-4"><a href="cozumel-port-guide.html" class="text-ocean-600 font-semibold">Terminal guide →</a> · <a href="ship-schedule/" class="text-ocean-600 font-semibold">Ship schedule →</a></p>
    </div>
    <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
      <img src="{PORT_IMG}" alt="{PORT_ALT}" width="600" height="450" loading="lazy" decoding="async" />
    </div>
  </div>
  <div class="mt-12 max-w-3xl mx-auto">{internal_links([("one-day-in-cozumel-from-a-cruise-ship.html", "One-day paths")])}</div>
</div></section>
{concierge_panel()}"""


def content_decision_reef_vs_beach() -> str:
    snap = snapshot_default(
        best_for="Choosing reef snorkel vs beach club",
        popular="Palancar/El Cielo vs Mr Sanchos/Chankanaab beach time",
    )
    return f"""<section class="pt-8 pb-6 bg-white"><div class="max-w-3xl mx-auto px-4">
  <p class="text-gray-600 leading-relaxed mb-4">If you want water and sun, Cozumel usually comes down to a boat reef day or a beach-club day. Chankanaab sits in the middle: park facilities plus a house reef.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-5xl mx-auto px-4">
  <div class="grid md:grid-cols-2 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-pr-100">
      <div class="card-media rounded-2xl overflow-hidden aspect-[16/10] mb-4">
        <img src="{SNORKEL_IMG}" alt="{SNORKEL_ALT}" width="600" height="375" loading="lazy" decoding="async" />
      </div>
      <h3 class="font-display font-bold text-lg mb-2">Reef / boat snorkel</h3>
      <p class="text-gray-600 mb-3">Better when you care about reef structure and multiple water stops. Marine life is natural and variable — guides help, but nothing underwater is guaranteed.</p>
      <a href="cozumel-snorkeling-tour.html" class="text-ocean-600 font-semibold">Snorkelling tours →</a>
      <span class="text-gray-300 mx-2">·</span>
      <a href="cozumel-catamaran-sail-and-snorkel.html" class="text-ocean-600 font-semibold">Catamaran →</a>
    </div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100">
      <div class="card-media rounded-2xl overflow-hidden aspect-[16/10] mb-4">
        <img src="{BEACHES_IMG}" alt="{BEACHES_ALT}" width="600" height="375" loading="lazy" decoding="async" />
      </div>
      <h3 class="font-display font-bold text-lg mb-2">Beach club day</h3>
      <p class="text-gray-600 mb-3">Better when you want loungers, shade, food and a slower pace. Clubs differ in atmosphere and facilities; check current inclusions with the operator rather than assuming a fixed package.</p>
      <a href="mr-sanchos-beach-club.html" class="text-ocean-600 font-semibold">Mr Sanchos →</a>
      <span class="text-gray-300 mx-2">·</span>
      <a href="cozumel-beach-day.html" class="text-ocean-600 font-semibold">Beach day options →</a>
    </div>
  </div>
  <p class="text-center mt-8 text-sm"><a href="chankanaab-park-tour.html" class="text-ocean-600 font-semibold">Prefer both? Look at Chankanaab →</a></p>
  <div class="mt-10 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>
{concierge_panel()}"""
