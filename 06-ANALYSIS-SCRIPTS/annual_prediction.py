#!/usr/bin/env python3
"""Annual Prediction Report - year-specific dasha + transit focus."""

import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

DASHA_WINDOWS = {
    2026: "Jupiter-Mercury, Mercury-Moon pratyantar",
    2027: "Jupiter-Mercury until May, then Jupiter-Ketu; transition to Jupiter-Venus",
    2028: "Jupiter-Venus (Apr 2028 – Dec 2030) — PRIME MARRIAGE WINDOW",
    2029: "Jupiter-Venus — marriage, career peak",
    2030: "Jupiter-Venus until Dec, then Jupiter-Sun",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, default=2027)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    dasha = DASHA_WINDOWS.get(args.year, "See dasha analysis")
    out = args.output or f"01-AKSHIT-ANALYSIS/ANNUAL_PREDICTION_{args.year}.md"
    lines = [
        f"# Annual Prediction — {args.year}",
        "",
        "## Dasha", dasha, "",
        "## Focus",
        "- Marriage: Jupiter-Venus window" if args.year in (2028, 2029) else "- Review current dasha",
        "- Career: Venus 10th lord",
        "- Transits: Check Jupiter/Saturn through 2,7,11",
    ]
    path = REPO_ROOT / out
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {path}")


if __name__ == "__main__":
    main()
