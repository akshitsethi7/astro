#!/usr/bin/env python3
"""
Akshit's Chart Analysis - Comprehensive analysis using knowledge base
"""

import json
from datetime import datetime

def load_chart():
    """Load Akshit's chart data"""
    with open('akshit_chart.json', 'r') as f:
        return json.load(f)

def load_dasha_data():
    """Load dasha data from chartsimp.json"""
    with open('chartsimp.json', 'r') as f:
        data = json.load(f)
        return data.get('data', {})

def analyze_chart():
    """Comprehensive chart analysis"""
    
    chart = load_chart()
    dasha_data = load_dasha_data()
    d1 = chart['D1']
    d9 = chart['D9']
    d10 = chart['D10']
    
    print("="*80)
    print("AKSHIT'S COMPREHENSIVE CHART ANALYSIS")
    print("="*80)
    print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    
    # CHART OVERVIEW
    print("\n" + "="*80)
    print("CHART OVERVIEW (D1 - Birth Chart)")
    print("="*80)
    
    asc = d1['ascendant']
    print(f"\nAscendant (Lagna): {asc['sign']} at {asc['degree']}°")
    print(f"Ascendant Lord: {asc['lord']}")
    print(f"Ascendant Nakshatra: {asc['nakshatra']}")
    print(f"\nChart Type: Leo Ascendant (Fire Sign, Fixed, Ruled by Sun)")

    
    # PLANETARY POSITIONS
    print("\n" + "="*80)
    print("PLANETARY POSITIONS & STRENGTHS")
    print("="*80)
    
    print(f"\n{'Planet':<12} {'Sign':<15} {'House':<8} {'Nakshatra':<20} {'Dignity':<15}")
    print("-"*80)
    
    for planet in d1['planets']:
        print(f"{planet['name']:<12} {planet['sign']:<15} {planet['house']:<8} "
              f"{planet['nakshatra']:<20} {planet['dignity']:<15}")
    
    # STRONG PLANETS
    print("\n✓ STRONG PLANETS:")
    print("  • Venus in Libra (EXALTED) - House 3")
    print("    → Excellent for communication, creativity, relationships")
    print("  • Saturn in Aquarius (OWN SIGN) - House 7")
    print("    → Strong for marriage, partnerships, discipline")
    print("  • Mars in Leo (Ascendant) - House 1")
    print("    → Good energy, confidence, leadership")
    
    print("\n⚠ COMBUST PLANETS:")
    print("  • Mercury (combust by Sun in Sagittarius)")
    print("    → Communication may need extra effort")
    
    # CURRENT DASHA
    print("\n" + "="*80)
    print("CURRENT DASHA PERIOD (Vimshottari)")
    print("="*80)
    
    dasha_balance = dasha_data.get('dasha_balance', {})
    dasha_periods = dasha_data.get('dasha_periods', [])
    
    if dasha_balance:
        lord = dasha_balance.get('lord', {})
        print(f"\nCurrent Mahadasha: {lord.get('name', 'N/A')}")
        print(f"Balance Remaining: {dasha_balance.get('description', 'N/A')}")
    
    # Find current period
    current_date = datetime.now()
    current_period = None
    
    for period in dasha_periods:
        try:
            start = datetime.fromisoformat(period['start'].replace('+05:30', ''))
            end = datetime.fromisoformat(period['end'].replace('+05:30', ''))
            if start <= current_date <= end:
                current_period = period
                break
        except:
            continue
    
    if current_period:
        print(f"\nMahadasha: {current_period['name']}")
        print(f"Period: {current_period['start'][:10]} to {current_period['end'][:10]}")
        
        # Find current antardasha
        for antardasha in current_period.get('antardasha', []):
            try:
                start = datetime.fromisoformat(antardasha['start'].replace('+05:30', ''))
                end = datetime.fromisoformat(antardasha['end'].replace('+05:30', ''))
                if start <= current_date <= end:
                    print(f"Current Antardasha: {antardasha['name']}")
                    print(f"Period: {antardasha['start'][:10]} to {antardasha['end'][:10]}")
                    break
            except:
                continue

    
    # MARRIAGE ANALYSIS
    print("\n" + "="*80)
    print("MARRIAGE ANALYSIS (Detailed)")
    print("="*80)
    
    print("\n1. 7TH HOUSE ANALYSIS (Primary Marriage House)")
    print("-"*80)
    print("   Sign: Aquarius (Saturn's sign)")
    print("   Lord: Saturn")
    print("   Saturn Position: House 7 itself (Own Sign - VERY STRONG)")
    print("   Planets in 7th: Saturn")
    
    print("\n   INTERPRETATION:")
    print("   ✓ Saturn in own sign in 7th house is EXCELLENT for marriage")
    print("   ✓ Indicates stable, long-lasting, committed relationship")
    print("   ✓ Spouse will be mature, responsible, disciplined")
    print("   ✓ May marry slightly later but marriage will be strong")
    print("   ✓ Partner may be older or more mature")
    print("   ✓ Relationship based on duty, commitment, and mutual respect")
    
    print("\n2. VENUS ANALYSIS (Karaka for Marriage)")
    print("-"*80)
    print("   Position: House 3, Libra (EXALTED)")
    print("   Nakshatra: Swati")
    print("   Dignity: Exalted (Best possible position)")
    
    print("\n   INTERPRETATION:")
    print("   ✓ EXALTED Venus is extremely auspicious for marriage")
    print("   ✓ Strong desire for love, romance, and partnership")
    print("   ✓ Attractive personality, charming nature")
    print("   ✓ Will attract good partners")
    print("   ✓ Love for beauty, arts, harmony in relationships")
    print("   ✓ Venus in 3rd house: communication in relationships is key")
    
    print("\n3. JUPITER ANALYSIS (Karaka for Husband in Female Chart)")
    print("-"*80)
    print("   Position: House 4, Scorpio")
    print("   Nakshatra: Jyeshtha")
    
    print("\n   INTERPRETATION:")
    print("   • Jupiter in 4th house: spouse brings happiness to home")
    print("   • Scorpio placement: deep, transformative relationship")
    print("   • Partner may be intense, passionate, protective")
    
    print("\n4. NAVAMSA (D9) ANALYSIS - Marriage Chart")
    print("-"*80)
    d9_asc = d9['ascendant']
    print(f"   D9 Ascendant: {d9_asc['sign']}")
    
    # Find Venus in D9
    venus_d9 = next((p for p in d9['planets'] if p['name'] == 'Venus'), None)
    if venus_d9:
        print(f"   Venus in D9: {venus_d9['sign']} (House {venus_d9['house']})")
        if venus_d9['sign'] == 'Taurus':
            print("   ✓ Venus in own sign in D9 - EXCELLENT for marriage")
    
    # Find Jupiter in D9
    jupiter_d9 = next((p for p in d9['planets'] if p['name'] == 'Jupiter'), None)
    if jupiter_d9:
        print(f"   Jupiter in D9: {jupiter_d9['sign']} (House {jupiter_d9['house']})")
        if jupiter_d9['sign'] == 'Virgo':
            print("   • Jupiter in Virgo in D9 - practical, service-oriented spouse")

    
    print("\n5. MARRIAGE TIMING ANALYSIS")
    print("-"*80)
    
    # Analyze dashas for marriage timing
    print("\n   Favorable Periods for Marriage:")
    
    for period in dasha_periods[:10]:
        planet = period['name']
        start = period['start'][:10]
        end = period['end'][:10]
        
        # Check if planet is connected to 7th house or marriage
        if planet in ['Venus', 'Saturn', 'Jupiter']:
            print(f"\n   • {planet} Mahadasha: {start} to {end}")
            
            if planet == 'Venus':
                print("     → Venus dasha HIGHLY favorable (exalted Venus)")
            elif planet == 'Saturn':
                print("     → Saturn dasha favorable (7th lord in 7th)")
            elif planet == 'Jupiter':
                print("     → Jupiter dasha good (natural benefic)")
            
            # Show some antardashas
            for antardasha in period.get('antardasha', [])[:3]:
                ad_planet = antardasha['name']
                ad_start = antardasha['start'][:10]
                ad_end = antardasha['end'][:10]
                if ad_planet in ['Venus', 'Saturn', 'Jupiter']:
                    print(f"       - {ad_planet} Antardasha: {ad_start} to {ad_end}")
    
    print("\n6. SPOUSE CHARACTERISTICS")
    print("-"*80)
    print("   Based on 7th house (Aquarius) and Saturn:")
    print("   • Mature, responsible, disciplined")
    print("   • Independent thinker, humanitarian values")
    print("   • Serious about commitments")
    print("   • May be in service/social work/technology")
    print("   • Practical, grounded approach to life")
    print("   • Values tradition and stability")
    
    print("\n   Based on Venus (Exalted in Libra):")
    print("   • Beautiful/handsome appearance")
    print("   • Refined taste, cultured")
    print("   • Diplomatic, balanced personality")
    print("   • Artistic or creative inclinations")
    print("   • Values harmony and peace")
    
    print("\n7. MARRIAGE YOGAS & DOSHAS")
    print("-"*80)
    
    yogas = dasha_data.get('yoga_details', [])
    
    # Check for Kuja Dosha
    mangal_dosha = dasha_data.get('mangal_dosha', {})
    has_dosha = mangal_dosha.get('has_dosha', False) or dasha_data.get('has_dosha', False)
    
    if has_dosha:
        print("   ⚠ KUJA DOSHA (Manglik) Present")
        print("   • Mars in 1st house creates Kuja Dosha")
        print("   • REMEDIES:")
        remedies = dasha_data.get('remedies', [])
        for remedy in remedies[:3]:
            print(f"     - {remedy}")
        print("   • NOTE: Saturn's strong position in 7th reduces negative effects")
    
    # Check for beneficial yogas
    for category in yogas:
        if category.get('name') == 'Major Yogas':
            for yoga in category.get('yoga_list', []):
                if yoga.get('has_yoga') and 'Raja' in yoga.get('name', ''):
                    print(f"\n   ✓ {yoga['name']}")
                    print(f"     {yoga.get('description', '')[:150]}...")
    
    print("\n8. OVERALL MARRIAGE ASSESSMENT")
    print("-"*80)
    print("   STRENGTHS:")
    print("   ✓✓✓ Exalted Venus - Excellent for love and marriage")
    print("   ✓✓✓ Saturn in own sign in 7th - Very strong for stable marriage")
    print("   ✓✓ Good D9 placements")
    print("   ✓ Multiple favorable dasha periods")
    
    print("\n   CONSIDERATIONS:")
    print("   • Kuja Dosha present - but mitigated by strong Saturn")
    print("   • May marry slightly later (Saturn's influence)")
    print("   • But marriage will be stable and long-lasting")
    
    print("\n   RECOMMENDATION:")
    print("   Marriage prospects are VERY FAVORABLE overall.")
    print("   The combination of exalted Venus and strong Saturn in 7th")
    print("   indicates a happy, stable, and harmonious married life.")

    
    # CAREER ANALYSIS
    print("\n\n" + "="*80)
    print("CAREER ANALYSIS (Detailed)")
    print("="*80)
    
    print("\n1. 10TH HOUSE ANALYSIS (Career House)")
    print("-"*80)
    print("   Sign: Taurus (Venus's sign)")
    print("   Lord: Venus")
    print("   Venus Position: House 3, Libra (EXALTED)")
    print("   Planets in 10th: None")
    
    print("\n   INTERPRETATION:")
    print("   ✓ 10th lord Venus is EXALTED - Excellent for career")
    print("   ✓ Venus in 3rd house: communication, media, arts, business")
    print("   ✓ Taurus 10th house: stable career, finance, luxury goods")
    print("   ✓ Strong potential for success in creative fields")
    
    print("\n2. SUN ANALYSIS (Karaka for Career/Authority)")
    print("-"*80)
    print("   Position: House 5, Sagittarius")
    print("   Nakshatra: Purva Ashadha")
    
    print("\n   INTERPRETATION:")
    print("   • Sun in 5th house: creative leadership")
    print("   • Sagittarius: teaching, philosophy, higher learning")
    print("   • Good for education, speculation, creative work")
    
    print("\n3. SATURN ANALYSIS (Karaka for Service/Work)")
    print("-"*80)
    print("   Position: House 7, Aquarius (OWN SIGN)")
    
    print("\n   INTERPRETATION:")
    print("   ✓ Strong Saturn: disciplined, hardworking")
    print("   • 7th house: partnerships, business, public dealing")
    print("   • May work in partnerships or with public")
    
    print("\n4. D10 ANALYSIS (Career Chart)")
    print("-"*80)
    d10_asc = d10['ascendant']
    print(f"   D10 Ascendant: {d10_asc['sign']}")
    
    # Check planets in D10
    print("\n   Key Planets in D10:")
    for planet in d10['planets']:
        if planet['house'] in [1, 10]:
            print(f"   • {planet['name']} in {planet['sign']} (House {planet['house']})")
    
    print("\n5. SUITABLE CAREER FIELDS")
    print("-"*80)
    print("   Based on Exalted Venus (10th lord) in 3rd house:")
    print("   ✓ Media & Communication")
    print("   ✓ Arts & Entertainment")
    print("   ✓ Fashion & Design")
    print("   ✓ Luxury Goods & Services")
    print("   ✓ Marketing & Advertising")
    print("   ✓ Public Relations")
    print("   ✓ Creative Writing")
    print("   ✓ Music & Performing Arts")
    
    print("\n   Based on Sun in 5th house (Sagittarius):")
    print("   • Education & Teaching")
    print("   • Philosophy & Counseling")
    print("   • Speculation & Investment")
    print("   • Sports & Entertainment")
    
    print("\n   Based on Strong Saturn:")
    print("   • Technology & IT")
    print("   • Engineering")
    print("   • Administration")
    print("   • Long-term projects")
    
    print("\n6. CAREER TIMING")
    print("-"*80)
    print("   Favorable Periods:")
    
    for period in dasha_periods[:8]:
        planet = period['name']
        if planet in ['Venus', 'Sun', 'Saturn', 'Mercury']:
            start = period['start'][:10]
            end = period['end'][:10]
            print(f"\n   • {planet} Mahadasha: {start} to {end}")
            
            if planet == 'Venus':
                print("     → EXCELLENT for career (10th lord, exalted)")
            elif planet == 'Sun':
                print("     → Good for authority, leadership positions")
            elif planet == 'Saturn':
                print("     → Steady growth, long-term success")
            elif planet == 'Mercury':
                print("     → Good for communication-based careers")
    
    print("\n7. CAREER YOGAS")
    print("-"*80)
    
    for category in yogas:
        if category.get('name') == 'Major Yogas':
            for yoga in category.get('yoga_list', []):
                if yoga.get('has_yoga'):
                    name = yoga.get('name', '')
                    if any(word in name for word in ['Raja', 'Malavya', 'Sasa']):
                        print(f"\n   ✓ {name}")
                        desc = yoga.get('description', '')
                        print(f"     {desc[:200]}...")
    
    print("\n8. OVERALL CAREER ASSESSMENT")
    print("-"*80)
    print("   STRENGTHS:")
    print("   ✓✓✓ Exalted Venus as 10th lord - Exceptional career potential")
    print("   ✓✓ Strong Saturn - Discipline and perseverance")
    print("   ✓✓ Sun in 5th - Creative leadership")
    print("   ✓ Multiple beneficial yogas")
    
    print("\n   BEST CAREER PATH:")
    print("   Creative fields with communication/media focus")
    print("   Combining art, beauty, and business")
    print("   Leadership roles in creative industries")
    
    print("\n   SUCCESS INDICATORS:")
    print("   Very high potential for career success")
    print("   Natural talent + hard work = Excellence")
    print("   Fame and recognition likely in chosen field")

    
    # LIFE PATH & RECOMMENDATIONS
    print("\n\n" + "="*80)
    print("LIFE PATH & RECOMMENDATIONS")
    print("="*80)
    
    print("\n1. KEY STRENGTHS TO LEVERAGE")
    print("-"*80)
    print("   • Exalted Venus: Use your charm, creativity, artistic talents")
    print("   • Strong Saturn: Your discipline and perseverance are assets")
    print("   • Mars in Ascendant: Confidence, energy, leadership")
    print("   • Leo Ascendant: Natural leadership, charisma")
    
    print("\n2. AREAS TO DEVELOP")
    print("-"*80)
    print("   • Mercury combust: Work on clear communication")
    print("   • Kuja Dosha: Practice patience in relationships")
    print("   • Balance fire (Leo) with earth (Saturn) energies")
    
    print("\n3. REMEDIES & PRACTICES")
    print("-"*80)
    print("   For Venus (already strong, maintain):")
    print("   • Wear white/light colors on Fridays")
    print("   • Engage in arts, music, beauty")
    print("   • Maintain harmonious relationships")
    
    print("\n   For Saturn (strengthen further):")
    print("   • Wear blue/black on Saturdays")
    print("   • Practice discipline and routine")
    print("   • Serve the elderly or underprivileged")
    print("   • Chant Saturn mantras")
    
    print("\n   For Kuja Dosha:")
    print("   • Visit Hanuman temple on Tuesdays")
    print("   • Chant Hanuman Chalisa")
    print("   • Fast on Tuesdays (optional)")
    print("   • Donate red items on Tuesdays")
    
    print("\n   For Mercury (combust):")
    print("   • Wear green on Wednesdays")
    print("   • Practice clear communication")
    print("   • Study and learning activities")
    
    print("\n4. LIFE TIMELINE (Key Periods)")
    print("-"*80)
    
    # Show next 5 major periods
    print("\n   Upcoming Major Periods:")
    for i, period in enumerate(dasha_periods[:5], 1):
        planet = period['name']
        start = period['start'][:10]
        end = period['end'][:10]
        print(f"\n   {i}. {planet} Mahadasha: {start} to {end}")
        
        # Give brief interpretation
        interpretations = {
            'Moon': 'Emotional growth, family focus, public dealings',
            'Mars': 'Energy, action, courage, property matters',
            'Rahu': 'Unconventional paths, foreign connections, technology',
            'Jupiter': 'Wisdom, expansion, teaching, spirituality',
            'Saturn': 'Discipline, hard work, long-term success',
            'Mercury': 'Communication, business, intellectual pursuits',
            'Ketu': 'Spirituality, detachment, research',
            'Venus': 'Love, luxury, arts, relationships, wealth',
            'Sun': 'Authority, leadership, government, father'
        }
        
        if planet in interpretations:
            print(f"       Focus: {interpretations[planet]}")
    
    print("\n5. OVERALL LIFE ASSESSMENT")
    print("-"*80)
    print("   Chart Quality: EXCELLENT")
    print("   • Strong benefics (Venus, Jupiter)")
    print("   • Well-placed Saturn for stability")
    print("   • Good yogas for success")
    print("   • Balanced chart with growth potential")
    
    print("\n   Life Themes:")
    print("   • Creative expression and leadership")
    print("   • Stable relationships and partnerships")
    print("   • Career success through talent + discipline")
    print("   • Balance between material and spiritual")
    
    print("\n   Advice:")
    print("   • Trust your creative instincts")
    print("   • Build on your natural charm and communication skills")
    print("   • Be patient with relationships - quality over speed")
    print("   • Combine your artistic talents with business acumen")
    print("   • Stay disciplined and focused on long-term goals")
    
    print("\n" + "="*80)
    print("END OF COMPREHENSIVE ANALYSIS")
    print("="*80)
    print("\nNote: This analysis uses classical Vedic astrology principles")
    print("combined with your specific chart data and dasha periods.")
    print("\nFor personalized guidance, consult with a qualified astrologer.")
    print("="*80 + "\n")


if __name__ == "__main__":
    analyze_chart()
