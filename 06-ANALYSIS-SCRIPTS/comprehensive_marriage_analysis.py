#!/usr/bin/env python3
"""
Comprehensive Marriage Analysis for Akshit
Based on Vedic Astrology principles from classical texts
Analyzes all planets, degrees, houses, and varga charts
"""

# Complete Chart Data with all details
CHART_DATA = {
    "D1": {
        "SUN": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "10°55'", "house": 5, "longitude": 250.916},
        "MOON": {"sign": "Virgo", "lord": "Mercury", "degree": "22°44'", "house": 2, "longitude": 172.733},
        "MARS": {"sign": "Leo", "lord": "Sun", "degree": "8°33'", "house": 1, "longitude": 128.55},
        "MERCURY": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "18°06'", "house": 5, "longitude": 258.1},
        "JUPITER": {"sign": "Scorpio", "lord": "Mars", "degree": "9°52'", "house": 4, "longitude": 219.867},
        "VENUS": {"sign": "Libra", "lord": "Venus", "degree": "25°24'", "house": 3, "longitude": 205.4},
        "SATURN": {"sign": "Aquarius", "lord": "Saturn", "degree": "13°46'", "house": 7, "longitude": 313.767},
        "RAHU": {"sign": "Libra", "lord": "Venus", "degree": "18°15'", "house": 3, "longitude": 198.25, "retrograde": True},
        "KETU": {"sign": "Aries", "lord": "Mars", "degree": "18°15'", "house": 9, "longitude": 18.25, "retrograde": True},
        "URANUS": {"sign": "Capricorn", "lord": "Saturn", "degree": "1°22'", "house": 6, "longitude": 271.367},
        "NEPTUNE": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "28°34'", "house": 5, "longitude": 268.567},
        "PLUTO": {"sign": "Scorpio", "lord": "Mars", "degree": "5°33'", "house": 4, "longitude": 215.55},
        "ASCENDANT": {"sign": "Leo", "lord": "Sun", "degree": "23°03'", "house": 1, "longitude": 143.05}
    },
    "D2": {
        "MARS": {"sign": "Leo", "lord": "Sun", "degree": "17°06'", "house": 2},
        "MOON": {"sign": "Virgo", "lord": "Mercury", "degree": "15°28'", "house": 2},
        "VENUS": {"sign": "Libra", "lord": "Venus", "degree": "20°48'", "house": 1},
        "RAHU": {"sign": "Libra", "lord": "Venus", "degree": "06°30'", "house": 1, "retrograde": True},
        "JUPITER": {"sign": "Scorpio", "lord": "Mars", "degree": "19°44'", "house": 1},
        "SUN": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "21°50'", "house": 2},
        "MERCURY": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "06°13'", "house": 1},
        "SATURN": {"sign": "Aquarius", "lord": "Saturn", "degree": "27°33'", "house": 2},
        "KETU": {"sign": "Aries", "lord": "Mars", "degree": "06°30'", "house": 1, "retrograde": True}
    },
    "D6": {
        "MARS": {"sign": "Leo", "lord": "Sun", "degree": "21°20'", "house": 1},
        "MOON": {"sign": "Virgo", "lord": "Mercury", "degree": "16°25'", "house": 2},
        "VENUS": {"sign": "Libra", "lord": "Venus", "degree": "02°25'", "house": 3},
        "RAHU": {"sign": "Libra", "lord": "Venus", "degree": "19°32'", "house": 3, "retrograde": True},
        "JUPITER": {"sign": "Scorpio", "lord": "Mars", "degree": "29°12'", "house": 4},
        "SUN": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "05°30'", "house": 5},
        "MERCURY": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "18°40'", "house": 5},
        "SATURN": {"sign": "Aquarius", "lord": "Saturn", "degree": "22°40'", "house": 7},
        "KETU": {"sign": "Aries", "lord": "Mars", "degree": "19°32'", "house": 9, "retrograde": True}
    },
    "D7": {
        "MARS": {"sign": "Leo", "lord": "Sun", "degree": "29°53'", "house": 10},
        "MOON": {"sign": "Virgo", "lord": "Mercury", "degree": "09°09'", "house": 9},
        "VENUS": {"sign": "Libra", "lord": "Venus", "degree": "27°49'", "house": 4},
        "RAHU": {"sign": "Libra", "lord": "Venus", "degree": "07°47'", "house": 3, "retrograde": True},
        "JUPITER": {"sign": "Scorpio", "lord": "Mars", "degree": "09°04'", "house": 8},
        "SUN": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "16°26'", "house": 3},
        "MERCURY": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "06°47'", "house": 5},
        "SATURN": {"sign": "Aquarius", "lord": "Saturn", "degree": "06°27'", "house": 6},
        "KETU": {"sign": "Aries", "lord": "Mars", "degree": "07°47'", "house": 9, "retrograde": True}
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
    },
    "D10": {
        "SUN": {"sign": "Pisces", "lord": "Jupiter", "degree": "19°11'", "house": 2},
        "RAHU": {"sign": "Aries", "lord": "Mars", "degree": "02°34'", "house": 3, "retrograde": True},
        "MERCURY": {"sign": "Gemini", "lord": "Mercury", "degree": "01°07'", "house": 5},
        "VENUS": {"sign": "Gemini", "lord": "Mercury", "degree": "14°02'", "house": 5},
        "SATURN": {"sign": "Gemini", "lord": "Mercury", "degree": "17°47'", "house": 5},
        "MARS": {"sign": "Libra", "lord": "Venus", "degree": "25°33'", "house": 9},
        "JUPITER": {"sign": "Libra", "lord": "Venus", "degree": "08°41'", "house": 9},
        "KETU": {"sign": "Libra", "lord": "Venus", "degree": "02°34'", "house": 9, "retrograde": True},
        "MOON": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "17°22'", "house": 11}
    },
    "D60": {
        "MARS": {"sign": "Leo", "lord": "Sun", "degree": "03°21'", "house": 1},
        "MOON": {"sign": "Virgo", "lord": "Mercury", "degree": "14°12'", "house": 6},
        "VENUS": {"sign": "Libra", "lord": "Venus", "degree": "24°15'", "house": 12},
        "RAHU": {"sign": "Libra", "lord": "Venus", "degree": "15°25'", "house": 10, "retrograde": True},
        "JUPITER": {"sign": "Scorpio", "lord": "Mars", "degree": "22°08'", "house": 6},
        "SUN": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "25°08'", "house": 9},
        "MERCURY": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "06°44'", "house": 12},
        "SATURN": {"sign": "Aquarius", "lord": "Saturn", "degree": "16°46'", "house": 5},
        "KETU": {"sign": "Aries", "lord": "Mars", "degree": "15°25'", "house": 4, "retrograde": True}
    }
}

# Nakshatra calculation
NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashirsha", "Ardra", "Punarvasu",
    "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta",
    "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
    "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha", "Purva Bhadrapada",
    "Uttara Bhadrapada", "Revati"
]

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

def analyze_planet_strength(planet, sign, degree_str):
    """Analyze planet strength"""
    strength = []
    
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
        strength.append("EXALTED - Very Strong")
    elif planet in debilitation and sign == debilitation[planet]:
        strength.append("DEBILITATED - Weak")
    elif planet in own_signs and sign == own_signs[planet]:
        strength.append("OWN SIGN - Strong")
    
    return "; ".join(strength) if strength else "Neutral"

def generate_comprehensive_analysis():
    """Generate comprehensive marriage analysis"""
    
    output = []
    output.append("="*80)
    output.append("COMPREHENSIVE MARRIAGE ANALYSIS FOR AKSHIT")
    output.append("Based on Vedic Astrology - Complete Planetary Analysis")
    output.append("="*80)
    output.append("")
    
    # D1 Analysis
    output.append("="*80)
    output.append("D1 (BIRTH CHART) - MAIN CHART ANALYSIS")
    output.append("="*80)
    output.append("")
    output.append("Ascendant: Leo 23°03' (Lord: Sun)")
    output.append("")
    
    d1 = CHART_DATA["D1"]
    output.append("PLANETARY POSITIONS IN D1:")
    output.append("-"*80)
    for planet in ["SUN", "MOON", "MARS", "MERCURY", "JUPITER", "VENUS", "SATURN", "RAHU", "KETU"]:
        if planet in d1:
            p = d1[planet]
            nakshatra = get_nakshatra(p.get("longitude", 0))
            pada = get_pada(p.get("longitude", 0))
            strength = analyze_planet_strength(planet, p["sign"], p["degree"])
            retro = " (Retrograde)" if p.get("retrograde") else ""
            output.append(f"{planet:10} | {p['sign']:12} | {p['degree']:8} | House {p['house']:2} | {nakshatra} Pada {pada} | {strength}{retro}")
    output.append("")
    
    # 7th House Analysis
    output.append("="*80)
    output.append("7TH HOUSE ANALYSIS (MARRIAGE HOUSE)")
    output.append("="*80)
    output.append("")
    output.append("7th House Sign: Aquarius (Lord: Saturn)")
    output.append("7th Lord: Saturn in Aquarius 13°46' (OWN SIGN in 7th House)")
    output.append("")
    
    planets_7th = [p for p, d in d1.items() if d.get("house") == 7 and p != "ASCENDANT"]
    if planets_7th:
        output.append("Planets in 7th House:")
        for planet in planets_7th:
            p = d1[planet]
            nakshatra = get_nakshatra(p.get("longitude", 0))
            output.append(f"  - {planet}: {p['sign']} {p['degree']} in {nakshatra}")
    else:
        output.append("No planets in 7th house (Empty house)")
    output.append("")
    
    output.append("ANALYSIS:")
    output.append("  ✓ Saturn (7th lord) in own sign Aquarius in 7th house - EXCELLENT")
    output.append("  ✓ This is a very strong placement indicating:")
    output.append("    • Stable, long-lasting marriage")
    output.append("    • Spouse will be mature, responsible, disciplined")
    output.append("    • Marriage will be based on commitment and duty")
    output.append("    • Spouse may be older or more mature in thinking")
    output.append("  ⚠ Saturn's nature indicates delayed marriage (likely after 30-32 years)")
    output.append("  ⚠ Some challenges in early marriage years, but stability increases with time")
    output.append("")
    
    # Venus Analysis
    output.append("="*80)
    output.append("VENUS ANALYSIS (MARRIAGE KARAKA)")
    output.append("="*80)
    output.append("")
    venus_d1 = d1["VENUS"]
    venus_nakshatra = get_nakshatra(venus_d1.get("longitude", 0))
    venus_pada = get_pada(venus_d1.get("longitude", 0))
    output.append(f"Venus in D1:")
    output.append(f"  - Sign: {venus_d1['sign']} (OWN SIGN - Very Strong)")
    output.append(f"  - Degree: {venus_d1['degree']}")
    output.append(f"  - House: {venus_d1['house']} (3rd House)")
    output.append(f"  - Nakshatra: {venus_nakshatra} Pada {venus_pada}")
    output.append(f"  - Longitude: 205°24'")
    output.append("")
    output.append("ANALYSIS:")
    output.append("  ✓ Venus in own sign Libra - EXCELLENT for marriage")
    output.append("  ✓ Strong Venus indicates:")
    output.append("    • Beautiful, attractive spouse")
    output.append("    • Good marital harmony")
    output.append("    • Material comfort in married life")
    output.append("    • Artistic and refined spouse")
    output.append("  ✓ 3rd house placement indicates:")
    output.append("    • Spouse may be from nearby or through siblings/communication")
    output.append("    • Good communication in marriage")
    output.append("    • Spouse may be involved in writing, communication, or short travels")
    output.append("")
    
    # Jupiter Analysis
    output.append("="*80)
    output.append("JUPITER ANALYSIS (SPOUSE KARAKA)")
    output.append("="*80)
    output.append("")
    jupiter_d1 = d1["JUPITER"]
    jupiter_nakshatra = get_nakshatra(jupiter_d1.get("longitude", 0))
    jupiter_pada = get_pada(jupiter_d1.get("longitude", 0))
    output.append(f"Jupiter in D1:")
    output.append(f"  - Sign: {jupiter_d1['sign']} (Scorpio - Friend's sign)")
    output.append(f"  - Degree: {jupiter_d1['degree']}")
    output.append(f"  - House: {jupiter_d1['house']} (4th House)")
    output.append(f"  - Nakshatra: {jupiter_nakshatra} Pada {jupiter_pada}")
    output.append("")
    output.append("ANALYSIS:")
    output.append("  ✓ Jupiter in 4th house indicates:")
    output.append("    • Spouse from good family background")
    output.append("    • Comfortable home and property")
    output.append("    • Good relationship with mother and family")
    output.append("  ✓ Jupiter in Scorpio (friend's sign) - Moderate strength")
    output.append("")
    
    # Navamsa Analysis
    output.append("="*80)
    output.append("NAVAMSA (D9) ANALYSIS - MOST IMPORTANT FOR MARRIAGE")
    output.append("="*80)
    output.append("")
    output.append("Navamsa Lagna: Leo (calculated from D1 ascendant)")
    output.append("")
    
    d9 = CHART_DATA["D9"]
    output.append("KEY PLANETS IN NAVAMSA:")
    output.append("-"*80)
    
    # Venus in Navamsa
    venus_d9 = d9["VENUS"]
    output.append(f"Venus in Navamsa:")
    output.append(f"  - Sign: {venus_d9['sign']} (Taurus - OWN SIGN - EXCELLENT!)")
    output.append(f"  - Degree: {venus_d9['degree']}")
    output.append(f"  - House: {venus_d9['house']} (8th House)")
    output.append("")
    output.append("  ANALYSIS:")
    output.append("  ✓ Venus in own sign Taurus in Navamsa - VERY FAVORABLE")
    output.append("  ✓ Double own sign (D1 Libra + D9 Taurus) - EXCEPTIONAL")
    output.append("  ⚠ 8th house placement indicates:")
    output.append("    • Transformation through marriage")
    output.append("    • Some challenges or changes in married life")
    output.append("    • Spouse may bring significant changes")
    output.append("    • Possible inheritance or shared resources")
    output.append("")
    
    # Jupiter in Navamsa
    jupiter_d9 = d9["JUPITER"]
    output.append(f"Jupiter in Navamsa:")
    output.append(f"  - Sign: {jupiter_d9['sign']} (Virgo - DEBILITATED)")
    output.append(f"  - Degree: {jupiter_d9['degree']}")
    output.append(f"  - House: {jupiter_d9['house']} (12th House)")
    output.append("")
    output.append("  ANALYSIS:")
    output.append("  ⚠ Jupiter debilitated in 12th house indicates:")
    output.append("    • Some challenges in spouse's nature or health")
    output.append("    • Spouse may be spiritual or religious")
    output.append("    • Possible foreign connection or different background")
    output.append("    • Expenses related to spouse")
    output.append("")
    
    # Moon in Navamsa
    moon_d9 = d9["MOON"]
    output.append(f"Moon in Navamsa:")
    output.append(f"  - Sign: {moon_d9['sign']} (Cancer - OWN SIGN)")
    output.append(f"  - Degree: {moon_d9['degree']}")
    output.append(f"  - House: {moon_d9['house']} (10th House)")
    output.append("")
    output.append("  ANALYSIS:")
    output.append("  ✓ Moon in own sign - Emotional fulfillment in marriage")
    output.append("  ✓ 10th house - Spouse may be career-oriented or from good status")
    output.append("")
    
    # Saturn in Navamsa
    saturn_d9 = d9["SATURN"]
    output.append(f"Saturn in Navamsa:")
    output.append(f"  - Sign: {saturn_d9['sign']} (Aquarius - OWN SIGN)")
    output.append(f"  - Degree: {saturn_d9['degree']}")
    output.append(f"  - House: {saturn_d9['house']} (5th House)")
    output.append("")
    output.append("  ANALYSIS:")
    output.append("  ✓ Saturn in own sign - Strong commitment")
    output.append("  ✓ 5th house - Good relationship with children")
    output.append("")
    
    # 7th House in Navamsa
    output.append("7th House in Navamsa: Aquarius (Lord: Saturn)")
    planets_7th_d9 = [p for p, d in d9.items() if d.get("house") == 7]
    if planets_7th_d9:
        output.append("Planets in 7th House (Navamsa):")
        for planet in planets_7th_d9:
            p = d9[planet]
            output.append(f"  - {planet}: {p['sign']} {p['degree']}")
    else:
        output.append("No planets in 7th house (Empty - Good)")
    output.append("")
    
    # Marriage Yogas
    output.append("="*80)
    output.append("MARRIAGE YOGAS (COMBINATIONS)")
    output.append("="*80)
    output.append("")
    
    yogas = []
    
    # Check for various yogas
    if venus_d1["sign"] == "Libra" and venus_d9["sign"] == "Taurus":
        yogas.append("✓ VENUS DOUBLE OWN SIGN YOGA - Exceptional for marriage")
    
    if d1["SATURN"]["sign"] == "Aquarius" and d1["SATURN"]["house"] == 7:
        yogas.append("✓ 7TH LORD IN OWN SIGN IN 7TH HOUSE - Very strong marriage")
    
    if moon_d9["sign"] == "Cancer":
        yogas.append("✓ MOON IN OWN SIGN IN NAVAMSA - Emotional fulfillment")
    
    if d1["SATURN"]["house"] == 7:
        yogas.append("⚠ SATURN IN 7TH HOUSE - Delayed but stable marriage")
    
    if venus_d9["house"] == 8:
        yogas.append("⚠ VENUS IN 8TH HOUSE NAVAMSA - Transformation through marriage")
    
    # Check for mutual aspects
    if d1["JUPITER"]["house"] == 4:  # Jupiter aspects 7th house (4th from 4th)
        yogas.append("✓ JUPITER ASPECTING 7TH HOUSE - Beneficial for marriage")
    
    if d1["MARS"]["house"] == 1:  # Mars aspects 7th house
        yogas.append("⚠ MARS ASPECTING 7TH HOUSE - Some conflicts possible")
    
    for yoga in yogas:
        output.append(f"  {yoga}")
    output.append("")
    
    # Dasha Analysis
    output.append("="*80)
    output.append("DASHA ANALYSIS - MARRIAGE TIMING")
    output.append("="*80)
    output.append("")
    output.append("Current Mahadasha: Jupiter (07-Jun-2020 to 07-Jun-2036)")
    output.append("Current Antardasha: Jupiter-Mercury (06-Feb-2025 to 14-May-2027)")
    output.append("")
    
    output.append("FAVORABLE PERIODS FOR MARRIAGE:")
    output.append("-"*80)
    output.append("")
    output.append("1. Jupiter-Mercury Antardasha (Feb 2025 - May 2027):")
    output.append("   - Mercury is in 5th house (romance, love, creativity)")
    output.append("   - Jupiter aspects 7th house from 4th house")
    output.append("   - This is a FAVORABLE period for marriage")
    output.append("   - Best sub-periods:")
    output.append("     • Jupiter-Mercury-Venus (Jul 2025 - Dec 2025) - VERY GOOD")
    output.append("     • Jupiter-Mercury-Moon (Jan 2026 - Mar 2026) - GOOD")
    output.append("")
    
    output.append("2. Jupiter-Venus Antardasha (Apr 2028 - Dec 2030):")
    output.append("   - Venus is marriage karaka in own sign")
    output.append("   - Jupiter-Venus combination is EXCELLENT for marriage")
    output.append("   - This is the MOST FAVORABLE period for marriage")
    output.append("   - Venus in own sign in both D1 and D9 makes this period very strong")
    output.append("")
    
    output.append("3. Jupiter-Sun Antardasha (Dec 2030 - Oct 2031):")
    output.append("   - Sun in 5th house (romance)")
    output.append("   - Moderate period for marriage")
    output.append("")
    
    output.append("4. Jupiter-Moon Antardasha (Oct 2031 - Feb 2033):")
    output.append("   - Moon in 2nd house (family, wealth)")
    output.append("   - Good period for marriage")
    output.append("")
    
    output.append("PREDICTED MARRIAGE TIMING:")
    output.append("  Based on Saturn in 7th house (delayed marriage) and dasha periods:")
    output.append("  • Most likely: April 2028 - December 2030 (Jupiter-Venus period)")
    output.append("  • Good possibility: July 2025 - December 2025 (Jupiter-Mercury-Venus)")
    output.append("  • Age at marriage: Likely 33-36 years (Saturn's delay)")
    output.append("")
    
    # Spouse Characteristics
    output.append("="*80)
    output.append("SPOUSE CHARACTERISTICS")
    output.append("="*80)
    output.append("")
    output.append("Based on 7th House (Aquarius) and Navamsa Analysis:")
    output.append("")
    output.append("PHYSICAL APPEARANCE:")
    output.append("  • Attractive and beautiful (Venus in own signs)")
    output.append("  • Medium to tall height (Aquarius)")
    output.append("  • Well-proportioned body")
    output.append("  • Pleasant and charming personality")
    output.append("")
    output.append("NATURE & PERSONALITY:")
    output.append("  • Mature, responsible, and disciplined (Saturn in 7th)")
    output.append("  • Independent and freedom-loving (Aquarius)")
    output.append("  • Scientific, technical, or humanitarian nature")
    output.append("  • May be older or more mature in thinking")
    output.append("  • Strong values and principles")
    output.append("  • May have some spiritual inclination (Jupiter in 12th Navamsa)")
    output.append("")
    output.append("BACKGROUND & FAMILY:")
    output.append("  • From good family background (Jupiter in 4th house)")
    output.append("  • Comfortable financial status")
    output.append("  • May be from different background or foreign connection")
    output.append("  • Family may be traditional and values-oriented")
    output.append("")
    output.append("PROFESSION:")
    output.append("  • Career-oriented (Moon in 10th Navamsa)")
    output.append("  • May be in technical, scientific, or humanitarian field")
    output.append("  • Good status and recognition")
    output.append("")
    
    # Post-Marriage Life
    output.append("="*80)
    output.append("POST-MARRIAGE LIFE ANALYSIS")
    output.append("="*80)
    output.append("")
    output.append("MARITAL HARMONY:")
    output.append("  ✓ Strong and stable marriage (Saturn in own sign in 7th)")
    output.append("  ✓ Good emotional bonding (Moon in own sign Navamsa)")
    output.append("  ✓ Material comfort (Venus in own signs)")
    output.append("  ⚠ Some initial challenges (Saturn's nature, Venus in 8th Navamsa)")
    output.append("  ✓ Relationship improves with time")
    output.append("")
    output.append("FINANCIAL STATUS:")
    output.append("  ✓ Good financial stability (Jupiter in 4th, Venus strong)")
    output.append("  ✓ Spouse contributes to wealth")
    output.append("  ✓ Comfortable lifestyle")
    output.append("")
    output.append("CHILDREN:")
    output.append("  ✓ Good relationship with children (Saturn in 5th Navamsa)")
    output.append("  ✓ Children will be responsible and disciplined")
    output.append("  ✓ May have 1-2 children")
    output.append("")
    output.append("HEALTH OF SPOUSE:")
    output.append("  ⚠ Some health concerns possible (Jupiter debilitated in 12th Navamsa)")
    output.append("  ✓ Regular health check-ups recommended")
    output.append("  ✓ Overall health will be manageable")
    output.append("")
    
    # D7 Analysis (Children)
    output.append("="*80)
    output.append("D7 (SAPTAMSA) ANALYSIS - CHILDREN & PROGENY")
    output.append("="*80)
    output.append("")
    d7 = CHART_DATA["D7"]
    output.append("Key placements in D7:")
    output.append(f"  - Venus: {d7['VENUS']['sign']} {d7['VENUS']['degree']} in House {d7['VENUS']['house']}")
    output.append(f"  - Jupiter: {d7['JUPITER']['sign']} {d7['JUPITER']['degree']} in House {d7['JUPITER']['house']}")
    output.append(f"  - Saturn: {d7['SATURN']['sign']} {d7['SATURN']['degree']} in House {d7['SATURN']['house']}")
    output.append("")
    output.append("ANALYSIS:")
    output.append("  ✓ Venus in 4th house D7 - Good for children")
    output.append("  ✓ Jupiter in 8th house D7 - Children may be spiritual")
    output.append("  ✓ Saturn in 6th house D7 - Some delays but children will be responsible")
    output.append("")
    
    # Remedies
    output.append("="*80)
    output.append("REMEDIES & SUGGESTIONS")
    output.append("="*80)
    output.append("")
    output.append("1. Worship Lord Shani (Saturn) - Saturday fasting")
    output.append("2. Chant Shani Mantra: 'Om Sham Shanicharaya Namah'")
    output.append("3. Donate black items on Saturdays")
    output.append("4. Worship Goddess Lakshmi (for Venus)")
    output.append("5. Chant Venus Mantra: 'Om Shukraya Namah'")
    output.append("6. Wear white clothes on Fridays")
    output.append("7. Perform Navagraha Puja regularly")
    output.append("8. Be patient - Saturn delays but gives stable results")
    output.append("")
    
    # Final Summary
    output.append("="*80)
    output.append("FINAL SUMMARY")
    output.append("="*80)
    output.append("")
    output.append("STRENGTHS:")
    output.append("  1. Venus in own sign in both D1 (Libra) and D9 (Taurus) - EXCEPTIONAL")
    output.append("  2. 7th lord Saturn in own sign Aquarius in 7th house - VERY STRONG")
    output.append("  3. Moon in own sign Cancer in Navamsa - Emotional stability")
    output.append("  4. Strong Jupiter-Venus period coming (2028-2030) - Best timing")
    output.append("  5. Multiple favorable yogas present")
    output.append("")
    output.append("CHALLENGES:")
    output.append("  1. Saturn in 7th house - Delayed marriage (likely after 30-32)")
    output.append("  2. Venus in 8th house Navamsa - Some transformation needed")
    output.append("  3. Jupiter debilitated in Navamsa - Some challenges in spouse")
    output.append("  4. Initial years may have some adjustments")
    output.append("")
    output.append("PREDICTIONS:")
    output.append("  • Marriage will be stable and long-lasting")
    output.append("  • Spouse will be mature, responsible, and attractive")
    output.append("  • Best timing: April 2028 - December 2030")
    output.append("  • Good timing: July 2025 - December 2025")
    output.append("  • Age at marriage: 33-36 years")
    output.append("  • Marriage will be through arranged or traditional means")
    output.append("  • Post-marriage life will be comfortable and stable")
    output.append("  • Relationship will improve with time")
    output.append("")
    output.append("="*80)
    output.append("END OF ANALYSIS")
    output.append("="*80)
    output.append("")
    output.append("Note: This analysis is based on classical Vedic Astrology principles.")
    output.append("For specific predictions, consult with a qualified astrologer who")
    output.append("can consider transits, ashtakavarga, and other advanced techniques.")
    output.append("")
    
    return "\n".join(output)

if __name__ == "__main__":
    analysis = generate_comprehensive_analysis()
    
    # Write to file
    with open("Akshit_Marriage_Analysis.txt", "w", encoding="utf-8") as f:
        f.write(analysis)
    
    print(analysis)
    print("\n" + "="*80)
    print("Analysis saved to: Akshit_Marriage_Analysis.txt")
    print("="*80)
