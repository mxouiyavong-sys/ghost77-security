# Contributing

Thanks for helping. This repository holds the public catalog for GhOsT77 Security: prices, buy links, service descriptions, agent discovery files, the JSON Schemas for them, and a small validator (`tools/validate_catalog.py`) with its tests. It is not the source code of the live sites.

## Ways to help

- **Report a bug or a wrong price or link:** open an issue at https://github.com/mxouiyavong-sys/ghost77-security/issues and choose "Bug report". Say which file and line is wrong and what it should say, with a source link if you have one.
- **Ask for an improvement:** open an issue and choose "Feature request".
- **Report a security vulnerability:** do **not** open a public issue. Follow [SECURITY.md](SECURITY.md).
- **Ask a general question:** open an issue, or email ghost77@mail.grokbot.com.

Issues and pull requests are public and searchable, and every message has its own URL. Please write in English.

## How changes are made (pull requests)

1. Fork the repository, or create a branch if you have write access.
2. Make your change in small, focused commits with clear messages.
3. Run the checks below and make sure they pass.
4. Open a pull request against `main` and describe what changed and why. Link any source page for a price or URL change.
5. A maintainer reviews it. The `main` branch is protected, so every change lands through a pull request. Changes to prices, buy links, or payout details are only merged after the owner confirms them against the live site.

## Requirements for an acceptable contribution

- `python3 tools/validate_catalog.py` prints `Catalog OK.`
- `python3 -W error -m unittest discover -s tests -v` passes with no warnings.
- `python3 -m pyflakes tools tests` reports nothing (install with `pip install pyflakes`).
- JSON files stay valid against the schemas in `schemas/`.
- Every URL uses `https://`.
- The only payout address anywhere is `0x659db9537fee7a3473ff6e2a5a661af65ae288e3` on Base. Pull requests that add or change a payout address will be rejected.
- No secrets: never commit passwords, API keys, tokens, private keys, seed phrases, or customer data.
- No made-up claims: do not add certifications, ratings, statistics, or customer results that are not real and sourced. Scanner grades must link to their source or to [TEST-RESULTS.md](TEST-RESULTS.md).
- Python code uses only the standard library, follows PEP 8 style, and keeps functions small and readable.
- Use English for text, comments, and commit messages.

## Tests (policy)

When you add new functionality to the validator, or a new rule the catalog must follow, add tests for it in `tests/` in the same pull request. A pull request that adds a check without a test that exercises it will not be merged. Bug fixes should include a test that fails without the fix.

Run the full test suite:

```
python3 -W error -m unittest discover -s tests -v
```

Optional coverage report (install with `pip install coverage`):

```
python3 -m coverage run --branch -m unittest discover -s tests
python3 -m coverage report --include='tools/*'
```

There is nothing to build. The catalog files are plain JSON, YAML, Markdown, and text, and the validator runs directly with Python 3.9 or newer.

## Versions and releases

The catalog uses [Semantic Versioning](https://semver.org/). Each release gets a git tag such as `v0.1.0` and an entry in [CHANGELOG.md](CHANGELOG.md) that says what changed in plain words. Changes to prices or services bump the minor version; fixes to wording or the validator bump the patch version.

## Licensing of contributions

By contributing you agree your contribution is provided under the license(s) in [LICENSE](LICENSE).
