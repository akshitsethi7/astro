#!/usr/bin/env python3
"""
Comprehensive Chart Analysis System
Uses the knowledge base to analyze birth charts
"""

import json
from typing import Dict, List, Any
from datetime import datetime

class ChartAnalyzer:
    """Main chart analysis engine"""
    
    def __init__(self, charts_file: str = 'chartsall', simple_file: str = 'chartsimp.json'):
        """Initialize with chart data files"""
        with open(charts_file, 'r') as f:
            self.charts = json.load(f)
        
        with open(simple_file, 'r') as f:
            self.simple_data = json.load(f)
    
    def get_d1_chart(self) -> Dict:
        """Get the main birth chart (D1/Rashi)"""
        return self.charts.get('D1', {})
    
    def get_d9_chart(self) -> Dict:
        """Get Navamsa chart (D9) - crucial for marriage"""
        return self.charts.get('D9', {})
    
    def get_d7_chart(self) -> Dict:
        """Get Saptamsa chart (D7) - for children"""
        return self.charts.get('D7', {})
    
    def get_d10_chart(self) -> Dict:
        """Get Dasamsa chart (D10) - for career"""
        return self.charts.get('D10', {})
    
    def get_yogas(self) -> List[Dict]:
        """Get all yogas from the chart"""
        return self.simple_data.get('data', {}).get('yoga_details', [])
    
    def get_dasha_periods(self) -> List[Dict]:
        """Get Vimshottari dasha periods"""
        return self.simple_data.get('data', {}).get('dasha_periods', [])
    
    def get_current_dasha(self, date: datetime = None) -> Dict:
        """Get current running dasha period"""
        if date is None:
            date = datetime.now()
        
        for period in self.get_dasha_periods():
            start = datetime.fromisoformat(period['start'].replace('+05:30', ''))
            end = datetime.fromisoformat(period['end'].replace('+05:30', ''))
            
            if start <= date <= end:
                return period
        
        return {}
    
    def analyze_marriage_prospects(self) -> Dict[str, Any]:
        """Analyze marriage prospects using classical methods"""
        d1 = self.get_d1_chart()
        d9 = self.get_d9_chart()
        
        analysis = {
            "summary": "",
            "factors": [],
            "timing": [],
            "spouse_indicators": [],
            "challenges": [],
            "strengths": []
        }
        
        # Analyze 7th house
        seventh_house = self._get_house(d1, 7)
        seventh_lord = self._find_planet_by_name(d1, seventh_house['lord'])
        
        analysis['factors'].append({
            "factor": "7th House Analysis",
            "house_sign": seventh_house['sign'],
            "lord": seventh_house['lord'],
            "lord_position": f"House {seventh_lord['house']}, {seventh_lord['sign']}" if seventh_lord else "Not found",
            "planets_in_7th": self._get_planets_in_house(d1, 7)
        })
        
        # Venus analysis (karaka for marriage)
        venus = self._find_planet_by_name(d1, 'Venus')
        if venus:
            analysis['factors'].append({
                "factor": "Venus (Marriage Karaka)",
                "position": f"House {venus['house']}, {venus['sign']}",
                "nakshatra": venus['nakshatra'],
                "dignity": venus['dignity'],
                "combust": venus['combust']
            })
        
        # Check for marriage yogas
        yogas = self.get_yogas()
        for yoga_category in yogas:
            for yoga in yoga_category.get('yoga_list', []):
                if yoga['has_yoga'] and 'marriage' in yoga['name'].lower():
                    analysis['strengths'].append(yoga['name'])
        
        # Check for Kuja Dosha
        for yoga_category in yogas:
            if yoga_category['name'] == 'Inauspicious Yogas':
                for yoga in yoga_category.get('yoga_list', []):
                    if yoga['has_yoga'] and yoga['name'] == 'Kuja Yoga':
                        analysis['challenges'].append({
                            "challenge": "Kuja Dosha (Manglik)",
                            "description": yoga['description']
                        })
        
        return analysis
    
    def analyze_career_prospects(self) -> Dict[str, Any]:
        """Analyze career prospects"""
        d1 = self.get_d1_chart()
        d10 = self.get_d10_chart()
        
        analysis = {
            "summary": "",
            "factors": [],
            "suitable_fields": [],
            "strengths": [],
            "timing": []
        }
        
        # Analyze 10th house
        tenth_house = self._get_house(d1, 10)
        tenth_lord = self._find_planet_by_name(d1, tenth_house['lord'])
        
        analysis['factors'].append({
            "factor": "10th House (Career)",
            "house_sign": tenth_house['sign'],
            "lord": tenth_house['lord'],
            "lord_position": f"House {tenth_lord['house']}, {tenth_lord['sign']}" if tenth_lord else "Not found",
            "planets_in_10th": self._get_planets_in_house(d1, 10)
        })
        
        # Analyze Sun (karaka for career/authority)
        sun = self._find_planet_by_name(d1, 'Sun')
        if sun:
            analysis['factors'].append({
                "factor": "Sun (Career Karaka)",
                "position": f"House {sun['house']}, {sun['sign']}",
                "dignity": sun['dignity']
            })
        
        # Check for Raja Yoga
        yogas = self.get_yogas()
        for yoga_category in yogas:
            for yoga in yoga_category.get('yoga_list', []):
                if yoga['has_yoga'] and 'raja' in yoga['name'].lower():
                    analysis['strengths'].append({
                        "yoga": yoga['name'],
                        "description": yoga['description']
                    })
        
        return analysis
    
    def analyze_planetary_strengths(self) -> Dict[str, Any]:
        """Analyze planetary strengths and weaknesses"""
        d1 = self.get_d1_chart()
        
        analysis = {
            "strong_planets": [],
            "weak_planets": [],
            "combust_planets": [],
            "retrograde_planets": []
        }
        
        for planet in d1.get('planets', []):
            planet_info = {
                "name": planet['name'],
                "sign": planet['sign'],
                "house": planet['house'],
                "dignity": planet['dignity']
            }
            
            # Check dignity
            if planet['dignity'] in ['Exalted', 'Own Sign', 'Moolatrikona']:
                analysis['strong_planets'].append(planet_info)
            elif planet['dignity'] in ['Debilitated', 'Enemy Sign']:
                analysis['weak_planets'].append(planet_info)
            
            # Check combustion
            if planet.get('combust', False):
                analysis['combust_planets'].append(planet_info)
            
            # Check retrograde
            if planet.get('retrograde', False):
                analysis['retrograde_planets'].append(planet_info)
        
        return analysis
    
    def generate_dasha_timeline(self, years: int = 10) -> List[Dict]:
        """Generate dasha timeline for next N years"""
        current_date = datetime.now()
        end_date = datetime(current_date.year + years, current_date.month, current_date.day)
        
        timeline = []
        
        for period in self.get_dasha_periods():
            start = datetime.fromisoformat(period['start'].replace('+05:30', ''))
            end = datetime.fromisoformat(period['end'].replace('+05:30', ''))
            
            if start <= end_date and end >= current_date:
                timeline.append({
                    "mahadasha": period['name'],
                    "start": start.strftime("%Y-%m-%d"),
                    "end": end.strftime("%Y-%m-%d"),
                    "antardashas": period.get('antardasha', [])
                })
        
        return timeline
    
    # Helper methods
    def _get_house(self, chart: Dict, house_num: int) -> Dict:
        """Get house information"""
        for house in chart.get('houses', []):
            if house['number'] == house_num:
                return house
        return {}
    
    def _find_planet_by_name(self, chart: Dict, name: str) -> Dict:
        """Find planet by name"""
        for planet in chart.get('planets', []):
            if planet['name'] == name:
                return planet
        return {}
    
    def _get_planets_in_house(self, chart: Dict, house_num: int) -> List[str]:
        """Get all planets in a specific house"""
        planets = []
        for planet in chart.get('planets', []):
            if planet['house'] == house_num:
                planets.append(planet['name'])
        return planets


if __name__ == "__main__":
    # Example usage
    analyzer = ChartAnalyzer()
    
    print("=== CHART ANALYSIS ===\n")
    
    # Marriage analysis
    print("MARRIAGE PROSPECTS:")
    marriage = analyzer.analyze_marriage_prospects()
    print(json.dumps(marriage, indent=2))
    
    print("\n" + "="*50 + "\n")
    
    # Career analysis
    print("CAREER PROSPECTS:")
    career = analyzer.analyze_career_prospects()
    print(json.dumps(career, indent=2))
