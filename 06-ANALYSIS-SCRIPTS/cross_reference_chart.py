#!/usr/bin/env python3
"""
Cross-Reference Script: Extracted Book Content vs Akshit's Chart Positions
Searches all extracted book content for rules that SPECIFICALLY match
Akshit's planetary positions, houses, signs, nakshatras, and yogas.

Usage:
    python3 cross_reference_chart.py
    python3 cross_reference_chart.py --topic marriage
    python3 cross_reference_chart.py --topic all --verbose
"""

import json
import re
import argparse
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Optional


CHART_DATA = {
    "birth": {
        "date": "December 26, 1994",
        "time": "22:50",
        "place": "Kanpur, India",
        "ascendant": "Leo",
        "ayanamsa": "Lahiri"
    },
    "planets_d1": {
        "Sun":     {"sign": "Sagittarius", "house": 5, "degree": 250.83, "nakshatra": "Mula",           "pada": 4, "dignity": "Neutral",  "combust": False, "retrograde": False},
        "Moon":    {"sign": "Virgo",       "house": 2, "degree": 171.58, "nakshatra": "Hasta",          "pada": 4, "dignity": "Neutral",  "combust": False, "retrograde": False},
        "Mars":    {"sign": "Leo",         "house": 1, "degree": 128.55, "nakshatra": "Magha",          "pada": 3, "dignity": "Neutral",  "combust": False, "retrograde": False},
        "Mercury": {"sign": "Sagittarius", "house": 5, "degree": 257.98, "nakshatra": "Purva Ashadha",  "pada": 2, "dignity": "Neutral",  "combust": True,  "retrograde": False},
        "Jupiter": {"sign": "Scorpio",     "house": 4, "degree": 219.85, "nakshatra": "Anuradha",       "pada": 2, "dignity": "Neutral",  "combust": False, "retrograde": False},
        "Venus":   {"sign": "Libra",       "house": 3, "degree": 205.33, "nakshatra": "Vishakha",       "pada": 2, "dignity": "Own Sign", "combust": False, "retrograde": False},
        "Saturn":  {"sign": "Aquarius",    "house": 7, "degree": 313.77, "nakshatra": "Shatabhisha",    "pada": 3, "dignity": "Own Sign", "combust": False, "retrograde": False},
        "Rahu":    {"sign": "Libra",       "house": 3, "degree": 199.69, "nakshatra": "Swati",          "pada": 4, "dignity": "Neutral",  "combust": False, "retrograde": True},
        "Ketu":    {"sign": "Aries",       "house": 9, "degree": 19.69,  "nakshatra": "Bharani",        "pada": 2, "dignity": "Neutral",  "combust": False, "retrograde": True},
    },
    "planets_d9": {
        "Saturn":  {"sign": "Aquarius",  "house": 5},
        "Rahu":    {"sign": "Pisces",    "house": 6},
        "Venus":   {"sign": "Taurus",    "house": 8},
        "Mars":    {"sign": "Gemini",    "house": 9},
        "Sun":     {"sign": "Cancer",    "house": 10},
        "Moon":    {"sign": "Cancer",    "house": 10},
        "Mercury": {"sign": "Virgo",     "house": 12},
        "Jupiter": {"sign": "Virgo",     "house": 12},
        "Ketu":    {"sign": "Virgo",     "house": 12},
    },
    "houses": {
        1: {"sign": "Leo",         "lord": "Sun"},
        2: {"sign": "Virgo",       "lord": "Mercury"},
        3: {"sign": "Libra",       "lord": "Venus"},
        4: {"sign": "Scorpio",     "lord": "Mars"},
        5: {"sign": "Sagittarius", "lord": "Jupiter"},
        6: {"sign": "Capricorn",   "lord": "Saturn"},
        7: {"sign": "Aquarius",    "lord": "Saturn"},
        8: {"sign": "Pisces",      "lord": "Jupiter"},
        9: {"sign": "Aries",       "lord": "Mars"},
        10: {"sign": "Taurus",     "lord": "Venus"},
        11: {"sign": "Gemini",     "lord": "Mercury"},
        12: {"sign": "Cancer",     "lord": "Moon"},
    },
    "key_features": {
        "ascendant": "Leo",
        "7th_lord": "Saturn",
        "7th_lord_house": 7,
        "7th_lord_sign": "Aquarius",
        "7th_lord_dignity": "Own Sign",
        "marriage_karaka": "Venus",
        "venus_sign": "Libra",
        "venus_dignity": "Own Sign",
        "venus_d9_sign": "Taurus",
        "venus_d9_dignity": "Own Sign",
        "d9_ascendant": "Libra",
        "darakaraka": "Mars",
        "atmakaraka": "Venus",
        "upapada": "Scorpio",
        "current_mahadasha": "Jupiter",
        "marriage_antardasha": "Venus",
    },
    "yogas_claimed": [
        "Venus in own sign D1 AND D9 (Shukra Dwi-Svamsha)",
        "Saturn in own sign in 7th house (Saptamesh Sva-Bhava)",
        "Moon in own sign in Navamsa Cancer (Chandra Sva-Rashi)",
        "Jupiter aspecting 7th house from 4th (Guru Drishti Saptama)",
    ]
}


SEARCH_PATTERNS = {
    "marriage_general": {
        "description": "General marriage rules applicable to chart",
        "patterns": [
            r"(?i)saturn\s+in\s+(the\s+)?7th\s+house",
            r"(?i)saturn\s+in\s+seventh\s+house",
            r"(?i)7th\s+lord\s+in\s+(the\s+)?7th\s+house",
            r"(?i)seventh\s+lord\s+in\s+seventh",
            r"(?i)saturn\s+in\s+aquarius",
            r"(?i)saturn\s+in\s+own\s+sign",
            r"(?i)shani\s+in\s+(the\s+)?7th",
            r"(?i)marriage.*delay",
            r"(?i)delay.*marriage",
            r"(?i)late\s+marriage",
            r"(?i)venus\s+in\s+libra",
            r"(?i)venus\s+in\s+own\s+sign",
            r"(?i)shukra.*swa",
            r"(?i)venus.*exalt",
            r"(?i)7th\s+house.*aquarius",
            r"(?i)aquarius.*7th\s+house",
            r"(?i)7th\s+house.*marriage",
            r"(?i)marriage.*7th\s+house",
            r"(?i)vivaha",
            r"(?i)kalatra",
            r"(?i)spouse.*7th",
            r"(?i)7th\s+house.*spouse",
            r"(?i)partner.*7th",
            r"(?i)venus.*marriage\s+karaka",
            r"(?i)marriage\s+karaka",
            r"(?i)leo\s+ascendant.*7th",
            r"(?i)7th\s+house.*leo",
        ]
    },
    "marriage_timing": {
        "description": "Marriage timing rules",
        "patterns": [
            r"(?i)jupiter.*venus.*dasha",
            r"(?i)venus.*jupiter.*dasha",
            r"(?i)guru.*shukra.*dasha",
            r"(?i)jupiter\s+mahadasha.*marriage",
            r"(?i)marriage.*jupiter\s+mahadasha",
            r"(?i)2-7-11",
            r"(?i)second.*seventh.*eleventh",
            r"(?i)marriage\s+timing",
            r"(?i)when.*marry",
            r"(?i)age\s+of\s+marriage",
            r"(?i)timing\s+of\s+marriage",
            r"(?i)saturn.*delay.*marriage",
            r"(?i)marriage.*after\s+30",
            r"(?i)marriage.*33",
            r"(?i)marriage.*34",
            r"(?i)marriage.*35",
        ]
    },
    "spouse_nature": {
        "description": "Spouse characteristics and nature",
        "patterns": [
            r"(?i)saturn\s+in\s+7th.*spouse",
            r"(?i)spouse.*saturn\s+in\s+7th",
            r"(?i)7th\s+lord.*own\s+sign.*spouse",
            r"(?i)spouse.*older",
            r"(?i)older\s+spouse",
            r"(?i)spouse.*age",
            r"(?i)age.*spouse",
            r"(?i)wife.*saturn",
            r"(?i)saturn.*wife",
            r"(?i)spouse.*appearance",
            r"(?i)spouse.*nature",
            r"(?i)character.*spouse",
            r"(?i)spouse.*character",
            r"(?i)kalatra",
            r"(?i)7th\s+house.*leo\s+ascendant",
            r"(?i)leo.*ascendant.*7th",
            r"(?i)spouse.*mature",
            r"(?i)mature.*partner",
            r"(?i)spouse.*responsible",
            r"(?i)venus.*beautiful",
            r"(?i)beautiful.*spouse",
            r"(?i)spouse.*venus",
            r"(?i)partner.*saturn",
            r"(?i)darakaraka",
            r"(?i)mars.*spouse",
            r"(?i)spouse.*mars",
        ]
    },
    "navamsa_marriage": {
        "description": "Navamsa (D9) marriage rules",
        "patterns": [
            r"(?i)navamsa.*venus",
            r"(?i)venus.*navamsa",
            r"(?i)venus\s+in\s+taurus.*navamsa",
            r"(?i)venus.*own\s+sign.*navamsa",
            r"(?i)navamsa.*marriage",
            r"(?i)D9.*marriage",
            r"(?i)navamsa.*libra.*ascendant",
            r"(?i)navamsa.*spouse",
            r"(?i)moon.*cancer.*navamsa",
            r"(?i)navamsa.*7th\s+house",
            r"(?i)navamsa.*8th\s+house",
            r"(?i)venus.*8th.*navamsa",
            r"(?i)navamsa.*ascendant",
            r"(?i)D9.*venus",
            r"(?i)venus.*D9",
            r"(?i)divisional.*marriage",
            r"(?i)navamsa.*quality",
            r"(?i)venus\s+in\s+8th",
            r"(?i)8th\s+house.*venus",
        ]
    },
    "jaimini": {
        "description": "Jaimini system rules",
        "patterns": [
            r"(?i)upapada",
            r"(?i)darakaraka",
            r"(?i)atmakaraka",
            r"(?i)chara\s+dasha",
            r"(?i)jaimini.*marriage",
            r"(?i)marriage.*jaimini",
            r"(?i)karakamsha",
            r"(?i)arudha.*7th",
            r"(?i)A7",
            r"(?i)jaimini.*sutra",
        ]
    },
    "yogas": {
        "description": "Yoga/combination rules",
        "patterns": [
            r"(?i)malavya\s+yoga",
            r"(?i)sasa\s+yoga",
            r"(?i)pancha\s+mahapurusha",
            r"(?i)raja\s+yoga",
            r"(?i)venus.*own\s+sign.*yoga",
            r"(?i)saturn.*own\s+sign.*yoga",
            r"(?i)venus.*libra.*yoga",
            r"(?i)saturn.*aquarius.*yoga",
            r"(?i)marriage.*yoga",
            r"(?i)vivaha.*yoga",
            r"(?i)gajakesari",
            r"(?i)budha\s+aditya",
            r"(?i)sun.*mercury.*conjunction",
            r"(?i)mercury.*sun.*conjunction",
            r"(?i)kendra.*trikona",
            r"(?i)dhana\s+yoga",
            r"(?i)lakshmi\s+yoga",
            r"(?i)musala\s+yoga",
            r"(?i)venus.*kendra",
            r"(?i)saturn.*kendra",
        ]
    },
    "saturn_7th_specific": {
        "description": "Saturn in 7th house specific rules (most important for marriage)",
        "patterns": [
            r"(?i)saturn\s+in\s+(the\s+)?seventh",
            r"(?i)saturn\s+in\s+(the\s+)?7th",
            r"(?i)shani\s+in\s+(the\s+)?7",
            r"(?i)saturn.*seventh\s+house",
            r"(?i)7th\s+house.*saturn",
            r"(?i)saturn.*kumbha.*7",
            r"(?i)saturn.*aquarius.*seventh",
            r"(?i)saptama.*shani",
            r"(?i)shani.*saptama",
        ]
    },
    "dasha_analysis": {
        "description": "Dasha period rules for current/upcoming periods",
        "patterns": [
            r"(?i)jupiter\s+mahadasha",
            r"(?i)guru\s+mahadasha",
            r"(?i)jupiter.*period",
            r"(?i)venus\s+antardasha",
            r"(?i)shukra\s+antardasha",
            r"(?i)jupiter.*venus.*period",
            r"(?i)guru.*shukra",
            r"(?i)vimshottari.*marriage",
            r"(?i)marriage.*vimshottari",
        ]
    },
    "career_10th": {
        "description": "Career rules (10th house Taurus, lord Venus)",
        "patterns": [
            r"(?i)10th\s+house.*taurus",
            r"(?i)taurus.*10th\s+house",
            r"(?i)venus.*10th\s+lord",
            r"(?i)10th\s+lord.*venus",
            r"(?i)10th\s+lord.*libra",
            r"(?i)10th\s+lord.*3rd\s+house",
            r"(?i)venus.*career",
            r"(?i)career.*venus",
            r"(?i)technology.*career",
            r"(?i)10th\s+house.*career",
            r"(?i)career.*10th\s+house",
            r"(?i)profession.*10th",
            r"(?i)10th\s+lord.*career",
            r"(?i)venus.*profession",
            r"(?i)venus.*success",
            r"(?i)mercury\s+in\s+5th.*career",
            r"(?i)mercury\s+in\s+5th.*intelligence",
            r"(?i)jupiter\s+in\s+4th.*career",
            r"(?i)jupiter\s+in\s+4th.*education",
            r"(?i)sun\s+in\s+5th.*creativity",
            r"(?i)5th\s+house.*mercury",
            r"(?i)5th\s+house.*sun",
            r"(?i)3rd\s+house.*venus",
            r"(?i)venus\s+in\s+3rd",
            r"(?i)communication.*career",
            r"(?i)media.*career",
            r"(?i)IT.*career",
            r"(?i)software.*career",
            r"(?i)business.*mercury",
            r"(?i)mercury.*business",
        ]
    },
    "health": {
        "description": "Health rules for Leo ascendant and chart placements",
        "patterns": [
            r"(?i)leo\s+ascendant.*health",
            r"(?i)health.*leo\s+ascendant",
            r"(?i)sun.*lord.*ascendant.*health",
            r"(?i)mars\s+in\s+1st.*health",
            r"(?i)mars\s+in\s+ascendant.*health",
            r"(?i)pitta.*constitution",
            r"(?i)heart.*leo",
            r"(?i)leo.*heart",
            r"(?i)digestion.*mercury",
            r"(?i)mercury.*digestion",
            r"(?i)stomach.*mercury",
            r"(?i)mercury.*stomach",
            r"(?i)combust.*mercury.*health",
            r"(?i)mercury\s+combust",
            r"(?i)5th\s+house.*health",
            r"(?i)health.*5th\s+house",
            r"(?i)saturn.*7th.*health",
            r"(?i)saturn.*joints",
            r"(?i)saturn.*bones",
            r"(?i)saturn.*back\s+pain",
            r"(?i)joint\s+pain.*saturn",
            r"(?i)mars\s+in\s+1st.*vitality",
            r"(?i)mars\s+in\s+1st.*strength",
            r"(?i)leo.*vitality",
            r"(?i)leo.*immunity",
            r"(?i)digestive.*problems",
            r"(?i)acidity.*mercury",
            r"(?i)anxiety.*mercury",
            r"(?i)nervous.*mercury",
            r"(?i)health.*saturn\s+in\s+7th",
            r"(?i)chronic.*saturn",
        ]
    },
    "wealth_2nd_11th": {
        "description": "Wealth rules (2nd/11th lord Mercury, Venus, Jupiter)",
        "patterns": [
            r"(?i)2nd\s+lord.*5th\s+house",
            r"(?i)11th\s+lord.*5th\s+house",
            r"(?i)mercury.*2nd\s+lord",
            r"(?i)mercury.*11th\s+lord",
            r"(?i)dhana\s+yoga",
            r"(?i)lakshmi\s+yoga",
            r"(?i)wealth.*venus",
            r"(?i)venus.*wealth",
            r"(?i)jupiter.*4th.*property",
            r"(?i)property.*jupiter",
            r"(?i)4th\s+house.*jupiter",
            r"(?i)2nd\s+house.*wealth",
            r"(?i)11th\s+house.*gains",
            r"(?i)gains.*11th\s+house",
            r"(?i)income.*mercury",
            r"(?i)mercury.*income",
            r"(?i)budha.*aditya",
            r"(?i)sun.*mercury.*yoga",
            r"(?i)wealth.*saturn",
            r"(?i)saturn.*wealth",
            r"(?i)savings.*saturn",
            r"(?i)investment.*mercury",
            r"(?i)mercury.*investment",
            r"(?i)real\s+estate.*jupiter",
            r"(?i)jupiter.*property",
        ]
    },
    "spirituality": {
        "description": "Spirituality rules (Jupiter 4th, Ketu 9th)",
        "patterns": [
            r"(?i)jupiter\s+in\s+4th.*spiritual",
            r"(?i)jupiter\s+in\s+4th.*wisdom",
            r"(?i)ketu\s+in\s+9th",
            r"(?i)9th\s+house.*ketu",
            r"(?i)ketu.*9th\s+house",
            r"(?i)ketu.*spiritual",
            r"(?i)spiritual.*ketu",
            r"(?i)ketu.*dharma",
            r"(?i)9th\s+house.*spiritual",
            r"(?i)4th\s+house.*jupiter",
            r"(?i)jupiter.*4th.*peace",
            r"(?i)meditation.*jupiter",
            r"(?i)jupiter.*meditation",
            r"(?i)mantra.*jupiter",
            r"(?i)pilgrimage.*9th",
            r"(?i)9th\s+house.*pilgrimage",
            r"(?i)detachment.*ketu",
            r"(?i)ketu.*detachment",
            r"(?i)moksha.*ketu",
            r"(?i)spirituality.*jupiter",
            r"(?i)mars\s+in\s+1st.*dharma",
            r"(?i)9th\s+lord.*mars",
            r"(?i)sun\s+in\s+5th.*purva\s+punya",
            r"(?i)5th\s+house.*spiritual",
        ]
    },
    "leo_ascendant": {
        "description": "Leo ascendant specific rules",
        "patterns": [
            r"(?i)leo\s+ascendant",
            r"(?i)simha\s+lagna",
            r"(?i)leo\s+rising",
            r"(?i)sun.*lord.*ascendant",
            r"(?i)ascendant.*leo",
        ]
    },
}

TOPIC_FILTER_MAP = {
    "marriage": ["marriage_general", "marriage_timing", "spouse_nature", "navamsa_marriage", "saturn_7th_specific", "dasha_analysis", "jaimini", "yogas"],
    "jaimini": ["jaimini"],
    "timing": ["marriage_timing", "dasha_analysis"],
    "spouse": ["spouse_nature", "saturn_7th_specific"],
    "yogas": ["yogas"],
    "career": ["career_10th", "leo_ascendant"],
    "health": ["health", "leo_ascendant"],
    "wealth": ["wealth_2nd_11th", "yogas", "leo_ascendant"],
    "spirituality": ["spirituality", "leo_ascendant"],
    "all": list(SEARCH_PATTERNS.keys()),
}


def load_extracted_books(extraction_dir: Path) -> List[Dict]:
    """Load all extracted book JSON files."""
    books = []
    json_files = sorted(extraction_dir.glob("*_extraction.json"))
    
    for jf in json_files:
        try:
            with open(jf, 'r', encoding='utf-8') as f:
                data = json.load(f)
                books.append(data)
        except Exception as e:
            print(f"  Warning: Could not load {jf.name}: {e}")
    
    return books


def search_book_content(book: Dict, patterns: List[str], context_lines: int = 3) -> List[Dict]:
    """Search a book's full text for pattern matches with surrounding context."""
    matches = []
    pages = book.get('full_text_pages', [])
    
    for page in pages:
        text = page.get('text', '')
        page_num = page.get('page', 0)
        lines = text.split('\n')
        
        for pat in patterns:
            try:
                for m in re.finditer(pat, text):
                    match_start = m.start()
                    char_pos = 0
                    match_line_idx = 0
                    for i, line in enumerate(lines):
                        if char_pos + len(line) >= match_start:
                            match_line_idx = i
                            break
                        char_pos += len(line) + 1
                    
                    start_idx = max(0, match_line_idx - context_lines)
                    end_idx = min(len(lines), match_line_idx + context_lines + 1)
                    context = '\n'.join(lines[start_idx:end_idx]).strip()
                    
                    if len(context) > 20:
                        matches.append({
                            'book': book.get('book_name', 'Unknown'),
                            'page': page_num,
                            'matched_text': m.group(0),
                            'context': context[:800],
                            'pattern': pat,
                        })
            except re.error:
                continue
    
    seen = set()
    unique = []
    for m in matches:
        key = (m['book'], m['page'], m['context'][:100])
        if key not in seen:
            seen.add(key)
            unique.append(m)
    
    return unique


def generate_report(all_results: Dict, output_path: Path, topic: str, verbose: bool):
    """Generate markdown report from cross-reference results."""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# CROSS-REFERENCE REPORT: Book Content vs Akshit's Chart\n\n")
        f.write(f"**Generated**: Auto-generated by cross_reference_chart.py\n")
        f.write(f"**Topic Filter**: {topic}\n")
        f.write(f"**Chart**: Akshit Sethi (Dec 26, 1994, 22:50, Kanpur, Leo Asc)\n\n")
        f.write("---\n\n")
        
        f.write("## Chart Quick Reference\n\n")
        f.write("| Planet | Sign | House | Nakshatra | Dignity |\n")
        f.write("|--------|------|-------|-----------|--------|\n")
        for planet, data in CHART_DATA['planets_d1'].items():
            f.write(f"| {planet} | {data['sign']} | {data['house']} | {data['nakshatra']} | {data['dignity']} |\n")
        f.write("\n**Key Features**: Leo Asc, Saturn own sign in 7th, Venus own sign in 3rd, ")
        f.write("Jupiter in 4th (Scorpio), Mars in 1st, Mercury combust in 5th\n\n")
        f.write("---\n\n")
        
        total_matches = 0
        
        f.write("## RESULTS BY CATEGORY\n\n")
        
        for category, data in sorted(all_results.items(), key=lambda x: len(x[1]['matches']), reverse=True):
            matches = data['matches']
            desc = data['description']
            total_matches += len(matches)
            
            f.write(f"### {category.replace('_', ' ').title()} ({len(matches)} matches)\n")
            f.write(f"*{desc}*\n\n")
            
            if not matches:
                f.write("No matches found in extracted books.\n\n")
                continue
            
            books_with_matches = defaultdict(list)
            for m in matches:
                books_with_matches[m['book']].append(m)
            
            f.write(f"**Found in {len(books_with_matches)} books:**\n\n")
            
            for book_name, book_matches in sorted(books_with_matches.items(), key=lambda x: len(x[1]), reverse=True):
                f.write(f"#### From: {book_name} ({len(book_matches)} references)\n\n")
                
                display_limit = 20 if verbose else 12
                for i, m in enumerate(book_matches[:display_limit]):
                    f.write(f"**Page {m['page']}** (matched: \"{m['matched_text']}\")\n")
                    f.write(f"```\n{m['context']}\n```\n\n")
                
                if len(book_matches) > display_limit:
                    f.write(f"*... and {len(book_matches) - display_limit} more references in this book*\n\n")
            
            f.write("---\n\n")
        
        f.write(f"## SUMMARY\n\n")
        f.write(f"**Total cross-references found**: {total_matches}\n\n")
        
        f.write("### Category Breakdown\n\n")
        f.write("| Category | Matches | Books |\n")
        f.write("|----------|---------|-------|\n")
        for category, data in sorted(all_results.items(), key=lambda x: len(x[1]['matches']), reverse=True):
            matches = data['matches']
            books = len(set(m['book'] for m in matches))
            f.write(f"| {category.replace('_', ' ').title()} | {len(matches)} | {books} |\n")
        
        f.write("\n### How to Use This Report\n\n")
        f.write("1. **High match count** = well-supported prediction (classical backing)\n")
        f.write("2. **Low match count** = prediction needs more verification or books need extraction\n")
        f.write("3. **Page references** let you go back to the original PDF for full context\n")
        f.write("4. **Multiple books agreeing** = highest confidence prediction\n")
        f.write("5. Re-run after extracting more books to increase coverage\n\n")
        
        f.write("### Predictions Ranked by Classical Support\n\n")
        
        marriage_matches = sum(len(all_results.get(cat, {}).get('matches', []))
                              for cat in ["marriage_general", "saturn_7th_specific", "marriage_timing", "spouse_nature"])
        navamsa_matches = len(all_results.get("navamsa_marriage", {}).get('matches', []))
        yoga_matches = len(all_results.get("yogas", {}).get('matches', []))
        jaimini_matches = len(all_results.get("jaimini", {}).get('matches', []))
        
        rankings = [
            ("Marriage timing & quality", marriage_matches),
            ("Navamsa marriage rules", navamsa_matches),
            ("Yoga combinations", yoga_matches),
            ("Jaimini techniques", jaimini_matches),
        ]
        
        f.write("| Prediction Area | Classical References | Support Level |\n")
        f.write("|----------------|--------------------|--------------|\n")
        for area, count in sorted(rankings, key=lambda x: x[1], reverse=True):
            level = "STRONG" if count > 20 else "MODERATE" if count > 10 else "NEEDS MORE DATA" if count > 0 else "NO DATA"
            f.write(f"| {area} | {count} | {level} |\n")
        
        f.write("\n---\n")
        f.write("*Run `python3 cross_reference_chart.py --topic all --verbose` for full output*\n")
    
    print(f"\nReport saved to: {output_path}")
    print(f"Total cross-references: {total_matches}")


def main():
    parser = argparse.ArgumentParser(description="Cross-reference extracted books against Akshit's chart")
    parser.add_argument('--topic', type=str, default='all',
                        choices=list(TOPIC_FILTER_MAP.keys()),
                        help='Topic to search for (default: all)')
    parser.add_argument('--verbose', action='store_true',
                        help='Show more matches per book')
    parser.add_argument('--extraction-dir', type=str, default=None,
                        help='Path to extracted_content directory')
    parser.add_argument('--output', type=str, default=None,
                        help='Output report path')
    
    args = parser.parse_args()
    
    script_dir = Path(__file__).parent.resolve()
    astro_root = script_dir.parent
    
    if args.extraction_dir:
        extraction_dir = Path(args.extraction_dir)
    else:
        candidates = [
            astro_root / "16-EXTRACTED-BOOKS" / "extracted_content",
            astro_root / "15-EXTRACTION-SYSTEM" / "extracted_content",
        ]
        extraction_dir = None
        for c in candidates:
            if c.exists() and list(c.glob("*_extraction.json")):
                extraction_dir = c
                break
        
        if extraction_dir is None:
            print("ERROR: No extracted content found. Run the extraction pipeline first:")
            print("  cd 15-EXTRACTION-SYSTEM && python3 run_extraction.py")
            return
    
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = astro_root / "01-AKSHIT-ANALYSIS" / f"CROSS_REFERENCE_REPORT_{args.topic.upper()}.md"
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    print("=" * 70)
    print("CROSS-REFERENCE: Extracted Books vs Akshit's Chart".center(70))
    print("=" * 70)
    print(f"\nExtraction dir: {extraction_dir}")
    print(f"Topic filter:   {args.topic}")
    print(f"Output:         {output_path}\n")
    
    print("Loading extracted books...")
    books = load_extracted_books(extraction_dir)
    print(f"Loaded {len(books)} books\n")
    
    if not books:
        print("ERROR: No books loaded. Check extraction directory.")
        return
    
    categories_to_search = TOPIC_FILTER_MAP.get(args.topic, list(SEARCH_PATTERNS.keys()))
    
    all_results = {}
    
    for category in categories_to_search:
        config = SEARCH_PATTERNS[category]
        print(f"Searching: {category} ({config['description']})...")
        
        category_matches = []
        for book in books:
            matches = search_book_content(book, config['patterns'])
            category_matches.extend(matches)
        
        all_results[category] = {
            'description': config['description'],
            'matches': category_matches
        }
        
        book_count = len(set(m['book'] for m in category_matches))
        print(f"  Found {len(category_matches)} references in {book_count} books")
    
    print(f"\nGenerating report...")
    generate_report(all_results, output_path, args.topic, args.verbose)
    
    print("\n" + "=" * 70)
    print("Cross-reference complete!".center(70))
    print("=" * 70)


if __name__ == "__main__":
    main()
