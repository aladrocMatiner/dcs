#!/usr/bin/env python3
"""
Check Markdown heading structure against required patterns.

Usage:
  ./check_doc_structure.py <root> --preset quick-takeoff
  ./check_doc_structure.py <root> --require-regex "Step-by-step" --require-regex "Common mistakes"
  ./check_doc_structure.py <root> --match "quick_takeoff\\..*\\.md$" --preset quick-takeoff
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


PRESETS: dict[str, list[str]] = {
    "quick-takeoff": [
        r"step[- ]by[- ]step|secuencia paso a paso|steg[- ]för[- ]steg|vaiheittain",
        r"keyboard|atajos|tangentbord|näppäimistö|bind",
        r"common mistakes|errores comunes|misstag|virheet",
        r"practice|práctica|övning|harjoitus",
    ]
}


def load_headings(text: str) -> list[str]:
    headings: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        headings.append(m.group(2).strip())
    return headings


def check_file(path: Path, required: list[re.Pattern[str]]) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    headings = load_headings(text)

    for pattern in required:
        if not any(pattern.search(h) for h in headings):
            errors.append(f"{path}: missing required heading matching /{pattern.pattern}/i")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Markdown heading structure.")
    parser.add_argument("root", type=Path)
    parser.add_argument("--preset", choices=sorted(PRESETS.keys()))
    parser.add_argument("--require-regex", action="append", default=[], help="Regex (repeatable), case-insensitive")
    parser.add_argument("--match", default=None, help="Only check files whose relative path matches this regex")
    parser.add_argument("--ignore", action="append", default=[], help="Path component to ignore (repeatable)")
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.exists() or not root.is_dir():
        print(f"[ERROR] Root directory not found: {root}", file=sys.stderr)
        return 2

    required_patterns: list[str] = []
    if args.preset:
        required_patterns.extend(PRESETS[args.preset])
    required_patterns.extend(args.require_regex)
    if not required_patterns:
        print("[ERROR] No requirements provided; use --preset or --require-regex", file=sys.stderr)
        return 2

    required = [re.compile(p, re.IGNORECASE) for p in required_patterns]
    match_re = re.compile(args.match) if args.match else None

    ignore_set = set(args.ignore)
    md_files: list[Path] = []
    for path in root.rglob("*.md"):
        if not path.is_file():
            continue
        rel = str(path.relative_to(root))
        if match_re and not match_re.search(rel):
            continue
        rel_parts = set(Path(rel).parts)
        if rel_parts & ignore_set:
            continue
        md_files.append(path)

    all_errors: list[str] = []
    for md_file in md_files:
        all_errors.extend(check_file(md_file, required))

    if all_errors:
        print("\n".join(all_errors), file=sys.stderr)
        print(f"\n[FAIL] {len(all_errors)} issue(s)", file=sys.stderr)
        return 1

    print(f"[OK] {len(md_files)} Markdown file(s) checked, headings match requirements")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

