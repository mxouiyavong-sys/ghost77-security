# Sources

Prices, service descriptions, and buy links in this repository were copied from public pages on 11 November 2026, between about 4:42 PM and 4:50 PM ET (America/New_York). Nothing here is a fabricated testimonial, sales count, or unpublished price.

## Primary (GhOsT77 Security)

- https://ghost77-security.onrender.com/ — homepage copy, FAQ, scanner grades, JSON-LD offers, Stripe Payment Links, authorization pointer, payout wallet
- https://ghost77-security.onrender.com/cleanup — Hacked Site Cleanup, $249 Stripe link
- https://ghost77-security.onrender.com/chatbot — FAQ Chatbot Setup $199 and Chatbot Care $29/month Stripe links
- https://ghost77-security.onrender.com/terms — draft terms (2026-11-10-draft4)
- https://ghost77-security.onrender.com/privacy
- https://ghost77-security.onrender.com/reports and https://ghost77-security.onrender.com/reports/feed.xml
- https://ghost77-security.onrender.com/sitemap.xml
- https://ghost77-security.onrender.com/robots.txt
- https://ghost77-security.onrender.com/.well-known/security.txt

## Agent endpoints used for reviews and machine purchase

- https://ghost77-agent.onrender.com/security/request — authorization and payment request (HTTP 200)
- https://ghost77-agent.onrender.com/security/authorization — testing authorization text (HTTP 200)
- https://ghost77-agent.onrender.com/llms.txt — review prices, USDC, caps, turnaround (HTTP 200)
- https://ghost77-agent.onrender.com/.well-known/agent.json and /.well-known/agent-card.json (HTTP 200, same document when checked)
- https://ghost77-agent.onrender.com/.well-known/x402 (HTTP 200)
- https://ghost77-agent.onrender.com/services.json (HTTP 200)
- https://ghost77-agent.onrender.com/openapi.json (HTTP 200)
- https://ghost77-agent.onrender.com/.well-known/mcp/server-card.json and /.well-known/mcp.json (HTTP 200)
- POST https://ghost77-agent.onrender.com/mcp — GET returns 405 and asks for JSON-RPC POST, which confirms the endpoint exists
- POST https://ghost77-agent.onrender.com/x402/contract_security_scan — unpaid request returned HTTP 402; payTo `0x659db9537fee7a3473ff6e2a5a661af65ae288e3`; $0.55 USDC on Base
- https://ghost77-agent.onrender.com/sitemap.xml
- https://ghost77-agent.onrender.com/health — HTTP 200 `{"ok": true, ...}`

## Stripe Payment Links

Each of the following returned HTTP 200 and a Stripe Checkout page when fetched (no payment was submitted):

- https://buy.stripe.com/3cIaEZ53K9UX0JA4M6gbm01 — Website Fix $99
- https://buy.stripe.com/7sY6oJdAggjl1NE2DYgbm02 — Website Upkeep $25/month
- https://buy.stripe.com/00waEZ3ZG9UXeAq2DYgbm0b — Hacked Site Cleanup $249
- https://buy.stripe.com/5kQ28t8fW3wzgIy3I2gbm0c — FAQ Chatbot Setup $199
- https://buy.stripe.com/14A28tcwc0kn63U1zUgbm0d — FAQ Chatbot Care $29/month
- https://buy.stripe.com/dRmeVf7bS5EH77YemGgbm03 — Quick security review $149
- https://buy.stripe.com/14A3cxeEk7MP8c2diCgbm04 — Standard security review $449
- https://buy.stripe.com/6oU6oJ1Ryebd1NE6Uegbm05 — Deep security review $999

Label-to-URL mapping is taken from the Security homepage and its JSON-LD `hasOfferCatalog`. Review Stripe links are on the homepage next to “Pay $149/$449/$999 by card”; JSON-LD `url` for the three review tiers points at the authorization request form, which is also a valid starting point.

## Checked and not present on the Security marketing site

These paths on https://ghost77-security.onrender.com returned HTTP 404: `/llms.txt`, `/.well-known/agent.json`, `/.well-known/x402`, `/openapi.yaml`, `/openapi.json`, `/pricing.json`, `/services.json`, `/api`, `/x402`, `/request`, `/authorize`, `/authorization`, `/rss`, `/reports/rss`, `/feed.xml`. Agents should use this repo and the agent-site URLs above instead.

## Contact note

The phone number (518) 532-8037 is published on both live sites. The live Security site and its security.txt list ghost77-secure@outlook.com. ghost77@mail.grokbot.com is included in this repo as an additional contact.
