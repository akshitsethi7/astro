#!/usr/bin/env python3
"""
Full BPHS Extraction and Content Distribution
Extract complete BPHS and distribute content to all 60 documents
"""
import sys
import json
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("Installing pdfplumber...")
    import os
    os.system(f"{sys.executable} -m pip install pdfplumber")
    import pdfplumber

def extract_full_bphs():
    """Extract complete BPHS book"""
    books_dir = Path("../../../Books")
    bphs_file = books_dir / "BPHS - 1 RSanthanam.pdf"
    
    if not bphs_file.exists():
        print(f"ERROR: {bphs_file} not found")
        return None
    
    print(f"Extracting COMPLETE BPHS: {bphs_file.name}")
    print("This will take 5-10 minutes for all ~400 pages...")
    print()
    
    all_pages = []
    
    with pdfplumber.open(bphs_file) as pdf:
        total = len(pdf.pages)
        print(f"Total pages: {total}")
        
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                all_pages.append({
                    'page': i + 1,
                    'text': text,
                    'length': len(text)
                })
            
            if (i + 1) % 50 == 0:
                print(f"  Processed {i + 1}/{total} pages ({int((i+1)/total*100)}%)")
    
    print(f"\n✓ Extracted {len(all_pages)} pages with text")
    print(f"  Total characters: {sum(p['length'] for p in all_pages):,}")
    
    return all_pages

def classify_content(all_pages):
    """Classify pages by topic"""
    
    # Comprehensive keyword mapping
    topic_keywords = {
        'planets': {
            'keywords': ['planet', 'sun', 'moon', 'mars', 'mercury', 'jupiter', 'venus', 
                        'saturn', 'rahu', 'ketu', 'graha', 'surya', 'chandra', 'mangal',
                        'budha', 'guru', 'shukra', 'shani', 'planetary'],
            'weight': 1.0
        },
        'houses': {
            'keywords': ['house', 'bhava', '1st house', '2nd house', '3rd house', '4th house',
                        '5th house', '6th house', '7th house', '8th house', '9th house',
                        '10th house', '11th house', '12th house', 'ascendant', 'lagna'],
            'weight': 1.0
        },
        'signs': {
            'keywords': ['sign', 'rashi', 'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo',
                        'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces',
                        'mesha', 'vrishabha', 'mithuna', 'karka', 'simha', 'kanya'],
            'weight': 1.0
        },
        'nakshatras': {
            'keywords': ['nakshatra', 'constellation', 'ashwini', 'bharani', 'krittika', 'rohini',
                        'mrigashira', 'ardra', 'punarvasu', 'pushya', 'ashlesha', 'magha'],
            'weight': 1.0
        },
        'aspects': {
            'keywords': ['aspect', 'drishti', 'glance', '7th aspect', 'special aspect', 'view'],
            'weight': 1.0
        },
        'marriage': {
            'keywords': ['marriage', 'spouse', 'wife', 'husband', '7th house', 'seventh house',
                        'vivaha', 'kalatra', 'partner', 'relationship', 'matrimony'],
            'weight': 1.5
        },
        'career': {
            'keywords': ['career', 'profession', '10th house', 'tenth house', 'karma', 'occupation',
                        'job', 'business', 'employment', 'livelihood'],
            'weight': 1.5
        },
        'wealth': {
            'keywords': ['wealth', 'money', 'finance', 'dhana', '2nd house', '11th house', 'income',
                        'gains', 'prosperity', 'riches', 'fortune'],
            'weight': 1.5
        },
        'children': {
            'keywords': ['children', 'progeny', '5th house', 'fifth house', 'putra', 'offspring',
                        'son', 'daughter', 'child'],
            'weight': 1.5
        },
        'health': {
            'keywords': ['health', 'disease', 'illness', '6th house', '8th house', 'rog', 'ailment',
                        'medical', 'sickness', 'malady'],
            'weight': 1.5
        },
        'longevity': {
            'keywords': ['longevity', 'ayurdaya', 'life span', 'maraka', 'death', 'killer'],
            'weight': 1.5
        },
        'dashas': {
            'keywords': ['dasha', 'mahadasha', 'antardasha', 'vimshottari', 'yogini', 'chara dasha',
                        'period', 'sub-period', 'planetary period'],
            'weight': 1.5
        },
        'transits': {
            'keywords': ['transit', 'gochara', 'movement', 'planetary transit', 'moving planet'],
            'weight': 1.5
        },
        'divisional': {
            'keywords': ['navamsa', 'divisional', 'varga', 'D9', 'D10', 'D7', 'D2', 'D3',
                        'hora', 'drekkana', 'saptamsa', 'dashamsa', 'shodasamsa'],
            'weight': 1.5
        },
        'yogas': {
            'keywords': ['yoga', 'combination', 'raja yoga', 'dhana yoga', 'neecha bhanga',
                        'parivartana', 'conjunction', 'planetary combination'],
            'weight': 1.5
        },
        'remedies': {
            'keywords': ['remedy', 'upaya', 'mantra', 'gemstone', 'puja', 'donation', 'charity',
                        'propitiation', 'ratna', 'japa'],
            'weight': 1.5
        }
    }
    
    # Classify each page
    classified = {topic: [] for topic in topic_keywords.keys()}
    
    for page_data in all_pages:
        text_lower = page_data['text'].lower()
        page_topics = {}
        
        # Score each topic
        for topic, config in topic_keywords.items():
            score = 0
            for keyword in config['keywords']:
                count = text_lower.count(keyword)
                score += count * config['weight']
            
            if score > 0:
                page_topics[topic] = score
        
        # Assign to top topics (can be multiple)
        if page_topics:
            max_score = max(page_topics.values())
            threshold = max_score * 0.3  # Include topics with 30%+ of max score
            
            for topic, score in page_topics.items():
                if score >= threshold:
                    classified[topic].append({
                        **page_data,
                        'relevance_score': score
                    })
    
    return classified

def save_classified_content(classified):
    """Save classified content to JSON"""
    output_file = Path("../extracted_content/bphs_full_classified.json")
    output_file.parent.mkdir(exist_ok=True)
    
    # Prepare for JSON (remove text to save space, keep references)
    summary = {}
    for topic, pages in classified.items():
        summary[topic] = {
            'page_count': len(pages),
            'pages': [{'page': p['page'], 'score': p['relevance_score'], 'length': p['length']} 
                     for p in pages]
        }
    
    with open(output_file, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\n✓ Saved classification to: {output_file}")
    
    # Also save full content
    full_output = Path("../extracted_content/bphs_full_content.json")
    with open(full_output, 'w') as f:
        json.dump(classified, f, indent=2)
    
    print(f"✓ Saved full content to: {full_output}")
    
    return summary

def print_statistics(classified):
    """Print extraction statistics"""
    print("\n" + "="*70)
    print("CONTENT CLASSIFICATION STATISTICS")
    print("="*70)
    
    for topic, pages in sorted(classified.items()):
        if pages:
            total_chars = sum(p['length'] for p in pages)
            avg_score = sum(p['relevance_score'] for p in pages) / len(pages)
            print(f"\n{topic.upper()}")
            print(f"  Pages: {len(pages)}")
            print(f"  Characters: {total_chars:,}")
            print(f"  Avg relevance: {avg_score:.1f}")
            print(f"  Top pages: {', '.join(str(p['page']) for p in sorted(pages, key=lambda x: x['relevance_score'], reverse=True)[:5])}")

if __name__ == "__main__":
    print("="*70)
    print("FULL BPHS EXTRACTION AND CLASSIFICATION")
    print("="*70)
    print()
    
    # Extract
    all_pages = extract_full_bphs()
    if not all_pages:
        sys.exit(1)
    
    # Classify
    print("\nClassifying content by topics...")
    classified = classify_content(all_pages)
    
    # Save
    summary = save_classified_content(classified)
    
    # Statistics
    print_statistics(classified)
    
    print("\n" + "="*70)
    print("EXTRACTION COMPLETE!")
    print("="*70)
    print("\nNext: Run content_distributor.py to fill all 60 documents")
