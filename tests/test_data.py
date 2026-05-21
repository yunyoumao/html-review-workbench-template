from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts.build_data_js import VALID_SEVERITIES, VALID_STATUSES, validate


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample-review.json"


class ReviewDataTests(unittest.TestCase):
    def test_sample_data_is_valid(self) -> None:
        data = json.loads(DATA.read_text(encoding="utf-8"))
        validate(data)
        self.assertGreaterEqual(len(data["items"]), 6)

    def test_values_are_supported(self) -> None:
        data = json.loads(DATA.read_text(encoding="utf-8"))
        severities = {item["severity"] for item in data["items"]}
        statuses = {item["status"] for item in data["items"]}
        self.assertLessEqual(severities, VALID_SEVERITIES)
        self.assertLessEqual(statuses, VALID_STATUSES)

    def test_item_ids_are_unique(self) -> None:
        data = json.loads(DATA.read_text(encoding="utf-8"))
        ids = [item["id"] for item in data["items"]]
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()
