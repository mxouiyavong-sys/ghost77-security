#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the GhOsT77 Security public catalog files.

Checks pricing.json and services.json against the JSON Schemas in schemas/
(a small, dependency-free subset of JSON Schema), and applies safety rules:

* every URL is HTTPS,
* every 0x wallet address used for payouts is the one published payout wallet,
* item ids are unique, prices are not negative,
* prices for the same id agree between pricing.json and services.json.

Usage:
    python3 tools/validate_catalog.py [REPO_ROOT]

Exit status is 0 when everything passes, 1 when any problem is found.
Only the Python 3 standard library is used. Nothing is fetched over the network.
"""

import json
import re
import sys
from pathlib import Path

PAYOUT_WALLET = "0x659db9537fee7a3473ff6e2a5a661af65ae288e3"
# Token contract addresses that may legitimately appear (not payout targets).
KNOWN_TOKEN_CONTRACTS = {
    "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",  # USDC on Base
}
WALLET_KEYS = {"payout_wallet", "pay_to", "payTo", "payto", "wallet"}

_TYPES = {
    "object": dict,
    "array": list,
    "string": str,
    "boolean": bool,
}


def _type_ok(value, expected):
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "null":
        return value is None
    py = _TYPES.get(expected)
    return py is not None and isinstance(value, py)


def check_schema(value, schema, path="$"):
    """Return a list of error strings for VALUE against a JSON Schema subset.

    Supported keywords: type, required, properties, additionalProperties
    (boolean), items, minItems, enum, pattern, format=uri (https only).
    """
    errors = []
    expected = schema.get("type")
    if expected is not None and not _type_ok(value, expected):
        return [f"{path}: expected {expected}, got {type(value).__name__}"]

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} not one of {schema['enum']}")

    if isinstance(value, str):
        pattern = schema.get("pattern")
        if pattern and not re.search(pattern, value):
            errors.append(f"{path}: {value!r} does not match {pattern}")
        if schema.get("format") == "uri" and not value.startswith("https://"):
            errors.append(f"{path}: URL must start with https:// ({value!r})")

    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing required key {key!r}")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    errors.append(f"{path}: unexpected key {key!r}")
        for key, sub in props.items():
            if key in value:
                errors.extend(check_schema(value[key], sub, f"{path}.{key}"))

    if isinstance(value, list):
        min_items = schema.get("minItems")
        if min_items is not None and len(value) < min_items:
            errors.append(f"{path}: needs at least {min_items} item(s)")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for i, item in enumerate(value):
                errors.extend(check_schema(item, item_schema, f"{path}[{i}]"))
    return errors


def _walk(value, path="$"):
    """Yield (path, key, value) for every scalar in a JSON document."""
    if isinstance(value, dict):
        for key, sub in value.items():
            if isinstance(sub, (dict, list)):
                yield from _walk(sub, f"{path}.{key}")
            else:
                yield f"{path}.{key}", key, sub
    elif isinstance(value, list):
        for i, sub in enumerate(value):
            yield from _walk(sub, f"{path}[{i}]")


def check_safety(doc):
    """Return errors for non-HTTPS URLs and unexpected wallet addresses."""
    errors = []
    for path, key, value in _walk(doc):
        if not isinstance(value, str):
            continue
        if value.startswith("http://"):
            errors.append(f"{path}: insecure http:// URL ({value})")
        for addr in re.findall(r"0x[0-9a-fA-F]{40}", value):
            low = addr.lower()
            if low == PAYOUT_WALLET or low in KNOWN_TOKEN_CONTRACTS:
                continue
            errors.append(f"{path}: unexpected wallet address {addr}")
        if key in WALLET_KEYS and re.fullmatch(r"0x[0-9a-fA-F]{40}", value):
            if value.lower() != PAYOUT_WALLET:
                errors.append(f"{path}: payout must go to {PAYOUT_WALLET}")
    return errors


def check_items(items, label):
    """Return errors for duplicate ids or negative prices in a list of items."""
    errors = []
    seen = set()
    for i, item in enumerate(items):
        if not isinstance(item, dict):
            continue
        item_id = item.get("id")
        if item_id in seen:
            errors.append(f"{label}[{i}]: duplicate id {item_id!r}")
        seen.add(item_id)
        price = item.get("price")
        if isinstance(price, (int, float)) and not isinstance(price, bool) and price < 0:
            errors.append(f"{label}[{i}]: negative price {price}")
    return errors


def check_price_agreement(pricing, services):
    """Return errors where the same id has different prices in the two files."""
    errors = []
    prices = {i.get("id"): i.get("price") for i in pricing.get("items", []) if isinstance(i, dict)}
    for svc in services.get("services", []):
        if not isinstance(svc, dict):
            continue
        sid = svc.get("id")
        if sid in prices and prices[sid] != svc.get("price"):
            errors.append(
                f"price mismatch for {sid!r}: pricing.json={prices[sid]} services.json={svc.get('price')}"
            )
    return errors


def load_json(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def validate_repo(root):
    """Validate the catalog files under ROOT. Return a list of error strings."""
    root = Path(root)
    errors = []
    docs = {}
    pairs = [
        ("pricing.json", "schemas/pricing.schema.json"),
        ("services.json", "schemas/services.schema.json"),
    ]
    for data_name, schema_name in pairs:
        try:
            data = load_json(root / data_name)
            schema = load_json(root / schema_name)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{data_name}: cannot load ({exc})")
            continue
        docs[data_name] = data
        errors.extend(f"{data_name} {e}" for e in check_schema(data, schema))
        errors.extend(f"{data_name} {e}" for e in check_safety(data))
    agent_path = root / ".well-known" / "agent.json"
    if agent_path.exists():
        try:
            errors.extend(f"agent.json {e}" for e in check_safety(load_json(agent_path)))
        except json.JSONDecodeError as exc:
            errors.append(f"agent.json: invalid JSON ({exc})")
    if "pricing.json" in docs:
        errors.extend(check_items(docs["pricing.json"].get("items", []), "pricing.json items"))
    if "services.json" in docs:
        errors.extend(check_items(docs["services.json"].get("services", []), "services.json services"))
    if "pricing.json" in docs and "services.json" in docs:
        errors.extend(check_price_agreement(docs["pricing.json"], docs["services.json"]))
    return errors


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    root = Path(argv[0]) if argv else Path(__file__).resolve().parent.parent
    errors = validate_repo(root)
    for err in errors:
        print(f"ERROR: {err}")
    if errors:
        print(f"{len(errors)} problem(s) found.")
        return 1
    print("Catalog OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
