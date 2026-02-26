#!/usr/bin/env python3
"""
Data Validator - Validates chart data and calculations
"""

import json
from typing import Dict, List, Tuple

class DataValidator:
    """Validate astrological chart data"""
    
    VALID_SIGNS = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
        'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ]
    
    VALID_PLANETS = ['Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn']
    
    VALID_NAKSHATRAS = [
        'Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra',
        'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'Purva Phalguni', 'Uttara Phalguni',
        'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha', 'Jyeshtha',
        'Mula', 'Purva Ashadha', 'Uttara Ashadha', 'Shravana', 'Dhanishta',
        'Shatabhisha', 'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati'
    ]
    
    SIGN_LORDS = {
        'Aries': 'Mars', 'Taurus': 'Venus', 'Gemini': 'Mercury',
        'Cancer': 'Moon', 'Leo': 'Sun', 'Virgo': 'Mercury',
        'Libra': 'Venus', 'Scorpio': 'Mars', 'Sagittarius': 'Jupiter',
        'Capricorn': 'Saturn', 'Aquarius': 'Saturn', 'Pisces': 'Jupiter'
    }
    
    def __init__(self, charts_file: str = 'chartsall', simple_file: str = 'chartsimp.json'):
        """Initialize validator with chart files"""
        with open(charts_file, 'r') as f:
            self.charts = json.load(f)
        
        with open(simple_file, 'r') as f:
            self.simple_data = json.load(f)
        
        self.errors = []
        self.warnings = []
    
    def validate_all(self) -> Tuple[List[str], List[str]]:
        """Run all validations"""
        self.errors = []
        self.warnings = []
        
        print("Running validations...")
        
        # Validate D1 chart
        self._validate_chart(self.charts.get('D1', {}), 'D1')
        
        # Validate other divisional charts
        for chart_name in ['D9', 'D10', 'D7', 'D12']:
            if chart_name in self.charts:
                self._validate_chart(self.charts[chart_name], chart_name)
        
        # Validate yogas
        self._validate_yogas()
        
        # Validate dashas
        self._validate_dashas()
        
        # Cross-validate data
        self._cross_validate()
        
        return self.errors, self.warnings
    
    def _validate_chart(self, chart: Dict, chart_name: str):
        """Validate a single chart"""
        if not chart:
            self.errors.append(f"{chart_name}: Chart data is empty")
            return
        
        # Validate ascendant
        asc = chart.get('ascendant', {})
        if not asc:
            self.errors.append(f"{chart_name}: Missing ascendant data")
        else:
            if asc.get('sign') not in self.VALID_SIGNS:
                self.errors.append(f"{chart_name}: Invalid ascendant sign: {asc.get('sign')}")
            
            # Validate degree (0-360)
            try:
                degree = float(asc.get('degree', 0))
                if not (0 <= degree < 360):
                    self.errors.append(f"{chart_name}: Invalid ascendant degree: {degree}")
            except (ValueError, TypeError):
                self.errors.append(f"{chart_name}: Invalid ascendant degree format")
            
            # Validate lord
            expected_lord = self.SIGN_LORDS.get(asc.get('sign'))
            if asc.get('lord') != expected_lord:
                self.warnings.append(
                    f"{chart_name}: Ascendant lord mismatch. "
                    f"Expected {expected_lord} for {asc.get('sign')}, got {asc.get('lord')}"
                )
        
        # Validate houses
        houses = chart.get('houses', [])
        if len(houses) != 12:
            self.errors.append(f"{chart_name}: Should have 12 houses, found {len(houses)}")
        
        for house in houses:
            if house.get('sign') not in self.VALID_SIGNS:
                self.errors.append(f"{chart_name}: Invalid sign in house {house.get('number')}")
            
            expected_lord = self.SIGN_LORDS.get(house.get('sign'))
            if house.get('lord') != expected_lord:
                self.warnings.append(
                    f"{chart_name}: House {house.get('number')} lord mismatch"
                )
        
        # Validate planets
        planets = chart.get('planets', [])
        found_planets = set()
        
        for planet in planets:
            planet_name = planet.get('name')
            
            # Check for duplicates
            if planet_name in found_planets:
                self.errors.append(f"{chart_name}: Duplicate planet: {planet_name}")
            found_planets.add(planet_name)
            
            # Validate planet name
            if planet_name not in self.VALID_PLANETS:
                self.warnings.append(f"{chart_name}: Unknown planet: {planet_name}")
            
            # Validate sign
            if planet.get('sign') not in self.VALID_SIGNS:
                self.errors.append(f"{chart_name}: Invalid sign for {planet_name}")
            
            # Validate house (1-12)
            house_num = planet.get('house')
            if not (1 <= house_num <= 12):
                self.errors.append(f"{chart_name}: Invalid house for {planet_name}: {house_num}")
            
            # Validate degree
            try:
                degree = float(planet.get('degree', 0))
                if not (0 <= degree < 360):
                    self.errors.append(f"{chart_name}: Invalid degree for {planet_name}: {degree}")
            except (ValueError, TypeError):
                self.errors.append(f"{chart_name}: Invalid degree format for {planet_name}")
            
            # Validate nakshatra
            nakshatra = planet.get('nakshatra')
            if nakshatra and nakshatra not in self.VALID_NAKSHATRAS:
                self.warnings.append(f"{chart_name}: Unknown nakshatra for {planet_name}: {nakshatra}")
        
        # Check for missing planets
        missing = set(self.VALID_PLANETS) - found_planets
        if missing:
            self.warnings.append(f"{chart_name}: Missing planets: {', '.join(missing)}")
    
    def _validate_yogas(self):
        """Validate yoga data"""
        yoga_details = self.simple_data.get('data', {}).get('yoga_details', [])
        
        if not yoga_details:
            self.warnings.append("No yoga data found")
            return
        
        for category in yoga_details:
            if 'name' not in category:
                self.errors.append("Yoga category missing name")
            
            for yoga in category.get('yoga_list', []):
                if 'name' not in yoga:
                    self.errors.append("Yoga missing name")
                if 'has_yoga' not in yoga:
                    self.errors.append(f"Yoga {yoga.get('name')} missing has_yoga field")
    
    def _validate_dashas(self):
        """Validate dasha data"""
        dasha_periods = self.simple_data.get('data', {}).get('dasha_periods', [])
        
        if not dasha_periods:
            self.warnings.append("No dasha data found")
            return
        
        for period in dasha_periods:
            if 'name' not in period:
                self.errors.append("Dasha period missing name")
            if 'start' not in period or 'end' not in period:
                self.errors.append(f"Dasha {period.get('name')} missing start/end dates")
            
            # Validate date format
            try:
                from datetime import datetime
                start = datetime.fromisoformat(period['start'].replace('+05:30', ''))
                end = datetime.fromisoformat(period['end'].replace('+05:30', ''))
                
                if start >= end:
                    self.errors.append(f"Dasha {period.get('name')}: start date after end date")
            except (ValueError, KeyError):
                self.errors.append(f"Dasha {period.get('name')}: invalid date format")
    
    def _cross_validate(self):
        """Cross-validate data between charts"""
        d1 = self.charts.get('D1', {})
        d9 = self.charts.get('D9', {})
        
        if not d1 or not d9:
            return
        
        # Check that planets exist in both charts
        d1_planets = {p['name'] for p in d1.get('planets', [])}
        d9_planets = {p['name'] for p in d9.get('planets', [])}
        
        if d1_planets != d9_planets:
            missing_in_d9 = d1_planets - d9_planets
            missing_in_d1 = d9_planets - d1_planets
            
            if missing_in_d9:
                self.warnings.append(f"Planets in D1 but not D9: {missing_in_d9}")
            if missing_in_d1:
                self.warnings.append(f"Planets in D9 but not D1: {missing_in_d1}")
    
    def print_report(self):
        """Print validation report"""
        print("\n" + "=" * 80)
        print("VALIDATION REPORT")
        print("=" * 80)
        
        if not self.errors and not self.warnings:
            print("\n✓ All validations passed! Data is clean.")
        else:
            if self.errors:
                print(f"\n❌ ERRORS ({len(self.errors)}):")
                for i, error in enumerate(self.errors, 1):
                    print(f"  {i}. {error}")
            
            if self.warnings:
                print(f"\n⚠ WARNINGS ({len(self.warnings)}):")
                for i, warning in enumerate(self.warnings, 1):
                    print(f"  {i}. {warning}")
        
        print("\n" + "=" * 80)


if __name__ == "__main__":
    validator = DataValidator()
    errors, warnings = validator.validate_all()
    validator.print_report()
