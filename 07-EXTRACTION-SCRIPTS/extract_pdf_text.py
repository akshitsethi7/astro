#!/usr/bin/env python3
"""
Extract text from all PDFs in Books folder
"""

import os
import sys
from pathlib import Path

# Try different PDF libraries
try:
    import PyPDF2
    PDF_LIB = "PyPDF2"
except ImportError:
    try:
        import pdfplumber
        PDF_LIB = "pdfplumber"
    except ImportError:
        try:
            import fitz  # PyMuPDF
            PDF_LIB = "pymupdf"
        except ImportError:
            PDF_LIB = None

def extract_with_pypdf2(pdf_path):
    """Extract text using PyPDF2"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error with PyPDF2: {e}")
    return text

def extract_with_pdfplumber(pdf_path):
    """Extract text using pdfplumber"""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error with pdfplumber: {e}")
    return text

def extract_with_pymupdf(pdf_path):
    """Extract text using PyMuPDF"""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text() + "\n"
        doc.close()
    except Exception as e:
        print(f"Error with PyMuPDF: {e}")
    return text

def extract_pdf_text(pdf_path):
    """Extract text from PDF using available library"""
    if PDF_LIB == "PyPDF2":
        return extract_with_pypdf2(pdf_path)
    elif PDF_LIB == "pdfplumber":
        return extract_with_pdfplumber(pdf_path)
    elif PDF_LIB == "pymupdf":
        return extract_with_pymupdf(pdf_path)
    else:
        return ""

def main():
    books_dir = Path("/Users/akshitsethi/Desktop/Books")
    output_dir = Path("/Users/akshitsethi/Desktop/astro/extracted_books")
    output_dir.mkdir(exist_ok=True)
    
    if PDF_LIB is None:
        print("No PDF library available. Installing PyPDF2...")
        os.system("pip3 install PyPDF2 pdfplumber pymupdf --quiet")
        # Try again
        try:
            import PyPDF2
            global PDF_LIB
            PDF_LIB = "PyPDF2"
        except:
            print("Could not install PDF libraries. Please install manually:")
            print("pip3 install PyPDF2 pdfplumber pymupdf")
            return
    
    print(f"Using PDF library: {PDF_LIB}")
    print(f"Extracting text from PDFs in: {books_dir}")
    print()
    
    pdf_files = list(books_dir.glob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files")
    print()
    
    extracted_texts = {}
    
    for pdf_file in pdf_files:
        print(f"Extracting: {pdf_file.name}...")
        try:
            text = extract_pdf_text(pdf_file)
            if text and len(text.strip()) > 100:  # Only save if substantial text
                # Save to file
                output_file = output_dir / f"{pdf_file.stem}.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(text)
                
                extracted_texts[pdf_file.name] = text[:5000]  # Store first 5000 chars for analysis
                print(f"  ✓ Extracted {len(text)} characters")
            else:
                print(f"  ⚠ Little or no text extracted")
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    # Save summary
    summary_file = output_dir / "extraction_summary.txt"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("PDF TEXT EXTRACTION SUMMARY\n")
        f.write("="*80 + "\n\n")
        for pdf_name, text_sample in extracted_texts.items():
            f.write(f"{pdf_name}:\n")
            f.write(f"  Sample: {text_sample[:500]}...\n\n")
    
    print()
    print(f"Extraction complete! Files saved to: {output_dir}")
    print(f"Summary saved to: {summary_file}")
    
    return extracted_texts

if __name__ == "__main__":
    main()
