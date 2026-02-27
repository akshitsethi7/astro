#!/usr/bin/env python3
"""
KP Sub-Lord Analysis (Krishnamurti Paddhati)

KP uses cuspal sub-lords and planet sub-lords for timing.
Full implementation requires Swiss Ephemeris for precise cusps and sub-divisions.
This script provides structure and references for marriage validation.

Usage:
    python 06-ANALYSIS-SCRIPTS/kp_sub_lord_analysis.py
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VARGAS_PATH = REPO_ROOT / "11-CONFIG-DATA" / "vargas_output.json"


def main() -> None:
    with VARGAS_PATH.open("r") as f:
        data = json.load(f)
    asc = data.get("ascendant", {}).get("sign", "Leo")
    # House from vargas.D1.planets (planets_d1 has no house)
    d1_planets = {p["name"]: p for p in data.get("vargas", {}).get("D1", {}).get("planets", []) if p["name"] != "Ascendant"}
    planets_d1 = data.get("planets_d1", {})

    lines = [
        "# KP Sub-Lord Analysis (Structure)",
        "",
        f"**Ascendant**: {asc}",
        "",
        "## Marriage Significators (KP)",
        "",
        "- **7th cusp sub-lord**: Determines marriage timing (requires precise cusp calculation)",
        "- **7th house significators**: Planets in 7th, aspecting 7th, 7th lord",
        "- **Venus sub-lord**: Marriage karaka",
        "- **Saturn sub-lord**: 7th lord for Leo ascendant",
        "",
        "## Chart Positions (for manual KP analysis)",
        "",
        "| Planet | Sign | House | Nakshatra |",
        "|--------|------|-------|-----------|",
    ]
    for name in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        p_d1 = planets_d1.get(name, {})
        p_vargas = d1_planets.get(name, {})
        house = p_vargas.get("house", "")
        lines.append(f"| {name} | {p_d1.get('sign', '')} | {house} | {p_d1.get('nakshatra', '')} |")
    lines.extend([
        "",
        "## Next Steps",
        "",
        "- Use Swiss Ephemeris or similar for precise cuspal sub-lords",
        "- 249 divisions (Vimshottari × 9 nakshatra padas) for sub-lord",
        "- Marriage when 7th cusp sub-lord's dasha operates",
        "",
        "*Full KP requires KP software or detailed ephemeris integration.*",
    ])

    out = REPO_ROOT / "02-MARRIAGE-ANALYSIS" / "KP_SUB_LORD_ANALYSIS.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
