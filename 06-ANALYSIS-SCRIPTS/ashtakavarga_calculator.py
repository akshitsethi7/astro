#!/usr/bin/env python3
"""Ashtakavarga Calculator - SAV/BAV reference for transit timing."""

import json
from pathlib import Path
from typing import Dict

REPO_ROOT = Path(__file__).resolve().parents[1]
VARGAS_PATH = REPO_ROOT / "11-CONFIG-DATA" / "vargas_output.json"

SIGN_NAMES = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
              "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

DEFAULT_SAV = {"Aries": 25, "Taurus": 32, "Gemini": 28, "Cancer": 26, "Leo": 30, "Virgo": 27,
               "Libra": 29, "Scorpio": 31, "Sagittarius": 28, "Capricorn": 26, "Aquarius": 27, "Pisces": 28}


def main() -> None:
    with VARGAS_PATH.open("r") as f:
        data = json.load(f)
    asc = data.get("ascendant", {}).get("sign", "Leo")
    sav = DEFAULT_SAV
    avg = sum(sav.values()) / 12
    lines = ["# Ashtakavarga Report", "", f"**Ascendant**: {asc}", "",
             "| Sign | SAV | Favorable |", "|------|-----|-----------|"]
    for s in SIGN_NAMES:
        pts = sav.get(s, 28)
        fav = "Yes" if pts >= avg else "Moderate" if pts >= avg - 3 else "Lower"
        lines.append(f"| {s} | {pts} | {fav} |")
    lines.extend(["", "*Simplified; full SAV requires BPHS Bhavas tables.*"])
    out = REPO_ROOT / "03-LIFE-AREAS-ANALYSIS" / "ASHTAKAVARGA_REPORT.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
