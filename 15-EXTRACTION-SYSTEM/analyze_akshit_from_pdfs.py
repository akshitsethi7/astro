#!/usr/bin/env python3
"""
COMPREHENSIVE MARRIAGE ANALYSIS FOR AKSHIT
Search ALL 33 PDFs for rules matching HIS SPECIFIC chart placements
Analyze D1, D9, D7, D10, D60 and current dashas
"""

import json
import os
from pathlib import Path
import re

# AKSHIT'S CHART DATA
AKSHIT_CHART = {
    'D1': {
        'SUN': {'sign': 'Sagittarius', 'house': 5, 'degree': '10°55\'', 'nakshatra': 'Mula'},
        'MOON': {'sign': 'Virgo', 'house': 2, 'degree': '22°44\'', 'nakshatra': 'Chitra'},
        'MARS': {'sign': 'Leo', 'house': 1, 'degree': '8°33\'', 'nakshatra': 'Magha'},
        'MERCURY': {'sign': 'Sagittarius', 'house': 5, 'degree': '18°06\'', 'nakshatra': 'Purva Ashadha'},
        'JUPITER': {'sign': 'Scorpio', 'house': 4, 'degree': '9°52\'', 'nakshatra': 'Anuradha'},
        'VENUS': {'sign': 'Libra', 'house': 3, 'degree': '25°24\'', 'nakshatra': 'Vishakha'},
        'SATURN': {'sign': 'Aquarius', 'house': 7, 'degree': '13°46\'', 'nakshatra': 'Shatabhisha'},
        'RAHU': {'sign': 'Libra', 'house': 3, 'degree': '18°15\''},
        'KETU': {'sign': 'Aries', 'house': 9, 'degree': '18°15\''},
        'ASCENDANT': {'sign': 'Leo', 'degree': '23°03\''}
    },
    'D9': {
        'SATURN': {'sign': 'Aquarius', 'house': 5},
        'RAHU': {'sign': 'Pisces', 'house': 6},
        'VENUS': {'sign': 'Taurus', 'house': 8},
        'MARS': {'sign': 'Gemini', 'house': 9},
        'SUN': {'sign': 'Cancer', 'house': 10},
        'MOON': {'sign': 'Cancer', 'house': 10},
        'MERCURY': {'sign': 'Virgo', 'house': 12},
        'JUPITER': {'sign': 'Virgo', 'house': 12},
        'KETU': {'sign': 'Virgo', 'house': 12},
        'ASCENDANT': {'sign': 'Libra'}
    },
    'D7': {
        'MARS': {'sign': 'Leo', 'house': 10},
        'MOON': {'sign': 'Virgo', 'house': 9},
        'VENUS': {'sign': 'Libra', 'house': 4},
        'RAHU': {'sign': 'Libra', 'house': 3},
        'JUPITER': {'sign': 'Scorpio', 'house': 8},
        'SUN': {'sign': 'Sagittarius', 'house': 3},
        'MERCURY': {'sign': 'Sagittarius', 'house': 5},
        'SATURN': {'sign': 'Aquarius', 'house': 6},
        'KETU': {'sign': 'Aries', 'house': 9}
    },
    'D10': {
        'SUN': {'sign': 'Pisces', 'house': 2},
        'RAHU': {'sign': 'Aries', 'house': 3},
        'MERCURY': {'sign': 'Gemini', 'house': 5},
        'VENUS': {'sign': 'Gemini', 'house': 5},
        'SATURN': {'sign': 'Gemini', 'house': 5},
        'MARS': {'sign': 'Libra', 'house': 9},
        'JUPITER': {'sign': 'Libra', 'house': 9},
        'KETU': {'sign': 'Libra', 'house': 9},
        'MOON': {'sign': 'Sagittarius', 'house': 11}
    },
    'D60': {
        'MARS': {'sign': 'Leo', 'house': 1},
        'MOON': {'sign': 'Virgo', 'house': 6},
        'VENUS': {'sign': 'Libra', 'house': 12},
        'RAHU': {'sign': 'Libra', 'house': 10},
        'JUPITER': {'sign': 'Scorpio', 'house': 6},
        'SUN': {'sign': 'Sagittarius', 'house': 9},
        'MERCURY': {'sign': 'Sagittarius', 'house': 12},
        'SATURN': {'sign': 'Aquarius', 'house': 5},
        'KETU': {'sign': 'Aries', 'house': 4}
    },
    'DASHA': {
        'current_mahadasha': 'Jupiter',
        'current_antardasha': 'Jupiter',
        'jupiter_period': '2020-2036',
        'saturn_period': '2036-2055',
        'jupiter_venus': '2027-2030',
        'jupiter_ketu': '2027'
    }
}

class AkshitMarriageAnalyzer:
    def __init__(self, extracted_dir):
        self.extracted_dir = Path(extracted_dir)
        self.chart = AKSHIT_CHART
        self.search_patterns = self.generate_chart_specific_patterns()
    
    def generate_chart_specific_patterns(self):
        """Generate search patterns based on Akshit's specific chart"""
        patterns = {}
        
        # D1 CHART SPECIFIC SEARCHES
        patterns['saturn_aquarius_7th'] = [
            r'saturn.*aquarius.*7th',
            r'saturn.*own.*sign.*7th',
            r'shani.*kumbha.*saptam',
            r'saturn.*7th.*house.*aquarius'
        ]
        
        patterns['venus_libra_3rd'] = [
            r'venus.*libra.*3rd',
            r'venus.*own.*sign.*3rd',
            r'shukra.*tula.*third',
            r'venus.*3rd.*house.*libra'
        ]
        
        patterns['jupiter_scorpio_4th'] = [
            r'jupiter.*scorpio.*4th',
            r'guru.*vrishchika.*fourth',
            r'jupiter.*4th.*house.*scorpio'
        ]
        
        patterns['mars_leo_1st'] = [
            r'mars.*leo.*1st',
            r'mars.*ascendant.*leo',
            r'mangal.*simha.*lagna'
        ]
        
        patterns['moon_virgo_2nd'] = [
            r'moon.*virgo.*2nd',
            r'chandra.*kanya.*second',
            r'moon.*2nd.*house.*virgo'
        ]
        
        patterns['sun_mercury_sagittarius_5th'] = [
            r'sun.*mercury.*sagittarius',
            r'sun.*5th.*house',
            r'mercury.*5th.*house'
        ]
        
        patterns['rahu_venus_libra_3rd'] = [
            r'rahu.*venus.*libra',
            r'rahu.*3rd.*house',
            r'rahu.*venus.*conjunction'
        ]
        
        # D9 (NAVAMSA) SPECIFIC
        patterns['d9_venus_taurus_8th'] = [
            r'navamsa.*venus.*taurus',
            r'd9.*venus.*8th',
            r'navamsa.*venus.*own.*sign',
            r'venus.*8th.*navamsa'
        ]
        
        patterns['d9_saturn_aquarius'] = [
            r'navamsa.*saturn.*aquarius',
            r'd9.*saturn.*own.*sign'
        ]
        
        patterns['d9_jupiter_virgo_12th'] = [
            r'navamsa.*jupiter.*virgo',
            r'd9.*jupiter.*12th'
        ]
        
        patterns['d9_sun_moon_cancer'] = [
            r'navamsa.*sun.*moon.*cancer',
            r'd9.*luminaries.*cancer'
        ]
        
        # D7 (SAPTAMSA) - CHILDREN
        patterns['d7_analysis'] = [
            r'saptamsa.*children',
            r'd7.*progeny',
            r'seventh.*division.*children'
        ]
        
        # D10 (DASHAMSA) - CAREER
        patterns['d10_analysis'] = [
            r'dashamsa.*career',
            r'd10.*profession',
            r'tenth.*division.*career'
        ]
        
        # D60 (SHASHTIAMSA) - KARMA
        patterns['d60_analysis'] = [
            r'shashtiamsa',
            r'd60.*karma',
            r'sixtieth.*division'
        ]
        
        # NAKSHATRA SPECIFIC
        patterns['shatabhisha_nakshatra'] = [
            r'shatabhisha.*marriage',
            r'shatabhisha.*spouse',
            r'shatabhisha.*7th'
        ]
        
        patterns['vishakha_nakshatra'] = [
            r'vishakha.*venus',
            r'vishakha.*marriage',
            r'vishakha.*spouse'
        ]
        
        patterns['chitra_nakshatra'] = [
            r'chitra.*moon',
            r'chitra.*marriage'
        ]
        
        patterns['magha_nakshatra'] = [
            r'magha.*mars',
            r'magha.*ascendant'
        ]
        
        patterns['anuradha_nakshatra'] = [
            r'anuradha.*jupiter',
            r'anuradha.*marriage'
        ]
        
        # DASHA SPECIFIC
        patterns['jupiter_mahadasha_marriage'] = [
            r'jupiter.*mahadasha.*marriage',
            r'guru.*dasha.*vivaha',
            r'jupiter.*period.*marriage'
        ]
        
        patterns['jupiter_venus_dasha'] = [
            r'jupiter.*venus.*dasha',
            r'guru.*shukra.*antardasha',
            r'jupiter.*venus.*period.*marriage'
        ]
        
        patterns['jupiter_ketu_dasha'] = [
            r'jupiter.*ketu.*dasha',
            r'guru.*ketu.*antardasha'
        ]
        
        # HOUSE LORD COMBINATIONS
        patterns['7th_lord_7th_house'] = [
            r'7th.*lord.*7th.*house',
            r'saptamesh.*saptam.*bhava',
            r'seventh.*lord.*seventh.*house'
        ]
        
        patterns['2nd_lord_5th_house'] = [
            r'2nd.*lord.*5th.*house',
            r'mercury.*5th.*house'
        ]
        
        patterns['11th_lord_5th_house'] = [
            r'11th.*lord.*5th.*house',
            r'mercury.*11th.*lord'
        ]
        
        # YOGAS IN CHART
        patterns['venus_own_sign_yoga'] = [
            r'venus.*own.*sign.*yoga',
            r'shukra.*swakshetra.*yoga'
        ]
        
        patterns['saturn_own_sign_7th_yoga'] = [
            r'saturn.*own.*sign.*7th.*yoga',
            r'shani.*swakshetra.*saptam'
        ]
        
        patterns['jupiter_4th_house_yoga'] = [
            r'jupiter.*4th.*house.*yoga',
            r'guru.*fourth.*bhava.*yoga'
        ]
        
        # ASPECTS
        patterns['saturn_aspects'] = [
            r'saturn.*aspect.*10th',
            r'saturn.*aspect.*1st',
            r'saturn.*aspect.*4th'
        ]
        
        patterns['jupiter_aspects'] = [
            r'jupiter.*aspect.*8th',
            r'jupiter.*aspect.*10th',
            r'jupiter.*aspect.*12th'
        ]
        
        patterns['mars_aspects'] = [
            r'mars.*aspect.*4th',
            r'mars.*aspect.*7th',
            r'mars.*aspect.*8th'
        ]
        
        # SPOUSE AGE WITH SATURN
        patterns['saturn_7th_spouse_age'] = [
            r'saturn.*7th.*age',
            r'saturn.*7th.*older',
            r'shani.*saptam.*age',
            r'saturn.*seventh.*older.*spouse'
        ]
        
        patterns['saturn_aquarius_age'] = [
            r'saturn.*aquarius.*age',
            r'saturn.*own.*sign.*age'
        ]
        
        # LEO ASCENDANT SPECIFIC
        patterns['leo_ascendant_marriage'] = [
            r'leo.*ascendant.*marriage',
            r'simha.*lagna.*vivaha',
            r'leo.*rising.*marriage'
        ]
        
        # TIMING - AGE 32-34
        patterns['marriage_age_30s'] = [
            r'marriage.*age.*30',
            r'marriage.*age.*32',
            r'marriage.*age.*33',
            r'marriage.*age.*34',
            r'late.*marriage.*30'
        ]
        
        # COMPREHENSIVE MARRIAGE ANALYSIS
        patterns['complete_marriage_analysis'] = [
            r'complete.*marriage.*analysis',
            r'comprehensive.*marriage',
            r'marriage.*prediction.*method'
        ]
        
        return patterns
    
    def search_in_book(self, json_file):
        """Search for Akshit-specific content in a book"""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            book_name = data.get('book_name', 'Unknown')
            pages = data.get('full_text_pages', [])
            
            results = {
                'book_name': book_name,
                'total_pages': len(pages),
                'findings': {}
            }
            
            # Search each pattern
            for category, patterns in self.search_patterns.items():
                category_results = []
                
                for page in pages:
                    text = page['text']
                    page_num = page['page']
                    
                    for pattern in patterns:
                        matches = re.finditer(pattern, text, re.IGNORECASE)
                        for match in matches:
                            # Get larger context (500 chars)
                            start = max(0, match.start() - 300)
                            end = min(len(text), match.end() + 300)
                            context = text[start:end]
                            
                            category_results.append({
                                'page': page_num,
                                'match': match.group(),
                                'context': context.replace('\n', ' ').strip(),
                                'full_page_text': text  # Store full page for detailed analysis
                            })
                
                if category_results:
                    results['findings'][category] = category_results
            
            return results
        
        except Exception as e:
            print(f"Error processing {json_file}: {e}")
            return None
    
    def search_all_books(self):
        """Search all books for Akshit's chart patterns"""
        json_files = list(self.extracted_dir.glob("*_extraction.json"))
        
        print("="*80)
        print("COMPREHENSIVE MARRIAGE ANALYSIS FOR AKSHIT")
        print("Searching 33 books for YOUR specific chart placements")
        print("="*80)
        
        all_results = []
        
        for json_file in json_files:
            print(f"\nSearching: {json_file.stem.replace('_extraction', '')[:60]}")
            results = self.search_in_book(json_file)
            
            if results and results['findings']:
                all_results.append(results)
                
                # Print summary
                total_matches = sum(len(findings) for findings in results['findings'].values())
                print(f"  ✓ Found {total_matches} relevant references")
                
                # Show top categories
                top_cats = sorted(results['findings'].items(), 
                                key=lambda x: len(x[1]), reverse=True)[:3]
                for cat, findings in top_cats:
                    print(f"    - {cat}: {len(findings)} matches")
        
        return all_results
    
    def save_comprehensive_analysis(self, results, output_file):
        """Save comprehensive analysis with chart-specific findings"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# AKSHIT'S MARRIAGE ANALYSIS - FROM ALL 33 CLASSICAL BOOKS\n\n")
            f.write("**Analysis Date**: February 26, 2026\n")
            f.write("**Birth Date**: December 26, 1994, 22:50, Kanpur\n")
            f.write("**Current Age**: 31 years\n")
            f.write("**Books Analyzed**: 33 classical texts\n\n")
            
            f.write("---\n\n")
            
            # CHART SUMMARY
            f.write("## YOUR CHART SUMMARY\n\n")
            f.write("### D1 (Birth Chart) - Key Placements\n\n")
            for planet, data in self.chart['D1'].items():
                if planet != 'ASCENDANT':
                    f.write(f"- **{planet}**: {data['sign']} in House {data['house']} ")
                    if 'nakshatra' in data:
                        f.write(f"({data['nakshatra']} nakshatra)")
                    f.write("\n")
            
            f.write("\n### D9 (Navamsa) - Marriage Chart\n\n")
            for planet, data in self.chart['D9'].items():
                if planet != 'ASCENDANT':
                    f.write(f"- **{planet}**: {data['sign']} in House {data['house']}\n")
            
            f.write("\n### Current Dasha Period\n\n")
            f.write(f"- **Mahadasha**: {self.chart['DASHA']['current_mahadasha']} (2020-2036)\n")
            f.write(f"- **Marriage Period**: Jupiter-Venus (2027-2030)\n\n")
            
            f.write("---\n\n")
            
            # SUMMARY TABLE
            f.write("## FINDINGS SUMMARY\n\n")
            f.write("| Book | Total Matches | Key Findings |\n")
            f.write("|------|---------------|-------------|\n")
            
            for result in results:
                book = result['book_name'][:45]
                total = sum(len(matches) for matches in result['findings'].values())
                
                # Get top 2 categories
                top_cats = sorted(result['findings'].items(), 
                                key=lambda x: len(x[1]), reverse=True)[:2]
                key_findings = ', '.join([f"{cat.replace('_', ' ')}" for cat, _ in top_cats])
                
                f.write(f"| {book} | {total} | {key_findings} |\n")
            
            f.write("\n---\n\n")
            
            # DETAILED FINDINGS BY CHART PLACEMENT
            f.write("## DETAILED FINDINGS - ORGANIZED BY YOUR CHART\n\n")
            
            # Group patterns by chart element
            chart_groups = {
                'SATURN IN AQUARIUS 7TH HOUSE (D1)': [
                    'saturn_aquarius_7th', 'saturn_own_sign_7th_yoga', 
                    'saturn_7th_spouse_age', 'saturn_aquarius_age', 'saturn_aspects'
                ],
                'VENUS IN LIBRA 3RD HOUSE (D1)': [
                    'venus_libra_3rd', 'venus_own_sign_yoga', 'rahu_venus_libra_3rd',
                    'vishakha_nakshatra'
                ],
                'JUPITER IN SCORPIO 4TH HOUSE (D1)': [
                    'jupiter_scorpio_4th', 'jupiter_4th_house_yoga', 'jupiter_aspects',
                    'anuradha_nakshatra'
                ],
                'MARS IN LEO 1ST HOUSE (D1)': [
                    'mars_leo_1st', 'mars_aspects', 'magha_nakshatra'
                ],
                'MOON IN VIRGO 2ND HOUSE (D1)': [
                    'moon_virgo_2nd', 'chitra_nakshatra'
                ],
                'SUN & MERCURY IN SAGITTARIUS 5TH HOUSE (D1)': [
                    'sun_mercury_sagittarius_5th', '2nd_lord_5th_house', '11th_lord_5th_house'
                ],
                'NAVAMSA (D9) ANALYSIS': [
                    'd9_venus_taurus_8th', 'd9_saturn_aquarius', 'd9_jupiter_virgo_12th',
                    'd9_sun_moon_cancer'
                ],
                'DIVISIONAL CHARTS (D7, D10, D60)': [
                    'd7_analysis', 'd10_analysis', 'd60_analysis'
                ],
                'DASHA PERIODS': [
                    'jupiter_mahadasha_marriage', 'jupiter_venus_dasha', 'jupiter_ketu_dasha'
                ],
                'SPECIAL YOGAS & COMBINATIONS': [
                    '7th_lord_7th_house', 'leo_ascendant_marriage'
                ],
                'MARRIAGE TIMING & AGE': [
                    'marriage_age_30s', 'complete_marriage_analysis'
                ],
                'NAKSHATRA ANALYSIS': [
                    'shatabhisha_nakshatra'
                ]
            }
            
            for group_name, categories in chart_groups.items():
                f.write(f"\n## {group_name}\n\n")
                
                for category in categories:
                    # Check if any book has this category
                    has_content = any(category in result['findings'] for result in results)
                    if not has_content:
                        continue
                    
                    f.write(f"### {category.replace('_', ' ').title()}\n\n")
                    
                    for result in results:
                        if category in result['findings']:
                            findings = result['findings'][category]
                            f.write(f"#### 📚 {result['book_name']}\n\n")
                            f.write(f"**Found {len(findings)} references**\n\n")
                            
                            # Show ALL references for chart-specific patterns
                            for i, finding in enumerate(findings, 1):
                                f.write(f"**Reference {i} (Page {finding['page']})**:\n\n")
                                f.write(f"{finding['context']}\n\n")
                                f.write("---\n\n")
        
        print(f"\n\n{'='*80}")
        print(f"COMPREHENSIVE ANALYSIS SAVED!")
        print(f"Output: {output_file}")
        print(f"{'='*80}")


def main():
    script_dir = Path(__file__).parent
    extracted_dir = script_dir / "extracted_content"
    output_file = script_dir.parent.parent / "AKSHIT_MARRIAGE_FROM_ALL_BOOKS.md"
    
    analyzer = AkshitMarriageAnalyzer(extracted_dir)
    results = analyzer.search_all_books()
    
    if results:
        analyzer.save_comprehensive_analysis(results, output_file)
        
        # Print statistics
        total_matches = sum(
            sum(len(matches) for matches in result['findings'].values())
            for result in results
        )
        
        print(f"\n{'='*80}")
        print(f"ANALYSIS COMPLETE!")
        print(f"Books with relevant content: {len(results)}")
        print(f"Total references found: {total_matches}")
        print(f"Output file: {output_file}")
        print(f"{'='*80}\n")
    else:
        print("No relevant content found!")


if __name__ == "__main__":
    main()
