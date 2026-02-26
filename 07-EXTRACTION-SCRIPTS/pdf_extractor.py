#!/usr/bin/env python3
"""
Robust PDF text extraction
"""

import os
import subprocess
from pathlib import Path

def check_and_install_libraries():
    """Check and install PDF libraries if needed"""
    libraries = ['PyPDF2', 'pdfplumber', 'pymupdf']
    missing = []
    
    for lib in libraries:
        try:
            if lib == 'pymupdf':
                __import__('fitz')
            else:
                __import__(lib)
            print(f"✓ {lib} available")
        except ImportError:
            missing.append(lib)
            print(f"✗ {lib} not available")
    
    if missing:
        print(f"\nInstalling missing libraries: {', '.join(missing)}")
        try:
            subprocess.check_call(['pip3', 'install'] + missing, 
                                stdout=subprocess.DEVNULL, 
                                stderr=subprocess.DEVNULL)
            print("✓ Libraries installed")
        except:
            print("⚠ Could not install automatically")
    
    return missing

def extract_text_simple(pdf_path):
    """Try multiple methods to extract text"""
    text = ""
    
    # Try PyPDF2
    try:
        import PyPDF2
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for i, page in enumerate(reader.pages[:5]):  # First 5 pages
                text += page.extract_text() + "\n"
        if text.strip():
            return text, "PyPDF2"
    except:
        pass
    
    # Try pdfplumber
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages[:5]):  # First 5 pages
                t = page.extract_text()
                if t:
                    text += t + "\n"
        if text.strip():
            return text, "pdfplumber"
    except:
        pass
    
    # Try PyMuPDF
    try:
        import fitz
        doc = fitz.open(pdf_path)
        for i in range(min(5, len(doc))):  # First 5 pages
            text += doc[i].get_text() + "\n"
        doc.close()
        if text.strip():
            return text, "PyMuPDF"
    except:
        pass
    
    return text, "none"

def main():
    books_dir = Path("/Users/akshitsethi/Desktop/Books")
    output_file = Path("/Users/akshitsethi/Desktop/astro/all_books_extracted.txt")
    
    print("Checking PDF libraries...")
    missing = check_and_install_libraries()
    print()
    
    pdf_files = sorted(books_dir.glob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files\n")
    
    all_text = []
    successful = 0
    
    for pdf_file in pdf_files:
        print(f"Extracting: {pdf_file.name[:70]}")
        text, method = extract_text_simple(pdf_file)
        
        if text and len(text.strip()) > 100:
            all_text.append(f"\n{'='*100}\n")
            all_text.append(f"BOOK: {pdf_file.name}\n")
            all_text.append(f"METHOD: {method}\n")
            all_text.append(f"{'='*100}\n\n")
            all_text.append(text[:10000])  # First 10000 chars
            all_text.append("\n\n")
            successful += 1
            print(f"  ✓ Extracted {len(text)} chars using {method}")
        else:
            print(f"  ✗ Failed to extract")
    
    # Save all extracted text
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("EXTRACTED TEXT FROM ALL ASTROLOGY BOOKS\n")
        f.write("="*100 + "\n\n")
        f.write(f"Successfully extracted: {successful}/{len(pdf_files)} books\n\n")
        f.write("".join(all_text))
    
    print(f"\n✓ Saved to: {output_file}")
    print(f"✓ Successfully extracted: {successful}/{len(pdf_files)} books")
    
    return output_file

if __name__ == "__main__":
    main()
