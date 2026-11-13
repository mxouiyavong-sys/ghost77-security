# Changelog

All notable changes to this repository are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- OpenSSF Best Practices Passing badge for this repository, with a link to the public badge page. This is a self-assessed badge, not a SOC 2 or ISO certification and not a degree.

### Changed

- `tools/`, `tests/`, and `schemas/` are now licensed under the MIT License. All other files remain all rights reserved. Copyright (c) 2026 Michael Xouiyavong. See [LICENSE](LICENSE).

## [0.1.0] - 2026-11-13

First tagged release of the public catalog.

### Added

- Public catalog for GhOsT77 Security: `pricing.json`, `services.json`, JSON Schemas, `llms.txt`, `.well-known/agent.json`, and `openapi.yaml`, with prices and buy links copied from the live site on 11 November 2026.
- `SECURITY.md` matching the live vulnerability disclosure policy.
- OpenSSF Scorecard workflow and badge, and Dependabot updates for GitHub Actions.
- `tools/validate_catalog.py`, a standard-library validator that checks the catalog against its schemas, requires HTTPS links, allows only the published payout wallet, and checks that prices agree between files.
- Automated tests in `tests/`, plus `CONTRIBUTING.md`, issue templates, and this changelog.

### Security

- No publicly known vulnerabilities have been fixed in this release.
