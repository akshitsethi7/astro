#!/usr/bin/env python3
"""Nakshatra Deep Analysis - planet nakshatras for personality/spouse traits."""

import json
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
VARGAS_PATH = REPO_ROOT / "11-CONFIG-DATA" / "vargas_output.json"

NAK_SIG = {
    "Magha": ("Ketu", "Royal, proud, ancestral"),
    "Hasta": ("Moon", "Skillful, crafty, healing"),
    "Swati": ("Rahu", "Independent, trade-oriented"),
    "Vishakha": ("Jupiter", "Determined, transformative"),
    "Anuradha": ("Saturn", "Loyal, friendship"),
    "Shatabhisha": ("Rahu", "Healing, mystical, innovative"),
    "Bharani": ("Venus", "Creative, transformative"),
    "Mula": ("Ketu", "Root-seeking, research"),
    "Purva Ashadha": ("Venus", "Invincible, ambitious"),
}


def main() -> None:
    with VARGAS_PATH.open("r") as f:
        data = json.load(f)
    planets = data.get("planets_d1", data.get("planets", {}))
    lines = ["# Nakshatra Deep Analysis", ""]
    for name in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Rahu", "Ketu"]:
        if name not in planets:
            continue
        p = planets[name]
        nak = p.get("nakshatra", "")
        lord, traits = NAK_SIG.get(nak, ("?", "—"))
        lines.append(f"### {name} in {nak} ({lord})")
        lines.append(f"- House {p.get('house', '?')} | {traits}")
        lines.append("")
    lines.extend([
        "## Marriage-Relevant",
        "- **Venus in Vishakha**: Jupiter-ruled — wisdom in partnership",
        "- **Saturn in Shatabhisha**: Rahu-ruled — spouse unconventional, healing",
        "- **Mars (DK) in Magha**: Ketu-ruled — spouse royal bearing",
    ])
    out = REPO_ROOT / "01-AKSHIT-ANALYSIS" / "NAKSHATRA_DEEP_ANALYSIS.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
