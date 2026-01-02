#!/usr/bin/env python3
"""
Check relative Markdown links exist on disk.

Skips fenced code blocks and inline code spans to avoid false positives from examples.

Usage:
  ./check_md_links.py <root>
  ./check_md_links.py <root> --ignore "node_modules" --ignore ".git"
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def strip_inline_code(line: str) -> str:
    out: list[str] = []
    in_code = False
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == "`":
            in_code = not in_code
            i += 1
            continue
        if not in_code:
            out.append(ch)
        i += 1
    return "".join(out)


def is_external_link(target: str) -> bool:
    lowered = target.lower()
    return (
        lowered.startswith("http://")
        or lowered.startswith("https://")
        or lowered.startswith("mailto:")
        or lowered.startswith("tel:")
    )


def normalize_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]
    return unquote(target)


def split_anchor(target: str) -> tuple[str, str | None]:
    if "#" in target:
        path_part, anchor = target.split("#", 1)
        return path_part, anchor or None
    return target, None


def check_file(md_path: Path) -> list[str]:
    errors: list[str] = []
    text = md_path.read_text(encoding="utf-8", errors="replace")

    in_fence = False
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(raw_line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        line = strip_inline_code(raw_line)
        for match in LINK_RE.finditer(line):
            raw_target = match.group(1)
            target = normalize_target(raw_target)
            if not target or target == "#":
                continue
            if is_external_link(target):
                continue
            if target.startswith("#"):
                continue

            path_part, _anchor = split_anchor(target)
            if not path_part or path_part in (".", "./"):
                continue
            if path_part.startswith("/"):
                errors.append(f"{md_path}:{line_number}: absolute link not allowed: {raw_target}")
                continue

            candidate = (md_path.parent / path_part).resolve()
            if not candidate.exists():
                errors.append(f"{md_path}:{line_number}: missing target: {raw_target}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check relative Markdown links exist.")
    parser.add_argument("root", type=Path, help="Root directory to scan")
    parser.add_argument("--ignore", action="append", default=[], help="Path component to ignore (repeatable)")
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.exists() or not root.is_dir():
        print(f"[ERROR] Root directory not found: {root}", file=sys.stderr)
        return 2

    ignore_set = set(args.ignore)
    md_files = []
    for path in root.rglob("*.md"):
        if not path.is_file():
            continue
        rel_parts = set(path.relative_to(root).parts)
        if rel_parts & ignore_set:
            continue
        md_files.append(path)

    all_errors: list[str] = []
    for md_file in md_files:
        all_errors.extend(check_file(md_file))

    if all_errors:
        print("\n".join(all_errors), file=sys.stderr)
        print(f"\n[FAIL] {len(all_errors)} broken link(s)", file=sys.stderr)
        return 1

    print(f"[OK] {len(md_files)} Markdown file(s) scanned, no broken relative links found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

