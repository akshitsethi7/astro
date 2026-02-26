#!/usr/bin/env python3
"""
Extract ALL 45 Books - Complete MASTER_PLAN Execution
This will take 1-2 hours to process all books
"""
import sys
import json
from pathlib import Path
from datetime import datetime
import time

try:
    import pdfplumber
except ImportError:
    print("Installing pdfplumber...")
    import os
    os.system(f"{sys.executable} -m pip install pdfplumber")
    import pdfplumber

# Book list from MASTER_PLAN
TIER_1_BOOKS = [
    "BPHS - 1 RSanthanam.pdf",
    "BPHS - 2 RSanthanam.pdf",
    "Brihat Jataka 2nd Ed. by V Subrahmanya Sastri.pdf",
    "Jataka Parijata Vol I of II by V Subrahmanya Sastri.pdf",
    "Jataka Parijata Vol II of II by V Subrahmanya Sastri.pdf",
    "Phaladeepika 2nd Ed. 1950 by V Subrahmanya Sastri.pdf",
    "2015.312156.Jataka-Parijata.pdf",
    "2015.486584.Jaimini-Sutras.pdf",
    "2015.92117.Mantreswaras-Phaladeepika.pdf",
    "2015.342229.Brihad-Vishal.pdf"
]

TIER_2_BOOKS = [
    "Introduction-to-Vedic-Astrology-Sanjay-Rath.pdf",
    "C.S._Patel_-_Navamsa_in_Astrology.pdf",
    "jyotish_astrology-and-timing-of-marriage_-k-n-rao_-english_hindi.pdf",
    "advanced study of vimshottari dasha_KK Pathak.pdf",
    "Three Hundred Important Combinations in Vedic Astrology.pdf"
]

TIER_3_BOOKS = [
    "2015.150536.Marriage-Married-Life-And-Children_text.pdf",
    "Astrology in Marriage Counselling_Manik Chand Jain.pdf",
    "kpreader-4-marriage-married-life-children.pdf",
    "A.K. Gour_Astrology of Professions.pdf",
    "Jyotish Evam Rog Vichar Of Bhoj Raj Dwivedi - Diamond Pocket Books Private Limited, New Delhi.pdf",
    "Narayana Dasa by Sanjay Rath.pdf"
]

def extract_book(pdf_path, max_pages=None):
    """Extract text from a single book"""
    try:
        all_pages = []
        
        with pdfplumber.open(pdf_path) as pdf:
            total = len(pdf.pages)
            if max_pages:
                total = min(total, max_pages)
            
            for i, page in enumerate(pdf.pages[:total]):
                text = page.extract_text()
                if text:
                    all_pages.append({
                        'page': i + 1,
                        'text': text,
                        'length': len(text)
                    })
                
                if (i + 1) % 50 == 0:
                    print(f"    {i + 1}/{total} pages ({int((i+1)/total*100)}%)")
        
        return all_pages, None
    
    except Exception as e:
        return None, str(e)

def classify_content(all_pages):
    """Classify pages by topic"""
    
    topic_keywords = {
        'planets': ['planet', 'sun', 'moon', 'mars', 'mercury', 'jupiter', 'venus', 
                   'saturn', 'rahu', 'ketu', 'graha', 'surya', 'chandra'],
        'houses': ['house', 'bhava', 'ascendant', 'lagna', 'kendra', 'trikona'],
        'signs': ['sign', 'rashi', 'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo',
                 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'],
        'nakshatras': ['nakshatra', 'constellation', 'ashwini', 'bharani', 'krittika'],
        'aspects': ['aspect', 'drishti', 'glance'],
        'marriage': ['marriage', 'spouse', 'wife', 'husband', '7th house', 'vivaha'],
        'career': ['career', 'profession', '10th house', 'karma', 'occupation'],
        'wealth': ['wealth', 'money', 'dhana', '2nd house', '11th house', 'income'],
        'children': ['children', 'progeny', '5th house', 'putra', 'offspring'],
        'health': ['health', 'disease', '6th house', '8th house', 'rog'],
        'longevity': ['longevity', 'ayurdaya', 'maraka', 'death'],
        'dashas': ['dasha', 'mahadasha', 'vimshottari', 'antardasha'],
        'transits': ['transit', 'gochara', 'movement'],
        'divisional': ['navamsa', 'varga', 'D9', 'D10', 'D7', 'divisional'],
        'yogas': ['yoga', 'combination', 'raja yoga', 'dhana yoga'],
        'remedies': ['remedy', 'mantra', 'gemstone', 'puja', 'upaya']
    }
    
    classified = {topic: [] for topic in topic_keywords.keys()}
    
    for page_data in all_pages:
        text_lower = page_data['text'].lower()
        page_topics = {}
        
        for topic, keywords in topic_keywords.items():
            score = sum(text_lower.count(kw) for kw in keywords)
            if score > 0:
                page_topics[topic] = score
        
        if page_topics:
            max_score = max(page_topics.values())
            threshold = max_score * 0.3
            
            for topic, score in page_topics.items():
                if score >= threshold:
                    classified[topic].append({
                        **page_data,
                        'relevance_score': score
                    })
    
    return classified

def extract_all_books(tier=None):
    """Extract all books or specific tier"""
    
    books_dir = Path("../../../Books")
    output_dir = Path("../extracted_content")
    output_dir.mkdir(exist_ok=True)
    
    # Select books based on tier
    if tier == 1:
        books_to_process = TIER_1_BOOKS
        tier_name = "Tier 1: Foundation Texts"
    elif tier == 2:
        books_to_process = TIER_1_BOOKS + TIER_2_BOOKS
        tier_name = "Tier 1 + 2: Foundation + Modern Masters"
    elif tier == 3:
        books_to_process = TIER_1_BOOKS + TIER_2_BOOKS + TIER_3_BOOKS
        tier_name = "Tier 1-3: Foundation + Modern + Specialized"
    else:
        # Get all PDFs
        books_to_process = [f.name for f in books_dir.glob("*.pdf")]
        tier_name = "ALL BOOKS"
    
    print("="*70)
    print(f"EXTRACTING {tier_name}")
    print("="*70)
    print(f"\nTotal books to process: {len(books_to_process)}")
    print(f"Estimated time: {len(books_to_process) * 2} minutes")
    print()
    
    all_classified = {topic: [] for topic in [
        'planets', 'houses', 'signs', 'nakshatras', 'aspects',
        'marriage', 'career', 'wealth', 'children', 'health',
        'longevity', 'dashas', 'transits', 'divisional', 'yogas', 'remedies'
    ]}
    
    extraction_log = []
    start_time = time.time()
    
    for i, book_name in enumerate(books_to_process, 1):
        book_path = books_dir / book_name
        
        if not book_path.exists():
            print(f"\n[{i}/{len(books_to_process)}] ⚠ SKIP: {book_name} (not found)")
            continue
        
        print(f"\n[{i}/{len(books_to_process)}] Extracting: {book_name}")
        book_start = time.time()
        
        pages, error = extract_book(book_path)
        
        if error:
            print(f"  ✗ ERROR: {error}")
            extraction_log.append({
                'book': book_name,
                'status': 'error',
                'error': error
            })
            continue
        
        if not pages:
            print(f"  ✗ No text extracted")
            extraction_log.append({
                'book': book_name,
                'status': 'no_text'
            })
            continue
        
        # Classify
        classified = classify_content(pages)
        
        # Merge into all_classified
        for topic, topic_pages in classified.items():
            for page in topic_pages:
                page['book'] = book_name
            all_classified[topic].extend(topic_pages)
        
        book_time = time.time() - book_start
        total_chars = sum(p['length'] for p in pages)
        
        print(f"  ✓ {len(pages)} pages, {total_chars:,} chars ({book_time:.1f}s)")
        
        extraction_log.append({
            'book': book_name,
            'status': 'success',
            'pages': len(pages),
            'characters': total_chars,
            'time': book_time
        })
    
    total_time = time.time() - start_time
    
    # Save combined classification
    print(f"\n{'='*70}")
    print("SAVING COMBINED CLASSIFICATION")
    print(f"{'='*70}")
    
    output_file = output_dir / "all_books_classified.json"
    with open(output_file, 'w') as f:
        json.dump(all_classified, f, indent=2)
    
    print(f"✓ Saved to: {output_file}")
    
    # Save extraction log
    log_file = output_dir / "extraction_log.json"
    with open(log_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'tier': tier_name,
            'total_books': len(books_to_process),
            'successful': len([l for l in extraction_log if l['status'] == 'success']),
            'total_time_minutes': total_time / 60,
            'books': extraction_log
        }, f, indent=2)
    
    print(f"✓ Saved log to: {log_file}")
    
    # Print statistics
    print(f"\n{'='*70}")
    print("EXTRACTION STATISTICS")
    print(f"{'='*70}")
    
    successful = [l for l in extraction_log if l['status'] == 'success']
    print(f"\nBooks processed: {len(successful)}/{len(books_to_process)}")
    print(f"Total time: {total_time/60:.1f} minutes")
    
    if successful:
        total_pages = sum(l['pages'] for l in successful)
        total_chars = sum(l['characters'] for l in successful)
        print(f"Total pages: {total_pages:,}")
        print(f"Total characters: {total_chars:,}")
    
    print(f"\nContent by topic:")
    for topic, pages in sorted(all_classified.items()):
        if pages:
            books = len(set(p['book'] for p in pages))
            print(f"  {topic:15s}: {len(pages):4d} pages from {books} books")
    
    return all_classified

if __name__ == "__main__":
    import sys
    
    tier = None
    if len(sys.argv) > 1:
        tier = int(sys.argv[1])
    
    print("\n" + "="*70)
    print("COMPLETE BOOK EXTRACTION SYSTEM")
    print("="*70)
    print()
    
    if tier:
        print(f"Processing Tier {tier}")
    else:
        print("Processing ALL BOOKS (this will take 1-2 hours)")
        response = input("\nContinue? (yes/no): ")
        if response.lower() != 'yes':
            print("Cancelled.")
            sys.exit(0)
    
    print()
    
    all_classified = extract_all_books(tier)
    
    print(f"\n{'='*70}")
    print("EXTRACTION COMPLETE!")
    print(f"{'='*70}")
    print("\nNext: Run content_distributor.py to update all documents")
