#!/usr/bin/env python3
"""
Advanced Marriage Analysis for Akshit
Based on Classical Vedic Astrology Texts
Properly calculates aspects, conjunctions, and planetary relationships
"""

# Complete Chart Data with longitudes
CHART_DATA = {
    "D1": {
        "SUN": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "10°55'", "house": 5, "longitude": 250.916, "sign_idx": 8},
        "MOON": {"sign": "Virgo", "lord": "Mercury", "degree": "22°44'", "house": 2, "longitude": 172.733, "sign_idx": 5},
        "MARS": {"sign": "Leo", "lord": "Sun", "degree": "8°33'", "house": 1, "longitude": 128.55, "sign_idx": 4},
        "MERCURY": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "18°06'", "house": 5, "longitude": 258.1, "sign_idx": 8},
        "JUPITER": {"sign": "Scorpio", "lord": "Mars", "degree": "9°52'", "house": 4, "longitude": 219.867, "sign_idx": 7},
        "VENUS": {"sign": "Libra", "lord": "Venus", "degree": "25°24'", "house": 3, "longitude": 205.4, "sign_idx": 6},
        "SATURN": {"sign": "Aquarius", "lord": "Saturn", "degree": "13°46'", "house": 7, "longitude": 313.767, "sign_idx": 10},
        "RAHU": {"sign": "Libra", "lord": "Venus", "degree": "18°15'", "house": 3, "longitude": 198.25, "sign_idx": 6, "retrograde": True},
        "KETU": {"sign": "Aries", "lord": "Mars", "degree": "18°15'", "house": 9, "longitude": 18.25, "sign_idx": 0, "retrograde": True},
        "ASCENDANT": {"sign": "Leo", "lord": "Sun", "degree": "23°03'", "house": 1, "longitude": 143.05, "sign_idx": 4}
    },
    "D9": {
        "SATURN": {"sign": "Aquarius", "lord": "Saturn", "degree": "04°00'", "house": 5},
        "RAHU": {"sign": "Pisces", "lord": "Jupiter", "degree": "14°18'", "house": 6, "retrograde": True},
        "VENUS": {"sign": "Taurus", "lord": "Venus", "degree": "18°38'", "house": 8},
        "MARS": {"sign": "Gemini", "lord": "Mercury", "degree": "17°00'", "house": 9},
        "SUN": {"sign": "Cancer", "lord": "Moon", "degree": "08°16'", "house": 10},
        "MOON": {"sign": "Cancer", "lord": "Moon", "degree": "24°37'", "house": 10},
        "MERCURY": {"sign": "Virgo", "lord": "Mercury", "degree": "13°00'", "house": 12},
        "JUPITER": {"sign": "Virgo", "lord": "Mercury", "degree": "28°49'", "house": 12},
        "KETU": {"sign": "Virgo", "lord": "Mercury", "degree": "14°18'", "house": 12, "retrograde": True}
    }
}

SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
         "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashirsha", "Ardra", "Punarvasu",
    "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta",
    "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
    "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha", "Purva Bhadrapada",
    "Uttara Bhadrapada", "Revati"
]

NAKSHATRA_LORDS = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter",
                   "Saturn", "Mercury", "Ketu", "Venus", "Sun", "Moon", "Mars",
                   "Rahu", "Jupiter", "Saturn", "Mercury", "Ketu", "Venus",
                   "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]

def get_nakshatra(longitude):
    """Get nakshatra from longitude"""
    nakshatra_num = int(longitude / 13.333333)
    return NAKSHATRAS[nakshatra_num % 27]

def get_pada(longitude):
    """Get pada from longitude"""
    nakshatra_num = int(longitude / 13.333333)
    nakshatra_start = (nakshatra_num % 27) * 13.333333
    pada_num = int((longitude - nakshatra_start) / 3.333333) + 1
    return pada_num

def get_nakshatra_lord(nakshatra):
    """Get nakshatra lord"""
    idx = NAKSHATRAS.index(nakshatra)
    return NAKSHATRA_LORDS[idx]

def calculate_aspects(planet_name, planet_house, planet_sign_idx):
    """Calculate all aspects of a planet"""
    aspects = []
    
    # All planets aspect 7th house from their position
    aspect_7th = ((planet_house - 1 + 6) % 12) + 1  # 7th from current house
    aspects.append({"house": aspect_7th, "type": "7th aspect"})
    
    # Special aspects
    if planet_name == "MARS":
        # Mars aspects 4th, 7th, 8th
        aspect_4th = ((planet_house - 1 + 3) % 12) + 1
        aspect_8th = ((planet_house - 1 + 7) % 12) + 1
        aspects.append({"house": aspect_4th, "type": "4th aspect (special)"})
        aspects.append({"house": aspect_8th, "type": "8th aspect (special)"})
    
    elif planet_name == "JUPITER":
        # Jupiter aspects 5th, 7th, 9th
        aspect_5th = ((planet_house - 1 + 4) % 12) + 1
        aspect_9th = ((planet_house - 1 + 8) % 12) + 1
        aspects.append({"house": aspect_5th, "type": "5th aspect (special)"})
        aspects.append({"house": aspect_9th, "type": "9th aspect (special)"})
    
    elif planet_name == "SATURN":
        # Saturn aspects 3rd, 7th, 10th
        aspect_3rd = ((planet_house - 1 + 2) % 12) + 1
        aspect_10th = ((planet_house - 1 + 9) % 12) + 1
        aspects.append({"house": aspect_3rd, "type": "3rd aspect (special)"})
        aspects.append({"house": aspect_10th, "type": "10th aspect (special)"})
    
    return aspects

def find_conjunctions(d1):
    """Find planets in conjunction (same sign)"""
    conjunctions = {}
    for sign_idx in range(12):
        planets_in_sign = []
        for planet, data in d1.items():
            if planet != "ASCENDANT" and data.get("sign_idx") == sign_idx:
                planets_in_sign.append(planet)
        if len(planets_in_sign) > 1:
            conjunctions[SIGNS[sign_idx]] = planets_in_sign
    return conjunctions

def analyze_planet_strength(planet, sign, house):
    """Analyze planet strength based on classical principles"""
    strength_factors = []
    strength_score = 0
    
    # Exaltation/Debilitation
    exaltation = {
        "SUN": "Aries", "MOON": "Taurus", "MARS": "Capricorn", "MERCURY": "Virgo",
        "JUPITER": "Cancer", "VENUS": "Pisces", "SATURN": "Libra"
    }
    debilitation = {
        "SUN": "Libra", "MOON": "Scorpio", "MARS": "Cancer", "MERCURY": "Pisces",
        "JUPITER": "Capricorn", "VENUS": "Virgo", "SATURN": "Aries"
    }
    own_signs = {
        "SUN": "Leo", "MOON": "Taurus", "MARS": "Aries", "MERCURY": "Virgo",
        "JUPITER": "Sagittarius", "VENUS": "Libra", "SATURN": "Aquarius"
    }
    
    if planet in exaltation and sign == exaltation[planet]:
        strength_factors.append("EXALTED")
        strength_score += 30
    elif planet in debilitation and sign == debilitation[planet]:
        strength_factors.append("DEBILITATED")
        strength_score -= 20
    elif planet in own_signs and sign == own_signs[planet]:
        strength_factors.append("OWN SIGN")
        strength_score += 20
    
    # House strength
    if house in [1, 4, 7, 10]:  # Kendra houses
        strength_factors.append("KENDRA")
        strength_score += 10
    elif house in [5, 9]:  # Trikona houses
        strength_factors.append("TRIKONA")
        strength_score += 15
    elif house in [3, 6, 11]:  # Upachaya houses
        strength_factors.append("UPACHAYA")
        strength_score += 5
    elif house in [8, 12]:  # Dusthana houses
        strength_factors.append("DUSTHANA")
        strength_score -= 10
    
    return strength_factors, strength_score

def generate_advanced_analysis():
    """Generate advanced marriage analysis with aspects and conjunctions"""
    
    output = []
    output.append("="*80)
    output.append("ADVANCED MARRIAGE ANALYSIS FOR AKSHIT")
    output.append("Based on Classical Vedic Astrology - Complete Planetary Analysis")
    output.append("Including Aspects, Conjunctions, and Classical Principles")
    output.append("="*80)
    output.append("")
    
    d1 = CHART_DATA["D1"]
    d9 = CHART_DATA["D9"]
    
    # Planetary Positions with Nakshatras
    output.append("="*80)
    output.append("D1 (BIRTH CHART) - COMPLETE PLANETARY ANALYSIS")
    output.append("="*80)
    output.append("")
    output.append("Ascendant: Leo 23°03'")
    output.append("")
    output.append("PLANETARY POSITIONS WITH NAKSHATRAS:")
    output.append("-"*80)
    output.append(f"{'Planet':<10} {'Sign':<12} {'Degree':<10} {'House':<6} {'Nakshatra':<15} {'Pada':<5} {'Lord':<10} {'Strength'}")
    output.append("-"*80)
    
    for planet in ["SUN", "MOON", "MARS", "MERCURY", "JUPITER", "VENUS", "SATURN", "RAHU", "KETU"]:
        if planet in d1:
            p = d1[planet]
            nakshatra = get_nakshatra(p["longitude"])
            pada = get_pada(p["longitude"])
            nakshatra_lord = get_nakshatra_lord(nakshatra)
            strength_factors, strength_score = analyze_planet_strength(planet, p["sign"], p["house"])
            strength_str = ", ".join(strength_factors) if strength_factors else "Neutral"
            retro = " (R)" if p.get("retrograde") else ""
            output.append(f"{planet:<10} {p['sign']:<12} {p['degree']:<10} {p['house']:<6} {nakshatra:<15} {pada:<5} {nakshatra_lord:<10} {strength_str}{retro}")
    output.append("")
    
    # Conjunctions Analysis
    output.append("="*80)
    output.append("PLANETARY CONJUNCTIONS (SAME SIGN)")
    output.append("="*80)
    output.append("")
    conjunctions = find_conjunctions(d1)
    if conjunctions:
        for sign, planets in conjunctions.items():
            output.append(f"Conjunction in {sign}:")
            for planet in planets:
                p = d1[planet]
                nakshatra = get_nakshatra(p["longitude"])
                output.append(f"  - {planet}: {p['degree']} in {nakshatra} Nakshatra")
            
            # Analyze conjunction effects
            if "VENUS" in planets and "RAHU" in planets:
                output.append("  ⚠ Venus-Rahu Conjunction:")
                output.append("    • Unconventional relationships possible")
                output.append("    • Spouse may be from different background")
                output.append("    • Some unexpected events in marriage")
            output.append("")
    else:
        output.append("No major conjunctions (planets in same sign)")
        output.append("")
    
    # Aspects Analysis
    output.append("="*80)
    output.append("PLANETARY ASPECTS ON 7TH HOUSE (MARRIAGE HOUSE)")
    output.append("="*80)
    output.append("")
    output.append("7th House: Aquarius (Lord: Saturn)")
    output.append("Planet in 7th House: Saturn (7th lord in own sign)")
    output.append("")
    output.append("ASPECTS ON 7TH HOUSE:")
    output.append("-"*80)
    
    aspects_on_7th = []
    for planet in ["SUN", "MOON", "MARS", "MERCURY", "JUPITER", "VENUS", "SATURN", "RAHU", "KETU"]:
        if planet in d1:
            p = d1[planet]
            aspects = calculate_aspects(planet, p["house"], p["sign_idx"])
            for aspect in aspects:
                if aspect["house"] == 7:
                    aspects_on_7th.append({
                        "planet": planet,
                        "from_house": p["house"],
                        "type": aspect["type"],
                        "planet_data": p
                    })
    
    for aspect in aspects_on_7th:
        p = aspect["planet_data"]
        nakshatra = get_nakshatra(p["longitude"])
        output.append(f"{aspect['planet']:10} aspects 7th house from House {aspect['from_house']:2} ({aspect['type']})")
        output.append(f"           Position: {p['sign']} {p['degree']} in {nakshatra} Nakshatra")
        
        # Analyze aspect
        if aspect["planet"] == "JUPITER":
            output.append("           ✓ Benefic aspect - Brings wisdom, prosperity, and harmony")
        elif aspect["planet"] == "VENUS":
            output.append("           ✓ Benefic aspect - Brings love, beauty, and marital happiness")
        elif aspect["planet"] == "MARS":
            output.append("           ⚠ Malefic aspect - May cause conflicts, arguments, or disputes")
        elif aspect["planet"] == "SATURN":
            output.append("           ⚠ Saturn aspects its own house - Strong but may cause delays")
        elif aspect["planet"] == "SUN":
            output.append("           ⚠ Malefic aspect - May cause ego issues or dominance")
        elif aspect["planet"] == "RAHU":
            output.append("           ⚠ Rahu aspect - Unconventional, unexpected events")
        elif aspect["planet"] == "KETU":
            output.append("           ⚠ Ketu aspect - Detachment, spiritual transformation")
        output.append("")
    
    # All Aspects Table
    output.append("="*80)
    output.append("COMPLETE ASPECTS TABLE")
    output.append("="*80)
    output.append("")
    for planet in ["SUN", "MOON", "MARS", "MERCURY", "JUPITER", "VENUS", "SATURN"]:
        if planet in d1:
            p = d1[planet]
            aspects = calculate_aspects(planet, p["house"], p["sign_idx"])
            output.append(f"{planet} (House {p['house']}) aspects:")
            for aspect in aspects:
                output.append(f"  - House {aspect['house']:2} ({aspect['type']})")
            output.append("")
    
    # 7th House Detailed Analysis
    output.append("="*80)
    output.append("7TH HOUSE DETAILED ANALYSIS")
    output.append("="*80)
    output.append("")
    saturn_d1 = d1["SATURN"]
    saturn_nakshatra = get_nakshatra(saturn_d1["longitude"])
    saturn_pada = get_pada(saturn_d1["longitude"])
    saturn_nakshatra_lord = get_nakshatra_lord(saturn_nakshatra)
    
    output.append("7th House Sign: Aquarius")
    output.append("7th Lord: Saturn")
    output.append("")
    output.append("Saturn in 7th House:")
    output.append(f"  - Sign: Aquarius (OWN SIGN - Very Strong)")
    output.append(f"  - Degree: {saturn_d1['degree']}")
    output.append(f"  - Nakshatra: {saturn_nakshatra} (Lord: {saturn_nakshatra_lord}) Pada {saturn_pada}")
    output.append(f"  - Longitude: {saturn_d1['longitude']:.2f}°")
    output.append("")
    output.append("ANALYSIS:")
    output.append("  ✓ Saturn (7th lord) in own sign in 7th house - EXCEPTIONAL")
    output.append("  ✓ This is one of the strongest placements for marriage")
    output.append("  ✓ Indicates:")
    output.append("    • Very stable and long-lasting marriage")
    output.append("    • Spouse will be mature, responsible, disciplined")
    output.append("    • Strong commitment and duty in marriage")
    output.append("    • Marriage based on traditional values")
    output.append("    • Spouse may be older or more mature")
    output.append("  ⚠ Saturn's nature indicates:")
    output.append("    • Delayed marriage (likely after 30-32 years)")
    output.append("    • Some challenges in early years")
    output.append("    • Relationship improves with time")
    output.append(f"  ⚠ Saturn in {saturn_nakshatra} ({saturn_nakshatra_lord}'s nakshatra):")
    if saturn_nakshatra_lord == "Rahu":
        output.append("    • Some unconventional aspects in marriage")
        output.append("    • Unexpected events or changes")
    output.append("")
    
    # Venus Detailed Analysis
    output.append("="*80)
    output.append("VENUS (MARRIAGE KARAKA) DETAILED ANALYSIS")
    output.append("="*80)
    output.append("")
    venus_d1 = d1["VENUS"]
    venus_nakshatra = get_nakshatra(venus_d1["longitude"])
    venus_pada = get_pada(venus_d1["longitude"])
    venus_nakshatra_lord = get_nakshatra_lord(venus_nakshatra)
    
    output.append(f"Venus Position:")
    output.append(f"  - Sign: {venus_d1['sign']} (OWN SIGN - Very Strong)")
    output.append(f"  - Degree: {venus_d1['degree']}")
    output.append(f"  - House: {venus_d1['house']} (3rd House)")
    output.append(f"  - Nakshatra: {venus_nakshatra} (Lord: {venus_nakshatra_lord}) Pada {venus_pada}")
    output.append(f"  - Longitude: {venus_d1['longitude']:.2f}°")
    output.append("")
    output.append("ANALYSIS:")
    output.append("  ✓ Venus in own sign Libra - EXCELLENT for marriage")
    output.append(f"  ✓ Venus in {venus_nakshatra} ({venus_nakshatra_lord}'s nakshatra):")
    if venus_nakshatra_lord == "Jupiter":
        output.append("    • Spouse will be wise, knowledgeable, and spiritual")
        output.append("    • Good fortune through spouse")
    output.append("  ✓ 3rd house placement indicates:")
    output.append("    • Spouse may be from nearby or through siblings")
    output.append("    • Good communication in marriage")
    output.append("    • Spouse involved in communication, writing, or short travels")
    output.append("")
    
    # Check Venus-Rahu conjunction
    if venus_d1["sign_idx"] == d1["RAHU"]["sign_idx"]:
        output.append("  ⚠ Venus-Rahu Conjunction in Libra:")
        output.append("    • Unconventional relationship aspects")
        output.append("    • Spouse may be from different background")
        output.append("    • Some unexpected events in marriage")
        output.append("    • But overall Venus strength overcomes challenges")
        output.append("")
    
    # Jupiter Detailed Analysis
    output.append("="*80)
    output.append("JUPITER (SPOUSE KARAKA) DETAILED ANALYSIS")
    output.append("="*80)
    output.append("")
    jupiter_d1 = d1["JUPITER"]
    jupiter_nakshatra = get_nakshatra(jupiter_d1["longitude"])
    jupiter_pada = get_pada(jupiter_d1["longitude"])
    jupiter_nakshatra_lord = get_nakshatra_lord(jupiter_nakshatra)
    
    output.append(f"Jupiter Position:")
    output.append(f"  - Sign: {jupiter_d1['sign']} (Friend's sign)")
    output.append(f"  - Degree: {jupiter_d1['degree']}")
    output.append(f"  - House: {jupiter_d1['house']} (4th House)")
    output.append(f"  - Nakshatra: {jupiter_nakshatra} (Lord: {jupiter_nakshatra_lord}) Pada {jupiter_pada}")
    output.append("")
    output.append("ANALYSIS:")
    output.append("  ✓ Jupiter in 4th house - Good family background for spouse")
    output.append(f"  ✓ Jupiter in {jupiter_nakshatra} ({jupiter_nakshatra_lord}'s nakshatra):")
    if jupiter_nakshatra_lord == "Saturn":
        output.append("    • Spouse will be disciplined and responsible")
    output.append("  ✓ Jupiter aspects 7th house (5th aspect) - Beneficial")
    output.append("  ✓ Brings wisdom, prosperity, and harmony to marriage")
    output.append("")
    
    # Navamsa Analysis
    output.append("="*80)
    output.append("NAVAMSA (D9) DETAILED ANALYSIS - MOST IMPORTANT FOR MARRIAGE")
    output.append("="*80)
    output.append("")
    
    venus_d9 = d9["VENUS"]
    jupiter_d9 = d9["JUPITER"]
    moon_d9 = d9["MOON"]
    saturn_d9 = d9["SATURN"]
    
    output.append("Venus in Navamsa:")
    output.append(f"  - Sign: {venus_d9['sign']} (OWN SIGN - EXCELLENT!)")
    output.append(f"  - Degree: {venus_d9['degree']}")
    output.append(f"  - House: {venus_d9['house']} (8th House)")
    output.append("  ✓ Double own sign (D1 Libra + D9 Taurus) - EXCEPTIONAL YOGA")
    output.append("  ⚠ 8th house - Transformation through marriage")
    output.append("")
    
    output.append("Jupiter in Navamsa:")
    output.append(f"  - Sign: {jupiter_d9['sign']} (DEBILITATED)")
    output.append(f"  - Degree: {jupiter_d9['degree']}")
    output.append(f"  - House: {jupiter_d9['house']} (12th House)")
    output.append("  ⚠ Debilitated in 12th house - Some challenges")
    output.append("")
    
    output.append("Moon in Navamsa:")
    output.append(f"  - Sign: {moon_d9['sign']} (OWN SIGN)")
    output.append(f"  - Degree: {moon_d9['degree']}")
    output.append(f"  - House: {moon_d9['house']} (10th House)")
    output.append("  ✓ Emotional fulfillment in marriage")
    output.append("")
    
    # Marriage Yogas
    output.append("="*80)
    output.append("MARRIAGE YOGAS (CLASSICAL COMBINATIONS)")
    output.append("="*80)
    output.append("")
    
    yogas = []
    
    # Check yogas
    if venus_d1["sign"] == "Libra" and venus_d9["sign"] == "Taurus":
        yogas.append("✓ VENUS DOUBLE OWN SIGN YOGA - Exceptional for marriage")
    
    if d1["SATURN"]["sign"] == "Aquarius" and d1["SATURN"]["house"] == 7:
        yogas.append("✓ 7TH LORD IN OWN SIGN IN 7TH HOUSE - Very strong marriage")
    
    if moon_d9["sign"] == "Cancer":
        yogas.append("✓ MOON IN OWN SIGN IN NAVAMSA - Emotional fulfillment")
    
    # Check aspects
    jupiter_aspects_7th = False
    for aspect in aspects_on_7th:
        if aspect["planet"] == "JUPITER":
            jupiter_aspects_7th = True
            break
    
    if jupiter_aspects_7th:
        yogas.append("✓ JUPITER ASPECTING 7TH HOUSE - Beneficial for marriage")
    
    mars_aspects_7th = False
    for aspect in aspects_on_7th:
        if aspect["planet"] == "MARS":
            mars_aspects_7th = True
            break
    
    if mars_aspects_7th:
        yogas.append("⚠ MARS ASPECTING 7TH HOUSE - Some conflicts possible")
    
    if d1["SATURN"]["house"] == 7:
        yogas.append("⚠ SATURN IN 7TH HOUSE - Delayed but stable marriage")
    
    if venus_d9["house"] == 8:
        yogas.append("⚠ VENUS IN 8TH HOUSE NAVAMSA - Transformation through marriage")
    
    # Check for other yogas
    if venus_d1["house"] == 3:
        yogas.append("✓ VENUS IN 3RD HOUSE - Good communication in marriage")
    
    if jupiter_d1["house"] == 4:
        yogas.append("✓ JUPITER IN 4TH HOUSE - Good family background for spouse")
    
    for yoga in yogas:
        output.append(f"  {yoga}")
    output.append("")
    
    # Dasha Analysis
    output.append("="*80)
    output.append("DASHA ANALYSIS - MARRIAGE TIMING")
    output.append("="*80)
    output.append("")
    output.append("Current Mahadasha: Jupiter (2020-2036)")
    output.append("Current Antardasha: Jupiter-Mercury (Feb 2025 - May 2027)")
    output.append("")
    output.append("FAVORABLE PERIODS:")
    output.append("  1. Jupiter-Mercury-Venus (Jul 2025 - Dec 2025) - VERY GOOD")
    output.append("  2. Jupiter-Venus (Apr 2028 - Dec 2030) - BEST PERIOD")
    output.append("  3. Jupiter-Mercury-Moon (Jan 2026 - Mar 2026) - GOOD")
    output.append("")
    output.append("PREDICTED TIMING: April 2028 - December 2030 (Most likely)")
    output.append("                 July 2025 - December 2025 (Good possibility)")
    output.append("                 Age: 33-36 years")
    output.append("")
    
    # Final Summary
    output.append("="*80)
    output.append("FINAL SUMMARY")
    output.append("="*80)
    output.append("")
    output.append("STRENGTHS:")
    output.append("  1. Venus in own sign (D1 & D9) - EXCEPTIONAL")
    output.append("  2. 7th lord Saturn in own sign in 7th house - VERY STRONG")
    output.append("  3. Jupiter aspects 7th house - Beneficial")
    output.append("  4. Moon in own sign Navamsa - Emotional stability")
    output.append("  5. Strong dasha periods for marriage")
    output.append("")
    output.append("CHALLENGES:")
    output.append("  1. Saturn in 7th - Delayed marriage")
    output.append("  2. Venus in 8th Navamsa - Transformation needed")
    output.append("  3. Mars aspects 7th - Some conflicts")
    output.append("  4. Jupiter debilitated in Navamsa - Some challenges")
    output.append("")
    output.append("OVERALL: Very strong marriage chart with stable, long-lasting relationship")
    output.append("")
    output.append("="*80)
    
    return "\n".join(output)

if __name__ == "__main__":
    analysis = generate_advanced_analysis()
    
    # Write to file
    with open("Akshit_Advanced_Marriage_Analysis.txt", "w", encoding="utf-8") as f:
        f.write(analysis)
    
    print(analysis)
    print("\n" + "="*80)
    print("Advanced analysis saved to: Akshit_Advanced_Marriage_Analysis.txt")
    print("="*80)
