#!/usr/bin/env python3
"""
Extract actual quotes with page numbers from top books
"""

import json
from pathlib import Path

def extract_quotes_from_book(book_file, max_quotes=20):
    """Extract actual text quotes from a book"""
    
    extracted_dir = Path('/Users/akshitsethi/Desktop/astro/astrology-learning/extraction-system/extracted_content')
    json_path = extracted_dir / f"{book_file}_extraction.json"
    
    if not json_path.exists():
        print(f"File not found: {json_path}")
        return []
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    book_name = data.get('book_name', book_file)
    full_text_pages = data.get('full_text_pages', [])
    
    print(f"\n{'='*80}")
    print(f"BOOK: {book_name}")
    print(f"Total Pages: {len(full_text_pages)}")
    print(f"{'='*80}\n")
    
    # Search keywords
    keywords = ['saturn', '7th house', 'marriage', 'venus', 'jupiter', 'spouse', 'navamsa']
    
    quotes = []
    for page_data in full_text_pages:
        page_num = page_data.get('page', 0)
        text = page_data.get('text', '')
        
        if not text or len(text) < 100:
            continue
        
        text_lower = text.lower()
        
        # Check if page contains relevant keywords
        if any(keyword in text_lower for keyword in keywords):
            quotes.append({
                'page': page_num,
                'text': text[:500]  # First 500 chars
            })
    
    # Print first few quotes
    for i, quote in enumerate(quotes[:max_quotes], 1):
        print(f"PAGE {quote['page']}:")
        print(f"{quote['text']}")
        print(f"\n{'-'*80}\n")
    
    return quotes

# Top books to extract from
top_books = [
    'vedic_astro_textbook',
    '2015.150536.Marriage-Married-Life-And-Children_text',
    'BPHS - 1 RSanthanam',
    'A.K. Gour_Astrology of Professions',
    'Astrology_ destiny and the wheel of time_ban',
    'A Text book of astrology_Anil Kumar Jain'
]

print("EXTRACTING ACTUAL QUOTES FROM TOP 6 BOOKS")
print("="*80)

all_quotes = {}
for book in top_books:
    quotes = extract_quotes_from_book(book, max_quotes=10)
    all_quotes[book] = quotes
    print(f"\nExtracted {len(quotes)} relevant pages from {book}\n")

print(f"\n\nTOTAL: Extracted content from {len(all_quotes)} books")
