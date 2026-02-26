#!/usr/bin/env python3
"""
Test script to verify extraction system works
Tests with a single book before running full extraction
"""

import sys
import subprocess
from pathlib import Path

# Auto-install dependencies if needed
def install_dependencies():
    """Install required packages if not available"""
    packages = ['PyPDF2', 'pdfplumber']
    for package in packages:
        try:
            __import__(package.lower().replace('-', '_'))
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

install_dependencies()

try:
    from pdf_extractor import AstrologyPDFExtractor
    print("✓ pdf_extractor module loaded")
except ImportError as e:
    print(f"✗ Error loading pdf_extractor: {e}")
    sys.exit(1)

try:
    from topic_organizer import TopicOrganizer
    print("✓ topic_organizer module loaded")
except ImportError as e:
    print(f"✗ Error loading topic_organizer: {e}")
    sys.exit(1)


def test_single_book():
    """Test extraction with a single book"""
    print("\n" + "=" * 60)
    print("Testing PDF Extraction System")
    print("=" * 60 + "\n")
    
    # Setup paths
    script_dir = Path(__file__).parent
    
    # Handle Books as separate workspace folder
    books_dir = script_dir.parent.parent.parent / "Books"
    if not books_dir.exists():
        # Try alternative path
        books_dir = script_dir.parent.parent / "Books"
    
    output_dir = script_dir / "test_output"
    output_dir.mkdir(exist_ok=True)
    
    if not books_dir.exists():
        print(f"✗ Books directory not found: {books_dir}")
        return False
    
    print(f"✓ Books directory found: {books_dir}")
    
    # Find a test book
    pdf_files = list(books_dir.glob("*.pdf"))
    if not pdf_files:
        print("✗ No PDF files found in Books directory")
        return False
    
    test_book = pdf_files[0]
    print(f"✓ Found {len(pdf_files)} PDF files")
    print(f"  Testing with: {test_book.name}\n")
    
    # Test extraction
    print("Testing PDF extraction...")
    try:
        extractor = AstrologyPDFExtractor(str(books_dir), str(output_dir))
        book_data = extractor.process_book(test_book)
        
        if 'error' in book_data:
            print(f"✗ Extraction failed: {book_data['error']}")
            return False
        
        print(f"✓ Extraction successful!")
        print(f"  Pages extracted: {book_data.get('total_pages', 0)}")
        print(f"  Chapters detected: {len(book_data.get('chapters', []))}")
        print(f"  Sutras found: {book_data.get('sutras_count', 0)}")
        print(f"  Examples found: {book_data.get('examples_count', 0)}")
        
        # Show topic coverage
        topic_cov = book_data.get('topic_coverage', {})
        if topic_cov:
            print(f"\n  Topic coverage:")
            for topic, count in sorted(topic_cov.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(f"    - {topic}: {count} pages")
        
        # Save test extraction
        extractor.save_extraction(book_data, test_book.stem)
        print(f"\n✓ Test extraction saved to: {output_dir}")
        
        return True
        
    except Exception as e:
        print(f"✗ Extraction error: {e}")
        import traceback
        traceback.print_exc()
        return False


def check_dependencies():
    """Check if required packages are installed"""
    print("\nChecking dependencies...")
    
    try:
        import PyPDF2
        print(f"✓ PyPDF2 version: {PyPDF2.__version__}")
    except ImportError:
        print("✗ PyPDF2 not installed")
        print("  Install with: pip install PyPDF2")
        return False
    
    try:
        import pdfplumber
        print(f"✓ pdfplumber installed")
    except ImportError:
        print("⚠ pdfplumber not installed (optional but recommended)")
        print("  Install with: pip install pdfplumber")
    
    return True


def main():
    """Run tests"""
    print("=" * 60)
    print("PDF Extraction System - Test Suite")
    print("=" * 60)
    
    # Check dependencies
    if not check_dependencies():
        print("\n✗ Dependency check failed")
        print("Install required packages with:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
    
    # Test extraction
    if test_single_book():
        print("\n" + "=" * 60)
        print("✓ All tests passed!")
        print("=" * 60)
        print("\nYou can now run the full extraction:")
        print("  python3 run_extraction.py --tier 1")
        sys.exit(0)
    else:
        print("\n" + "=" * 60)
        print("✗ Tests failed")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    main()
