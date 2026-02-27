#!/usr/bin/env python3
"""
Narayana Dasha Calculator (Jaimini)

Narayana Dasha starts from the stronger of Lagna or 7th house.
Duration = years from sign lord to the sign (zodiacal count).
Uses planet positions from vargas_output.json.

Usage:
    python 06-ANALYSIS-SCRIPTS/narayana_dasha.py
"""

import json
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
VARGAS_PATH = REPO_ROOT / "11-CONFIG-DATA" / "vargas_output.json"

SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
         "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

SIGN_LORDS: Dict[str, str] = {
    "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
    "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
    "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter",
}


@dataclass
class NarayanaPeriod:
    sign: str
    years: int
    start: date
    end: date


def zodiac_distance(from_sign: str, to_sign: str) -> int:
    """Count signs from from_sign to to_sign (zodiacal order)."""
    i = SIGNS.index(from_sign)
    j = SIGNS.index(to_sign)
    d = (j - i) % 12
    return d if d > 0 else 12


def main() -> None:
    with VARGAS_PATH.open("r") as f:
        data = json.load(f)
    asc = data.get("ascendant", {}).get("sign", "Leo")
    dt_str = data.get("birth", {}).get("datetime_local", "1994-12-26")
    y, m, d = map(int, dt_str.split("T")[0].split("-")[:3])
    birth = date(y, m, d)

    # Planet positions (sign)
    planets = data.get("planets_d1", {})
    lord_pos: Dict[str, str] = {}
    for pname, pdata in planets.items():
        if pname in SIGN_LORDS.values() or pname in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
            lord_pos[pname] = pdata.get("sign", "")

    def years_for_sign(sign: str) -> int:
        lord = SIGN_LORDS.get(sign, "")
        pos = lord_pos.get(lord, "")
        if not pos or pos not in SIGNS:
            return 5  # fallback
        dist = zodiac_distance(pos, sign)
        if dist == 0:
            return 1  # lord in own sign
        yrs = dist if dist <= 6 else 12 - dist
        return max(1, yrs)  # minimum 1 year

    # Start from Lagna (Leo)
    start_idx = SIGNS.index(asc) if asc in SIGNS else 4
    periods: List[NarayanaPeriod] = []
    cur = birth
    for i in range(24):
        idx = (start_idx + i) % 12
        sign = SIGNS[idx]
        yrs = years_for_sign(sign)
        end = cur + timedelta(days=int(yrs * 365.25))
        periods.append(NarayanaPeriod(sign, yrs, cur, end))
        cur = end

    as_of = date(2026, 2, 27)
    current = next((p for p in periods if p.start <= as_of < p.end), periods[-1])

    lines = [
        "# Narayana Dasha Timeline (Jaimini)",
        "",
        f"**Ascendant**: {asc}",
        f"**Current**: {current.sign} ({current.years} years) until {current.end}",
        "",
        "| Sign | Years | Start | End |",
        "|------|-------|-------|-----|",
    ]
    for p in periods[:16]:
        lines.append(f"| {p.sign} | {p.years} | {p.start} | {p.end} |")
    lines.append("")
    lines.append("## Marriage (7th house = Aquarius)")
    for p in periods:
        if p.sign == "Aquarius":
            lines.append(f"- **Aquarius**: {p.start} – {p.end}")

    out = REPO_ROOT / "04-DASHA-ANALYSIS" / "NARAYANA_DASHA_TIMELINE.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
