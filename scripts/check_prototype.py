#!/usr/bin/env python3
"""Fast static checks for the Beacon verification fixture."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "examples/beacon/prototype/index.html"
CSS = ROOT / "examples/beacon/prototype/styles.css"
JS = ROOT / "examples/beacon/prototype/app.js"


class Inspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.elements: list[str] = []
        self.live_regions = 0
        self.buttons = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        self.elements.append(tag)
        if values.get("id"):
            self.ids.append(str(values["id"]))
        if values.get("aria-live"):
            self.live_regions += 1
        if tag == "button":
            self.buttons += 1


def main() -> int:
    inspector = Inspector()
    inspector.feed(HTML.read_text(encoding="utf-8"))
    css = CSS.read_text(encoding="utf-8")
    js = JS.read_text(encoding="utf-8")
    required_elements = {"header", "main", "section", "aside", "button", "label"}
    missing = required_elements - set(inspector.elements)
    checks = {
        "required semantic elements": not missing,
        "unique IDs": len(inspector.ids) == len(set(inspector.ids)),
        "live status region": inspector.live_regions >= 1,
        "interactive controls": inspector.buttons >= 4,
        "visible focus style": ":focus-visible" in css,
        "reduced motion": "prefers-reduced-motion" in css,
        "narrow layout": "max-width: 760px" in css,
        "acknowledgement feedback": "status-message" in js and "Acknowledged" in js,
    }
    failed = [name for name, passed in checks.items() if not passed]
    for name, passed in checks.items():
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
