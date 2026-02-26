#!/usr/bin/env python3
"""
Extract ONE book and distribute content intelligently across all folders
"""
import sys
import pdfplumber
from pathlib import Path
import re

def extract_bphs():
    """Extract BPHS and organize by topics"""
    
    # Find BPHS book
    books_dir = Path("../../../Books")
    bphs_file = books_dir / "BPHS - 1 RSanthanam.pdf"
    
    if not bphs_file.exists():
        print(f"ERROR: {bphs_file} not found")
        return
    
    print(f"Extracting: {bphs_file.name}")
    print("This will take a few minutes...")
    
    # Extract all text
    all_text = []
    with pdfplumber.open(bphs_file) as pdf:
        for i, page in enumerate(pdf.pages[:100]):  # First 100 pages for now
            text = page.extract_text()
            if text:
                all_text.append({
                    'page': i + 1,
                    'text': text
                })
            if (i + 1) % 10 == 0:
                print(f"  Processed {i + 1} pages...")
    
    print(f"✓ Extracted {len(all_text)} pages")
    
    # Organize by topics
    topics = {
        'planets': [],
        'houses': [],
        'signs': [],
        'nakshatras': [],
        'aspects': [],
        'marriage': [],
        'career': [],
        'wealth': [],
        'children': [],
        'health': [],
        'dashas': [],
        'transits': [],
        'divisional': [],
        'yogas': [],
        'remedies': []
    }
    
    # Keywords for each topic
    keywords = {
        'planets': ['planet', 'sun', 'moon', 'mars', 'mercury', 'jupiter', 'venus', 'saturn', 'rahu', 'ketu'],
        'houses': ['house', 'bhava', 'ascendant', 'lagna'],
        'signs': ['sign', 'rashi', 'aries', 'taurus', 'gemini'],
        'nakshatras': ['nakshatra', 'constellation'],
        'aspects': ['aspect', 'drishti'],
        'marriage': ['marriage', 'spouse', '7th house', 'seventh'],
        'career': ['career', 'profession', '10th house', 'tenth'],
        'wealth': ['wealth', 'money', 'dhana', '2nd house', '11th house'],
        'children': ['children', 'progeny', '5th house', 'putra'],
        'health': ['health', 'disease', '6th house', '8th house'],
        'dashas': ['dasha', 'mahadasha', 'vimshottari'],
        'transits': ['transit', 'gochara'],
        'divisional': ['navamsa', 'varga', 'divisional'],
        'yogas': ['yoga', 'combination', 'raja yoga'],
        'remedies': ['remedy', 'mantra', 'gemstone']
    }
    
    # Classify pages
    for page_data in all_text:
        text_lower = page_data['text'].lower()
        for topic, words in keywords.items():
            if any(word in text_lower for word in words):
                topics[topic].append(page_data)
    
    # Print statistics
    print("\nContent distribution:")
    for topic, pages in topics.items():
        print(f"  {topic}: {len(pages)} pages")
    
    return topics, all_text

if __name__ == "__main__":
    topics, all_text = extract_bphs()
    
    # Save for use
    import json
    output = {
        'topics': {k: len(v) for k, v in topics.items()},
        'total_pages': len(all_text)
    }
    
    with open('../extraction_stats.json', 'w') as f:
        json.dump(output, f, indent=2)
    
    print("\n✓ Extraction complete!")
    print("Run the content distributor next to fill all documents")
