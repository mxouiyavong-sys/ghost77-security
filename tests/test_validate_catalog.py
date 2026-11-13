# SPDX-License-Identifier: MIT
"""Tests for tools/validate_catalog.py. Run: python3 -m unittest discover -s tests -v"""

import copy
import io
import json
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import validate_catalog as vc  # noqa: E402

WALLET = vc.PAYOUT_WALLET
OTHER = "0x" + "1" * 40


class RealRepoTest(unittest.TestCase):
    def test_repository_catalog_is_valid(self):
        self.assertEqual(vc.validate_repo(ROOT), [])

    def test_main_returns_zero_on_repo(self):
        with redirect_stdout(io.StringIO()) as out:
            self.assertEqual(vc.main([str(ROOT)]), 0)
        self.assertIn("Catalog OK", out.getvalue())


class SchemaTest(unittest.TestCase):
    def test_type_mismatch(self):
        self.assertTrue(vc.check_schema("x", {"type": "object"}))
        self.assertTrue(vc.check_schema(True, {"type": "number"}))
        self.assertTrue(vc.check_schema(1.5, {"type": "integer"}))
        self.assertEqual(vc.check_schema(None, {"type": "null"}), [])
        self.assertTrue(vc.check_schema(1, {"type": "weird"}))

    def test_required_and_additional(self):
        schema = {"type": "object", "required": ["a"], "additionalProperties": False,
                  "properties": {"a": {"type": "string"}}}
        self.assertEqual(vc.check_schema({"a": "ok"}, schema), [])
        errs = vc.check_schema({"b": 1}, schema)
        self.assertTrue(any("missing required key 'a'" in e for e in errs))
        self.assertTrue(any("unexpected key 'b'" in e for e in errs))

    def test_enum_pattern_and_uri(self):
        self.assertTrue(vc.check_schema("weekly", {"enum": ["monthly"]}))
        self.assertTrue(vc.check_schema("0x12", {"type": "string", "pattern": "^0x[a-f0-9]{40}$"}))
        self.assertTrue(vc.check_schema("http://a.example", {"type": "string", "format": "uri"}))
        self.assertEqual(vc.check_schema("https://a.example", {"type": "string", "format": "uri"}), [])

    def test_arrays(self):
        schema = {"type": "array", "minItems": 1, "items": {"type": "number"}}
        self.assertTrue(vc.check_schema([], schema))
        self.assertTrue(vc.check_schema(["x"], schema))
        self.assertEqual(vc.check_schema([1, 2.5], schema), [])


class SafetyTest(unittest.TestCase):
    def test_http_url_rejected(self):
        self.assertTrue(vc.check_safety({"u": "http://example.com"}))

    def test_wallet_rules(self):
        self.assertEqual(vc.check_safety({"payout_wallet": WALLET}), [])
        self.assertEqual(vc.check_safety({"payout_wallet": WALLET.upper().replace("0X", "0x")}), [])
        self.assertEqual(vc.check_safety({"note": "USDC 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"}), [])
        errs = vc.check_safety({"x": [{"pay_to": OTHER}]})
        self.assertTrue(any("unexpected wallet" in e for e in errs))
        self.assertTrue(any("payout must go to" in e for e in errs))

    def test_non_strings_ignored(self):
        self.assertEqual(vc.check_safety({"n": 3, "b": True, "z": None}), [])


class ItemsTest(unittest.TestCase):
    def test_duplicates_and_negative_price(self):
        items = [{"id": "a", "price": 1}, {"id": "a", "price": -5}, "junk"]
        errs = vc.check_items(items, "items")
        self.assertTrue(any("duplicate id" in e for e in errs))
        self.assertTrue(any("negative price" in e for e in errs))

    def test_price_agreement(self):
        pricing = {"items": [{"id": "a", "price": 99}, "junk"]}
        self.assertEqual(vc.check_price_agreement(pricing, {"services": [{"id": "a", "price": 99}, "junk"]}), [])
        self.assertTrue(vc.check_price_agreement(pricing, {"services": [{"id": "a", "price": 98}]}))


class BrokenRepoTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        for name in ["pricing.json", "services.json", "schemas", ".well-known"]:
            src = ROOT / name
            if src.is_dir():
                shutil.copytree(src, self.tmp / name)
            else:
                shutil.copy(src, self.tmp / name)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def _edit(self, name, fn):
        path = self.tmp / name
        data = json.loads(path.read_text(encoding="utf-8"))
        fn(data)
        path.write_text(json.dumps(data), encoding="utf-8")

    def test_wrong_wallet_detected(self):
        self._edit("pricing.json", lambda d: d.__setitem__("payout_wallet", OTHER))
        self.assertTrue(any("payout must go to" in e for e in vc.validate_repo(self.tmp)))

    def test_price_mismatch_detected(self):
        def bump(d):
            d["items"][0]["price"] = d["items"][0]["price"] + 1
        self._edit("pricing.json", bump)
        self.assertTrue(any("price mismatch" in e for e in vc.validate_repo(self.tmp)))

    def test_missing_and_invalid_files(self):
        (self.tmp / "services.json").unlink()
        (self.tmp / ".well-known" / "agent.json").write_text("{not json", encoding="utf-8")
        errs = vc.validate_repo(self.tmp)
        self.assertTrue(any("services.json: cannot load" in e for e in errs))
        self.assertTrue(any("agent.json: invalid JSON" in e for e in errs))

    def test_main_reports_failure(self):
        self._edit("services.json", lambda d: d.pop("services"))
        with redirect_stdout(io.StringIO()) as out:
            self.assertEqual(vc.main([str(self.tmp)]), 1)
        self.assertIn("problem(s) found", out.getvalue())

    def test_copy_is_independent(self):
        data = vc.load_json(self.tmp / "pricing.json")
        self.assertEqual(copy.deepcopy(data), data)


if __name__ == "__main__":
    unittest.main()
