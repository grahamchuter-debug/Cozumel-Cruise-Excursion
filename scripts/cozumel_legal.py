"""Legal, about, contact and methodology pages for Cozumel Cruise Excursion."""
from cozumel_helpers import concierge_panel, internal_links


def content_about() -> str:
    return f"""<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 prose-coz">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">About Cozumel Cruise Excursion</h2>
  <p class="text-gray-600 leading-relaxed mb-4">We publish independent planning guidance for cruise passengers calling at Cozumel, Mexico. The focus is practical: which kind of day fits your ship time, how the terminals differ, and how island options compare with a mainland day trip.</p>
  <p class="text-gray-600 leading-relaxed mb-4">This site is not a cruise line, not a ticket marketplace, and not an official port authority. Where we discuss excursions, we do so editorially so you can compare choices before you decide how to spend the day.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Ship schedules shown here are synced from the Caribbean Shore Excursions authority dataset for Cozumel. Times can still change — always confirm with your cruise line.</p>
  <p class="text-gray-600 leading-relaxed mb-8">Regional context lives on <a href="https://caribbeanshoreexcursion.com/" class="text-ocean-600 font-medium">Caribbean Shore Excursions</a>. Cozumel detail lives here.</p>
  {internal_links()}
</div></section>
{concierge_panel()}"""


def content_contact() -> str:
    return f"""<section class="pt-10 pb-8 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Contact</h2>
  <p class="text-gray-600 leading-relaxed mb-4">If you want help narrowing a Cozumel port day, the most useful details are your ship name, call date, terminal if you know it, and whether you prefer reef time, a beach club, ruins, or an easy low-effort day.</p>
  <p class="text-gray-600 leading-relaxed mb-6">Email <a class="text-ocean-600 font-semibold" href="mailto:hello@cozumelcruiseexcursion.com">hello@cozumelcruiseexcursion.com</a>. We are an independent planning resource and do not promise instant replies.</p>
  <ul class="space-y-2 text-sm text-gray-600 mb-8">
    <li><a class="text-ocean-600 font-semibold" href="ship-schedule/">Find your ship schedule</a></li>
    <li><a class="text-ocean-600 font-semibold" href="best-cozumel-shore-excursions.html">Compare excursion types</a></li>
    <li><a class="text-ocean-600 font-semibold" href="cozumel-port-guide.html">Read the port guide</a></li>
  </ul>
  {internal_links()}
</div></section>
{concierge_panel()}"""


def content_privacy() -> str:
    return """<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Privacy</h2>
  <p class="text-gray-600 leading-relaxed mb-4">This is a static planning website. In this phase we do not operate a booking engine, payment system, or passenger account database.</p>
  <p class="text-gray-600 leading-relaxed mb-4">If you contact us by email after the concierge address is activated, we will use your message only to respond about Cozumel port-day planning. We will not sell contact details.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Standard web server and CDN logs may record technical request data (such as IP address, user agent and requested URL) as part of delivering the site securely. We do not add analytics trackers in this build.</p>
  <p class="text-gray-600 leading-relaxed">If our contact or tooling practices change, this page will be updated before those features go live.</p>
</div></section>"""


def content_terms() -> str:
    return """<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Terms of use</h2>
  <p class="text-gray-600 leading-relaxed mb-4">Content on Cozumel Cruise Excursion is provided for general information and planning. It is not a contract of carriage, not travel insurance, and not a guarantee of excursion availability, wildlife sightings, weather, ferry conditions or on-time return to your ship.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Cruise schedules, pier assignments and excursion details can change. Confirm final arrangements with your cruise line and any operator you choose.</p>
  <p class="text-gray-600 leading-relaxed mb-4">We are independent of cruise lines and of Cozumel's port operators. Mentions of places, parks or beach clubs are for orientation and do not imply partnership unless we say so explicitly.</p>
  <p class="text-gray-600 leading-relaxed">You are responsible for leaving enough time to reboard, for following local rules (including marine park guidance), and for checking any medical or activity requirements before water or adventure activities.</p>
</div></section>"""


def content_methodology() -> str:
    return f"""<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">How we assess Cozumel excursions</h2>
  <p class="text-gray-600 leading-relaxed mb-4">We judge options the way a cruise passenger has to: against the length of the call, the terminal you use, heat and transfer time, and how much buffer you need before all aboard.</p>
  <div class="space-y-4 text-sm text-gray-600 mb-8">
    <div class="bg-sand-50 rounded-2xl p-5 border border-pr-100"><h3 class="font-display font-bold text-gray-900 mb-2">Cruise timing first</h3><p>A brilliant full-day mainland trip is the wrong answer on a short call. We favour options that leave a realistic return window.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-5 border border-ocean-100"><h3 class="font-display font-bold text-gray-900 mb-2">Decision clarity</h3><p>Reef versus beach club, island versus mainland, San Gervasio versus major mainland ruins — passengers need honest trade-offs, not marketplace noise.</p></div>
    <div class="bg-sand-50 rounded-2xl p-5 border border-pr-100"><h3 class="font-display font-bold text-gray-900 mb-2">No invented proof</h3><p>We do not invent star ratings, review counts or “places left”. Trust comes from clear planning language and transparent limits.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-5 border border-ocean-100"><h3 class="font-display font-bold text-gray-900 mb-2">Schedule integrity</h3><p>Call lists are generated from the Caribbean authority import for Cozumel, then checked for count and record-level match before pages are built.</p></div>
  </div>
  {internal_links()}
</div></section>
{concierge_panel()}"""


def all_legal_content() -> dict[str, str]:
    return {
        "about.html": content_about(),
        "contact.html": content_contact(),
        "privacy.html": content_privacy(),
        "terms.html": content_terms(),
        "methodology.html": content_methodology(),
    }
