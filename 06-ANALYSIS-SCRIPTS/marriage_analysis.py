#!/usr/bin/env python3
"""
Marriage Analysis Script for Akshit
Analyzes marriage prospects, timing, and spouse characteristics based on Vedic Astrology
"""

import json
from datetime import datetime

# Chart data from user
CHART_DATA = {
    "D1": {
        "SUN": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "10°55'", "house": 5},
        "MOON": {"sign": "Virgo", "lord": "Mercury", "degree": "22°44'", "house": 2},
        "MARS": {"sign": "Leo", "lord": "Sun", "degree": "8°33'", "house": 1},
        "MERCURY": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "18°06'", "house": 5},
        "JUPITER": {"sign": "Scorpio", "lord": "Mars", "degree": "9°52'", "house": 4},
        "VENUS": {"sign": "Libra", "lord": "Venus", "degree": "25°24'", "house": 3},
        "SATURN": {"sign": "Aquarius", "lord": "Saturn", "degree": "13°46'", "house": 7},
        "RAHU": {"sign": "Libra", "lord": "Venus", "degree": "18°15'", "house": 3, "retrograde": True},
        "KETU": {"sign": "Aries", "lord": "Mars", "degree": "18°15'", "house": 9, "retrograde": True},
        "URANUS": {"sign": "Capricorn", "lord": "Saturn", "degree": "1°22'", "house": 6},
        "NEPTUNE": {"sign": "Sagittarius", "lord": "Jupiter", "degree": "28°34'", "house": 5},
        "PLUTO": {"sign": "Scorpio", "lord": "Mars", "degree": "5°33'", "house": 4},
        "ASCENDANT": {"sign": "Leo", "lord": "Sun", "degree": "23°03'", "house": 1}
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
    }
}

# Sign lords mapping
SIGN_LORDS = {
    "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
    "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
    "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
}

# Exaltation signs
EXALTATION = {
    "Sun": "Aries", "Moon": "Taurus", "Mars": "Capricorn", "Mercury": "Virgo",
    "Jupiter": "Cancer", "Venus": "Pisces", "Saturn": "Libra"
}

# Debilitation signs
DEBILITATION = {
    "Sun": "Libra", "Moon": "Scorpio", "Mars": "Cancer", "Mercury": "Pisces",
    "Jupiter": "Capricorn", "Venus": "Virgo", "Saturn": "Aries"
}

# Own signs (Moolatrikona)
OWN_SIGNS = {
    "Sun": "Leo", "Moon": "Taurus", "Mars": "Aries", "Mercury": "Virgo",
    "Jupiter": "Sagittarius", "Venus": "Libra", "Saturn": "Aquarius"
}

# Benefic planets
BENEFICS = ["Jupiter", "Venus", "Mercury", "Moon"]
MALEFICS = ["Sun", "Mars", "Saturn", "Rahu", "Ketu"]

def get_planet_in_house(chart, house_num):
    """Get all planets in a specific house"""
    planets = []
    for planet, data in chart.items():
        if planet != "ASCENDANT" and data.get("house") == house_num:
            planets.append((planet, data))
    return planets

def get_planet_position(chart, planet_name):
    """Get position of a specific planet"""
    return chart.get(planet_name)

def analyze_7th_house_d1():
    """Analyze 7th house in D1 chart"""
    print("\n" + "="*70)
    print("7TH HOUSE ANALYSIS (D1 - Main Chart)")
    print("="*70)
    
    d1 = CHART_DATA["D1"]
    planets_in_7th = get_planet_in_house(d1, 7)
    
    print(f"\n7th House Sign: Aquarius (Lord: Saturn)")
    print(f"Planets in 7th House:")
    
    if planets_in_7th:
        for planet, data in planets_in_7th:
            print(f"  - {planet}: {data['sign']} {data['degree']} (Lord: {data['lord']})")
    else:
        print("  - No planets in 7th house")
    
    # 7th lord analysis
    seventh_lord = "Saturn"
    saturn_d1 = get_planet_position(d1, "SATURN")
    print(f"\n7th Lord (Saturn) Placement:")
    print(f"  - Sign: {saturn_d1['sign']} (Own sign - Strong!)")
    print(f"  - House: {saturn_d1['house']} (7th house - Excellent for marriage)")
    print(f"  - Degree: {saturn_d1['degree']}")
    
    # Analysis
    print(f"\n📊 Analysis:")
    print(f"  ✓ Saturn in own sign Aquarius in 7th house is VERY STRONG")
    print(f"  ✓ This indicates a stable, mature, and committed marriage")
    print(f"  ✓ Spouse will be responsible, disciplined, and older in nature")
    print(f"  ✓ Marriage may come after some delay (Saturn's nature)")
    print(f"  ⚠ Saturn in 7th can indicate age difference or delayed marriage")

def analyze_navamsa():
    """Analyze Navamsa (D9) chart - Most important for marriage"""
    print("\n" + "="*70)
    print("NAVAMSA (D9) ANALYSIS - Marriage & Spirituality")
    print("="*70)
    
    d9 = CHART_DATA["D9"]
    
    # Navamsa Lagna
    print(f"\nNavamsa Lagna: Need to calculate from D1 ascendant")
    print(f"  (Typically Leo for your chart)")
    
    # 7th house in Navamsa
    print(f"\n7th House in Navamsa: Aquarius (Lord: Saturn)")
    planets_in_7th_d9 = get_planet_in_house(d9, 7)
    print(f"Planets in 7th House (Navamsa):")
    if planets_in_7th_d9:
        for planet, data in planets_in_7th_d9:
            print(f"  - {planet}: {data['sign']} {data['degree']}")
    else:
        print("  - No planets in 7th house")
    
    # Venus in Navamsa (most important for marriage)
    venus_d9 = get_planet_position(d9, "VENUS")
    print(f"\nVenus in Navamsa (Marriage Karaka):")
    print(f"  - Sign: {venus_d9['sign']} (Taurus - Own sign - EXCELLENT!)")
    print(f"  - House: {venus_d9['house']} (8th house)")
    print(f"  - Degree: {venus_d9['degree']}")
    print(f"  📊 Venus in own sign Taurus is VERY FAVORABLE for marriage")
    print(f"  ⚠ However, in 8th house indicates some challenges or transformations")
    
    # Jupiter in Navamsa (Spouse karaka)
    jupiter_d9 = get_planet_position(d9, "JUPITER")
    print(f"\nJupiter in Navamsa (Spouse Karaka):")
    print(f"  - Sign: {jupiter_d9['sign']} (Virgo)")
    print(f"  - House: {jupiter_d9['house']} (12th house)")
    print(f"  - Degree: {jupiter_d9['degree']}")
    print(f"  📊 Jupiter in Virgo (debilitated) in 12th house")
    print(f"  ⚠ This may indicate some challenges in spouse's nature or relationship")
    
    # Saturn in Navamsa
    saturn_d9 = get_planet_position(d9, "SATURN")
    print(f"\nSaturn in Navamsa:")
    print(f"  - Sign: {saturn_d9['sign']} (Aquarius - Own sign)")
    print(f"  - House: {saturn_d9['house']} (5th house)")
    print(f"  - Degree: {saturn_d9['degree']}")
    
    # Moon in Navamsa
    moon_d9 = get_planet_position(d9, "MOON")
    print(f"\nMoon in Navamsa (Mind & Emotions):")
    print(f"  - Sign: {moon_d9['sign']} (Cancer - Own sign)")
    print(f"  - House: {moon_d9['house']} (10th house)")
    print(f"  - Degree: {moon_d9['degree']}")
    print(f"  ✓ Moon in own sign indicates emotional stability in marriage")

def analyze_venus():
    """Analyze Venus - Marriage Karaka"""
    print("\n" + "="*70)
    print("VENUS ANALYSIS - Marriage Karaka")
    print("="*70)
    
    d1 = CHART_DATA["D1"]
    d9 = CHART_DATA["D9"]
    
    venus_d1 = get_planet_position(d1, "VENUS")
    venus_d9 = get_planet_position(d9, "VENUS")
    
    print(f"\nVenus in D1 (Main Chart):")
    print(f"  - Sign: {venus_d1['sign']} (Libra - Own sign - STRONG!)")
    print(f"  - House: {venus_d1['house']} (3rd house)")
    print(f"  - Degree: {venus_d1['degree']}")
    print(f"  ✓ Venus in own sign Libra indicates strong marriage prospects")
    print(f"  ✓ 3rd house placement shows spouse may be from nearby or through siblings")
    
    print(f"\nVenus in D9 (Navamsa):")
    print(f"  - Sign: {venus_d9['sign']} (Taurus - Own sign - EXCELLENT!)")
    print(f"  - House: {venus_d9['house']} (8th house)")
    print(f"  - Degree: {venus_d9['degree']}")
    print(f"  ✓ Double own sign placement (D1 and D9) is VERY FAVORABLE")
    print(f"  ⚠ 8th house in D9 indicates transformation through marriage")

def analyze_jupiter():
    """Analyze Jupiter - Spouse Karaka"""
    print("\n" + "="*70)
    print("JUPITER ANALYSIS - Spouse Karaka")
    print("="*70)
    
    d1 = CHART_DATA["D1"]
    d9 = CHART_DATA["D9"]
    
    jupiter_d1 = get_planet_position(d1, "JUPITER")
    jupiter_d9 = get_planet_position(d9, "JUPITER")
    
    print(f"\nJupiter in D1 (Main Chart):")
    print(f"  - Sign: {jupiter_d1['sign']} (Scorpio)")
    print(f"  - House: {jupiter_d1['house']} (4th house)")
    print(f"  - Degree: {jupiter_d1['degree']}")
    print(f"  📊 Jupiter in Scorpio (friend's sign) in 4th house")
    print(f"  ✓ Spouse may have good family background")
    
    print(f"\nJupiter in D9 (Navamsa):")
    print(f"  - Sign: {jupiter_d9['sign']} (Virgo - Debilitated)")
    print(f"  - House: {jupiter_d9['house']} (12th house)")
    print(f"  - Degree: {jupiter_d9['degree']}")
    print(f"  ⚠ Jupiter debilitated in 12th house may indicate some challenges")
    print(f"  ⚠ Spouse may be spiritual or may have some health issues")

def analyze_marriage_yogas():
    """Analyze marriage yogas"""
    print("\n" + "="*70)
    print("MARRIAGE YOGAS ANALYSIS")
    print("="*70)
    
    d1 = CHART_DATA["D1"]
    d9 = CHART_DATA["D9"]
    
    yogas = []
    
    # Venus in own sign in D1 and D9
    venus_d1 = get_planet_position(d1, "VENUS")
    venus_d9 = get_planet_position(d9, "VENUS")
    if venus_d1['sign'] == "Libra" and venus_d9['sign'] == "Taurus":
        yogas.append("✓ VENUS DOUBLE OWN SIGN YOGA - Excellent for marriage")
    
    # 7th lord in own sign
    saturn_d1 = get_planet_position(d1, "SATURN")
    if saturn_d1['sign'] == "Aquarius" and saturn_d1['house'] == 7:
        yogas.append("✓ 7TH LORD IN OWN SIGN IN 7TH HOUSE - Very strong marriage")
    
    # Moon in own sign in Navamsa
    moon_d9 = get_planet_position(d9, "MOON")
    if moon_d9['sign'] == "Cancer":
        yogas.append("✓ MOON IN OWN SIGN IN NAVAMSA - Emotional fulfillment in marriage")
    
    # Saturn in 7th house
    if saturn_d1['house'] == 7:
        yogas.append("⚠ SATURN IN 7TH HOUSE - Delayed but stable marriage")
    
    # Venus in 8th house in Navamsa
    if venus_d9['house'] == 8:
        yogas.append("⚠ VENUS IN 8TH HOUSE NAVAMSA - Transformation through marriage")
    
    print("\nDetected Yogas:")
    for yoga in yogas:
        print(f"  {yoga}")

def analyze_dasha_timing():
    """Analyze dasha periods for marriage timing"""
    print("\n" + "="*70)
    print("DASHA ANALYSIS - Marriage Timing")
    print("="*70)
    
    print("\nCurrent Period:")
    print("  - Mahadasha: Jupiter (2020-2036)")
    print("  - Antardasha: Jupiter-Mercury (Feb 2025 - May 2027)")
    
    print("\n🔮 Favorable Periods for Marriage:")
    
    # Jupiter-Mercury period
    print("\n1. Jupiter-Mercury Antardasha (Feb 2025 - May 2027):")
    print("   - Mercury is in 5th house (romance, love)")
    print("   - Jupiter aspects 7th house")
    print("   - This is a FAVORABLE period for marriage")
    
    # Jupiter-Venus period
    print("\n2. Jupiter-Venus Antardasha (Apr 2028 - Dec 2030):")
    print("   - Venus is marriage karaka in own sign")
    print("   - Jupiter-Venus combination is EXCELLENT for marriage")
    print("   - This is the MOST FAVORABLE period for marriage")
    
    # Jupiter-Sun period
    print("\n3. Jupiter-Sun Antardasha (Dec 2030 - Oct 2031):")
    print("   - Sun in 5th house (romance)")
    print("   - Moderate period for marriage")
    
    # Jupiter-Moon period
    print("\n4. Jupiter-Moon Antardasha (Oct 2031 - Feb 2033):")
    print("   - Moon in 2nd house (family)")
    print("   - Good period for marriage")
    
    print("\n📅 Specific Favorable Sub-Periods:")
    print("   - Jupiter-Mercury-Venus (Jul 2025 - Dec 2025): Good")
    print("   - Jupiter-Mercury-Sun (Dec 2025 - Jan 2026): Moderate")
    print("   - Jupiter-Mercury-Moon (Jan 2026 - Mar 2026): Good")
    print("   - Jupiter-Venus period (Apr 2028 - Dec 2030): BEST PERIOD")

def analyze_spouse_characteristics():
    """Analyze spouse characteristics"""
    print("\n" + "="*70)
    print("SPOUSE CHARACTERISTICS")
    print("="*70)
    
    d1 = CHART_DATA["D1"]
    d9 = CHART_DATA["D9"]
    
    saturn_d1 = get_planet_position(d1, "SATURN")
    venus_d9 = get_planet_position(d9, "VENUS")
    jupiter_d9 = get_planet_position(d9, "JUPITER")
    
    print("\nBased on 7th House and Navamsa:")
    print(f"  - 7th House Sign: Aquarius (Saturn ruled)")
    print(f"  - Spouse will be:")
    print(f"    • Mature, responsible, and disciplined")
    print(f"    • Independent and freedom-loving (Aquarius)")
    print(f"    • May be older or more mature in thinking")
    print(f"    • Scientific, technical, or humanitarian nature")
    print(f"    • May have some delays or challenges in early life")
    
    print(f"\n  - Venus in Navamsa (Taurus, 8th house):")
    print(f"    • Spouse will be beautiful/attractive")
    print(f"    • Materially comfortable")
    print(f"    • May bring transformation in your life")
    print(f"    • Strong values and principles")
    
    print(f"\n  - Jupiter in Navamsa (Virgo, 12th house):")
    print(f"    • Spouse may be spiritual or religious")
    print(f"    • May have some health concerns")
    print(f"    • May be from a different background or foreign connection")

def generate_summary():
    """Generate overall summary"""
    print("\n" + "="*70)
    print("OVERALL MARRIAGE ANALYSIS SUMMARY")
    print("="*70)
    
    print("\n✅ STRENGTHS:")
    print("  1. Venus in own sign Libra (D1) and Taurus (D9) - EXCELLENT")
    print("  2. 7th lord Saturn in own sign Aquarius in 7th house - VERY STRONG")
    print("  3. Moon in own sign Cancer in Navamsa - Emotional stability")
    print("  4. Strong Jupiter-Venus period coming (2028-2030) - Best timing")
    
    print("\n⚠️  CHALLENGES:")
    print("  1. Saturn in 7th house - Delayed marriage (likely after 30)")
    print("  2. Venus in 8th house Navamsa - Some transformation needed")
    print("  3. Jupiter debilitated in Navamsa - Some challenges in spouse")
    
    print("\n🎯 RECOMMENDATIONS:")
    print("  1. Most favorable period: April 2028 - December 2030 (Jupiter-Venus)")
    print("  2. Good period: February 2025 - May 2027 (Jupiter-Mercury)")
    print("  3. Spouse will be mature, responsible, and from good family")
    print("  4. Marriage will be stable and long-lasting")
    print("  5. Some delay is indicated but marriage will be strong")
    
    print("\n💡 ADDITIONAL NOTES:")
    print("  - Rahu-Ketu axis in 3rd-9th houses may indicate spouse from")
    print("    different background or through travel/communication")
    print("  - Strong 5th house (Sun, Mercury, Neptune) indicates")
    print("    romantic nature and good relationship with children")
    print("  - 7th house Saturn suggests marriage after maturity and")
    print("    through arranged or traditional means")

def main():
    """Main analysis function"""
    print("\n" + "="*70)
    print("MARRIAGE ANALYSIS FOR AKSHIT")
    print("="*70)
    print("\nThis analysis is based on Vedic Astrology principles")
    print("Focusing on D1 (Birth Chart), D9 (Navamsa), and Dasha periods")
    
    analyze_7th_house_d1()
    analyze_navamsa()
    analyze_venus()
    analyze_jupiter()
    analyze_marriage_yogas()
    analyze_dasha_timing()
    analyze_spouse_characteristics()
    generate_summary()
    
    print("\n" + "="*70)
    print("END OF ANALYSIS")
    print("="*70)
    print("\nNote: This is a general analysis. For specific predictions,")
    print("consult with a qualified Vedic astrologer who can consider")
    print("transits, ashtakavarga, and other advanced techniques.")

if __name__ == "__main__":
    main()
