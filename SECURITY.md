# Security policy

Report a vulnerability in GhOsT77 Security, the GhOsT77 agent, Getaway Genie, or this repository. Do not attach passwords, API keys, seed phrases, or customer data.

This file matches the live vulnerability disclosure policy published 12 November 2026:

https://ghost77-security.onrender.com/security/vulnerability-disclosure

## Where to report

Email **ghost77-secure@outlook.com**. That is the intake path named in the public vulnerability disclosure policy.

Machine-readable contacts:

- https://ghost77-security.onrender.com/.well-known/security.txt
- https://ghost77-agent.onrender.com/.well-known/security.txt
- https://getawaygenie.vercel.app/.well-known/security.txt

Please include the affected URL or component, a short description, steps to reproduce, the potential impact, and your preferred contact. English is preferred.

Do not send vulnerability details through a public Discord channel, and do not dictate secrets to Rebecca, the AI receptionist. The phone line and Discord are for general questions only.

## Scope

In scope (GhOsT77-owned systems only):

- https://ghost77-security.onrender.com
- https://ghost77-agent.onrender.com
- https://getawaygenie.vercel.app
- This public sales repository
- Public agent discovery files on those hosts (for example `/.well-known/agent.json`, `/.well-known/x402`, `/.well-known/mcp/server-card.json`, `/llms.txt`)
- Rebecca, the Vapi AI phone receptionist at +1 518 532 8037, as a GhOsT77-operated service (do not leave secrets on the call)

This repository is a sales and discovery page. It does not host application source code or accept unauthenticated report uploads.

Out of scope: systems you do not own or are not authorized to test (including customer sites); third-party platforms GhOsT77 uses but does not operate (Render, Vercel, Stripe, GitHub, Discord, Outlook, Vapi, Virtuals, Coinbase/x402 infrastructure, and similar); denial-of-service or load testing; social engineering or phishing; physical attacks; and reports that include secrets in the report itself.

Default testing must stay non-destructive. Anything beyond normal page and file requests needs written authorization first. The customer testing authorization at https://ghost77-agent.onrender.com/security/authorization is only for paid, consent-only reviews of a customer's systems, not for testing GhOsT77.

## What to expect

- Acknowledgement within 3 business days
- An initial assessment within 10 business days
- An update at least every 30 days until the issue is resolved or we explain why we will not change it
- Notice when a fix or mitigation is available

This is not a paid bug-bounty program. Coordinated disclosure, safe-harbour language, and the full scope text are in the policy linked above. Have a lawyer review that safe-harbour section before relying on it; it is not legal advice.

## Payment address (only if a report is ever tied to a paid review)

USDC on Base is paid only to `0x659db9537fee7a3473ff6e2a5a661af65ae288e3`. Do not send funds to any other address.

<!-- After the owner enables GitHub private vulnerability reporting, add a short sentence here: "You can also use GitHub's private vulnerability reporting form on this repository's Security tab." Do not add that sentence until the setting is actually on. -->
