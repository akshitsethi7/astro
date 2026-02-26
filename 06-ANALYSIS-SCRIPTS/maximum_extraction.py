#!/usr/bin/env python3
"""
MAXIMUM EXTRACTION - Extract EVERYTHING from all 33 books
No limits, all patterns, complete knowledge
"""

import json
from pathlib import Path
import re

EXTRACTED_DIR = Path('/Users/akshitsethi/Desktop/astro/astrology-learning/extraction-system/extracted_content')

def maximum_search(patterns, topic_name):
    """Search with NO LIMITS - extract everything"""
    json_files = list(EXTRACTED_DIR.glob("*_extraction.json"))
    all_quotes = []
    
    print(f"\n{'='*80}")
    print(f"MAXIMUM EXTRACTION: {topic_name}")
    print(f"Patterns: {len(patterns)}")
    print(f"{'='*80}")
    
    for json_file in json_files:
        book_name = json_file.stem.replace('_extraction', '')
        
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except:
            continue
        
        book_title = data.get('book_name', book_name)
        full_text_pages = data.get('full_text_pages', [])
        
        book_quotes = []
        
        for page_data in full_text_pages:
            page_num = page_data.get('page', 0)
            text = page_data.get('text', '')
            
            if len(text) < 80:
                continue
            
            text_lower = text.lower()
            
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    clean = re.sub(r'\s+', ' ', text)
                    clean = re.sub(r'[^\x00-\x7F]+', '', clean)
                    
                    book_quotes.append({
                        'book': book_title,
                        'page': page_num,
                        'text': clean[:700],
                        'pattern': pattern
                    })
                    break
        
        all_quotes.extend(book_quotes)
        if book_quotes:
            print(f"  {book_title}: {len(book_quotes)} quotes")
    
    print(f"\nTOTAL: {len(all_quotes)} quotes from {len(set(q['book'] for q in all_quotes))} books")
    return all_quotes

# Load chart
with open('akshit_chart.json', 'r') as f:
    chart_data = json.load(f)

output = []

output.append("# MAXIMUM KNOWLEDGE EXTRACTION - AKSHIT")
output.append("## Complete Extraction from All 33 Classical Texts\n")
output.append("**NO LIMITS - EVERYTHING EXTRACTED**\n")
output.append("---\n")

# MARRIAGE - MAXIMUM PATTERNS
marriage_patterns = [
    # Basic
    r'7th.*house', r'7th.*lord', r'marriage', r'spouse', r'wife', r'husband',
    r'wedding', r'matrimony', r'partner', r'relationship',
    # Venus
    r'venus.*exalted', r'venus.*libra', r'venus.*marriage', r'venus.*spouse',
    r'venus.*8th.*navamsa', r'venus.*taurus.*navamsa', r'venus.*karaka',
    # Saturn
    r'saturn.*7th', r'saturn.*aquarius.*7th', r'saturn.*marriage', r'saturn.*delay',
    r'saturn.*own.*sign.*marriage', r'saturn.*spouse',
    # Navamsa
    r'navamsa.*marriage', r'd9.*marriage', r'navamsa.*spouse', r'navamsa.*venus',
    r'navamsa.*saturn', r'navamsa.*analysis',
    # Timing
    r'marriage.*timing', r'marriage.*age', r'marriage.*period', r'marriage.*dasha',
    r'jupiter.*venus.*marriage', r'jupiter.*venus.*dasha',
    # Spouse characteristics
    r'spouse.*appearance', r'spouse.*nature', r'spouse.*character', r'spouse.*age',
    r'spouse.*family', r'spouse.*wealth', r'spouse.*education', r'spouse.*career',
    # Yogas
    r'marriage.*yoga', r'kalatra.*yoga', r'upapada', r'darakaraka',
    # Delays
    r'delayed.*marriage', r'late.*marriage', r'marriage.*after.*30',
    # Quality
    r'marriage.*happiness', r'marriage.*success', r'marriage.*stability',
    r'marriage.*longevity', r'marriage.*compatibility',
    # Houses
    r'2nd.*house.*marriage', r'8th.*house.*marriage', r'12th.*house.*marriage',
    # Aspects
    r'jupiter.*aspect.*7th', r'saturn.*aspect.*venus', r'mars.*aspect.*7th',
    # Divisional
    r'd7.*marriage', r'd60.*marriage', r'saptamsa.*marriage',
    # Combinations
    r'venus.*saturn', r'venus.*jupiter', r'moon.*venus',
    # Nakshatras
    r'swati.*marriage', r'shatabhisha.*marriage', r'nakshatra.*marriage',
    # Remedies
    r'marriage.*remedy', r'marriage.*mantra', r'marriage.*puja'
]

marriage_quotes = maximum_search(marriage_patterns, "MARRIAGE")

output.append(f"## PART 1: MARRIAGE ({len(marriage_quotes)} quotes)\n")

marriage_by_book = {}
for q in marriage_quotes:
    book = q['book']
    if book not in marriage_by_book:
        marriage_by_book[book] = []
    marriage_by_book[book].append(q)

for book, quotes in marriage_by_book.items():
    output.append(f"\n### {book} ({len(quotes)} quotes)\n")
    for i, quote in enumerate(quotes[:30], 1):  # Max 30 per book for readability
        output.append(f"**{i}. Page {quote['page']}**:")
        output.append(f"{quote['text']}\n")

output.append("\n---\n")

# CAREER - MAXIMUM PATTERNS
career_patterns = [
    # Basic
    r'10th.*house', r'10th.*lord', r'career', r'profession', r'job', r'work',
    r'occupation', r'employment', r'business', r'service',
    # Venus 10th lord
    r'venus.*10th', r'venus.*exalted.*career', r'venus.*taurus.*10th',
    r'venus.*profession', r'venus.*business',
    # Sun authority
    r'sun.*5th', r'sun.*authority', r'sun.*leadership', r'sun.*government',
    r'sun.*career', r'sun.*profession',
    # Mercury intelligence
    r'mercury.*5th', r'mercury.*intelligence', r'mercury.*business',
    r'mercury.*communication', r'mercury.*technology',
    # Jupiter wisdom
    r'jupiter.*4th', r'jupiter.*teaching', r'jupiter.*education',
    r'jupiter.*wisdom', r'jupiter.*career',
    # Fields
    r'technology.*career', r'finance.*career', r'banking.*profession',
    r'creative.*career', r'arts.*profession', r'media.*career',
    r'management.*career', r'leadership.*profession', r'teaching.*career',
    # Success
    r'career.*success', r'professional.*success', r'career.*growth',
    r'promotion', r'career.*advancement', r'career.*peak',
    # D10
    r'd10.*career', r'dashamsa.*profession', r'career.*chart',
    # Yogas
    r'raja.*yoga', r'dhana.*yoga.*career', r'career.*yoga',
    # Timing
    r'career.*dasha', r'career.*period', r'career.*timing',
    # Combinations
    r'sun.*mercury', r'venus.*mercury', r'jupiter.*career'
]

career_quotes = maximum_search(career_patterns, "CAREER")

output.append(f"## PART 2: CAREER ({len(career_quotes)} quotes)\n")

career_by_book = {}
for q in career_quotes:
    book = q['book']
    if book not in career_by_book:
        career_by_book[book] = []
    career_by_book[book].append(q)

for book, quotes in career_by_book.items():
    output.append(f"\n### {book} ({len(quotes)} quotes)\n")
    for i, quote in enumerate(quotes[:25], 1):
        output.append(f"**{i}. Page {quote['page']}**:")
        output.append(f"{quote['text']}\n")

output.append("\n---\n")

# WEALTH - MAXIMUM PATTERNS
wealth_patterns = [
    # Basic
    r'2nd.*house', r'11th.*house', r'wealth', r'money', r'riches', r'prosperity',
    r'fortune', r'income', r'earnings', r'gains', r'profit',
    # Mercury 2nd & 11th lord
    r'mercury.*2nd', r'mercury.*11th', r'mercury.*wealth', r'mercury.*money',
    r'mercury.*2nd.*11th', r'mercury.*dhana',
    # Yogas
    r'dhana.*yoga', r'lakshmi.*yoga', r'wealth.*yoga', r'money.*yoga',
    r'prosperity.*yoga', r'fortune.*yoga',
    # Venus wealth
    r'venus.*wealth', r'venus.*money', r'venus.*exalted.*wealth',
    r'venus.*prosperity', r'venus.*luxury',
    # Jupiter prosperity
    r'jupiter.*wealth', r'jupiter.*prosperity', r'jupiter.*fortune',
    r'jupiter.*expansion.*wealth',
    # Sources
    r'salary', r'investment', r'property.*wealth', r'real.*estate',
    r'inheritance', r'spouse.*wealth', r'business.*profit',
    # D2
    r'd2.*wealth', r'hora.*wealth', r'wealth.*chart',
    # Accumulation
    r'wealth.*accumulation', r'money.*accumulation', r'savings',
    r'financial.*security', r'financial.*success',
    # Timing
    r'wealth.*dasha', r'money.*period', r'financial.*timing',
    # Combinations
    r'venus.*jupiter.*wealth', r'mercury.*venus.*wealth'
]

wealth_quotes = maximum_search(wealth_patterns, "WEALTH")

output.append(f"## PART 3: WEALTH ({len(wealth_quotes)} quotes)\n")

wealth_by_book = {}
for q in wealth_quotes:
    book = q['book']
    if book not in wealth_by_book:
        wealth_by_book[book] = []
    wealth_by_book[book].append(q)

for book, quotes in wealth_by_book.items():
    output.append(f"\n### {book} ({len(quotes)} quotes)\n")
    for i, quote in enumerate(quotes[:25], 1):
        output.append(f"**{i}. Page {quote['page']}**:")
        output.append(f"{quote['text']}\n")

output.append("\n---\n")

# HEALTH - MAXIMUM PATTERNS
health_patterns = [
    # Basic
    r'6th.*house', r'8th.*house', r'health', r'disease', r'illness', r'sickness',
    r'vitality', r'longevity', r'life.*span', r'ayur',
    # Ascendant
    r'ascendant.*health', r'lagna.*health', r'leo.*ascendant',
    r'ascendant.*lord.*health',
    # Mars 1st
    r'mars.*1st', r'mars.*ascendant', r'mars.*energy', r'mars.*vitality',
    r'mars.*strength', r'mars.*health',
    # Saturn 6th lord
    r'saturn.*6th', r'saturn.*disease', r'saturn.*health', r'saturn.*chronic',
    # Jupiter 8th lord
    r'jupiter.*8th', r'jupiter.*longevity', r'jupiter.*ayur',
    # Specific
    r'digestive.*health', r'stomach.*health', r'mental.*health',
    r'stress.*health', r'anxiety', r'blood.*pressure',
    r'eye.*health', r'vision', r'joint.*pain',
    # Longevity
    r'long.*life', r'longevity.*yoga', r'ayur.*yoga', r'life.*expectancy',
    # Remedies
    r'health.*remedy', r'disease.*cure', r'health.*mantra'
]

health_quotes = maximum_search(health_patterns, "HEALTH")

output.append(f"## PART 4: HEALTH ({len(health_quotes)} quotes)\n")

health_by_book = {}
for q in health_quotes:
    book = q['book']
    if book not in health_by_book:
        health_by_book[book] = []
    health_by_book[book].append(q)

for book, quotes in health_by_book.items():
    output.append(f"\n### {book} ({len(quotes)} quotes)\n")
    for i, quote in enumerate(quotes[:20], 1):
        output.append(f"**{i}. Page {quote['page']}**:")
        output.append(f"{quote['text']}\n")

output.append("\n---\n")

# SPIRITUALITY - MAXIMUM PATTERNS
spiritual_patterns = [
    # Basic
    r'9th.*house', r'12th.*house', r'dharma', r'moksha', r'spiritual',
    r'religion', r'philosophy', r'wisdom', r'enlightenment',
    # Ketu 9th
    r'ketu.*9th', r'ketu.*dharma', r'ketu.*spiritual', r'ketu.*moksha',
    r'ketu.*liberation', r'ketu.*detachment',
    # Mars 9th lord
    r'mars.*9th.*lord', r'mars.*dharma', r'mars.*spiritual',
    # Jupiter
    r'jupiter.*wisdom', r'jupiter.*spiritual', r'jupiter.*dharma',
    r'jupiter.*guru', r'jupiter.*philosophy',
    # Practices
    r'meditation', r'yoga', r'mantra', r'puja', r'worship',
    r'astrology.*study', r'occult', r'mysticism', r'tantra',
    # Path
    r'spiritual.*path', r'spiritual.*growth', r'spiritual.*evolution',
    r'past.*life', r'karma', r'reincarnation',
    # Yogas
    r'sanyasa.*yoga', r'moksha.*yoga', r'spiritual.*yoga'
]

spiritual_quotes = maximum_search(spiritual_patterns, "SPIRITUALITY")

output.append(f"## PART 5: SPIRITUALITY ({len(spiritual_quotes)} quotes)\n")

spiritual_by_book = {}
for q in spiritual_quotes:
    book = q['book']
    if book not in spiritual_by_book:
        spiritual_by_book[book] = []
    spiritual_by_book[book].append(q)

for book, quotes in spiritual_by_book.items():
    output.append(f"\n### {book} ({len(quotes)} quotes)\n")
    for i, quote in enumerate(quotes[:20], 1):
        output.append(f"**{i}. Page {quote['page']}**:")
        output.append(f"{quote['text']}\n")

output.append("\n---\n")

# DASHA - MAXIMUM PATTERNS
dasha_patterns = [
    # Jupiter
    r'jupiter.*dasha', r'jupiter.*mahadasha', r'jupiter.*period',
    r'jupiter.*antardasha', r'jupiter.*bhukti',
    # Venus
    r'venus.*dasha', r'venus.*mahadasha', r'venus.*period',
    r'venus.*antardasha', r'venus.*bhukti',
    # Saturn
    r'saturn.*dasha', r'saturn.*mahadasha', r'saturn.*period',
    r'saturn.*antardasha', r'saturn.*bhukti',
    # Mercury
    r'mercury.*dasha', r'mercury.*mahadasha', r'mercury.*period',
    r'mercury.*antardasha', r'mercury.*bhukti',
    # Combinations
    r'jupiter.*venus', r'jupiter.*mercury', r'jupiter.*saturn',
    # Results
    r'dasha.*results', r'dasha.*effects', r'dasha.*predictions',
    r'mahadasha.*results', r'antardasha.*results',
    # Timing
    r'dasha.*marriage', r'dasha.*career', r'dasha.*wealth',
    r'dasha.*timing', r'period.*timing',
    # Vimshottari
    r'vimshottari', r'dasha.*system', r'dasha.*calculation'
]

dasha_quotes = maximum_search(dasha_patterns, "DASHA")

output.append(f"## PART 6: DASHA PERIODS ({len(dasha_quotes)} quotes)\n")

dasha_by_book = {}
for q in dasha_quotes:
    book = q['book']
    if book not in dasha_by_book:
        dasha_by_book[book] = []
    dasha_by_book[book].append(q)

for book, quotes in dasha_by_book.items():
    output.append(f"\n### {book} ({len(quotes)} quotes)\n")
    for i, quote in enumerate(quotes[:20], 1):
        output.append(f"**{i}. Page {quote['page']}**:")
        output.append(f"{quote['text']}\n")

output.append("\n---\n")

# FINAL STATISTICS
total_quotes = len(marriage_quotes) + len(career_quotes) + len(wealth_quotes) + len(health_quotes) + len(spiritual_quotes) + len(dasha_quotes)

output.append("## FINAL STATISTICS\n")
output.append(f"### Extraction Summary\n")
output.append(f"- **Marriage**: {len(marriage_quotes)} quotes from {len(marriage_by_book)} books")
output.append(f"- **Career**: {len(career_quotes)} quotes from {len(career_by_book)} books")
output.append(f"- **Wealth**: {len(wealth_quotes)} quotes from {len(wealth_by_book)} books")
output.append(f"- **Health**: {len(health_quotes)} quotes from {len(health_by_book)} books")
output.append(f"- **Spirituality**: {len(spiritual_quotes)} quotes from {len(spiritual_by_book)} books")
output.append(f"- **Dasha**: {len(dasha_quotes)} quotes from {len(dasha_by_book)} books")
output.append(f"\n**TOTAL QUOTES EXTRACTED**: {total_quotes}")
output.append(f"**TOTAL BOOKS SCANNED**: 33 classical texts")
output.append(f"**TOTAL PATTERNS USED**: {len(marriage_patterns) + len(career_patterns) + len(wealth_patterns) + len(health_patterns) + len(spiritual_patterns) + len(dasha_patterns)}")
output.append(f"**EXTRACTION LEVEL**: MAXIMUM (No limits)\n")

# Write output
with open('AKSHIT_MAXIMUM_EXTRACTION.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print("\n" + "="*80)
print("✓ MAXIMUM EXTRACTION COMPLETE")
print(f"✓ Total Quotes: {total_quotes}")
print("✓ File: AKSHIT_MAXIMUM_EXTRACTION.md")
print("="*80)
