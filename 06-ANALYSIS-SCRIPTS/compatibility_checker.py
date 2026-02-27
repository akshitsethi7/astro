#!/usr/bin/env python3
"""Compatibility Checker - Ashtakoota template for two charts."""

import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chart1", default=str(REPO_ROOT / "11-CONFIG-DATA" / "vargas_output.json"))
    parser.add_argument("--chart2", default=None)
    parser.add_argument("--output", default="02-MARRIAGE-ANALYSIS/COMPATIBILITY_REPORT_TEMPLATE.md")
    args = parser.parse_args()
    lines = [
        "# Compatibility Report (Template)",
        "",
        "Ashtakoota + Dashakoota matching. Add partner chart with --chart2 for full analysis.",
        "",
        "| Category | Points |",
        "|----------|--------|",
        "| Varna | 1 |", "| Vashya | 2 |", "| Tara | 3 |", "| Yoni | 4 |",
        "| Graha Maitri | 5 |", "| Gana | 6 |", "| Bhakoot | 7 |", "| Nadi | 8 |",
        "",
        "**Total**: 36 max. 18+ acceptable.",
    ]
    out = REPO_ROOT / args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
