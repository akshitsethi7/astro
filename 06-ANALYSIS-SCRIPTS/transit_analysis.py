#!/usr/bin/env python3
"""
Transit Analysis Script for Akshit's Chart

Calculates Jupiter and Saturn transit positions (sign + house) over a given
year range and generates a markdown report. Also identifies simple
double-transit windows where BOTH Jupiter and Saturn activate key houses
for marriage (2, 7, 11 from Lagna).

Inputs:
- Natal data: 11-CONFIG-DATA/vargas_output.json

Outputs:
- A markdown report summarizing transits and double-transit windows.

Usage:
    python 06-ANALYSIS-SCRIPTS/transit_analysis.py --start-year 2026 --end-year 2035

Requirements:
- astronomy-engine (optional; falls back to approximate positions if not installed)
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

try:
    import astronomy
    from astronomy import Body, Time, EclipticLongitude
    HAS_ASTRONOMY = True
except ImportError:
    HAS_ASTRONOMY = False

REPO_ROOT = Path(__file__).resolve().parents[1]
VARGAS_PATH = REPO_ROOT / "11-CONFIG-DATA" / "vargas_output.json"

SIGN_NAMES = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces",
]

KEY_MARRIAGE_HOUSES_FROM_LAGNA = {2, 7, 11}


@dataclass
class HouseCusp:
    house: int
    lon: float


@dataclass
class TransitSegment:
    start: date
    end: date
    sign: str
    house: int


@dataclass
class DoubleTransitWindow:
    start: date
    end: date
    jupiter_house: int
    saturn_house: int


def load_house_cusps(path: Path) -> List[HouseCusp]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    cusps_raw = data.get("house_cusps_d1")
    if not cusps_raw:
        raise RuntimeError("house_cusps_d1 not found in vargas_output.json")
    cusps = [HouseCusp(h["house"], float(h["lon"])) for h in cusps_raw]
    cusps.sort(key=lambda c: c.lon)
    return cusps


def sign_from_lon(lon: float) -> str:
    lon = lon % 360.0
    return SIGN_NAMES[int(lon // 30.0)]


def house_for_lon(lon: float, cusps: List[HouseCusp]) -> int:
    lon = lon % 360.0
    n = len(cusps)
    for i, cusp in enumerate(cusps):
        next_cusp = cusps[(i + 1) % n]
        start, end = cusp.lon, next_cusp.lon
        if i == n - 1:
            if lon >= start or lon < end:
                return cusp.house
        elif start <= lon < end:
            return cusp.house
    return cusps[-1].house


def daterange(start: date, end: date) -> Iterable[date]:
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


def _approx_longitude_jupiter(d: date) -> float:
    ref = date(2000, 1, 1)
    return ((d - ref).days * 0.083) % 360


def _approx_longitude_saturn(d: date) -> float:
    ref = date(2000, 1, 1)
    return ((d - ref).days * 0.033) % 360


def compute_daily_positions(
    start_year: int, end_year: int, cusps: List[HouseCusp],
) -> Tuple[Dict[str, List[TransitSegment]], List[DoubleTransitWindow]]:
    start_date = date(start_year, 1, 1)
    end_date = date(end_year, 12, 31)

    def get_lon(planet: str, d: date) -> float:
        if HAS_ASTRONOMY:
            t = astronomy.Time.Make(d.year, d.month, d.day, 0, 0, 0.0)
            body = astronomy.Body.Jupiter if planet == "Jupiter" else astronomy.Body.Saturn
            return astronomy.EclipticLongitude(body, t)
        return _approx_longitude_jupiter(d) if planet == "Jupiter" else _approx_longitude_saturn(d)

    segments: Dict[str, List[TransitSegment]] = {"Jupiter": [], "Saturn": []}
    prev_state: Dict[str, Tuple[str, int, date]] = {}
    double_windows: List[DoubleTransitWindow] = []
    in_window, window_start, last_j_house, last_s_house = False, None, None, None

    for d in daterange(start_date, end_date):
        daily_houses: Dict[str, int] = {}
        for name in ("Jupiter", "Saturn"):
            lon = get_lon(name, d)
            sign, house = sign_from_lon(lon), house_for_lon(lon, cusps)
            daily_houses[name] = house
            if name not in prev_state:
                prev_state[name] = (sign, house, d)
            else:
                prev_sign, prev_house, seg_start = prev_state[name]
                if sign != prev_sign or house != prev_house:
                    segments[name].append(TransitSegment(seg_start, d - timedelta(days=1), prev_sign, prev_house))
                    prev_state[name] = (sign, house, d)

        j_house, s_house = daily_houses["Jupiter"], daily_houses["Saturn"]
        j_hits = j_house in KEY_MARRIAGE_HOUSES_FROM_LAGNA
        s_hits = s_house in KEY_MARRIAGE_HOUSES_FROM_LAGNA
        if j_hits and s_hits:
            if not in_window:
                in_window, window_start = True, d
            last_j_house, last_s_house = j_house, s_house
        else:
            if in_window and window_start:
                double_windows.append(DoubleTransitWindow(window_start, d - timedelta(days=1), last_j_house or j_house, last_s_house or s_house))
            in_window, window_start = False, None

    for name, (sign, house, seg_start) in prev_state.items():
        segments[name].append(TransitSegment(seg_start, end_date, sign, house))
    if in_window and window_start:
        double_windows.append(DoubleTransitWindow(window_start, end_date, last_j_house or 7, last_s_house or 7))

    return segments, double_windows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-year", type=int, default=2026)
    parser.add_argument("--end-year", type=int, default=2035)
    parser.add_argument("--output", default="03-LIFE-AREAS-ANALYSIS/TRANSIT_REPORT_2026_2035.md")
    args = parser.parse_args()

    cusps = load_house_cusps(VARGAS_PATH)
    segments, double_windows = compute_daily_positions(args.start_year, args.end_year, cusps)

    lines = [
        f"# Transit Report {args.start_year}-{args.end_year}",
        "",
        "Automatically generated by `06-ANALYSIS-SCRIPTS/transit_analysis.py`.",
        "",
        "## Overview",
        "- **Planets**: Jupiter, Saturn",
        "- **Houses**: From D1 cusps in vargas_output.json",
        "- **Double transit**: Both in houses 2, 7, or 11 from Lagna",
        "",
    ]
    for planet in ("Jupiter", "Saturn"):
        lines.append(f"## {planet} Transits")
        lines.append("| Start | End | Sign | House |")
        lines.append("|-------|-----|------|-------|")
        for seg in segments[planet]:
            lines.append(f"| {seg.start} | {seg.end} | {seg.sign} | {seg.house} |")
        lines.append("")
    lines.append("## Double Transit Windows")
    if double_windows:
        lines.append("| Start | End | J House | S House |")
        for w in double_windows:
            lines.append(f"| {w.start} | {w.end} | {w.jupiter_house} | {w.saturn_house} |")
    else:
        lines.append("None in this period.")
    out = REPO_ROOT / args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
