#!/usr/bin/env python3
"""
Knowledge-Based Analyzer
Uses the knowledge base documents to provide detailed analysis
"""

import json
import os
from pathlib import Path
from chart_analyzer import ChartAnalyzer

class KnowledgeAnalyzer:
    """Analyze charts using knowledge base"""
    
    def __init__(self, analyzer: ChartAnalyzer, knowledge_base_path: str = "logy-learning"):
        self.analyzer = analyzer
        self.kb_path = Path(knowledge_base_path)
        self.knowledge = self._load_knowledge()
    
    def _load_knowledge(self) -> dict:
        """Load knowledge from markdown files"""
        knowledge = {
            'marriage': {},
            'career': {},
            'foundations': {},
            'methods': {}
        }
        
        # Load marriage knowledge
        marriage_path = self.kb_path / "01-marriage"
        if marriage_path.exists():
            for file in marriage_path.glob("*.md"):
                with open(file, 'r') as f:
                    knowledge['marriage'][file.stem] = f.read()
        
        # Load career knowledge
        career_path = self.kb_path / "02-career"
        if career_path.exists():
            for file in career_path.glob("*.md"):
                with open(file, 'r') as f:
                    knowledge['career'][file.stem] = f.read()
        
        # Load foundations
        foundations_path = self.kb_path / "00-foundations"
        if foundations_path.exists():
            for file in foundations_path.glob("*.md"):
                with open(file, 'r') as f:
                    knowledge['foundations'][file.stem] = f.read()
        
        return knowledge
    
    def analyze_marriage_with_knowledge(self) -> dict:
        """Detailed marriage analysis using knowledge base"""
        d1 = self.analyzer.get_d1_chart()
        d9 = self.analyzer.get_d9_chart()
        
        analysis = {
            "overall_assessment": "",
            "detailed_factors": [],
            "timing_indicators": [],
            "spouse_characteristics": [],
            "remedial_measures": [],
            "knowledge_applied": []
        }
        
        # 1. Analyze 7th house (primary marriage house)
        seventh_house = self.analyzer._get_house(d1, 7)
        seventh_lord = self.analyzer._find_planet_by_name(d1, seventh_house['lord'])
        planets_in_7th = self.analyzer._get_planets_in_house(d1, 7)
        
        analysis['detailed_factors'].append({
            "category": "7th House Analysis",
            "sign": seventh_house['sign'],
            "lord": seventh_house['lord'],
            "lord_placement": f"House {seventh_lord['house']}" if seventh_lord else "Not found",
            "planets_present": planets_in_7th,
            "interpretation": self._interpret_7th_house(seventh_house, seventh_lord, planets_in_7th)
        })
        
        # 2. Analyze Venus (karaka for marriage)
        venus = self.analyzer._find_planet_by_name(d1, 'Venus')
        if venus:
            analysis['detailed_factors'].append({
                "category": "Venus Analysis (Marriage Karaka)",
                "house": venus['house'],
                "sign": venus['sign'],
                "nakshatra": venus['nakshatra'],
                "dignity": venus['dignity'],
                "combust": venus['combust'],
                "interpretation": self._interpret_venus(venus)
            })
        
        # 3. Analyze Jupiter (karaka for husband in female chart)
        jupiter = self.analyzer._find_planet_by_name(d1, 'Jupiter')
        if jupiter:
            analysis['detailed_factors'].append({
                "category": "Jupiter Analysis (Husband Karaka)",
                "house": jupiter['house'],
                "sign": jupiter['sign'],
                "dignity": jupiter['dignity'],
                "interpretation": self._interpret_jupiter_marriage(jupiter)
            })
        
        # 4. Navamsa (D9) analysis
        d9_asc = d9.get('ascendant', {})
        venus_d9 = self.analyzer._find_planet_by_name(d9, 'Venus')
        
        analysis['detailed_factors'].append({
            "category": "Navamsa (D9) Analysis",
            "d9_lagna": d9_asc.get('sign'),
            "venus_in_d9": f"{venus_d9['sign']} (House {venus_d9['house']})" if venus_d9 else "Not found",
            "interpretation": self._interpret_navamsa(d9, venus_d9)
        })
        
        # 5. Check for marriage yogas
        yogas = self.analyzer.get_yogas()
        marriage_yogas = self._extract_marriage_yogas(yogas)
        if marriage_yogas:
            analysis['detailed_factors'].append({
                "category": "Marriage Yogas",
                "yogas": marriage_yogas
            })
        
        # 6. Timing analysis using dashas
        timing = self._analyze_marriage_timing()
        analysis['timing_indicators'] = timing
        
        # 7. Spouse characteristics
        spouse_traits = self._analyze_spouse_characteristics(d1, d9)
        analysis['spouse_characteristics'] = spouse_traits
        
        # 8. Overall assessment
        analysis['overall_assessment'] = self._generate_marriage_assessment(analysis)
        
        return analysis
    
    def analyze_career_with_knowledge(self) -> dict:
        """Detailed career analysis using knowledge base"""
        d1 = self.analyzer.get_d1_chart()
        d10 = self.analyzer.get_d10_chart()
        
        analysis = {
            "overall_assessment": "",
            "detailed_factors": [],
            "suitable_professions": [],
            "timing_indicators": [],
            "strengths": [],
            "challenges": []
        }
        
        # 1. Analyze 10th house (career house)
        tenth_house = self.analyzer._get_house(d1, 10)
        tenth_lord = self.analyzer._find_planet_by_name(d1, tenth_house['lord'])
        planets_in_10th = self.analyzer._get_planets_in_house(d1, 10)
        
        analysis['detailed_factors'].append({
            "category": "10th House Analysis",
            "sign": tenth_house['sign'],
            "lord": tenth_house['lord'],
            "lord_placement": f"House {tenth_lord['house']}" if tenth_lord else "Not found",
            "planets_present": planets_in_10th,
            "interpretation": self._interpret_10th_house(tenth_house, tenth_lord, planets_in_10th)
        })
        
        # 2. Analyze Sun (karaka for career/authority)
        sun = self.analyzer._find_planet_by_name(d1, 'Sun')
        if sun:
            analysis['detailed_factors'].append({
                "category": "Sun Analysis (Career Karaka)",
                "house": sun['house'],
                "sign": sun['sign'],
                "dignity": sun['dignity'],
                "interpretation": self._interpret_sun_career(sun)
            })
        
        # 3. Analyze Saturn (karaka for service/work)
        saturn = self.analyzer._find_planet_by_name(d1, 'Saturn')
        if saturn:
            analysis['detailed_factors'].append({
                "category": "Saturn Analysis (Service Karaka)",
                "house": saturn['house'],
                "sign": saturn['sign'],
                "dignity": saturn['dignity'],
                "interpretation": self._interpret_saturn_career(saturn)
            })
        
        # 4. D10 analysis
        d10_asc = d10.get('ascendant', {})
        analysis['detailed_factors'].append({
            "category": "Dasamsa (D10) Analysis",
            "d10_lagna": d10_asc.get('sign'),
            "interpretation": self._interpret_d10(d10)
        })
        
        # 5. Suitable professions based on planetary positions
        professions = self._suggest_professions(d1, d10)
        analysis['suitable_professions'] = professions
        
        # 6. Career timing
        timing = self._analyze_career_timing()
        analysis['timing_indicators'] = timing
        
        return analysis
    
    def _interpret_7th_house(self, house, lord, planets) -> str:
        """Interpret 7th house for marriage"""
        interpretations = []
        
        # Sign interpretation
        sign_meanings = {
            'Aries': 'Spouse may be energetic, independent, and assertive',
            'Taurus': 'Spouse may be stable, practical, and value-oriented',
            'Gemini': 'Spouse may be communicative, intellectual, and versatile',
            'Cancer': 'Spouse may be emotional, nurturing, and family-oriented',
            'Leo': 'Spouse may be confident, generous, and leadership-oriented',
            'Virgo': 'Spouse may be analytical, service-oriented, and detail-focused',
            'Libra': 'Spouse may be diplomatic, balanced, and relationship-focused',
            'Scorpio': 'Spouse may be intense, transformative, and deep',
            'Sagittarius': 'Spouse may be philosophical, adventurous, and optimistic',
            'Capricorn': 'Spouse may be ambitious, disciplined, and traditional',
            'Aquarius': 'Spouse may be unconventional, humanitarian, and independent',
            'Pisces': 'Spouse may be spiritual, compassionate, and intuitive'
        }
        
        interpretations.append(sign_meanings.get(house['sign'], ''))
        
        # Lord placement
        if lord:
            if lord['house'] in [1, 5, 9]:
                interpretations.append("7th lord in trine - favorable for marriage")
            elif lord['house'] in [6, 8, 12]:
                interpretations.append("7th lord in dusthana - may face challenges")
        
        # Planets in 7th
        if planets:
            if 'Jupiter' in planets:
                interpretations.append("Jupiter in 7th - auspicious for marriage")
            if 'Venus' in planets:
                interpretations.append("Venus in 7th - strong desire for partnership")
            if 'Saturn' in planets:
                interpretations.append("Saturn in 7th - may delay marriage but gives stability")
            if 'Mars' in planets:
                interpretations.append("Mars in 7th - Kuja Dosha, may need remedies")
        
        return ". ".join(interpretations)
    
    def _interpret_venus(self, venus) -> str:
        """Interpret Venus for marriage"""
        interpretations = []
        
        if venus['dignity'] in ['Exalted', 'Own Sign']:
            interpretations.append("Strong Venus indicates good marriage prospects")
        elif venus['dignity'] == 'Debilitated':
            interpretations.append("Weak Venus may create challenges in relationships")
        
        if venus['combust']:
            interpretations.append("Combust Venus may affect relationship clarity")
        
        if venus['house'] in [1, 4, 7, 10]:
            interpretations.append("Venus in Kendra gives relationship strength")
        
        return ". ".join(interpretations)
    
    def _interpret_jupiter_marriage(self, jupiter) -> str:
        """Interpret Jupiter for marriage (husband karaka)"""
        interpretations = []
        
        if jupiter['dignity'] in ['Exalted', 'Own Sign']:
            interpretations.append("Strong Jupiter indicates wise and supportive spouse")
        
        if jupiter['house'] in [1, 5, 7, 9]:
            interpretations.append("Jupiter well-placed for marriage happiness")
        
        return ". ".join(interpretations)
    
    def _interpret_navamsa(self, d9, venus_d9) -> str:
        """Interpret Navamsa chart"""
        interpretations = []
        
        interpretations.append("Navamsa shows the true nature of marriage and spouse")
        
        if venus_d9:
            if venus_d9['dignity'] in ['Exalted', 'Own Sign']:
                interpretations.append("Venus strong in D9 - harmonious marriage")
        
        return ". ".join(interpretations)
    
    def _interpret_10th_house(self, house, lord, planets) -> str:
        """Interpret 10th house for career"""
        interpretations = []
        
        if lord and lord['dignity'] in ['Exalted', 'Own Sign']:
            interpretations.append("Strong 10th lord indicates successful career")
        
        if planets:
            if 'Sun' in planets:
                interpretations.append("Sun in 10th - leadership and authority")
            if 'Jupiter' in planets:
                interpretations.append("Jupiter in 10th - teaching, advisory roles")
            if 'Mercury' in planets:
                interpretations.append("Mercury in 10th - communication, business")
        
        return ". ".join(interpretations)
    
    def _interpret_sun_career(self, sun) -> str:
        """Interpret Sun for career"""
        if sun['dignity'] in ['Exalted', 'Own Sign']:
            return "Strong Sun indicates leadership abilities and career success"
        return "Sun's position influences career authority and recognition"
    
    def _interpret_saturn_career(self, saturn) -> str:
        """Interpret Saturn for career"""
        if saturn['dignity'] in ['Exalted', 'Own Sign']:
            return "Strong Saturn indicates disciplined career growth and longevity"
        return "Saturn influences work ethic and service-oriented careers"
    
    def _interpret_d10(self, d10) -> str:
        """Interpret D10 chart"""
        return "D10 chart shows career potential and professional achievements"
    
    def _extract_marriage_yogas(self, yogas) -> list:
        """Extract marriage-related yogas"""
        marriage_yogas = []
        
        for category in yogas:
            for yoga in category.get('yoga_list', []):
                if yoga['has_yoga']:
                    # Check if yoga affects marriage
                    desc_lower = yoga['description'].lower()
                    if any(word in desc_lower for word in ['marriage', 'spouse', 'partner', 'relationship']):
                        marriage_yogas.append({
                            "name": yoga['name'],
                            "description": yoga['description']
                        })
        
        return marriage_yogas
    
    def _analyze_marriage_timing(self) -> list:
        """Analyze marriage timing from dashas"""
        timing = []
        
        # Get current and upcoming dashas
        timeline = self.analyzer.generate_dasha_timeline(15)
        
        for period in timeline:
            planet = period['mahadasha']
            
            # Check if planet is connected to 7th house or Venus
            d1 = self.analyzer.get_d1_chart()
            planet_data = self.analyzer._find_planet_by_name(d1, planet)
            
            if planet_data:
                if planet_data['house'] == 7 or planet == 'Venus':
                    timing.append({
                        "period": f"{planet} Mahadasha",
                        "timeframe": f"{period['start']} to {period['end']}",
                        "significance": "Favorable for marriage"
                    })
        
        return timing[:3]  # Return top 3
    
    def _analyze_career_timing(self) -> list:
        """Analyze career timing from dashas"""
        timing = []
        
        timeline = self.analyzer.generate_dasha_timeline(10)
        
        for period in timeline:
            planet = period['mahadasha']
            
            d1 = self.analyzer.get_d1_chart()
            planet_data = self.analyzer._find_planet_by_name(d1, planet)
            
            if planet_data:
                if planet_data['house'] == 10 or planet in ['Sun', 'Saturn']:
                    timing.append({
                        "period": f"{planet} Mahadasha",
                        "timeframe": f"{period['start']} to {period['end']}",
                        "significance": "Important for career growth"
                    })
        
        return timing[:3]
    
    def _analyze_spouse_characteristics(self, d1, d9) -> list:
        """Analyze spouse characteristics"""
        traits = []
        
        # From 7th house sign
        seventh_house = self.analyzer._get_house(d1, 7)
        traits.append(f"7th house in {seventh_house['sign']} suggests specific personality traits")
        
        # From Venus
        venus = self.analyzer._find_planet_by_name(d1, 'Venus')
        if venus:
            traits.append(f"Venus in {venus['sign']} influences spouse's nature")
        
        return traits
    
    def _suggest_professions(self, d1, d10) -> list:
        """Suggest suitable professions"""
        professions = []
        
        # Based on 10th house planets
        planets_in_10th = self.analyzer._get_planets_in_house(d1, 10)
        
        profession_map = {
            'Sun': ['Government', 'Leadership', 'Politics', 'Administration'],
            'Moon': ['Public relations', 'Hospitality', 'Psychology', 'Nursing'],
            'Mars': ['Engineering', 'Military', 'Sports', 'Surgery'],
            'Mercury': ['Business', 'Writing', 'Teaching', 'Communication'],
            'Jupiter': ['Teaching', 'Law', 'Finance', 'Counseling'],
            'Venus': ['Arts', 'Entertainment', 'Fashion', 'Luxury goods'],
            'Saturn': ['Service', 'Labor', 'Mining', 'Real estate']
        }
        
        for planet in planets_in_10th:
            if planet in profession_map:
                professions.extend(profession_map[planet])
        
        return list(set(professions))  # Remove duplicates
    
    def _generate_marriage_assessment(self, analysis) -> str:
        """Generate overall marriage assessment"""
        assessment = []
        
        assessment.append("Based on comprehensive chart analysis:")
        
        # Count positive and negative factors
        positive_factors = len([f for f in analysis['detailed_factors'] 
                               if 'favorable' in str(f).lower() or 'auspicious' in str(f).lower()])
        
        if positive_factors > 2:
            assessment.append("Overall marriage prospects are favorable.")
        else:
            assessment.append("Marriage prospects require attention to certain factors.")
        
        if analysis['timing_indicators']:
            assessment.append(f"Favorable timing indicated in upcoming periods.")
        
        return " ".join(assessment)


if __name__ == "__main__":
    from chart_analyzer import ChartAnalyzer
    
    analyzer = ChartAnalyzer()
    kb_analyzer = KnowledgeAnalyzer(analyzer)
    
    print("=== KNOWLEDGE-BASED MARRIAGE ANALYSIS ===\n")
    marriage = kb_analyzer.analyze_marriage_with_knowledge()
    print(json.dumps(marriage, indent=2))
