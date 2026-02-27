#!/usr/bin/env python3
"""
Vimshottari Dasha Calculator - outputs JSON for UI consumption.
Uses Moon nakshatra from vargas_output.json.
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VARGAS_PATH = REPO_ROOT / "11-CONFIG-DATA" / "vargas_output.json"

# Nakshatra order (27), each 13°20'
NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu",
    "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta",
    "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
    "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha", "Purva Bhadrapada",
    "Uttara Bhadrapada", "Revati",
]

# Vimshottari: planet order at birth, years each
PLANET_ORDER = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]
PLANET_YEARS = {"Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10, "Mars": 7, "Rahu": 18, "Jupiter": 16, "Saturn": 19, "Mercury": 17}
TOTAL_YEARS = 120


def nakshatra_to_dasha_lord(nak: str) -> str:
    """First dasha lord from nakshatra (3 nakshatras per planet)."""
    idx = next((i for i, n in enumerate(NAKSHATRAS) if n.lower() == nak.strip().lower()), 12)
    return PLANET_ORDER[idx // 3]


def degrees_remaining_in_nakshatra(lon: float) -> float:
    """Degrees left in current nakshatra (each = 13.333...)."""
    deg_in_nak = lon % 13.333333333333334
    return 13.333333333333334 - deg_in_nak


def main() -> None:
    with VARGAS_PATH.open("r") as f:
        data = json.load(f)
    moon = data["planets_d1"]["Moon"]
    moon_lon = moon["lon"]
    moon_nak = moon["nakshatra"]
    dt_str = data["birth"]["datetime_local"]
    birth = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))

    first_lord = nakshatra_to_dasha_lord(moon_nak)
    years_elapsed_in_first = (degrees_remaining_in_nakshatra(moon_lon) / 13.333333333333334) * PLANET_YEARS[first_lord]
    balance_years = PLANET_YEARS[first_lord] - years_elapsed_in_first

    # Build mahadasha sequence starting from first_lord
    idx = PLANET_ORDER.index(first_lord)
    sequence = PLANET_ORDER[idx:] + PLANET_ORDER[:idx]

    # Start from birth, first dasha is balance of first_lord
    cur = birth
    dasha_periods = []
    for i, planet in enumerate(sequence):
        if i == 0:
            yrs = balance_years
        else:
            yrs = PLANET_YEARS[planet]
        end = cur + timedelta(days=int(yrs * 365.25))
        # Antardashas: same order, proportion of mahadasha
        antardashas = []
        acur = cur
        for j, ap in enumerate(PLANET_ORDER[PLANET_ORDER.index(planet):] + PLANET_ORDER[:PLANET_ORDER.index(planet)]):
            ayrs = yrs * PLANET_YEARS[ap] / TOTAL_YEARS
            aend = acur + timedelta(days=int(ayrs * 365.25))
            # Pratyantar: simplified, 9 per antar
            pratyantars = []
            pcur = acur
            for k, pp in enumerate(PLANET_ORDER[PLANET_ORDER.index(ap):] + PLANET_ORDER[:PLANET_ORDER.index(ap)]):
                pyrs = ayrs * PLANET_YEARS[pp] / TOTAL_YEARS
                pend = pcur + timedelta(days=int(pyrs * 365.25))
                pratyantars.append({
                    "name": pp, "start": pcur.strftime("%Y-%m-%dT%H:%M:%S+05:30"),
                    "end": pend.strftime("%Y-%m-%dT%H:%M:%S+05:30"), "id": k + 1
                })
                pcur = pend
                if len(pratyantars) >= 9:
                    break
            antardashas.append({
                "name": ap, "start": acur.strftime("%Y-%m-%dT%H:%M:%S+05:30"),
                "end": aend.strftime("%Y-%m-%dT%H:%M:%S+05:30"), "id": j + 1,
                "pratyantardasha": pratyantars
            })
            acur = aend
            if acur >= end:
                break
        dasha_periods.append({
            "name": planet, "start": cur.strftime("%Y-%m-%dT%H:%M:%S+05:30"),
            "end": end.strftime("%Y-%m-%dT%H:%M:%S+05:30"), "id": i + 1,
            "antardasha": antardashas
        })
        cur = end

    balance_days = int(balance_years * 365.25)
    months = balance_days // 30
    days = balance_days % 30
    out = {
        "data": {
            "dasha_balance": {
                "duration": f"P0Y{months}M{days}D",
                "lord": {"vedic_name": first_lord, "name": first_lord, "id": PLANET_ORDER.index(first_lord)},
                "description": f" {months} months {days} days"
            },
            "dasha_periods": dasha_periods
        }
    }

    ui_path = REPO_ROOT / "12-DEVELOPMENT" / "astro-marriage-ui" / "lib" / "data" / "akshitDashaData.json"
    ui_path.parent.mkdir(parents=True, exist_ok=True)
    with ui_path.open("w") as f:
        json.dump(out, f, indent=2)
    print(f"Wrote: {ui_path}")


if __name__ == "__main__":
    main()
