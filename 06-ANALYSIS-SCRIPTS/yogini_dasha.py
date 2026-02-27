#!/usr/bin/env python3
"""Yogini Dasha Calculator - 36-year cycle from Moon nakshatra."""

import argparse
import json
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
VARGAS_PATH = REPO_ROOT / "11-CONFIG-DATA" / "vargas_output.json"

NAKSHATRA_ORDER = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu",
    "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta",
    "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
    "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha", "Purva Bhadrapada",
    "Uttara Bhadrapada", "Revati",
]

YOGINI_SEQUENCE = [
    ("Mangala", 1, "Moon"), ("Pingala", 2, "Sun"), ("Dhanya", 3, "Jupiter"),
    ("Bhramari", 4, "Mars"), ("Bhadrika", 5, "Mercury"), ("Ulka", 6, "Saturn"),
    ("Siddha", 7, "Venus"), ("Sankata", 8, "Rahu"),
]


@dataclass
class YoginiPeriod:
    name: str
    years: int
    ruler: str
    start_date: date
    end_date: date


def nakshatra_to_number(nak: str) -> int:
    for i, name in enumerate(NAKSHATRA_ORDER, 1):
        if name.lower() == nak.strip().lower():
            return i
    raise ValueError(f"Unknown nakshatra: {nak}")


def get_birth_yogini_index(nak_num: int) -> int:
    r = (nak_num + 3) % 8
    return (r - 1) % 8 if r else 7


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chart", default=None)
    parser.add_argument("--output", default="04-DASHA-ANALYSIS/YOGINI_DASHA_TIMELINE.md")
    args = parser.parse_args()

    path = Path(args.chart) if args.chart else VARGAS_PATH
    if not path.is_absolute():
        path = REPO_ROOT / path
    with path.open("r") as f:
        data = json.load(f)
    moon_nak = data.get("planets_d1", data.get("planets", {})).get("Moon", {}).get("nakshatra", "Hasta")
    dt_str = data.get("birth", {}).get("datetime_local", "1994-12-26")
    y, m, d = map(int, dt_str.split("T")[0].split("-")[:3])
    birth_date = date(y, m, d)

    nak_num = nakshatra_to_number(moon_nak)
    start_idx = get_birth_yogini_index(nak_num)

    periods: List[YoginiPeriod] = []
    cur = birth_date
    for i in range(32):
        idx = (start_idx + i) % 8
        name, years, ruler = YOGINI_SEQUENCE[idx]
        end = cur + timedelta(days=int(years * 365.25))
        periods.append(YoginiPeriod(name, years, ruler, cur, end))
        cur = end

    as_of = date(2026, 2, 27)
    current = next((p for p in periods if p.start_date <= as_of < p.end_date), periods[-1])

    lines = [
        "# Yogini Dasha Timeline",
        "",
        f"**Birth Moon Nakshatra**: {moon_nak}",
        f"**Current Yogini**: {current.name} ({current.ruler})",
        "",
        "| Yogini | Ruler | Years | Start | End |",
        "|--------|-------|-------|-------|-----|",
    ]
    for p in periods[:16]:
        lines.append(f"| {p.name} | {p.ruler} | {p.years} | {p.start_date} | {p.end_date} |")
    lines.append("")
    lines.append("## Marriage-Relevant (Venus/Jupiter)")
    for p in periods:
        if p.ruler in ("Venus", "Jupiter") and 2020 <= p.start_date.year <= 2040:
            lines.append(f"- **{p.name}** ({p.ruler}): {p.start_date} – {p.end_date}")

    out = REPO_ROOT / args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
