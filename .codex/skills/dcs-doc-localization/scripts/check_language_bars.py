#!/usr/bin/env python3
"""
Validate the standard EN/ES/SV/FI language bar for Markdown doc sets.

It checks that:
- A language bar exists when multiple sibling language files exist.
- The current language label is bold and not a link.
- Other existing language files are linked.
- Links are relative (no http/https, no absolute / paths).

Usage:
  ./check_language_bars.py <root>
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


LANGS = {
    "en": {"flag": "🇬🇧", "label": "English"},
    "es": {"flag": "🇪🇸", "label": "Español"},
    "sv": {"flag": "🇸🇪", "label": "Svenska"},
    "fi": {"flag": "🇫🇮", "label": "Suomi"},
}

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def detect_lang(filename: str) -> str:
    for code in ("en", "es", "sv", "fi"):
        if filename.endswith(f".{code}.md"):
            return code
    if filename.endswith(".md"):
        return "en"
    return "en"


def base_name(filename: str) -> str:
    for code in ("en", "es", "sv", "fi"):
        suffix = f".{code}.md"
        if filename.endswith(suffix):
            return filename[: -len(suffix)]
    if filename.endswith(".md"):
        return filename[: -len(".md")]
    return filename


def expected_sibling(dir_path: Path, base: str, lang: str) -> Path:
    if lang == "en":
        return dir_path / f"{base}.md"
    return dir_path / f"{base}.{lang}.md"


def is_relative(target: str) -> bool:
    lowered = target.lower().strip()
    if lowered.startswith(("http://", "https://", "mailto:")):
        return False
    if lowered.startswith("/"):
        return False
    return True


def find_language_bar(lines: list[str]) -> tuple[int, str] | None:
    # Search only near top.
    for i, line in enumerate(lines[:25]):
        if all(LANGS[code]["flag"] in line for code in ("en", "es", "sv", "fi")):
            return i, line.strip()
    return None


@dataclass(frozen=True)
class BarInfo:
    line_number: int
    text: str
    link_targets: set[str]


def parse_bar(line_number: int, line: str) -> BarInfo:
    targets = set(LINK_RE.findall(line))
    return BarInfo(line_number=line_number + 1, text=line, link_targets=targets)


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    lang = detect_lang(path.name)
    base = base_name(path.name)
    siblings = {code: expected_sibling(path.parent, base, code) for code in LANGS.keys()}
    existing = {code for code, p in siblings.items() if p.exists()}

    # Only require a bar if at least 2 languages exist in the set.
    if len(existing) < 2:
        return errors

    found = find_language_bar(lines)
    if not found:
        errors.append(f"{path}: missing language bar (expected EN/ES/SV/FI line near top)")
        return errors

    bar = parse_bar(*found)

    # Validate link relativity.
    for target in bar.link_targets:
        if not is_relative(target):
            errors.append(f"{path}:{bar.line_number}: non-relative language bar link: {target}")

    # Current language must be bold label, not a link target.
    current_label = LANGS[lang]["label"]
    if f"**{current_label}**" not in bar.text:
        errors.append(f"{path}:{bar.line_number}: current language not bold: expected **{current_label}**")

    current_expected = siblings[lang].name
    if current_expected in bar.link_targets:
        errors.append(f"{path}:{bar.line_number}: current language should not link to itself: {current_expected}")

    # All other existing language siblings should be linked.
    for code in sorted(existing):
        if code == lang:
            continue
        expected_name = siblings[code].name
        if expected_name not in bar.link_targets:
            errors.append(f"{path}:{bar.line_number}: missing bar link for {code}: {expected_name}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate EN/ES/SV/FI language bars.")
    parser.add_argument("root", type=Path)
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.exists() or not root.is_dir():
        print(f"[ERROR] Root directory not found: {root}", file=sys.stderr)
        return 2

    md_files = [p for p in root.rglob("*.md") if p.is_file()]
    all_errors: list[str] = []
    for md_file in md_files:
        all_errors.extend(check_file(md_file))

    if all_errors:
        print("\n".join(all_errors), file=sys.stderr)
        print(f"\n[FAIL] {len(all_errors)} issue(s)", file=sys.stderr)
        return 1

    print(f"[OK] {len(md_files)} Markdown file(s) scanned, language bars look consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

