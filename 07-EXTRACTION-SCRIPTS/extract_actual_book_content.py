#!/usr/bin/env python3
"""
Extract ACTUAL content from PDFs about Akshit's specific chart placements
With real page numbers and quotes from classical texts
"""

import json
from pathlib import Path
import re

EXTRACTED_DIR = Path('/Users/akshitsethi/Desktop/astro/astrology-learning/extraction-system/extracted_content')

# Akshit's specific placements to search for
SEARCH_TOPICS = {
    'Saturn in 7th house Aquarius': [
        r'saturn.*7th.*house',
        r'7th.*lord.*saturn',
        r'saturn.*aquarius.*7th',
        r'saturn.*own.*sign.*7th',
        r'shani.*saptam.*bhava'
    ],
    'Venus in Libra 3rd house': [
        r'venus.*libra',
        r'venus.*own.*sign',
        r'venus.*exalted.*libra',
        r'venus.*3rd.*house',
        r'shukra.*tula'
    ],
    'Jupiter in Scorpio 4th house': [
        r'jupiter.*scorpio',
        r'jupiter.*4th.*house',
        r'guru.*vrishchika',
        r'jupiter.*fourth.*bhava'
    ],
    'Leo Ascendant marriage': [
        r'leo.*ascendant.*marriage',
        r'leo.*rising.*spouse',
        r'simha.*lagna.*vivaha'
    ],
    'Navamsa Venus Taurus': [
        r'navamsa.*venus',
        r'venus.*taurus.*navamsa',
        r'd9.*venus',
        r'navamsa.*marriage'
    ],
    'Jupiter-Venus dasha marriage': [
        r'jupiter.*venus.*dasha',
        r'guru.*shukra.*period',
        r'jupiter.*venus.*marriage',
        r'benefic.*dasha.*marriage'
    ],
    'Spouse age older': [
        r'spouse.*age',
        r'spouse.*older',
        r'age.*difference.*marriage',
        r'saturn.*7th.*age'
    ]
}

def extract_actual_quotes(book_file, topic, patterns, max_quotes=5):
    """Extract actual text quotes from a book for a specific topic"""
    
    json_path = EXTRACTED_DIR / f"{book_file}_extraction.json"
    
    if not json_path.exists():
        return []
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        return []
    
    book_name = data.get('book_name', book_file)
    full_text_pages = data.get('full_text_pages', [])
    
    quotes = []
    
    for page_data in full_text_pages:
        page_num = page_data.get('page', 0)
        text = page_data.get('text', '')
        
        if not text or len(text) < 100:
            continue
        
        text_lower = text.lower()
        
        # Check if any pattern matches
        for pattern in patterns:
            if re.search(pattern, text_lower, re.IGNORECASE):
                quotes.append({
                    'book': book_name,
                    'page': page_num,
                    'text': text[:800],  # First 800 chars
                    'pattern': pattern
                })
                break  # One quote per page
        
        if len(quotes) >= max_quotes:
            break
    
    return quotes

def analyze_all_books_for_actual_content():
    """Search all books and extract actual quotes"""
    
    json_files = list(EXTRACTED_DIR.glob("*_extraction.json"))
    
    print(f"Searching {len(json_files)} books for actual content...")
    print("="*80)
    
    all_findings = {}
    
    for topic, patterns in SEARCH_TOPICS.items():
        print(f"\n\nSEARCHING FOR: {topic}")
        print("="*80)
        
        topic_quotes = []
        
        for json_file in json_files:
            book_name = json_file.stem.replace('_extraction', '')
            quotes = extract_actual_quotes(book_name, topic, patterns, max_quotes=3)
            topic_quotes.extend(quotes)
        
        all_findings[topic] = topic_quotes
        
        print(f"Found {len(topic_quotes)} quotes from {len(set(q['book'] for q in topic_quotes))} books")
        
        # Show first 3 quotes
        for i, quote in enumerate(topic_quotes[:3], 1):
            print(f"\n{i}. {quote['book']} - Page {quote['page']}")
            print(f"   {quote['text'][:200]}...")
    
    return all_findings

def generate_report_with_actual_quotes(all_findings):
    """Generate report with actual book quotes"""
    
    output_file = Path('AKSHIT_MARRIAGE_WITH_ACTUAL_BOOK_QUOTES.md')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# AKSHIT'S MARRIAGE ANALYSIS - WITH ACTUAL BOOK QUOTES\n\n")
        f.write("**Analysis Date**: February 26, 2026\n")
        f.write("**Birth Details**: December 26, 1994, 22:50, Kanpur (Age 31)\n\n")
        
        f.write("## CHART PLACEMENTS\n\n")
        f.write("- **Ascendant**: Leo\n")
        f.write("- **Saturn**: Aquarius 7th house (Own Sign)\n")
        f.write("- **Venus**: Libra 3rd house (Exalted)\n")
        f.write("- **Jupiter**: Scorpio 4th house\n")
        f.write("- **D9 Venus**: Taurus 8th house (Own Sign)\n")
        f.write("- **Current Dasha**: Jupiter-Venus\n\n")
        
        f.write("---\n\n")
        
        for topic, quotes in all_findings.items():
            f.write(f"\n## {topic.upper()}\n\n")
            f.write(f"**Found in {len(set(q['book'] for q in quotes))} books, {len(quotes)} total references**\n\n")
            
            if not quotes:
                f.write("*No specific content found in extracted books*\n\n")
                continue
            
            # Group by book
            books = {}
            for quote in quotes:
                book = quote['book']
                if book not in books:
                    books[book] = []
                books[book].append(quote)
            
            for book, book_quotes in books.items():
                f.write(f"\n### {book}\n\n")
                
                for quote in book_quotes[:5]:  # Max 5 quotes per book
                    f.write(f"**Page {quote['page']}**:\n")
                    f.write(f"> {quote['text'][:600]}\n\n")
                    if len(quote['text']) > 600:
                        f.write(f"> ...(continued)\n\n")
            
            f.write("\n---\n")
        
        f.write("\n\n## SUMMARY\n\n")
        f.write("This analysis contains ACTUAL quotes from classical astrology texts.\n")
        f.write("Each quote includes the book name and page number for verification.\n\n")
        
        total_quotes = sum(len(quotes) for quotes in all_findings.values())
        total_books = len(set(q['book'] for quotes in all_findings.values() for q in quotes))
        
        f.write(f"**Total Quotes Extracted**: {total_quotes}\n")
        f.write(f"**Books Referenced**: {total_books}\n")
    
    print(f"\n\n{'='*80}")
    print(f"REPORT SAVED: {output_file}")
    print(f"{'='*80}")
    print(f"Total quotes: {total_quotes}")
    print(f"Books referenced: {total_books}")

if __name__ == '__main__':
    findings = analyze_all_books_for_actual_content()
    generate_report_with_actual_quotes(findings)
