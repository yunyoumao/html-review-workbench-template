from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "sample-review.json"
TARGET = ROOT / "data" / "sample-review.js"

REQUIRED_ITEM_FIELDS = {"id", "title", "category", "severity", "status", "owner", "evidence", "next_step"}
VALID_SEVERITIES = {"High", "Medium", "Low"}
VALID_STATUSES = {"Open", "In Progress", "Done"}


def validate(data: dict) -> None:
    if not data.get("title"):
        raise ValueError("Missing review title.")
    items = data.get("items")
    if not isinstance(items, list) or not items:
        raise ValueError("Expected a non-empty items list.")
    seen_ids: set[str] = set()
    for item in items:
        missing = REQUIRED_ITEM_FIELDS - set(item)
        if missing:
            raise ValueError(f"{item.get('id', '<unknown>')} missing fields: {sorted(missing)}")
        if item["id"] in seen_ids:
            raise ValueError(f"Duplicate item id: {item['id']}")
        seen_ids.add(item["id"])
        if item["severity"] not in VALID_SEVERITIES:
            raise ValueError(f"{item['id']} has invalid severity: {item['severity']}")
        if item["status"] not in VALID_STATUSES:
            raise ValueError(f"{item['id']} has invalid status: {item['status']}")


def main() -> int:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    validate(data)
    TARGET.write_text(
        "window.REVIEW_WORKBENCH_DATA = "
        + json.dumps(data, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Wrote {TARGET.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
