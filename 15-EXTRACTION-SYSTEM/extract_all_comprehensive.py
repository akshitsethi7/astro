#!/usr/bin/env python3
"""
Comprehensive extraction of ALL 46 books
Attempts multiple extraction methods for maximum coverage
"""
import sys
import json
from pathlib import Path
from datetime import datetime
import time

try:
    import pdfplumber
except ImportError:
    import os
    os.system(f"{sys.executable} -m pip install pdfplumber")
    import pdfplumber

def extract_book_comprehensive(pdf_path):
    """Try multiple methods to extract text"""
    all_pages = []
    
    try:
        # Method 1: pdfplumber (best for text PDFs)
        with pdfplumber.open(pdf_path) as pdf:
            total = len(pdf.pages)
            
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text and len(text.strip()) > 50:  # Meaningful text
                    all_pages.append({
                        'page': i + 1,
                        'text': text,
                        'length': len(text),
                        'method': 'pdfplumber'
                    })
                
                if (i + 1) % 100 == 0:
                    print(f"    {i + 1}/{total} pages")
        
        return all_pages, None
        
    except Exception as e:
        return None, str(e)

def classify_pages(all_pages):
    """Classify pages by topic with comprehensive keywords"""
    
    topic_keywords = {
        'planets': {
            'primary': ['planet', 'sun', 'moon', 'mars', 'mercury', 'jupiter', 'venus', 'saturn', 'rahu', 'ketu'],
            'secondary': ['graha', 'surya', 'chandra', 'mangal', 'budha', 'guru', 'shukra', 'shani', 'planetary']
        },
        'houses': {
            'primary': ['house', 'bhava', 'ascendant', 'lagna'],
            'secondary': ['1st house', '2nd house', '7th house', '10th house', 'kendra', 'trikona', 'dusthana']
        },
        'signs': {
            'primary': ['sign', 'rashi', 'zodiac'],
            'secondary': ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 
                         'sagittarius', 'capricorn', 'aquarius', 'pisces']
        },
        'nakshatras': {
            'primary': ['nakshatra', 'constellation', 'lunar mansion'],
            'secondary': ['ashwini', 'bharani', 'krittika', 'rohini', 'mrigashira', 'ardra']
        },
        'aspects': {
            'primary': ['aspect', 'drishti'],
            'secondary': ['7th aspect', 'special aspect', 'planetary glance']
        },
        'marriage': {
            'primary': ['marriage', 'spouse', 'matrimony', 'wedding'],
            'secondary': ['wife', 'husband', '7th house', 'vivaha', 'kalatra', 'partner']
        },
        'career': {
            'primary': ['career', 'profession', 'occupation', 'job'],
            'secondary': ['10th house', 'karma', 'business', 'employment', 'livelihood']
        },
        'wealth': {
            'primary': ['wealth', 'money', 'finance', 'prosperity'],
            'secondary': ['dhana', '2nd house', '11th house', 'income', 'gains', 'riches']
        },
        'children': {
            'primary': ['children', 'progeny', 'offspring'],
            'secondary': ['5th house', 'putra', 'son', 'daughter', 'child']
        },
        'health': {
            'primary': ['health', 'disease', 'illness', 'medical'],
            'secondary': ['6th house', '8th house', 'rog', 'ailment', 'sickness']
        },
        'longevity': {
            'primary': ['longevity', 'life span', 'ayurdaya'],
            'secondary': ['maraka', 'death', 'killer planet', 'longevity calculation']
        },
        'dashas': {
            'primary': ['dasha', 'mahadasha', 'antardasha'],
            'secondary': ['vimshottari', 'yogini', 'chara dasha', 'period', 'planetary period']
        },
        'transits': {
            'primary': ['transit', 'gochara'],
            'secondary': ['planetary movement', 'transiting planet', 'current position']
        },
        'divisional': {
            'primary': ['navamsa', 'divisional', 'varga'],
            'secondary': ['D9', 'D10', 'D7', 'D2', 'hora', 'drekkana', 'saptamsa', 'dashamsa']
        },
        'yogas': {
            'primary': ['yoga', 'combination'],
            'secondary': ['raja yoga', 'dhana yoga', 'neecha bhanga', 'planetary combination']
        },
        'remedies': {
            'primary': ['remedy', 'upaya', 'remedial'],
            'secondary': ['mantra', 'gemstone', 'puja', 'donation', 'charity', 'ratna']
        }
    }
    
    classified = {topic: [] for topic in topic_keywords.keys()}
    
    for page_data in all_pages:
        text_lower = page_data['text'].lower()
        page_scores = {}
        
        for topic, keywords in topic_keywords.items():
            score = 0
            # Primary keywords worth more
            for kw in keywords['primary']:
                score += text_lower.count(kw) * 2
            # Secondary keywords
            for kw in keywords['secondary']:
                score += text_lower.count(kw)
            
            if score > 0:
                page_scores[topic] = score
        
        # Assign to topics with significant scores
        if page_scores:
            max_score = max(page_scores.values())
            threshold = max(2, max_score * 0.2)  # At least 2 or 20% of max
            
            for topic, score in page_scores.items():
                if score >= threshold:
                    classified[topic].append({
                        **page_data,
                        'relevance_score': score
                    })
    
    return classified

def extract_all_books():
    """Extract all books in Books directory"""
    
    books_dir = Path("../../../Books")
    output_dir = Path("../extracted_content")
    output_dir.mkdir(exist_ok=True)
    
    # Get all PDFs
    all_pdfs = sorted(books_dir.glob("*.pdf"))
    
    print("="*70)
    print(f"COMPREHENSIVE EXTRACTION - ALL {len(all_pdfs)} BOOKS")
    print("="*70)
    print(f"\nThis will take 1-2 hours")
    print(f"Starting: {datetime.now().strftime('%H:%M:%S')}")
    print()
    
    all_classified = {topic: [] for topic in [
        'planets', 'houses', 'signs', 'nakshatras', 'aspects',
        'marriage', 'career', 'wealth', 'children', 'health',
        'longevity', 'dashas', 'transits', 'divisional', 'yogas', 'remedies'
    ]}
    
    extraction_log = []
    start_time = time.time()
    successful = 0
    
    for i, pdf_path in enumerate(all_pdfs, 1):
        book_name = pdf_path.name
        print(f"\n[{i}/{len(all_pdfs)}] {book_name}")
        book_start = time.time()
        
        pages, error = extract_book_comprehensive(pdf_path)
        
        if error:
            print(f"  ✗ ERROR: {error}")
            extraction_log.append({'book': book_name, 'status': 'error', 'error': error})
            continue
        
        if not pages:
            print(f"  ⚠ No extractable text (likely scanned images)")
            extraction_log.append({'book': book_name, 'status': 'no_text'})
            continue
        
        # Classify
        classified = classify_pages(pages)
        
        # Merge
        for topic, topic_pages in classified.items():
            for page in topic_pages:
                page['book'] = book_name
            all_classified[topic].extend(topic_pages)
        
        book_time = time.time() - book_start
        total_chars = sum(p['length'] for p in pages)
        successful += 1
        
        print(f"  ✓ {len(pages)} pages, {total_chars:,} chars ({book_time:.1f}s)")
        
        extraction_log.append({
            'book': book_name,
            'status': 'success',
            'pages': len(pages),
            'characters': total_chars,
            'time': book_time
        })
    
    total_time = time.time() - start_time
    
    # Save
    print(f"\n{'='*70}")
    print("SAVING RESULTS")
    print(f"{'='*70}")
    
    output_file = output_dir / "all_books_classified.json"
    with open(output_file, 'w') as f:
        json.dump(all_classified, f, indent=2)
    print(f"✓ Saved: {output_file}")
    
    log_file = output_dir / "extraction_log.json"
    with open(log_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'total_books': len(all_pdfs),
            'successful': successful,
            'failed': len(all_pdfs) - successful,
            'total_time_minutes': total_time / 60,
            'books': extraction_log
        }, f, indent=2)
    print(f"✓ Saved: {log_file}")
    
    # Statistics
    print(f"\n{'='*70}")
    print("FINAL STATISTICS")
    print(f"{'='*70}")
    
    print(f"\nBooks: {successful}/{len(all_pdfs)} extracted successfully")
    print(f"Time: {total_time/60:.1f} minutes")
    print(f"Ended: {datetime.now().strftime('%H:%M:%S')}")
    
    success_logs = [l for l in extraction_log if l['status'] == 'success']
    if success_logs:
        total_pages = sum(l['pages'] for l in success_logs)
        total_chars = sum(l['characters'] for l in success_logs)
        print(f"\nTotal pages: {total_pages:,}")
        print(f"Total characters: {total_chars:,}")
    
    print(f"\nContent by topic:")
    for topic, pages in sorted(all_classified.items()):
        if pages:
            books = len(set(p['book'] for p in pages))
            print(f"  {topic:15s}: {len(pages):5d} pages from {books:2d} books")
    
    return all_classified, successful, len(all_pdfs)

if __name__ == "__main__":
    print("\n" + "="*70)
    print("COMPLETE BOOK EXTRACTION - ALL 46 BOOKS")
    print("="*70)
    print("\nThis will extract ALL books with text content")
    print("Estimated time: 1-2 hours")
    print()
    
    response = input("Continue? (yes/no): ")
    if response.lower() != 'yes':
        print("Cancelled.")
        sys.exit(0)
    
    print()
    all_classified, successful, total = extract_all_books()
    
    print(f"\n{'='*70}")
    print(f"COMPLETE! Extracted {successful}/{total} books")
    print(f"{'='*70}")
    print("\nNext: Run content_distributor.py to update all documents")
