#!/usr/bin/env python3
"""
COMPREHENSIVE MARRIAGE ANALYSIS FROM ALL 33 EXTRACTED PDFs
Search for ACTUAL content with PAGE NUMBERS and QUOTES

Akshit's Chart Key Features:
- Birth: Dec 26, 1994, 22:50, Kanpur (Age 31)
- Ascendant: Leo
- Saturn in Aquarius 7th house (own sign)
- Venus in Libra 3rd house (exalted)
- Jupiter in Scorpio 4th house
- D9: Libra ascendant, Venus in Taurus 8th, Jupiter in Virgo 12th
- Current Dasha: Jupiter-Venus (marriage favorable)
"""

import json
from pathlib import Path
import re

# Chart data
CHART_DATA = {
    'ascendant': 'Leo',
    'saturn': {'sign': 'Aquarius', 'house': 7, 'dignity': 'Own Sign'},
    'venus': {'sign': 'Libra', 'house': 3, 'dignity': 'Exalted'},
    'jupiter': {'sign': 'Scorpio', 'house': 4},
    'd9_ascendant': 'Libra',
    'd9_venus': {'sign': 'Taurus', 'house': 8},
    'd9_jupiter': {'sign': 'Virgo', 'house': 12},
    'current_dasha': 'Jupiter-Venus'
}

# Search patterns - comprehensive list
SEARCH_PATTERNS = {
    # Saturn patterns
    'saturn_7th': [
        r'saturn.*7th.*house',
        r'7th.*house.*saturn',
        r'saturn.*marriage',
        r'saturn.*spouse',
        r'saturn.*aquarius',
        r'saturn.*own.*sign.*7th'
    ],
    
    # Venus patterns
    'venus_marriage': [
        r'venus.*exalted',
        r'venus.*libra',
        r'venus.*3rd.*house',
        r'venus.*marriage',
        r'exalted.*venus.*marriage'
    ],
    
    # Jupiter patterns
    'jupiter_marriage': [
        r'jupiter.*4th.*house',
        r'jupiter.*scorpio',
        r'jupiter.*dasha.*marriage',
        r'jupiter.*venus.*dasha'
    ],
    
    # Navamsa patterns
    'navamsa': [
        r'navamsa.*marriage',
        r'd9.*marriage',
        r'navamsa.*venus',
        r'navamsa.*jupiter',
        r'libra.*navamsa'
    ],
    
    # Marriage timing
    'timing': [
        r'marriage.*timing',
        r'age.*marriage',
        r'dasha.*marriage',
        r'jupiter.*venus.*period',
        r'30.*31.*32.*marriage'
    ],
    
    # Spouse characteristics
    'spouse': [
        r'spouse.*age',
        r'spouse.*characteristics',
        r'7th.*lord',
        r'spouse.*older',
        r'spouse.*younger'
    ],
    
    # Leo ascendant
    'leo_asc': [
        r'leo.*ascendant.*marriage',
        r'leo.*rising.*marriage',
        r'sun.*ascendant.*lord'
    ]
}

def search_in_text(text, patterns):
    """Search for patterns in text"""
    matches = []
    text_lower = text.lower()
    
    for pattern in patterns:
        if re.search(pattern, text_lower, re.IGNORECASE):
            matches.append(pattern)
    
    return matches

def analyze_all_books():
    """Analyze all 33 extracted books"""
    
    extracted_dir = Path('/Users/akshitsethi/Desktop/astro/astrology-learning/extraction-system/extracted_content')
    json_files = list(extracted_dir.glob("*_extraction.json"))
    
    print(f"=" * 80)
    print(f"COMPREHENSIVE MARRIAGE ANALYSIS FROM {len(json_files)} BOOKS")
    print(f"=" * 80)
    print()
    
    all_findings = {}
    
    for json_file in sorted(json_files):
        book_name = json_file.stem.replace('_extraction', '')
        
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            book_findings = analyze_book(data, book_name)
            
            if book_findings['total_matches'] > 0:
                all_findings[book_name] = book_findings
                print_book_summary(book_name, book_findings)
        
        except Exception as e:
            print(f"Error processing {book_name}: {e}")
    
    # Generate comprehensive report
    generate_report(all_findings)
    
    return all_findings

def analyze_book(data, book_name):
    """Analyze a single book for all patterns"""
    
    findings = {
        'book_name': data.get('book_name', book_name),
        'total_pages': data.get('total_pages', 0),
        'matches_by_category': {},
        'total_matches': 0,
        'sample_quotes': []
    }
    
    # Get full text pages
    full_text_pages = data.get('full_text_pages', [])
    
    if not full_text_pages:
        return findings
    
    # Search each category
    for category, patterns in SEARCH_PATTERNS.items():
        category_matches = []
        
        for page_data in full_text_pages:
            page_num = page_data.get('page', 0)
            text = page_data.get('text', '')
            
            if not text or len(text) < 50:
                continue
            
            matches = search_in_text(text, patterns)
            
            if matches:
                category_matches.append({
                    'page': page_num,
                    'text_preview': text[:300],
                    'patterns_found': matches
                })
        
        if category_matches:
            findings['matches_by_category'][category] = category_matches
            findings['total_matches'] += len(category_matches)
            
            # Save sample quotes (first 3 per category)
            for match in category_matches[:3]:
                findings['sample_quotes'].append({
                    'category': category,
                    'page': match['page'],
                    'text': match['text_preview']
                })
    
    return findings

def print_book_summary(book_name, findings):
    """Print summary for one book"""
    
    print(f"\n{'='*80}")
    print(f"BOOK: {findings['book_name']}")
    print(f"Total Pages: {findings['total_pages']}")
    print(f"Relevant Matches: {findings['total_matches']}")
    print(f"{'='*80}")
    
    for category, matches in findings['matches_by_category'].items():
        print(f"\n  {category.upper()}: {len(matches)} matches")
        
        # Show first 2 page numbers
        pages = [m['page'] for m in matches[:5]]
        print(f"    Pages: {', '.join(map(str, pages))}")

def generate_report(all_findings):
    """Generate comprehensive markdown report"""
    
    output_file = Path('AKSHIT_MARRIAGE_ANALYSIS_FROM_ALL_PDFS.md')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# AKSHIT'S MARRIAGE ANALYSIS - FROM ALL 33 CLASSICAL TEXTS\n\n")
        f.write("**Analysis Date**: February 26, 2026\n")
        f.write("**Birth Details**: December 26, 1994, 22:50, Kanpur (Age 31)\n\n")
        
        f.write("## CHART SUMMARY\n\n")
        f.write("- **Ascendant**: Leo\n")
        f.write("- **Saturn**: Aquarius 7th house (Own Sign)\n")
        f.write("- **Venus**: Libra 3rd house (Exalted)\n")
        f.write("- **Jupiter**: Scorpio 4th house\n")
        f.write("- **D9 Ascendant**: Libra\n")
        f.write("- **Current Dasha**: Jupiter-Venus\n\n")
        
        f.write(f"## BOOKS ANALYZED: {len(all_findings)}\n\n")
        
        # Summary table
        f.write("| Book | Total Pages | Relevant Matches |\n")
        f.write("|------|-------------|------------------|\n")
        
        for book_name, findings in sorted(all_findings.items(), 
                                         key=lambda x: x[1]['total_matches'], 
                                         reverse=True):
            f.write(f"| {findings['book_name'][:50]} | {findings['total_pages']} | {findings['total_matches']} |\n")
        
        f.write("\n\n## DETAILED FINDINGS BY BOOK\n\n")
        
        # Detailed findings
        for book_name, findings in sorted(all_findings.items(), 
                                         key=lambda x: x[1]['total_matches'], 
                                         reverse=True):
            f.write(f"\n### {findings['book_name']}\n\n")
            f.write(f"**Total Pages**: {findings['total_pages']}  \n")
            f.write(f"**Relevant Matches**: {findings['total_matches']}\n\n")
            
            for category, matches in findings['matches_by_category'].items():
                f.write(f"\n#### {category.upper().replace('_', ' ')}\n\n")
                f.write(f"Found on {len(matches)} pages: ")
                pages = [str(m['page']) for m in matches[:10]]
                f.write(f"{', '.join(pages)}\n\n")
                
                # Show sample quotes
                for i, match in enumerate(matches[:2], 1):
                    f.write(f"**Page {match['page']} - Sample {i}**:\n")
                    f.write(f"> {match['text_preview'][:250]}...\n\n")
        
        f.write("\n\n## NEXT STEPS\n\n")
        f.write("1. Read detailed content from high-match books\n")
        f.write("2. Extract specific rules about Saturn in 7th, Venus exalted, etc.\n")
        f.write("3. Cross-reference multiple books for each prediction\n")
        f.write("4. Create final analysis with page-by-page references\n")
    
    print(f"\n\n{'='*80}")
    print(f"REPORT SAVED: {output_file}")
    print(f"{'='*80}")

if __name__ == '__main__':
    findings = analyze_all_books()
    print(f"\n\nAnalysis complete! Found relevant content in {len(findings)} books.")
