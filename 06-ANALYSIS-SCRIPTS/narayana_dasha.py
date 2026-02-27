#!/usr/bin/env python3
"""
Narayana Dasha Calculator (Jaimini)

Narayana Dasha starts from the stronger of Lagna or 7th house.
Each sign's period = years based on lord-to-sign count (simplified).
For Leo ascendant: Lagna=Leo, 7th=Aquarius. Both fixed; use Lagna as default.

Usage:
    python 06-ANALYSIS-SCRIPTS/narayana_dasha.py
"""

import json
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parents[1]
VARGAS_PATH = REPO_ROOT / "11-CONFIG-DATA" / "vargas_output.json"

SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
         "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

# Simplified: years per sign (lord-to-sign count). Leo=5, Virgo=5, etc.
# Full calculation requires BPHS rules.
DEFAULT_YEARS = {s: 5 for s in SIGNS}
DEFAULT_YEARS["Leo"] = 6
DEFAULT_YEARS["Aquarius"] = 6


@dataclass
class NarayanaPeriod:
    sign: str
    years: int
    start: date
    end: date


def main() -> None:
    with VARGAS_PATH.open("r") as f:
        data = json.load(f)
    asc = data.get("ascendant", {}).get("sign", "Leo")
    dt_str = data.get("birth", {}).get("datetime_local", "1994-12-26")
    y, m, d = map(int, dt_str.split("T")[0].split("-")[:3])
    birth = date(y, m, d)

    # Start from Lagna (Leo)
    start_idx = SIGNS.index(asc) if asc in SIGNS else 4
    periods: List[NarayanaPeriod] = []
    cur = birth
    for i in range(24):
        idx = (start_idx + i) % 12
        sign = SIGNS[idx]
        yrs = DEFAULT_YEARS.get(sign, 5)
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
        if p.sign == "Aquarius" and 2020 <= p.start.year <= 2040:
            lines.append(f"- **Aquarius**: {p.start} – {p.end}")

    out = REPO_ROOT / "04-DASHA-ANALYSIS" / "NARAYANA_DASHA_TIMELINE.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
