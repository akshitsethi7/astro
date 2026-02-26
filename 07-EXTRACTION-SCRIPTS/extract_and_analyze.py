#!/usr/bin/env python3
"""
Extract text from PDFs and create comprehensive analysis
"""

import os
import sys
from pathlib import Path

# Try to import PDF libraries
try:
    import PyPDF2
    HAS_PYPDF2 = True
except:
    HAS_PYPDF2 = False

try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except:
    HAS_PDFPLUMBER = False

try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except:
    HAS_PYMUPDF = False

def extract_text_pypdf2(pdf_path):
    """Extract using PyPDF2"""
    text = ""
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages[:10]:  # First 10 pages
                text += page.extract_text() + "\n"
    except:
        pass
    return text

def extract_text_pdfplumber(pdf_path):
    """Extract using pdfplumber"""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages[:10]:  # First 10 pages
                t = page.extract_text()
                if t:
                    text += t + "\n"
    except:
        pass
    return text

def extract_text_pymupdf(pdf_path):
    """Extract using PyMuPDF"""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(min(10, len(doc))):  # First 10 pages
            text += doc[page_num].get_text() + "\n"
        doc.close()
    except:
        pass
    return text

def extract_pdf(pdf_path):
    """Extract text from PDF"""
    if HAS_PDFPLUMBER:
        return extract_text_pdfplumber(pdf_path)
    elif HAS_PYMUPDF:
        return extract_text_pymupdf(pdf_path)
    elif HAS_PYPDF2:
        return extract_text_pypdf2(pdf_path)
    return ""

def main():
    books_dir = Path("/Users/akshitsethi/Desktop/Books")
    output_file = Path("/Users/akshitsethi/Desktop/astro/extracted_books_content.txt")
    
    print("PDF Extraction Status:")
    print(f"PyPDF2: {HAS_PYPDF2}")
    print(f"pdfplumber: {HAS_PDFPLUMBER}")
    print(f"PyMuPDF: {HAS_PYMUPDF}")
    print()
    
    if not (HAS_PYPDF2 or HAS_PDFPLUMBER or HAS_PYMUPDF):
        print("No PDF libraries available. Please install:")
        print("pip3 install PyPDF2 pdfplumber pymupdf")
        return
    
    pdf_files = sorted(books_dir.glob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files")
    print()
    
    all_content = []
    marriage_books = []
    timing_books = []
    navamsa_books = []
    general_books = []
    
    for pdf_file in pdf_files:
        name_lower = pdf_file.name.lower()
        print(f"Processing: {pdf_file.name[:60]}...")
        
        text = extract_pdf(pdf_file)
        
        if text and len(text.strip()) > 200:
            # Categorize books
            if any(word in name_lower for word in ['marriage', 'married', 'vivah', 'wedding']):
                marriage_books.append((pdf_file.name, text))
            elif any(word in name_lower for word in ['timing', 'dasha', 'mahadasha', 'antardasha']):
                timing_books.append((pdf_file.name, text))
            elif any(word in name_lower for word in ['navamsa', 'd9']):
                navamsa_books.append((pdf_file.name, text))
            else:
                general_books.append((pdf_file.name, text))
            
            all_content.append(f"\n{'='*80}\n")
            all_content.append(f"BOOK: {pdf_file.name}\n")
            all_content.append(f"{'='*80}\n\n")
            all_content.append(text[:5000])  # First 5000 chars
            all_content.append("\n\n")
            print(f"  ✓ Extracted {len(text)} characters")
        else:
            print(f"  ⚠ Could not extract text")
    
    # Save all content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("EXTRACTED CONTENT FROM ALL ASTROLOGY BOOKS\n")
        f.write("="*80 + "\n\n")
        f.write("".join(all_content))
    
    # Save categorized summary
    summary_file = Path("/Users/akshitsethi/Desktop/astro/books_summary.txt")
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("BOOKS CATEGORIZATION SUMMARY\n")
        f.write("="*80 + "\n\n")
        f.write(f"MARRIAGE BOOKS ({len(marriage_books)}):\n")
        for name, _ in marriage_books:
            f.write(f"  - {name}\n")
        f.write(f"\nTIMING/DASHA BOOKS ({len(timing_books)}):\n")
        for name, _ in timing_books:
            f.write(f"  - {name}\n")
        f.write(f"\nNAVAMSA BOOKS ({len(navamsa_books)}):\n")
        for name, _ in navamsa_books:
            f.write(f"  - {name}\n")
        f.write(f"\nGENERAL BOOKS ({len(general_books)}):\n")
        for name, _ in general_books:
            f.write(f"  - {name}\n")
    
    print()
    print(f"✓ Extracted content saved to: {output_file}")
    print(f"✓ Summary saved to: {summary_file}")
    print(f"\nCategories:")
    print(f"  Marriage books: {len(marriage_books)}")
    print(f"  Timing/Dasha books: {len(timing_books)}")
    print(f"  Navamsa books: {len(navamsa_books)}")
    print(f"  General books: {len(general_books)}")
    
    return {
        'marriage': marriage_books,
        'timing': timing_books,
        'navamsa': navamsa_books,
        'general': general_books,
        'all_content': "".join(all_content)
    }

if __name__ == "__main__":
    result = main()
