#!/usr/bin/env python3
"""Test extraction with full text"""

import sys
sys.path.append('astrology-learning/extraction-system')

from pdf_extractor import AstrologyPDFExtractor
from pathlib import Path

# Extract just the K.N. Rao marriage book
books_dir = Path('../Books')
output_dir = Path('astrology-learning/extraction-system/test_output')
output_dir.mkdir(exist_ok=True)

extractor = AstrologyPDFExtractor(str(books_dir), str(output_dir))

# Process just one book
pdf_file = books_dir / 'jyotish_astrology-and-timing-of-marriage_-k-n-rao_-english_hindi.pdf'

print(f"Extracting: {pdf_file.name}")
book_data = extractor.process_book(pdf_file)

print(f"\nBook data keys: {list(book_data.keys())}")
print(f"Has full_text_pages: {'full_text_pages' in book_data}")

if 'full_text_pages' in book_data:
    print(f"Full text pages count: {len(book_data['full_text_pages'])}")
    print(f"\nSample from page 1:")
    print(book_data['full_text_pages'][0]['text'][:500])

# Save it
extractor.save_extraction(book_data, pdf_file.stem)
print(f"\nSaved to: {output_dir}")

# Verify saved file
import json
saved_file = output_dir / f"{pdf_file.stem}_extraction.json"
with open(saved_file, 'r') as f:
    saved_data = json.load(f)

print(f"\nSaved data keys: {list(saved_data.keys())}")
print(f"Saved has full_text_pages: {'full_text_pages' in saved_data}")
