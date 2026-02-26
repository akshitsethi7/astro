#!/usr/bin/env python3
"""
Report Generator - Creates comprehensive astrological reports
"""

import json
from datetime import datetime
from chart_analyzer import ChartAnalyzer

class ReportGenerator:
    """Generate detailed astrological reports"""
    
    def __init__(self, analyzer: ChartAnalyzer):
        self.analyzer = analyzer
    
    def generate_complete_report(self, output_file: str = None) -> str:
        """Generate a complete astrological report"""
        report = []
        
        # Header
        report.append("=" * 80)
        report.append("COMPREHENSIVE ASTROLOGICAL ANALYSIS REPORT")
        report.append("=" * 80)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 80)
        report.append("")
        
        # Chart Overview
        report.extend(self._generate_chart_overview())
        
        # Planetary Positions
        report.extend(self._generate_planetary_positions())
        
        # Yogas
        report.extend(self._generate_yoga_analysis())
        
        # Marriage Analysis
        report.extend(self._generate_marriage_report())
        
        # Career Analysis
        report.extend(self._generate_career_report())
        
        # Dasha Analysis
        report.extend(self._generate_dasha_report())
        
        # Divisional Charts Summary
        report.extend(self._generate_divisional_charts_summary())
        
        # Recommendations
        report.extend(self._generate_recommendations())
        
        report_text = "\n".join(report)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report_text)
            print(f"Report saved to: {output_file}")
        
        return report_text
    
    def _generate_chart_overview(self) -> list:
        """Generate chart overview section"""
        lines = []
        d1 = self.analyzer.get_d1_chart()
        
        lines.append("\n" + "=" * 80)
        lines.append("CHART OVERVIEW")
        lines.append("=" * 80)
        
        asc = d1.get('ascendant', {})
        lines.append(f"\nAscendant (Lagna): {asc.get('sign', 'N/A')} ({asc.get('degree', 'N/A')}°)")
        lines.append(f"Ascendant Lord: {asc.get('lord', 'N/A')}")
        lines.append(f"Ascendant Nakshatra: {asc.get('nakshatra', 'N/A')}")
        
        return lines
    
    def _generate_planetary_positions(self) -> list:
        """Generate planetary positions section"""
        lines = []
        d1 = self.analyzer.get_d1_chart()
        
        lines.append("\n" + "=" * 80)
        lines.append("PLANETARY POSITIONS (D1 - Rashi Chart)")
        lines.append("=" * 80)
        lines.append("")
        
        lines.append(f"{'Planet':<12} {'Sign':<15} {'House':<8} {'Nakshatra':<20} {'Dignity':<15} {'Status':<15}")
        lines.append("-" * 100)
        
        for planet in d1.get('planets', []):
            status = []
            if planet.get('combust'):
                status.append('Combust')
            if planet.get('retrograde'):
                status.append('Retrograde')
            status_str = ', '.join(status) if status else 'Normal'
            
            lines.append(
                f"{planet['name']:<12} "
                f"{planet['sign']:<15} "
                f"{planet['house']:<8} "
                f"{planet['nakshatra']:<20} "
                f"{planet['dignity']:<15} "
                f"{status_str:<15}"
            )
        
        # Planetary strengths
        strengths = self.analyzer.analyze_planetary_strengths()
        
        if strengths['strong_planets']:
            lines.append("\nSTRONG PLANETS:")
            for p in strengths['strong_planets']:
                lines.append(f"  • {p['name']} in {p['sign']} ({p['dignity']})")
        
        if strengths['weak_planets']:
            lines.append("\nWEAK PLANETS:")
            for p in strengths['weak_planets']:
                lines.append(f"  • {p['name']} in {p['sign']} ({p['dignity']})")
        
        if strengths['combust_planets']:
            lines.append("\nCOMBUST PLANETS (weakened by Sun):")
            for p in strengths['combust_planets']:
                lines.append(f"  • {p['name']}")
        
        return lines
    
    def _generate_yoga_analysis(self) -> list:
        """Generate yoga analysis section"""
        lines = []
        
        lines.append("\n" + "=" * 80)
        lines.append("YOGA ANALYSIS")
        lines.append("=" * 80)
        
        yogas = self.analyzer.get_yogas()
        
        for category in yogas:
            lines.append(f"\n{category['name'].upper()}")
            lines.append("-" * 80)
            
            active_yogas = [y for y in category.get('yoga_list', []) if y['has_yoga']]
            
            if active_yogas:
                for yoga in active_yogas:
                    lines.append(f"\n✓ {yoga['name']}")
                    lines.append(f"  {yoga['description']}")
            else:
                lines.append("  No active yogas in this category")
        
        return lines
    
    def _generate_marriage_report(self) -> list:
        """Generate marriage analysis section"""
        lines = []
        
        lines.append("\n" + "=" * 80)
        lines.append("MARRIAGE ANALYSIS")
        lines.append("=" * 80)
        
        marriage = self.analyzer.analyze_marriage_prospects()
        
        lines.append("\nKEY FACTORS:")
        for factor in marriage['factors']:
            lines.append(f"\n{factor['factor']}:")
            for key, value in factor.items():
                if key != 'factor':
                    lines.append(f"  • {key}: {value}")
        
        if marriage['strengths']:
            lines.append("\nSTRENGTHS:")
            for strength in marriage['strengths']:
                lines.append(f"  ✓ {strength}")
        
        if marriage['challenges']:
            lines.append("\nCHALLENGES:")
            for challenge in marriage['challenges']:
                if isinstance(challenge, dict):
                    lines.append(f"  ⚠ {challenge['challenge']}")
                    lines.append(f"    {challenge['description'][:200]}...")
                else:
                    lines.append(f"  ⚠ {challenge}")
        
        # Navamsa analysis
        d9 = self.analyzer.get_d9_chart()
        lines.append("\nNAVAMSA (D9) CHART - Marriage & Spouse:")
        lines.append(f"  Navamsa Lagna: {d9.get('ascendant', {}).get('sign', 'N/A')}")
        
        venus_d9 = self.analyzer._find_planet_by_name(d9, 'Venus')
        if venus_d9:
            lines.append(f"  Venus in D9: {venus_d9['sign']} (House {venus_d9['house']})")
        
        return lines
    
    def _generate_career_report(self) -> list:
        """Generate career analysis section"""
        lines = []
        
        lines.append("\n" + "=" * 80)
        lines.append("CAREER ANALYSIS")
        lines.append("=" * 80)
        
        career = self.analyzer.analyze_career_prospects()
        
        lines.append("\nKEY FACTORS:")
        for factor in career['factors']:
            lines.append(f"\n{factor['factor']}:")
            for key, value in factor.items():
                if key != 'factor':
                    lines.append(f"  • {key}: {value}")
        
        if career['strengths']:
            lines.append("\nSTRENGTHS & YOGAS:")
            for strength in career['strengths']:
                if isinstance(strength, dict):
                    lines.append(f"  ✓ {strength['yoga']}")
                    lines.append(f"    {strength['description'][:200]}...")
                else:
                    lines.append(f"  ✓ {strength}")
        
        # D10 analysis
        d10 = self.analyzer.get_d10_chart()
        lines.append("\nDASAMSA (D10) CHART - Career & Profession:")
        lines.append(f"  D10 Lagna: {d10.get('ascendant', {}).get('sign', 'N/A')}")
        
        return lines
    
    def _generate_dasha_report(self) -> list:
        """Generate dasha analysis section"""
        lines = []
        
        lines.append("\n" + "=" * 80)
        lines.append("DASHA ANALYSIS (Vimshottari)")
        lines.append("=" * 80)
        
        # Current dasha
        current = self.analyzer.get_current_dasha()
        if current:
            lines.append(f"\nCURRENT MAHADASHA: {current['name']}")
            lines.append(f"Period: {current['start']} to {current['end']}")
        
        # Upcoming timeline
        lines.append("\nUPCOMING DASHA PERIODS (Next 10 Years):")
        timeline = self.analyzer.generate_dasha_timeline(10)
        
        for period in timeline[:5]:  # Show first 5 periods
            lines.append(f"\n{period['mahadasha']} Mahadasha:")
            lines.append(f"  {period['start']} to {period['end']}")
            
            # Show first few antardashas
            if period['antardashas']:
                lines.append("  Key Antardashas:")
                for antardasha in period['antardashas'][:3]:
                    lines.append(f"    - {antardasha['name']}: {antardasha['start'][:10]} to {antardasha['end'][:10]}")
        
        return lines
    
    def _generate_divisional_charts_summary(self) -> list:
        """Generate divisional charts summary"""
        lines = []
        
        lines.append("\n" + "=" * 80)
        lines.append("DIVISIONAL CHARTS (VARGAS) SUMMARY")
        lines.append("=" * 80)
        
        charts_info = {
            'D1': 'Rashi - Overall life',
            'D9': 'Navamsa - Marriage & dharma',
            'D10': 'Dasamsa - Career & profession',
            'D7': 'Saptamsa - Children',
            'D12': 'Dwadasamsa - Parents',
            'D20': 'Vimsamsa - Spiritual pursuits',
            'D24': 'Chaturvimsamsa - Education',
            'D30': 'Trimsamsa - Evils & misfortunes'
        }
        
        for chart_name, description in charts_info.items():
            chart = self.analyzer.charts.get(chart_name, {})
            if chart:
                asc = chart.get('ascendant', {})
                lines.append(f"\n{chart_name} - {description}")
                lines.append(f"  Lagna: {asc.get('sign', 'N/A')}")
        
        return lines
    
    def _generate_recommendations(self) -> list:
        """Generate recommendations section"""
        lines = []
        
        lines.append("\n" + "=" * 80)
        lines.append("RECOMMENDATIONS & REMEDIES")
        lines.append("=" * 80)
        
        lines.append("\nBased on the chart analysis:")
        
        # Check for weak planets
        strengths = self.analyzer.analyze_planetary_strengths()
        
        if strengths['weak_planets']:
            lines.append("\nFor Weak Planets:")
            for planet in strengths['weak_planets']:
                lines.append(f"  • {planet['name']}: Consider strengthening through mantras, gemstones, or charity")
        
        if strengths['combust_planets']:
            lines.append("\nFor Combust Planets:")
            for planet in strengths['combust_planets']:
                lines.append(f"  • {planet['name']}: Perform remedies to reduce combustion effects")
        
        lines.append("\nGeneral Recommendations:")
        lines.append("  • Regular meditation and spiritual practices")
        lines.append("  • Charity on days ruled by weak planets")
        lines.append("  • Consult with a qualified astrologer for personalized remedies")
        
        lines.append("\n" + "=" * 80)
        lines.append("END OF REPORT")
        lines.append("=" * 80)
        
        return lines


if __name__ == "__main__":
    # Generate report
    analyzer = ChartAnalyzer()
    generator = ReportGenerator(analyzer)
    
    report = generator.generate_complete_report('COMPLETE_CHART_REPORT.txt')
    print("\nReport generated successfully!")
    print("\nFirst 50 lines of report:")
    print("\n".join(report.split("\n")[:50]))
