#!/usr/bin/env python3
"""
Master Chart Analysis Script
Runs all analysis modules and generates comprehensive reports
"""

import sys
import json
from datetime import datetime
from chart_analyzer import ChartAnalyzer
from report_generator import ReportGenerator
from data_validator import DataValidator
from knowledge_analyzer import KnowledgeAnalyzer

def main():
    """Main analysis workflow"""
    
    print("=" * 80)
    print("COMPREHENSIVE CHART ANALYSIS SYSTEM")
    print("=" * 80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Step 1: Validate data
    print("Step 1: Validating chart data...")
    print("-" * 80)
    validator = DataValidator()
    errors, warnings = validator.validate_all()
    validator.print_report()
    
    if errors:
        print("\n⚠ Found errors in data. Proceeding with caution...")
    else:
        print("\n✓ Data validation passed!")
    
    input("\nPress Enter to continue to analysis...")
    
    # Step 2: Initialize analyzers
    print("\n\nStep 2: Initializing analysis engines...")
    print("-" * 80)
    analyzer = ChartAnalyzer()
    kb_analyzer = KnowledgeAnalyzer(analyzer)
    report_gen = ReportGenerator(analyzer)
    print("✓ Analyzers initialized")
    
    # Step 3: Run analyses
    print("\n\nStep 3: Running comprehensive analysis...")
    print("-" * 80)
    
    # Basic chart info
    print("\n📊 CHART OVERVIEW:")
    d1 = analyzer.get_d1_chart()
    asc = d1.get('ascendant', {})
    print(f"  Ascendant: {asc.get('sign')} at {asc.get('degree')}°")
    print(f"  Ascendant Lord: {asc.get('lord')}")
    print(f"  Nakshatra: {asc.get('nakshatra')}")
    
    # Current dasha
    current_dasha = analyzer.get_current_dasha()
    if current_dasha:
        print(f"\n  Current Mahadasha: {current_dasha['name']}")
        print(f"  Period: {current_dasha['start'][:10]} to {current_dasha['end'][:10]}")
    
    input("\nPress Enter to continue...")
    
    # Marriage analysis
    print("\n\n💑 MARRIAGE ANALYSIS:")
    print("-" * 80)
    marriage = kb_analyzer.analyze_marriage_with_knowledge()
    
    print("\nKey Factors:")
    for factor in marriage['detailed_factors'][:3]:
        print(f"\n  {factor['category']}:")
        for key, value in factor.items():
            if key not in ['category', 'interpretation']:
                print(f"    • {key}: {value}")
        if 'interpretation' in factor:
            print(f"    → {factor['interpretation']}")
    
    if marriage['timing_indicators']:
        print("\n  Favorable Timing:")
        for timing in marriage['timing_indicators']:
            print(f"    • {timing['period']}: {timing['timeframe']}")
    
    input("\nPress Enter to continue...")
    
    # Career analysis
    print("\n\n💼 CAREER ANALYSIS:")
    print("-" * 80)
    career = kb_analyzer.analyze_career_with_knowledge()
    
    print("\nKey Factors:")
    for factor in career['detailed_factors'][:3]:
        print(f"\n  {factor['category']}:")
        for key, value in factor.items():
            if key not in ['category', 'interpretation']:
                print(f"    • {key}: {value}")
        if 'interpretation' in factor:
            print(f"    → {factor['interpretation']}")
    
    if career['suitable_professions']:
        print("\n  Suitable Professions:")
        for prof in career['suitable_professions'][:5]:
            print(f"    • {prof}")
    
    input("\nPress Enter to continue...")
    
    # Yogas
    print("\n\n🔮 ACTIVE YOGAS:")
    print("-" * 80)
    yogas = analyzer.get_yogas()
    
    for category in yogas:
        active = [y for y in category.get('yoga_list', []) if y['has_yoga']]
        if active:
            print(f"\n  {category['name']}:")
            for yoga in active[:3]:
                print(f"    ✓ {yoga['name']}")
    
    input("\nPress Enter to continue...")
    
    # Planetary strengths
    print("\n\n⭐ PLANETARY STRENGTHS:")
    print("-" * 80)
    strengths = analyzer.analyze_planetary_strengths()
    
    if strengths['strong_planets']:
        print("\n  Strong Planets:")
        for p in strengths['strong_planets']:
            print(f"    ✓ {p['name']} in {p['sign']} ({p['dignity']})")
    
    if strengths['weak_planets']:
        print("\n  Weak Planets:")
        for p in strengths['weak_planets']:
            print(f"    ⚠ {p['name']} in {p['sign']} ({p['dignity']})")
    
    if strengths['combust_planets']:
        print("\n  Combust Planets:")
        for p in strengths['combust_planets']:
            print(f"    🔥 {p['name']}")
    
    input("\nPress Enter to generate reports...")
    
    # Step 4: Generate reports
    print("\n\nStep 4: Generating detailed reports...")
    print("-" * 80)
    
    # Text report
    print("\n  Generating comprehensive text report...")
    report_gen.generate_complete_report('COMPLETE_CHART_REPORT.txt')
    print("  ✓ Saved: COMPLETE_CHART_REPORT.txt")
    
    # JSON reports
    print("\n  Generating JSON reports...")
    
    with open('marriage_analysis.json', 'w') as f:
        json.dump(marriage, f, indent=2)
    print("  ✓ Saved: marriage_analysis.json")
    
    with open('career_analysis.json', 'w') as f:
        json.dump(career, f, indent=2)
    print("  ✓ Saved: career_analysis.json")
    
    # Dasha timeline
    timeline = analyzer.generate_dasha_timeline(10)
    with open('dasha_timeline.json', 'w') as f:
        json.dump(timeline, f, indent=2)
    print("  ✓ Saved: dasha_timeline.json")
    
    # Summary
    print("\n\n" + "=" * 80)
    print("ANALYSIS COMPLETE!")
    print("=" * 80)
    print("\nGenerated Files:")
    print("  1. COMPLETE_CHART_REPORT.txt - Comprehensive text report")
    print("  2. marriage_analysis.json - Detailed marriage analysis")
    print("  3. career_analysis.json - Detailed career analysis")
    print("  4. dasha_timeline.json - 10-year dasha timeline")
    print("\n" + "=" * 80)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAnalysis interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
