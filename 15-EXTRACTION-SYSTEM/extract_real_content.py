#!/usr/bin/env python3
"""
HONEST PDF CONTENT EXTRACTION
Actually read PDFs and extract REAL content with page numbers and quotes
No making things up - only what's actually in the books
"""

import json
from pathlib import Path
import re

def extract_marriage_content_with_references():
    """Extract actual marriage content from PDFs with page numbers"""
    
    extracted_dir = Path('astrology-learning/extraction-system/extracted_content')
    
    # Priority books for marriage
    priority_books = [
        '2015.150536.Marriage-Married-Life-And-Children_text_extraction.json',
        'jyotish_astrology-and-timing-of-marriage_-k-n-rao_-english_hindi_extraction.json',
        'Astrology in Marriage Counselling_Manik Chand Jain_extraction.json',
        'BPHS - 1 RSanthanam_extraction.json',
        'BPHS - 2 RSanthanam_extraction.json'
    ]
    
    output = []
    output.append("# HONEST EXTRACTION - ACTUAL CONTENT FROM PDFs\n")
    output.append("**Extraction Date**: February 26, 2026\n")
    output.append("**Method**: Direct PDF text extraction with page references\n\n")
    output.append("---\n\n")
    
    for book_file in priority_books:
        book_path = extracted_dir / book_file
        
        if not book_path.exists():
            output.append(f"## {book_file.replace('_extraction.json', '')}\n")
            output.append("**Status**: File not found\n\n")
            continue
        
        try:
            with open(book_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            book_name = data.get('book_name', 'Unknown')
            output.append(f"## {book_name}\n\n")
            output.append(f"**Total Pages**: {data.get('total_pages', 0)}\n")
            output.append(f"**Chapters**: {len(data.get('chapters', []))}\n")
            
            # Get topic pages
            topic_pages = data.get('topic_pages', {})
            marriage_pages = topic_pages.get('marriage', [])
            
            output.append(f"**Marriage Content Pages**: {len(marriage_pages)}\n\n")
            
            if marriage_pages:
                output.append("### Sample Marriage Content (First 10 pages)\n\n")
                
                for i, page_info in enumerate(marriage_pages[:10], 1):
                    page_num = page_info['page']
                    preview = page_info.get('preview', '')
                    
                    output.append(f"**Page {page_num}**:\n")
                    output.append(f"```\n{preview}\n```\n\n")
            
            # Get sutras
            sutras = data.get('sutras', [])
            if sutras:
                output.append(f"### Sample Sutras/Rules (First 10)\n\n")
                for i, sutra in enumerate(sutras[:10], 1):
                    output.append(f"**Sutra {i} (Page {sutra['page']})**:\n")
                    output.append(f"{sutra['text']}\n\n")
            
            # Get examples
            examples = data.get('examples', [])
            if examples:
                output.append(f"### Sample Examples (First 5)\n\n")
                for i, example in enumerate(examples[:5], 1):
                    output.append(f"**Example {i} (Page {example['page']})**:\n")
                    output.append(f"{example['text']}\n\n")
            
            output.append("---\n\n")
            
        except Exception as e:
            output.append(f"**Error**: {str(e)}\n\n")
    
    # Save output
    output_file = Path('HONEST_PDF_EXTRACTION.md')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output)
    
    print(f"Honest extraction saved to: {output_file}")
    return ''.join(output)

if __name__ == "__main__":
    content = extract_marriage_content_with_references()
    print(content[:2000])  # Print first 2000 chars
