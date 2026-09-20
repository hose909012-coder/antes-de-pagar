#!/usr/bin/env python3
"""Validate the repository's portable plugin, compatibility manifest, and skill."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME = "antes-de-pagar"


def load_json(relative: str) -> dict:
    path = ROOT / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AssertionError(f"Invalid {relative}: {exc}") from exc


def main() -> int:
    portable = load_json("plugin.json")
    compatibility = load_json(".codex-plugin/plugin.json")
    marketplace = load_json(".agents/plugins/marketplace.json")

    assert portable.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    assert portable.get("name") == compatibility.get("name") == NAME
    assert portable.get("version") == compatibility.get("version")
    assert re.fullmatch(r"\d+\.\d+\.\d+", portable["version"])
    assert marketplace.get("name") == NAME
    assert marketplace["plugins"][0]["name"] == NAME
    assert marketplace["plugins"][0]["policy"] == {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL",
    }

    skill = (ROOT / "skills" / NAME / "SKILL.md").read_text(encoding="utf-8")
    assert skill.startswith("---\n")
    assert re.search(r"^name: antes-de-pagar$", skill, re.MULTILINE)
    assert re.search(r"^description: .+", skill, re.MULTILINE)

    required = [
        "README.md",
        "PRIVACY.md",
        "TERMS.md",
        "SECURITY.md",
        "CONTRIBUTING.md",
        "LICENSE",
        "tests/cases.md",
    ]
    for relative in required:
        assert (ROOT / relative).is_file(), f"Missing {relative}"

    placeholder = "[" + "TODO:"
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".json", ".yaml", ".py"}:
            assert placeholder not in path.read_text(encoding="utf-8"), f"Placeholder in {path}"

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
