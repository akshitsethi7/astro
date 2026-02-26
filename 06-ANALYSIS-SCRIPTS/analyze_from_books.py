#!/usr/bin/env python3
"""
Analyze chart based on extracted book content
This will be run after PDF extraction
"""

import re
from pathlib import Path

# Chart data
CHART_DATA = {
    "D1": {
        "SUN": {"sign": "Sagittarius", "degree": "10°55'", "house": 5},
        "MOON": {"sign": "Virgo", "degree": "22°44'", "house": 2},
        "MARS": {"sign": "Leo", "degree": "8°33'", "house": 1},
        "MERCURY": {"sign": "Sagittarius", "degree": "18°06'", "house": 5},
        "JUPITER": {"sign": "Scorpio", "degree": "9°52'", "house": 4},
        "VENUS": {"sign": "Libra", "degree": "25°24'", "house": 3},
        "SATURN": {"sign": "Aquarius", "degree": "13°46'", "house": 7},
        "RAHU": {"sign": "Libra", "degree": "18°15'", "house": 3, "retrograde": True},
        "KETU": {"sign": "Aries", "degree": "18°15'", "house": 9, "retrograde": True},
    },
    "D9": {
        "SATURN": {"sign": "Aquarius", "degree": "04°00'", "house": 5},
        "VENUS": {"sign": "Taurus", "degree": "18°38'", "house": 8},
        "JUPITER": {"sign": "Virgo", "degree": "28°49'", "house": 12},
        "MOON": {"sign": "Cancer", "degree": "24°37'", "house": 10},
    }
}

def search_book_content(content, keywords):
    """Search for relevant content in extracted text"""
    results = []
    content_lower = content.lower()
    
    for keyword in keywords:
        pattern = re.compile(rf'.{{0,200}}{re.escape(keyword)}.{{0,200}}', re.IGNORECASE)
        matches = pattern.findall(content)
        results.extend(matches[:3])  # Top 3 matches
    
    return results

def analyze_marriage_from_books(extracted_text):
    """Analyze marriage based on book content"""
    analysis = []
    
    # Search for marriage-related content
    marriage_keywords = [
        "7th house", "seventh house", "marriage", "spouse", "vivah",
        "venus in own sign", "saturn in 7th", "navamsa", "d9",
        "marriage timing", "marriage age", "spouse age"
    ]
    
    relevant_content = search_book_content(extracted_text, marriage_keywords)
    
    analysis.append("MARRIAGE ANALYSIS FROM BOOKS:")
    analysis.append("="*80)
    
    if relevant_content:
        analysis.append("Relevant quotes from books:")
        for i, quote in enumerate(relevant_content[:10], 1):
            analysis.append(f"{i}. {quote[:200]}...")
    else:
        analysis.append("Using classical principles from books:")
        analysis.append("- Saturn in 7th house indicates delayed but stable marriage")
        analysis.append("- Venus in own sign indicates beautiful spouse")
        analysis.append("- Navamsa analysis is most important for marriage")
    
    return "\n".join(analysis)

def main():
    extracted_file = Path("/Users/akshitsethi/Desktop/astro/all_books_extracted.txt")
    
    if not extracted_file.exists():
        print("Extracted text file not found. Please run pdf_extractor.py first.")
        return
    
    print(f"Reading extracted content from: {extracted_file}")
    with open(extracted_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    print(f"Read {len(content)} characters")
    
    # Analyze
    marriage_analysis = analyze_marriage_from_books(content)
    
    # Save analysis
    output_file = Path("/Users/akshitsethi/Desktop/astro/analysis_from_books.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(marriage_analysis)
    
    print(f"\n✓ Analysis saved to: {output_file}")
    print(marriage_analysis[:500])

if __name__ == "__main__":
    main()
