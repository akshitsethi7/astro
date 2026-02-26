#!/usr/bin/env python3
"""
Quick Analysis Script - Fast chart overview
"""

from chart_analyzer import ChartAnalyzer
from knowledge_analyzer import KnowledgeAnalyzer
import json

def quick_analysis():
    """Run a quick analysis and display key insights"""
    
    print("\n" + "="*80)
    print("QUICK CHART ANALYSIS")
    print("="*80 + "\n")
    
    # Initialize
    analyzer = ChartAnalyzer()
    kb_analyzer = KnowledgeAnalyzer(analyzer)
    
    # Basic Info
    d1 = analyzer.get_d1_chart()
    asc = d1.get('ascendant', {})
    
    print("📊 CHART BASICS")
    print("-" * 80)
    print(f"Ascendant: {asc.get('sign')} at {asc.get('degree')}°")
    print(f"Ascendant Lord: {asc.get('lord')}")
    print(f"Nakshatra: {asc.get('nakshatra')}")
    
    # Current Dasha
    current = analyzer.get_current_dasha()
    if current:
        print(f"\nCurrent Mahadasha: {current['name']}")
        print(f"Period: {current['start'][:10]} to {current['end'][:10]}")
    
    # Planetary Strengths
    print("\n\n⭐ PLANETARY STRENGTHS")
    print("-" * 80)
    strengths = analyzer.analyze_planetary_strengths()
    
    if strengths['strong_planets']:
        print("\nStrong Planets:")
        for p in strengths['strong_planets']:
            print(f"  ✓ {p['name']} in {p['sign']} ({p['dignity']})")
    
    if strengths['weak_planets']:
        print("\nWeak Planets:")
        for p in strengths['weak_planets']:
            print(f"  ⚠ {p['name']} in {p['sign']} ({p['dignity']})")
    
    if strengths['combust_planets']:
        print("\nCombust Planets:")
        for p in strengths['combust_planets']:
            print(f"  🔥 {p['name']}")
    
    # Key Yogas
    print("\n\n🔮 ACTIVE YOGAS")
    print("-" * 80)
    yogas = analyzer.get_yogas()
    yoga_count = 0
    
    for category in yogas:
        active = [y for y in category.get('yoga_list', []) if y['has_yoga']]
        if active:
            print(f"\n{category['name']}:")
            for yoga in active[:3]:
                print(f"  ✓ {yoga['name']}")
                yoga_count += 1
    
    print(f"\nTotal Active Yogas: {yoga_count}")
    
    # Marriage Quick View
    print("\n\n💑 MARRIAGE OVERVIEW")
    print("-" * 80)
    marriage = analyzer.analyze_marriage_prospects()
    
    for factor in marriage['factors'][:2]:
        print(f"\n{factor['factor']}:")
        for key, value in list(factor.items())[:4]:
            if key != 'factor':
                print(f"  • {key}: {value}")
    
    if marriage['challenges']:
        print("\n⚠ Challenges:")
        for challenge in marriage['challenges']:
            if isinstance(challenge, dict):
                print(f"  • {challenge['challenge']}")
    
    # Career Quick View
    print("\n\n💼 CAREER OVERVIEW")
    print("-" * 80)
    career = analyzer.analyze_career_prospects()
    
    for factor in career['factors'][:2]:
        print(f"\n{factor['factor']}:")
        for key, value in list(factor.items())[:4]:
            if key != 'factor':
                print(f"  • {key}: {value}")
    
    if career['strengths']:
        print("\n✓ Strengths:")
        for strength in career['strengths'][:2]:
            if isinstance(strength, dict):
                print(f"  • {strength['yoga']}")
    
    # Next Steps
    print("\n\n" + "="*80)
    print("NEXT STEPS")
    print("="*80)
    print("\nFor detailed analysis, run:")
    print("  python3 analyze_chart.py")
    print("\nFor full report:")
    print("  python3 report_generator.py")
    print("\nFor data validation:")
    print("  python3 data_validator.py")
    print("\n" + "="*80 + "\n")


if __name__ == "__main__":
    quick_analysis()
