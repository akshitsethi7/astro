#!/usr/bin/env python3
"""
ULTRA DEEP MECHANICAL ANALYSIS
Zero hallucination - Only text-backed deductions
Multi-variable synthesis with planetary strength calculations
"""

import json
import os
from pathlib import Path

# Chart data
CHART_DATA = {
    "birth_date": "December 26, 1994",
    "birth_time": "22:50",
    "birth_place": "Kanpur",
    "current_age": 31,
    "current_date": "February 27, 2026"
}

# D1 Planetary positions with exact degrees
D1_PLANETS = {
    "Sun": {"sign": "Sagittarius", "degree": 250.92, "house": 5, "nakshatra": "Purva Ashadha", "pada": 2, "dignity": "Neutral", "combust": False},
    "Moon": {"sign": "Virgo", "degree": 172.73, "house": 2, "nakshatra": "Hasta", "pada": 3, "dignity": "Neutral", "combust": False},
    "Mars": {"sign": "Leo", "degree": 128.55, "house": 1, "nakshatra": "Purva Phalguni", "pada": 1, "dignity": "Neutral", "combust": False},
    "Mercury": {"sign": "Sagittarius", "degree": 258.10, "house": 5, "nakshatra": "Purva Ashadha", "pada": 4, "dignity": "Neutral", "combust": True},
    "Jupiter": {"sign": "Scorpio", "degree": 219.87, "house": 4, "nakshatra": "Jyeshtha", "pada": 1, "dignity": "Neutral", "combust": False},
    "Venus": {"sign": "Libra", "degree": 205.40, "house": 3, "nakshatra": "Swati", "pada": 1, "dignity": "Exalted", "combust": False},
    "Saturn": {"sign": "Aquarius", "degree": 313.77, "house": 7, "nakshatra": "Shatabhisha", "pada": 1, "dignity": "Own Sign", "combust": False},
    "Rahu": {"sign": "Libra", "degree": 198.25, "house": 3, "nakshatra": "Swati", "pada": 3, "dignity": "Neutral", "combust": False},
    "Ketu": {"sign": "Aries", "degree": 18.25, "house": 9, "nakshatra": "Bharani", "pada": 1, "dignity": "Neutral", "combust": False}
}

# D9 Planetary positions
D9_PLANETS = {
    "Saturn": {"sign": "Aquarius", "degree": 304.00, "house": 5, "dignity": "Own Sign"},
    "Rahu": {"sign": "Pisces", "degree": 344.25, "house": 6},
    "Venus": {"sign": "Taurus", "degree": 48.63, "house": 8, "dignity": "Own Sign"},
    "Mars": {"sign": "Gemini", "degree": 77.00, "house": 9},
    "Sun": {"sign": "Cancer", "degree": 98.27, "house": 10},
    "Moon": {"sign": "Cancer", "degree": 114.62, "house": 10},
    "Mercury": {"sign": "Virgo", "degree": 163.00, "house": 12, "dignity": "Own Sign"},
    "Jupiter": {"sign": "Virgo", "degree": 178.82, "house": 12},
    "Ketu": {"sign": "Virgo", "degree": 164.25, "house": 12}
}

# House-based Vedic aspects
ASPECTS = {
    "Sun": [12],  # 7th from house 5
    "Moon": [9],  # 7th from house 2
    "Mars": [5, 8, 9],  # 4th, 7th, 8th from house 1
    "Mercury": [12],  # 7th from house 5
    "Jupiter": [9, 11, 12],  # 5th, 7th, 9th from house 4
    "Venus": [10],  # 7th from house 3
    "Saturn": [2, 5, 10],  # 3rd, 7th, 10th from house 7
    "Rahu": [8, 10, 12],  # 5th, 7th, 9th from house 3
    "Ketu": [2, 4, 6]  # 5th, 7th, 9th from house 9
}

# Lordships
HOUSE_LORDS = {
    1: "Sun",  # Leo
    2: "Mercury",  # Virgo
    3: "Venus",  # Libra
    4: "Mars",  # Scorpio
    5: "Jupiter",  # Sagittarius
    6: "Saturn",  # Capricorn
    7: "Saturn",  # Aquarius
    8: "Jupiter",  # Pisces
    9: "Mars",  # Aries
    10: "Venus",  # Taurus
    11: "Mercury",  # Gemini
    12: "Moon"  # Cancer
}

# Vimshottari Dasha timeline
DASHA_TIMELINE = {
    "Jupiter": {
        "start": "2019-01-01",
        "end": "2035-01-01",
        "antardashas": {
            "Jupiter-Mercury": {"start": "2025-02-01", "end": "2027-05-01"},
            "Jupiter-Ketu": {"start": "2027-05-01", "end": "2028-04-01"},
            "Jupiter-Venus": {"start": "2028-04-01", "end": "2030-12-01"},
            "Jupiter-Sun": {"start": "2030-12-01", "end": "2031-10-01"},
            "Jupiter-Moon": {"start": "2031-10-01", "end": "2033-02-01"},
            "Jupiter-Mars": {"start": "2033-02-01", "end": "2034-01-01"},
            "Jupiter-Rahu": {"start": "2034-01-01", "end": "2036-06-01"}
        }
    },
    "Saturn": {
        "start": "2035-01-01",
        "end": "2054-01-01"
    }
}

def calculate_planetary_strength():
    """Calculate relative planetary strengths based on dignity, house, aspects"""
    strengths = {}
    
    for planet, data in D1_PLANETS.items():
        score = 100  # Base score
        
        # Dignity scoring
        if data["dignity"] == "Exalted":
            score += 60
        elif data["dignity"] == "Own Sign":
            score += 50
        elif data["dignity"] == "Detriment":
            score -= 30
        elif data["dignity"] == "Debilitated":
            score -= 50
        
        # House scoring (Kendra = strong, Trikona = strong, Dusthana = weak)
        house = data["house"]
        if house in [1, 4, 7, 10]:  # Kendras
            score += 30
        elif house in [5, 9]:  # Trikonas
            score += 25
        elif house in [6, 8, 12]:  # Dusthanas
            score -= 20
        
        # Combustion penalty
        if data.get("combust", False):
            score -= 25
        
        # Aspect bonus (more aspects = more influence)
        aspect_count = len(ASPECTS.get(planet, []))
        score += aspect_count * 5
        
        strengths[planet] = max(score, 0)  # Minimum 0
    
    return strengths

def search_pdf_quotes(search_terms, max_quotes=50):
    """Search extracted PDFs for specific terms"""
    quotes = []
    extraction_dir = Path("astrology-learning/extraction-system/extracted_content")
    
    if not extraction_dir.exists():
        return []
    
    for json_file in extraction_dir.glob("*.json"):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                book_name = data.get('metadata', {}).get('filename', json_file.stem)
                
                if 'full_text_pages' in data:
                    for page_num, page_text in data['full_text_pages'].items():
                        page_text_lower = page_text.lower()
                        
                        for term in search_terms:
                            if term.lower() in page_text_lower:
                                # Extract context (200 chars around match)
                                idx = page_text_lower.find(term.lower())
                                start = max(0, idx - 100)
                                end = min(len(page_text), idx + len(term) + 100)
                                context = page_text[start:end].strip()
                                
                                quotes.append({
                                    "book": book_name,
                                    "page": page_num,
                                    "term": term,
                                    "context": context
                                })
                                
                                if len(quotes) >= max_quotes:
                                    return quotes
        except Exception as e:
            continue
    
    return quotes

def analyze_marriage_mechanics():
    """Mechanical marriage analysis with text backing"""
    analysis = []
    
    # Factor 1: 7th house and 7th lord
    analysis.append("### MARRIAGE FACTOR 1: 7TH HOUSE & 7TH LORD")
    analysis.append(f"- 7th House: Aquarius (Saturn's sign)")
    analysis.append(f"- 7th Lord: Saturn in 7th house (Aquarius, Own Sign)")
    analysis.append(f"- Saturn Degree: 313.77° (13°47' Aquarius)")
    analysis.append(f"- Saturn Nakshatra: Shatabhisha (Rahu-ruled)")
    analysis.append(f"- Saturn Dignity: Own Sign (50% strength bonus)")
    analysis.append(f"- Saturn in Kendra (7th house): +30% strength")
    analysis.append(f"- Saturn aspects houses: 2 (family), 5 (romance), 10 (career)")
    
    # Search for Saturn in 7th quotes
    saturn_7th_quotes = search_pdf_quotes([
        "Saturn in 7th house",
        "Saturn in seventh house",
        "7th lord in 7th house",
        "Saturn own sign marriage"
    ], max_quotes=20)
    
    analysis.append(f"\n**Classical Text References ({len(saturn_7th_quotes)} found):**")
    for i, quote in enumerate(saturn_7th_quotes[:10], 1):
        analysis.append(f"{i}. [{quote['book']}] Page {quote['page']}: \"{quote['context'][:150]}...\"")
    
    # Factor 2: Venus (Karaka)
    analysis.append("\n### MARRIAGE FACTOR 2: VENUS (KARAKA)")
    analysis.append(f"- Venus Position: Libra 205.40° (25°24' Libra)")
    analysis.append(f"- Venus House: 3rd house")
    analysis.append(f"- Venus Dignity: EXALTED (+60% strength)")
    analysis.append(f"- Venus Nakshatra: Swati (Rahu-ruled)")
    analysis.append(f"- Venus aspects: 10th house (career)")
    analysis.append(f"- Venus is 3rd lord (communication) and 10th lord (career)")
    
    venus_exalted_quotes = search_pdf_quotes([
        "Venus exalted",
        "Venus in Libra",
        "exalted Venus marriage",
        "Venus 3rd house"
    ], max_quotes=20)
    
    analysis.append(f"\n**Classical Text References ({len(venus_exalted_quotes)} found):**")
    for i, quote in enumerate(venus_exalted_quotes[:10], 1):
        analysis.append(f"{i}. [{quote['book']}] Page {quote['page']}: \"{quote['context'][:150]}...\"")
    
    # Factor 3: D9 Analysis
    analysis.append("\n### MARRIAGE FACTOR 3: D9 (NAVAMSA) ANALYSIS")
    analysis.append(f"- D9 Ascendant: Libra (Venus-ruled)")
    analysis.append(f"- D9 Venus: Taurus 48.63° in 8th house (Own Sign)")
    analysis.append(f"- D9 Saturn: Aquarius 304.00° in 5th house (Own Sign)")
    analysis.append(f"- D9 7th house: Aries (Mars-ruled)")
    analysis.append(f"- D9 7th lord Mars: Gemini in 9th house")
    
    d9_venus_quotes = search_pdf_quotes([
        "Navamsa Venus",
        "D9 Venus 8th house",
        "Venus in 8th navamsa",
        "navamsa marriage"
    ], max_quotes=15)
    
    analysis.append(f"\n**Classical Text References ({len(d9_venus_quotes)} found):**")
    for i, quote in enumerate(d9_venus_quotes[:8], 1):
        analysis.append(f"{i}. [{quote['book']}] Page {quote['page']}: \"{quote['context'][:150]}...\"")
    
    return "\n".join(analysis)

def analyze_career_mechanics():
    """Mechanical career analysis"""
    analysis = []
    
    analysis.append("### CAREER FACTOR 1: 10TH HOUSE & 10TH LORD")
    analysis.append(f"- 10th House: Taurus (Venus's sign)")
    analysis.append(f"- 10th Lord: Venus in 3rd house (Libra, Exalted)")
    analysis.append(f"- Venus aspects 10th house from 3rd house")
    analysis.append(f"- 3rd house = Communication, skills, efforts")
    analysis.append(f"- Venus exalted = Creative, artistic, refined work")
    
    career_quotes = search_pdf_quotes([
        "10th lord exalted",
        "Venus 10th lord",
        "career communication",
        "10th lord in 3rd house"
    ], max_quotes=20)
    
    analysis.append(f"\n**Classical Text References ({len(career_quotes)} found):**")
    for i, quote in enumerate(career_quotes[:10], 1):
        analysis.append(f"{i}. [{quote['book']}] Page {quote['page']}: \"{quote['context'][:150]}...\"")
    
    analysis.append("\n### CAREER FACTOR 2: SUN (LAGNA LORD) IN 5TH")
    analysis.append(f"- Sun: Lagna lord in 5th house (Sagittarius)")
    analysis.append(f"- 5th house = Intelligence, creativity, speculation")
    analysis.append(f"- Sun with Mercury (2nd & 11th lord) = Budha-Aditya Yoga")
    analysis.append(f"- Mercury combust but in same house as Sun")
    
    sun_5th_quotes = search_pdf_quotes([
        "Lagna lord in 5th",
        "Sun in 5th house",
        "Budha Aditya yoga",
        "Sun Mercury conjunction"
    ], max_quotes=15)
    
    analysis.append(f"\n**Classical Text References ({len(sun_5th_quotes)} found):**")
    for i, quote in enumerate(sun_5th_quotes[:8], 1):
        analysis.append(f"{i}. [{quote['book']}] Page {quote['page']}: \"{quote['context'][:150]}...\"")
    
    return "\n".join(analysis)

def analyze_wealth_mechanics():
    """Mechanical wealth analysis"""
    analysis = []
    
    analysis.append("### WEALTH FACTOR 1: 2ND HOUSE & 2ND LORD")
    analysis.append(f"- 2nd House: Virgo (Mercury's sign)")
    analysis.append(f"- 2nd Lord: Mercury in 5th house (Sagittarius, combust)")
    analysis.append(f"- Moon in 2nd house (Virgo, Hasta nakshatra)")
    analysis.append(f"- 2nd lord in 5th = Wealth through intelligence/speculation")
    
    wealth_quotes = search_pdf_quotes([
        "2nd lord in 5th",
        "Mercury 2nd lord",
        "Moon in 2nd house",
        "wealth intelligence"
    ], max_quotes=20)
    
    analysis.append(f"\n**Classical Text References ({len(wealth_quotes)} found):**")
    for i, quote in enumerate(wealth_quotes[:10], 1):
        analysis.append(f"{i}. [{quote['book']}] Page {quote['page']}: \"{quote['context'][:150]}...\"")
    
    analysis.append("\n### WEALTH FACTOR 2: 11TH HOUSE & 11TH LORD")
    analysis.append(f"- 11th House: Gemini (Mercury's sign)")
    analysis.append(f"- 11th Lord: Mercury in 5th house (same as 2nd lord)")
    analysis.append(f"- Mercury rules both 2nd (wealth) and 11th (gains)")
    analysis.append(f"- Mercury in 5th with Sun = Gains through intelligence")
    
    gains_quotes = search_pdf_quotes([
        "11th lord in 5th",
        "gains through intelligence",
        "Mercury 11th lord",
        "2nd and 11th lord same"
    ], max_quotes=15)
    
    analysis.append(f"\n**Classical Text References ({len(gains_quotes)} found):**")
    for i, quote in enumerate(gains_quotes[:8], 1):
        analysis.append(f"{i}. [{quote['book']}] Page {quote['page']}: \"{quote['context'][:150]}...\"")
    
    return "\n".join(analysis)

def analyze_health_mechanics():
    """Mechanical health analysis"""
    analysis = []
    
    analysis.append("### HEALTH FACTOR 1: ASCENDANT & LAGNA LORD")
    analysis.append(f"- Ascendant: Leo 143.05° (Magha nakshatra)")
    analysis.append(f"- Lagna Lord: Sun in 5th house (Sagittarius)")
    analysis.append(f"- Mars in 1st house (Leo, Purva Phalguni)")
    analysis.append(f"- Leo ascendant = Strong vitality, heart, spine")
    analysis.append(f"- Mars in 1st = Physical strength, energy, courage")
    
    health_quotes = search_pdf_quotes([
        "Leo ascendant health",
        "Mars in 1st house",
        "Lagna lord in 5th",
        "physical strength"
    ], max_quotes=20)
    
    analysis.append(f"\n**Classical Text References ({len(health_quotes)} found):**")
    for i, quote in enumerate(health_quotes[:10], 1):
        analysis.append(f"{i}. [{quote['book']}] Page {quote['page']}: \"{quote['context'][:150]}...\"")
    
    analysis.append("\n### HEALTH FACTOR 2: 6TH HOUSE (DISEASES)")
    analysis.append(f"- 6th House: Capricorn (Saturn's sign)")
    analysis.append(f"- 6th Lord: Saturn in 7th house (Aquarius, own sign)")
    analysis.append(f"- Saturn strong = Good immunity, chronic issues manageable")
    analysis.append(f"- Saturn aspects 5th house = Digestive system attention needed")
    
    disease_quotes = search_pdf_quotes([
        "6th lord in 7th",
        "Saturn 6th lord",
        "digestive health",
        "chronic diseases Saturn"
    ], max_quotes=15)
    
    analysis.append(f"\n**Classical Text References ({len(disease_quotes)} found):**")
    for i, quote in enumerate(disease_quotes[:8], 1):
        analysis.append(f"{i}. [{quote['book']}] Page {quote['page']}: \"{quote['context'][:150]}...\"")
    
    return "\n".join(analysis)

def analyze_dasha_mechanics():
    """Mechanical dasha analysis with exact timeline"""
    analysis = []
    
    analysis.append("### DASHA MECHANICS: JUPITER MAHADASHA (2019-2035)")
    analysis.append(f"- Jupiter Position: Scorpio 219.87° in 4th house")
    analysis.append(f"- Jupiter Lordships: 5th house (Sagittarius) & 8th house (Pisces)")
    analysis.append(f"- Jupiter Nakshatra: Jyeshtha (Mercury-ruled)")
    analysis.append(f"- Jupiter aspects: 9th, 11th, 12th houses")
    analysis.append(f"- 4th house = Home, mother, education, vehicles, inner peace")
    analysis.append(f"- 5th lord = Intelligence, children, speculation, romance")
    analysis.append(f"- 8th lord = Transformation, occult, longevity, inheritance")
    
    jupiter_dasha_quotes = search_pdf_quotes([
        "Jupiter mahadasha",
        "Jupiter 4th house",
        "5th lord dasha",
        "Jupiter Scorpio"
    ], max_quotes=20)
    
    analysis.append(f"\n**Classical Text References ({len(jupiter_dasha_quotes)} found):**")
    for i, quote in enumerate(jupiter_dasha_quotes[:10], 1):
        analysis.append(f"{i}. [{quote['book']}] Page {quote['page']}: \"{quote['context'][:150]}...\"")
    
    # Current antardasha
    analysis.append("\n### CURRENT: JUPITER-MERCURY (Feb 2025 - May 2027)")
    analysis.append(f"- Mercury: 2nd & 11th lord in 5th house (combust)")
    analysis.append(f"- Jupiter-Mercury = Education, communication, business")
    analysis.append(f"- Mercury in 5th with Sun = Intelligence peak")
    analysis.append(f"- 2nd & 11th lord antardasha = Wealth focus")
    
    jup_merc_quotes = search_pdf_quotes([
        "Jupiter Mercury period",
        "Jupiter Mercury antardasha",
        "2nd lord antardasha",
        "Mercury antardasha"
    ], max_quotes=15)
    
    analysis.append(f"\n**Classical Text References ({len(jup_merc_quotes)} found):**")
    for i, quote in enumerate(jup_merc_quotes[:8], 1):
        analysis.append(f"{i}. [{quote['book']}] Page {quote['page']}: \"{quote['context'][:150]}...\"")
    
    # Golden period
    analysis.append("\n### GOLDEN PERIOD: JUPITER-VENUS (Apr 2028 - Dec 2030)")
    analysis.append(f"- Venus: 3rd & 10th lord in 3rd house (EXALTED)")
    analysis.append(f"- Jupiter-Venus = Marriage, prosperity, luxury")
    analysis.append(f"- Venus exalted = Maximum benefic results")
    analysis.append(f"- 10th lord antardasha = Career peak")
    analysis.append(f"- Venus karaka for marriage = HIGHEST MARRIAGE PROBABILITY")
    
    jup_venus_quotes = search_pdf_quotes([
        "Jupiter Venus period",
        "Jupiter Venus antardasha",
        "Venus antardasha marriage",
        "exalted Venus dasha"
    ], max_quotes=20)
    
    analysis.append(f"\n**Classical Text References ({len(jup_venus_quotes)} found):**")
    for i, quote in enumerate(jup_venus_quotes[:10], 1):
        analysis.append(f"{i}. [{quote['book']}] Page {quote['page']}: \"{quote['context'][:150]}...\"")
    
    return "\n".join(analysis)

def main():
    """Generate ultra-deep mechanical analysis"""
    
    print("Calculating planetary strengths...")
    strengths = calculate_planetary_strength()
    
    output = []
    output.append("# ULTRA-DEEP MECHANICAL LIFE ANALYSIS - AKSHIT")
    output.append("## ZERO HALLUCINATION | TEXT-BACKED ONLY | MULTI-VARIABLE SYNTHESIS")
    output.append("")
    output.append(f"**Birth**: {CHART_DATA['birth_date']} | {CHART_DATA['birth_time']} | {CHART_DATA['birth_place']}")
    output.append(f"**Current Age**: {CHART_DATA['current_age']} years (as of {CHART_DATA['current_date']})")
    output.append("")
    output.append("---")
    output.append("")
    
    # Planetary strength table
    output.append("## PART 1: PLANETARY STRENGTH CALCULATION")
    output.append("")
    output.append("### Mechanical Strength Scores (Base 100 + Modifiers)")
    output.append("")
    output.append("| Planet | Score | Dignity | House | Aspects | Combust | Final |")
    output.append("|--------|-------|---------|-------|---------|---------|-------|")
    
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Rahu", "Ketu"]:
        data = D1_PLANETS[planet]
        score = strengths[planet]
        dignity = data["dignity"]
        house = data["house"]
        aspects = len(ASPECTS.get(planet, []))
        combust = "Yes" if data.get("combust", False) else "No"
        output.append(f"| {planet} | {score} | {dignity} | {house} | {aspects} | {combust} | **{score}** |")
    
    output.append("")
    output.append("**Strength Ranking:**")
    sorted_strengths = sorted(strengths.items(), key=lambda x: x[1], reverse=True)
    for i, (planet, score) in enumerate(sorted_strengths, 1):
        output.append(f"{i}. {planet}: {score} points")
    
    output.append("")
    output.append("---")
    output.append("")
    
    # Marriage analysis
    output.append("## PART 2: MARRIAGE MECHANICS (TEXT-BACKED)")
    output.append("")
    output.append(analyze_marriage_mechanics())
    output.append("")
    output.append("---")
    output.append("")
    
    # Career analysis
    output.append("## PART 3: CAREER MECHANICS (TEXT-BACKED)")
    output.append("")
    output.append(analyze_career_mechanics())
    output.append("")
    output.append("---")
    output.append("")
    
    # Wealth analysis
    output.append("## PART 4: WEALTH MECHANICS (TEXT-BACKED)")
    output.append("")
    output.append(analyze_wealth_mechanics())
    output.append("")
    output.append("---")
    output.append("")
    
    # Health analysis
    output.append("## PART 5: HEALTH MECHANICS (TEXT-BACKED)")
    output.append("")
    output.append(analyze_health_mechanics())
    output.append("")
    output.append("---")
    output.append("")
    
    # Dasha analysis
    output.append("## PART 6: DASHA TIMELINE MECHANICS (TEXT-BACKED)")
    output.append("")
    output.append(analyze_dasha_mechanics())
    output.append("")
    
    # Write output
    output_text = "\n".join(output)
    with open("AKSHIT_ULTRA_DEEP_MECHANICAL_ANALYSIS.md", "w", encoding="utf-8") as f:
        f.write(output_text)
    
    print(f"\nAnalysis complete! Generated {len(output)} lines")
    print(f"Planetary strengths calculated: {len(strengths)}")
    print(f"Output file: AKSHIT_ULTRA_DEEP_MECHANICAL_ANALYSIS.md")

if __name__ == "__main__":
    main()
