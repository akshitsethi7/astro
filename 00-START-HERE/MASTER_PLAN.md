# MASTER PLAN
## Akshit's Vedic Astrology Knowledge System

**Created**: February 27, 2026  
**Subject**: Akshit Sethi | Dec 26, 1994 | 22:50 | Kanpur | Leo Ascendant (Lahiri)  
**Current Age**: 31 | **Current Dasha**: Jupiter-Mercury (Feb 5, 2025 – May 14, 2027)  
**Current Pratyantardasha**: Mercury-Moon (Jan 16 – Mar 26, 2026)

---

## 1. KNOWLEDGE INVENTORY

### What We Have

| Asset | Count | Status |
|-------|-------|--------|
| PDF books | 46 | 33 text-extracted, 13 being OCR-processed |
| Extracted book pages | ~14,600+ | Searchable JSON + markdown |
| Classical cross-references | 1,865 | Matched to Akshit's specific positions |
| Analysis documents | 44+ | Covering all life areas |
| Learning materials | 80+ files | Foundations through advanced |
| Python scripts | 69+ | Extraction, analysis, cross-reference |
| Chart data files | 5 | D1-D60, all dashas, nakshatras |
| Divisional charts computed | 17 | D1,D2,D3,D4,D6,D7,D9,D10,D12,D16,D20,D24,D27,D30,D40,D45,D60 |

### Prediction Confidence Summary

| Life Area | Key Prediction | Confidence | Systems Validating |
|-----------|---------------|------------|-------------------|
| **Marriage timing** | Late 2028 - Late 2029 | 92% | Vimshottari + Chara Dasha + K.N. Rao 2-7-11 |
| **Marriage promised** | Yes | 99% | Parashari + Jaimini + all texts |
| **Marriage quality** | 9/10 | 90% | Jupiter on UL + Saturn own sign 7th + Venus own sign |
| **Spouse age** | Could be any age; mature character | FAIR | Jaimini Su.59 does NOT apply |
| **Spouse nature** | Beautiful (Jupiter), strong (Mars DK), sensuous (Venus) | 85% | BPHS Ch.33 |
| **Meeting spouse** | 2028-2029 (Jupiter-Venus antardasha) | 85% | Vimshottari + KN Rao double transit |
| **Career peak** | 2028-2035 | 85% | Venus 10th lord own sign + Jupiter dasha |
| **Income peak** | Rs 60-90 lakh/year (2028-2030) | 85% | Jupiter-Venus dasha period |

---

## 2. CRITICAL CORRECTIONS (Feb 27, 2026)

### Chart Data Source Priority
- `vargas_output.json` — **primary** (Lahiri sidereal, Dec 26 1994 Kanpur)
- **Next.js UI** — uses `akshitChartData.ts` + `akshitDashaData.json` (both from vargas)
- `chartsimp.json` — legacy/supplementary (different chart; NOT used by UI)
- `chartsall` — NOT for Vedic (tropical/Scorpio asc)

### Dasha Dates
- Jupiter-Mercury: **Feb 5, 2025 – May 14, 2027**
- Jupiter-Venus (marriage window): **Apr 19, 2028 – Dec 19, 2030**

---

## 3. SCRIPTS BUILT (Completed)

| Script | Purpose | Output |
|--------|---------|--------|
| `transit_analysis.py` | Jupiter/Saturn transits 2026-2035 | `03-LIFE-AREAS-ANALYSIS/TRANSIT_REPORT_2026_2035.md` |
| `ashtakavarga_calculator.py` | SAV tables | `03-LIFE-AREAS-ANALYSIS/ASHTAKAVARGA_REPORT.md` |
| `yogini_dasha.py` | Yogini Dasha timeline | `04-DASHA-ANALYSIS/YOGINI_DASHA_TIMELINE.md` |
| `nakshatra_deep_analysis.py` | Planet nakshatras | `01-AKSHIT-ANALYSIS/NAKSHATRA_DEEP_ANALYSIS.md` |
| `compatibility_checker.py` | Ashtakoota template | `02-MARRIAGE-ANALYSIS/COMPATIBILITY_REPORT_TEMPLATE.md` |
| `annual_prediction.py` | Year-specific reports | `01-AKSHIT-ANALYSIS/ANNUAL_PREDICTION_YYYY.md` |
| `narayana_dasha.py` | Narayana Dasha timeline | `04-DASHA-ANALYSIS/NARAYANA_DASHA_TIMELINE.md` |
| `kp_sub_lord_analysis.py` | KP sub-lord structure | `02-MARRIAGE-ANALYSIS/KP_SUB_LORD_ANALYSIS.md` |
| `cross_reference_chart.py` | Marriage cross-reference | `01-AKSHIT-ANALYSIS/CROSS_REFERENCE_REPORT_MARRIAGE.md` |
| `vimshottari_dasha.py` | Vimshottari dasha JSON for UI | `12-DEVELOPMENT/astro-marriage-ui/lib/data/akshitDashaData.json` |

---

## 4. DOCUMENTS CREATED

| Document | Location |
|----------|----------|
| Transit Report 2026-2035 | `03-LIFE-AREAS-ANALYSIS/TRANSIT_REPORT_2026_2035.md` |
| Yogini Dasha Timeline | `04-DASHA-ANALYSIS/YOGINI_DASHA_TIMELINE.md` |
| Ashtakavarga Report | `03-LIFE-AREAS-ANALYSIS/ASHTAKAVARGA_REPORT.md` |
| Nakshatra Deep Analysis | `01-AKSHIT-ANALYSIS/NAKSHATRA_DEEP_ANALYSIS.md` |
| Education/Siblings/Parents | `03-LIFE-AREAS-ANALYSIS/EDUCATION_SIBLINGS_PARENTS_ANALYSIS.md` |
| Remedial Timing Guide | `18-REMEDIES/REMEDIAL_TIMING_GUIDE.md` |
| Annual Predictions 2027, 2028 | `01-AKSHIT-ANALYSIS/ANNUAL_PREDICTION_2027.md`, `ANNUAL_PREDICTION_2028.md` |
| Narayana Dasha Timeline | `04-DASHA-ANALYSIS/NARAYANA_DASHA_TIMELINE.md` |
| KP Sub-Lord Analysis | `02-MARRIAGE-ANALYSIS/KP_SUB_LORD_ANALYSIS.md` |
| C.S. Patel / Jataka Review | `01-AKSHIT-ANALYSIS/NAVAMSA_JATAKA_REVIEW.md` |
| Cross-Reference Marriage | `01-AKSHIT-ANALYSIS/CROSS_REFERENCE_REPORT_MARRIAGE.md` (2,410 refs) |
| Cross-Reference Career | `01-AKSHIT-ANALYSIS/CROSS_REFERENCE_REPORT_CAREER.md` (387 refs) |
| Cross-Reference Health | `01-AKSHIT-ANALYSIS/CROSS_REFERENCE_REPORT_HEALTH.md` (63 refs) |
| Cross-Reference Wealth | `01-AKSHIT-ANALYSIS/CROSS_REFERENCE_REPORT_WEALTH.md` (1,003 refs) |
| Cross-Reference Spirituality | `01-AKSHIT-ANALYSIS/CROSS_REFERENCE_REPORT_SPIRITUALITY.md` (200 refs) |

---

## 5. ARCHIVED

- **COMPLETE_MARRIAGE_ANALYSIS.md** (wrong chart: Scorpio 1985) → Replaced with redirect; original in `13-ARCHIVE/COMPLETE_MARRIAGE_ANALYSIS_WRONG_CHART.md`

---

## 6. COMPLETED FIXES (Feb 27, 2026)

| Gap | Fix |
|-----|-----|
| UI showed wrong chart (1985) | Switched to vargas → `akshitChartData.ts`, `akshitDashaData.json` |
| Narayana Dasha simplified | Lord-to-sign durations from chart; proper BPHS logic |
| KP report missing houses | Pull house from `vargas.D1.planets` |
| Dasha page brittle import | Uses local `akshitDashaData.json` |
| Jaimini page | Added `/jaimini` with Darakaraka, Upapada, Chara, Narayana |

---

## 7. BOOK KNOWLEDGE & CROSS-REFERENCE

### Synthesized Analysis (14,069 quotes, 33 books)

**Primary source**: `01-AKSHIT-ANALYSIS/AKSHIT_SYNTHESIZED_LIFE_ANALYSIS.md`

| Life Area | Quotes | Key Classical Principles |
|-----------|--------|--------------------------|
| **Marriage** | 2,893 | Saturn 7th own sign → stable, mature partner; Venus own sign (Libra) → beautiful, artistic spouse; D9 Venus 8th → transformative marriage |
| **Career** | 2,885 | Venus 10th lord own sign → creative/communication success; Mercury 5th → tech, media, finance; Jupiter 4th → education foundation |
| **Wealth** | 2,355 | Dhana Yoga (2nd+11th lord in 5th); Lakshmi Yoga (Venus); Budha-Aditya (Sun-Mercury); peak 2028-2030, 2038-2041 |
| **Health** | 2,200 | Leo Asc + Mars 1st → strong vitality; Mercury 5th → watch digestion; Saturn 7th → joint/back after 40 |
| **Spirituality** | 2,522 | Jupiter 4th + Ketu 9th → high inclination; meditation, mantra, pilgrimage; Jupiter dasha favors growth |
| **Dasha** | 1,214 | Jupiter-Venus = golden period; Saturn Mahadasha = maturity, stability |

### Cross-Reference by Topic

Run to get book-specific page references:

```bash
python3 06-ANALYSIS-SCRIPTS/cross_reference_chart.py --topic marriage    # 2,410 refs
python3 06-ANALYSIS-SCRIPTS/cross_reference_chart.py --topic career     # 387 refs
python3 06-ANALYSIS-SCRIPTS/cross_reference_chart.py --topic health     # 63 refs
python3 06-ANALYSIS-SCRIPTS/cross_reference_chart.py --topic wealth     # 1,003 refs
python3 06-ANALYSIS-SCRIPTS/cross_reference_chart.py --topic spirituality  # 200 refs
python3 06-ANALYSIS-SCRIPTS/cross_reference_chart.py --topic all --verbose
```

Output: `01-AKSHIT-ANALYSIS/CROSS_REFERENCE_REPORT_<TOPIC>.md`

---

## 8. FILE REFERENCE MAP

### Start Here
- **This file**: `00-START-HERE/MASTER_PLAN.md`
- **Task checklist**: `00-START-HERE/MASTER_PLAN_TASKS.md`
- **Synthesized (all life areas)**: `01-AKSHIT-ANALYSIS/AKSHIT_SYNTHESIZED_LIFE_ANALYSIS.md`
- **Quick look**: `01-AKSHIT-ANALYSIS/QUICK_REFERENCE_GUIDE.md`
- **Transit report**: `03-LIFE-AREAS-ANALYSIS/TRANSIT_REPORT_2026_2035.md`

### Marriage
- **DEFINITIVE**: `02-MARRIAGE-ANALYSIS/DEFINITIVE_MARRIAGE_RECONCILIATION.md`
- **Jaimini**: `02-MARRIAGE-ANALYSIS/JAIMINI_MARRIAGE_ANALYSIS.md`
- **KP structure**: `02-MARRIAGE-ANALYSIS/KP_SUB_LORD_ANALYSIS.md`
- **Compatibility template**: `02-MARRIAGE-ANALYSIS/COMPATIBILITY_REPORT_TEMPLATE.md`
- **Cross-reference**: Marriage (2,410), Career (387), Health (63), Wealth (1,003), Spirituality (200) — `01-AKSHIT-ANALYSIS/CROSS_REFERENCE_REPORT_*.md`

### Career, Finance, Health, Spirituality
- `03-LIFE-AREAS-ANALYSIS/AKSHIT_COMPREHENSIVE_CAREER_ANALYSIS.md`
- `03-LIFE-AREAS-ANALYSIS/AKSHIT_COMPREHENSIVE_FINANCIAL_ANALYSIS.md`
- `03-LIFE-AREAS-ANALYSIS/AKSHIT_COMPREHENSIVE_HEALTH_ANALYSIS.md`
- Cross-reference: Career (387), Health (63), Wealth (1,003), Spirituality (200)

### Dasha
- `04-DASHA-ANALYSIS/AKSHIT_JUPITER_SATURN_DASHA_ANALYSIS.md`
- `04-DASHA-ANALYSIS/YOGINI_DASHA_TIMELINE.md`
- `04-DASHA-ANALYSIS/NARAYANA_DASHA_TIMELINE.md`

### UI (12-DEVELOPMENT/astro-marriage-ui)
- Chart data: `lib/data/akshitChartData.ts`
- Dasha data: `lib/data/akshitDashaData.json`
- Pages: Chart, Dasha, Transits, Jaimini, Compatibility, etc.

### Scripts (06-ANALYSIS-SCRIPTS)
- `transit_analysis.py`, `yogini_dasha.py`, `narayana_dasha.py`, `vimshottari_dasha.py`
- `ashtakavarga_calculator.py`, `nakshatra_deep_analysis.py`, `annual_prediction.py`
- `cross_reference_chart.py`, `kp_sub_lord_analysis.py`, `compatibility_checker.py`

---

## 9. EXTERNAL TOOLS (Supplementary)

| Tool | URL | Use For |
|------|-----|---------|
| **Lagna360** | [app.lagna360.com](https://app.lagna360.com) | Dasha, transits, Ashtakavarga, Shadbala, Upagrahas, AI Q&A |
| Period predictions | [predictions/period](https://app.lagna360.com/predictions/period) | Dasha period cross-check |
| Dasha | [horoscope/dasha](https://app.lagna360.com/horoscope/dasha) | Vimshottari validation |
| Transits | [horoscope/transits](https://app.lagna360.com/horoscope/transits) | Live transit vs `TRANSIT_REPORT_2026_2035.md` |
| Panchang | [panchang](https://app.lagna360.com/panchang) | Muhurta for marriage dates |

*Create chart with Dec 26, 1994, 22:50, Kanpur. Use for cross-validation and features not yet in scripts (Upagrahas, Shadbala, Shad Varga).*

---

## 10. REMAINING (Future)

- Topic organizer (blocked: extraction format mismatch)
- Compatibility calculator (full Ashtakoota with partner data)
- Cross-reference for all topics: **done** (Marriage 2,410, Career 387, Health 63, Wealth 1,003, Spirituality 200)

---

*Last updated: February 27, 2026. MASTER_PLAN complete. Book knowledge: 14,069 quotes across 6 life areas.*
