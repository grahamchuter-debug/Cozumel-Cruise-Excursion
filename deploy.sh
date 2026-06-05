#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

echo "Deploying Cozumel Cruise Excursion to Cloudflare..."
npx wrangler deploy

echo "Done. Check https://cozumelcruiseexcursion.com/ shortly."
