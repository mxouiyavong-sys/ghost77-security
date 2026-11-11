# Publish notes (not published)

This folder is a local draft only. It has a git commit on this machine. It has not been created as a GitHub repository and has not been pushed.

## Connected GitHub account

Checked read-only with the cursor-github connector `get_me` / `list_my_repositories` on 11 November 2026:

- Account: **mxouiyavong-sys** (profile name: Ghost77-Agent)
- Profile: https://github.com/mxouiyavong-sys
- Blog field: https://ghost77-agent.onrender.com
- Type: User (no organization was returned by `get_me`)
- Existing repos under that account include `crew2` (private) and public forks such as `ruth`, `local-ai-registry`, `ArbiVault`, `for-funsies`, `hero`, `ai-research`, and `spoovault`, plus the profile repo `mxouiyavong-sys`. There is **no** existing `ghost77-security` repo.
- The account has admin permission on those repos.

## Can the connector create the repo?

No `create_repository` (or equivalent) tool is available in the cursor-github connector. Branches, issues, and pull requests can be created on an existing repo, but a new repository cannot be created through that connector. Do not use another path to create or push this repo until the owner explicitly asks.

## Proposed GitHub settings

- Owner: `mxouiyavong-sys`
- Repository name: `ghost77-security`
- Visibility: public
- Description: `GhOsT77 Security: website fixes, hacked-site cleanup, FAQ chatbot setup, monthly upkeep, and consent-only security reviews. Pricing and buy links for people and AI agents.`
- Homepage: `https://ghost77-security.onrender.com`
- Topics: `security`, `website-security`, `small-business`, `cybersecurity`, `malware-cleanup`, `chatbot`, `security-audit`, `security-review`, `stripe`, `usdc`, `base`, `x402`, `ai-agents`, `llms-txt`

Do not upload secrets, private code, VPS addresses, or internal paths if this is published later.
