# MASTER PLAN — Task Checklist

**Subject**: Akshit Sethi | Dec 26, 1994 | 22:50 | Kanpur  
**Last Updated**: February 27, 2026

---

## ✅ Completed

| # | Task | Status |
|---|------|--------|
| 1 | Venus exalted → own sign (Libra) in all docs | Done |
| 2 | Lagna360 + External Tools section in MASTER_PLAN | Done |
| 3 | Cross-reference reports (Marriage 2,410, Career 387, Health 63, Wealth 1,003, Spirituality 200) | Done |
| 4 | Transit report with marriage window context | Done |
| 5 | DEFINITIVE_MARRIAGE_RECONCILIATION cross-ref count + links | Done |
| 6 | Verification links in AKSHIT_SYNTHESIZED_LIFE_ANALYSIS | Done |
| 7 | UI chart data from vargas (akshitChartData.ts, akshitDashaData.json) | Done |
| 8 | Jaimini page (/jaimini) with DK, UL, Chara, Narayana | Done |
| 9 | Narayana Dasha lord-to-sign durations | Done |
| 10 | KP report house numbers from vargas | Done |

---

## 🔄 Scripts to Run (Verification)

| Script | Command | Output |
|--------|---------|--------|
| Transit | `python3 transit_analysis.py` | `03-LIFE-AREAS-ANALYSIS/TRANSIT_REPORT_2026_2035.md` |
| Yogini Dasha | `python3 yogini_dasha.py` | `04-DASHA-ANALYSIS/YOGINI_DASHA_TIMELINE.md` |
| Narayana Dasha | `python3 narayana_dasha.py` | `04-DASHA-ANALYSIS/NARAYANA_DASHA_TIMELINE.md` |
| Vimshottari | `python3 vimshottari_dasha.py` | `12-DEVELOPMENT/astro-marriage-ui/lib/data/akshitDashaData.json` |
| Ashtakavarga | `python3 ashtakavarga_calculator.py` | `03-LIFE-AREAS-ANALYSIS/ASHTAKAVARGA_REPORT.md` |
| Nakshatra | `python3 nakshatra_deep_analysis.py` | `01-AKSHIT-ANALYSIS/NAKSHATRA_DEEP_ANALYSIS.md` |
| Cross-ref Marriage | `python3 cross_reference_chart.py --topic marriage` | `01-AKSHIT-ANALYSIS/CROSS_REFERENCE_REPORT_MARRIAGE.md` |
| Annual 2027 | `python3 annual_prediction.py 2027` | `01-AKSHIT-ANALYSIS/ANNUAL_PREDICTION_2027.md` |
| Annual 2028 | `python3 annual_prediction.py 2028` | `01-AKSHIT-ANALYSIS/ANNUAL_PREDICTION_2028.md` |

*Run from `06-ANALYSIS-SCRIPTS/` with `11-CONFIG-DATA/vargas_output.json` in parent.*

---

## 📋 Pending (Future)

| # | Task | Notes |
|---|------|-------|
| 1 | Topic organizer | Blocked: extraction format mismatch |
| 2 | Full Ashtakoota compatibility calculator | Needs partner birth data input |
| 3 | Upagraha (shadow planet) analysis | Consider Lagna360 or new script |
| 4 | Shadbala calculator | Consider Lagna360 or new script |

---

## 📂 Quick Links

- **MASTER_PLAN**: [MASTER_PLAN.md](MASTER_PLAN.md)
- **Synthesized Analysis**: [../01-AKSHIT-ANALYSIS/AKSHIT_SYNTHESIZED_LIFE_ANALYSIS.md](../01-AKSHIT-ANALYSIS/AKSHIT_SYNTHESIZED_LIFE_ANALYSIS.md)
- **Marriage Reconciliation**: [../02-MARRIAGE-ANALYSIS/DEFINITIVE_MARRIAGE_RECONCILIATION.md](../02-MARRIAGE-ANALYSIS/DEFINITIVE_MARRIAGE_RECONCILIATION.md)
- **Transit Report**: [../03-LIFE-AREAS-ANALYSIS/TRANSIT_REPORT_2026_2035.md](../03-LIFE-AREAS-ANALYSIS/TRANSIT_REPORT_2026_2035.md)
- **Lagna360**: [app.lagna360.com](https://app.lagna360.com)
