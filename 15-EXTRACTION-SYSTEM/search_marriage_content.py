#!/usr/bin/env python3
"""
Search all extracted PDFs for marriage-specific content
Focus on: Saturn in 7th, spouse age, marriage timing, spouse characteristics
"""

import json
import os
from pathlib import Path
import re

class MarriageContentSearcher:
    def __init__(self, extracted_dir):
        self.extracted_dir = Path(extracted_dir)
        
        # COMPREHENSIVE Search keywords - EVERYTHING about marriage
        self.search_patterns = {
            # ALL PLANETS IN 7TH HOUSE
            'sun_7th': [r'sun.*7th', r'7th.*sun', r'surya.*saptam'],
            'moon_7th': [r'moon.*7th', r'7th.*moon', r'chandra.*saptam'],
            'mars_7th': [r'mars.*7th', r'7th.*mars', r'mangal.*saptam', r'kuja.*7th'],
            'mercury_7th': [r'mercury.*7th', r'7th.*mercury', r'budha.*saptam'],
            'jupiter_7th': [r'jupiter.*7th', r'7th.*jupiter', r'guru.*saptam'],
            'venus_7th': [r'venus.*7th', r'7th.*venus', r'shukra.*saptam'],
            'saturn_7th': [r'saturn.*7th', r'7th.*saturn', r'shani.*saptam'],
            'rahu_7th': [r'rahu.*7th', r'7th.*rahu'],
            'ketu_7th': [r'ketu.*7th', r'7th.*ketu'],
            
            # 7TH LORD IN ALL HOUSES
            '7th_lord_houses': [r'7th.*lord.*house', r'seventh.*lord', r'kalatra.*lord', r'saptamesh'],
            
            # VENUS (MARRIAGE KARAKA)
            'venus_analysis': [r'venus.*marriage', r'shukra.*vivaha', r'venus.*spouse', r'venus.*wife'],
            'venus_signs': [r'venus.*sign', r'venus.*exalted', r'venus.*debilitated', r'venus.*own sign'],
            'venus_houses': [r'venus.*house', r'shukra.*bhava'],
            
            # JUPITER (FOR WOMEN)
            'jupiter_marriage': [r'jupiter.*husband', r'jupiter.*marriage', r'guru.*vivaha'],
            
            # NAVAMSA (D9) - MARRIAGE CHART
            'navamsa_marriage': [r'navamsa.*marriage', r'D9.*marriage', r'navamsa.*spouse', r'd9.*7th'],
            'navamsa_venus': [r'navamsa.*venus', r'd9.*venus', r'navamsa.*shukra'],
            'navamsa_7th': [r'navamsa.*7th.*house', r'd9.*seventh'],
            
            # SPOUSE AGE - COMPREHENSIVE
            'spouse_age': [r'spouse.*age', r'age.*spouse', r'older.*spouse', r'younger.*spouse', 
                          r'age.*difference', r'age.*gap', r'partner.*age', r'age.*husband', r'age.*wife'],
            
            # SPOUSE APPEARANCE
            'spouse_appearance': [r'spouse.*appearance', r'spouse.*looks', r'spouse.*beauty', 
                                 r'spouse.*complexion', r'spouse.*height', r'physical.*spouse'],
            
            # SPOUSE NATURE/PERSONALITY
            'spouse_nature': [r'spouse.*nature', r'spouse.*character', r'spouse.*personality',
                             r'spouse.*temperament', r'spouse.*behavior'],
            
            # SPOUSE PROFESSION
            'spouse_profession': [r'spouse.*profession', r'spouse.*career', r'spouse.*occupation',
                                 r'partner.*work', r'wife.*career', r'husband.*profession'],
            
            # SPOUSE FAMILY
            'spouse_family': [r'spouse.*family', r'in-laws', r'spouse.*background', r'partner.*family'],
            
            # MARRIAGE TIMING - ALL METHODS
            'marriage_timing_general': [r'marriage.*timing', r'when.*marry', r'marriage.*age', r'vivaha.*kala'],
            'marriage_dasha': [r'marriage.*dasha', r'marriage.*mahadasha', r'marriage.*antardasha',
                              r'dasha.*marriage', r'vivaha.*dasha'],
            'marriage_transit': [r'marriage.*transit', r'transit.*marriage', r'gochara.*vivaha'],
            'marriage_progression': [r'marriage.*progression', r'progression.*marriage'],
            
            # MARRIAGE YOGAS
            'marriage_yogas': [r'marriage.*yoga', r'vivaha.*yoga', r'kalatra.*yoga', r'spouse.*yoga'],
            'raja_yoga_marriage': [r'raja.*yoga.*marriage', r'dhana.*yoga.*marriage'],
            
            # MARRIAGE DENIAL/DELAY
            'marriage_denial': [r'marriage.*denial', r'no.*marriage', r'marriage.*obstruction',
                               r'marriage.*delay', r'delayed.*marriage', r'late.*marriage'],
            
            # LOVE VS ARRANGED
            'love_marriage': [r'love.*marriage', r'love.*affair', r'romance.*marriage', r'gandharva.*vivaha'],
            'arranged_marriage': [r'arranged.*marriage', r'brahma.*vivaha', r'traditional.*marriage'],
            
            # MULTIPLE MARRIAGES
            'multiple_marriages': [r'two.*marriage', r'multiple.*marriage', r'second.*marriage',
                                  r'remarriage', r'divorce', r'separation'],
            
            # MARRIAGE HAPPINESS
            'marriage_happiness': [r'marriage.*happiness', r'happy.*marriage', r'marital.*bliss',
                                  r'marriage.*success', r'harmonious.*marriage'],
            'marriage_problems': [r'marriage.*problem', r'marital.*discord', r'marriage.*conflict',
                                 r'unhappy.*marriage', r'marriage.*trouble'],
            
            # CHILDREN FROM MARRIAGE
            'children_marriage': [r'children.*marriage', r'progeny.*marriage', r'5th.*house.*marriage',
                                 r'putra.*vivaha'],
            
            # UPAPADA LAGNA
            'upapada': [r'upapada', r'arudha.*7th', r'UL'],
            
            # DARAKARAKA
            'darakaraka': [r'darakaraka', r'DK', r'spouse.*significator'],
            
            # COMPATIBILITY
            'compatibility': [r'compatibility', r'matching', r'kuta', r'guna.*milan', r'horoscope.*matching'],
            
            # MANGLIK/KUJA DOSHA
            'manglik': [r'manglik', r'mangal.*dosha', r'kuja.*dosha', r'mars.*dosha'],
            
            # NAKSHATRAS FOR MARRIAGE
            'nakshatra_marriage': [r'nakshatra.*marriage', r'nakshatra.*spouse', r'star.*marriage'],
            
            # ASPECTS TO 7TH HOUSE
            'aspects_7th': [r'aspect.*7th', r'7th.*aspect', r'drishti.*saptam'],
            
            # MARRIAGE REMEDIES
            'marriage_remedies': [r'marriage.*remedy', r'marriage.*upaya', r'marriage.*mantra',
                                 r'marriage.*puja', r'marriage.*gemstone'],
            
            # FOREIGN SPOUSE
            'foreign_spouse': [r'foreign.*spouse', r'foreign.*marriage', r'intercaste', r'different.*culture'],
            
            # MARRIAGE MUHURTA
            'marriage_muhurta': [r'marriage.*muhurta', r'vivaha.*muhurta', r'wedding.*timing',
                                r'auspicious.*marriage'],
            
            # CASE STUDIES
            'marriage_examples': [r'example.*marriage', r'case.*marriage', r'chart.*marriage',
                                 r'horoscope.*marriage.*example']
        }
    
    def search_in_book(self, json_file):
        """Search for marriage content in a single book"""
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
            
            # Search each category
            for category, patterns in self.search_patterns.items():
                category_results = []
                
                for page in pages:
                    text = page['text']
                    page_num = page['page']
                    
                    # Check if any pattern matches
                    for pattern in patterns:
                        matches = re.finditer(pattern, text, re.IGNORECASE)
                        for match in matches:
                            # Get context (200 chars before and after)
                            start = max(0, match.start() - 200)
                            end = min(len(text), match.end() + 200)
                            context = text[start:end]
                            
                            category_results.append({
                                'page': page_num,
                                'match': match.group(),
                                'context': context.replace('\n', ' ').strip()
                            })
                
                if category_results:
                    results['findings'][category] = category_results
            
            return results
        
        except Exception as e:
            print(f"Error processing {json_file}: {e}")
            return None
    
    def search_all_books(self):
        """Search all extracted books"""
        json_files = list(self.extracted_dir.glob("*_extraction.json"))
        
        print(f"Searching {len(json_files)} books for marriage content...")
        print("="*70)
        
        all_results = []
        
        for json_file in json_files:
            print(f"\nSearching: {json_file.stem.replace('_extraction', '')}")
            results = self.search_in_book(json_file)
            
            if results and results['findings']:
                all_results.append(results)
                
                # Print summary
                for category, findings in results['findings'].items():
                    print(f"  {category}: {len(findings)} matches")
        
        return all_results
    
    def save_results(self, results, output_file):
        """Save search results to markdown"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# MARRIAGE CONTENT FROM ALL 33 EXTRACTED BOOKS\n\n")
            f.write("**Search Date**: February 26, 2026\n")
            f.write(f"**Books Searched**: {len(results)}\n\n")
            f.write("---\n\n")
            
            # Summary table - count total findings per book
            f.write("## SUMMARY OF FINDINGS\n\n")
            f.write("| Book | Total Matches | Top Categories |\n")
            f.write("|------|---------------|----------------|\n")
            
            for result in results:
                book = result['book_name'][:50]
                findings = result['findings']
                
                # Count total matches
                total = sum(len(matches) for matches in findings.values())
                
                # Get top 3 categories
                category_counts = [(cat, len(matches)) for cat, matches in findings.items()]
                category_counts.sort(key=lambda x: x[1], reverse=True)
                top_cats = ', '.join([f"{cat}({count})" for cat, count in category_counts[:3]])
                
                f.write(f"| {book} | {total} | {top_cats} |\n")
            
            # Category summary
            f.write("\n### CATEGORY TOTALS ACROSS ALL BOOKS\n\n")
            all_categories = {}
            for result in results:
                for category, matches in result['findings'].items():
                    if category not in all_categories:
                        all_categories[category] = 0
                    all_categories[category] += len(matches)
            
            sorted_cats = sorted(all_categories.items(), key=lambda x: x[1], reverse=True)
            for cat, count in sorted_cats:
                f.write(f"- **{cat.replace('_', ' ').title()}**: {count} references\n")
            
            # Detailed findings - ALL CATEGORIES
            f.write("\n---\n\n")
            f.write("## DETAILED FINDINGS BY CATEGORY\n\n")
            
            # Group categories logically
            category_groups = {
                'PLANETS IN 7TH HOUSE': ['sun_7th', 'moon_7th', 'mars_7th', 'mercury_7th', 
                                         'jupiter_7th', 'venus_7th', 'saturn_7th', 'rahu_7th', 'ketu_7th'],
                '7TH LORD & HOUSE': ['7th_lord_houses', 'aspects_7th'],
                'VENUS & JUPITER ANALYSIS': ['venus_analysis', 'venus_signs', 'venus_houses', 
                                             'jupiter_marriage'],
                'NAVAMSA (D9) ANALYSIS': ['navamsa_marriage', 'navamsa_venus', 'navamsa_7th'],
                'SPOUSE CHARACTERISTICS': ['spouse_age', 'spouse_appearance', 'spouse_nature', 
                                          'spouse_profession', 'spouse_family'],
                'MARRIAGE TIMING': ['marriage_timing_general', 'marriage_dasha', 'marriage_transit', 
                                   'marriage_progression'],
                'MARRIAGE YOGAS & COMBINATIONS': ['marriage_yogas', 'raja_yoga_marriage'],
                'MARRIAGE TYPES': ['love_marriage', 'arranged_marriage', 'foreign_spouse'],
                'MARRIAGE QUALITY': ['marriage_happiness', 'marriage_problems', 'multiple_marriages'],
                'MARRIAGE DENIAL/DELAY': ['marriage_denial'],
                'SPECIAL TECHNIQUES': ['upapada', 'darakaraka', 'nakshatra_marriage'],
                'COMPATIBILITY & DOSHAS': ['compatibility', 'manglik'],
                'CHILDREN & PROGENY': ['children_marriage'],
                'REMEDIES & MUHURTA': ['marriage_remedies', 'marriage_muhurta'],
                'CASE STUDIES': ['marriage_examples']
            }
            
            for group_name, categories in category_groups.items():
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
                            f.write(f"#### {result['book_name']} ({len(findings)} references)\n\n")
                            
                            # Show top 10 references for each category
                            for finding in findings[:10]:
                                f.write(f"**Page {finding['page']}**: {finding['context']}\n\n")
                            
                            if len(findings) > 10:
                                f.write(f"*...and {len(findings) - 10} more references*\n\n")
                            
                            f.write("---\n\n")
        
        print(f"\n\nResults saved to: {output_file}")


def main():
    script_dir = Path(__file__).parent
    extracted_dir = script_dir / "extracted_content"
    output_file = script_dir.parent.parent / "MARRIAGE_CONTENT_ALL_BOOKS.md"
    
    searcher = MarriageContentSearcher(extracted_dir)
    results = searcher.search_all_books()
    
    if results:
        searcher.save_results(results, output_file)
        print(f"\n{'='*70}")
        print(f"SEARCH COMPLETE!")
        print(f"Found marriage content in {len(results)} books")
        print(f"Output: {output_file}")
        print(f"{'='*70}")
    else:
        print("No marriage content found!")


if __name__ == "__main__":
    main()
