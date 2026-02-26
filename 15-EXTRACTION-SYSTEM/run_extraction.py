#!/usr/bin/env python3
"""
Master Extraction Runner
Runs the complete extraction and organization pipeline
"""

import sys
from pathlib import Path
from pdf_extractor import AstrologyPDFExtractor
from topic_organizer import TopicOrganizer


# Book priority list from MASTER_PLAN
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
    "jyotish_astrology-and-timing-of-marriage_-k-n-rao.pdf",
    "advanced study of vimshottari dasha_KK Pathak.pdf",
    "Three Hundred Important Combinations in Vedic Astrology.pdf"
]

TIER_3_BOOKS = [
    "2015.150536.Marriage-Married-Life-And-Children_text.pdf",
    "Astrology in Marriage Counselling_Manik Chand Jain.pdf",
    "kpreader-4-marriage-married-life-children.pdf",
    "A.K. Gour_Astrology of Professions.pdf",
    "Jyotish Evam Rog Vichar Of Bhoj Raj Dwivedi - Diamond Pocket Books Private Limited, New Delhi.pdf"
]


def print_banner(text):
    """Print formatted banner"""
    print("\n" + "=" * 70)
    print(text.center(70))
    print("=" * 70 + "\n")


def run_full_extraction(books_dir, output_dir, tier=None):
    """Run complete extraction pipeline"""
    
    print_banner("VEDIC ASTROLOGY CONTENT EXTRACTION SYSTEM")
    
    # Determine which books to process
    if tier == 1:
        book_list = TIER_1_BOOKS
        print("Processing TIER 1: Foundation Texts (10 books)")
    elif tier == 2:
        book_list = TIER_1_BOOKS + TIER_2_BOOKS
        print("Processing TIER 1 + 2: Foundation + Modern Masters (15 books)")
    elif tier == 3:
        book_list = TIER_1_BOOKS + TIER_2_BOOKS + TIER_3_BOOKS
        print("Processing TIER 1-3: Foundation + Modern + Specialized (20 books)")
    else:
        book_list = None
        print("Processing ALL BOOKS (45 books)")
    
    # Step 1: Extract from PDFs
    print_banner("STEP 1: PDF EXTRACTION")
    extraction_output = Path(output_dir) / "extracted_content"
    extractor = AstrologyPDFExtractor(books_dir, str(extraction_output))
    
    extractions = extractor.process_all_books(book_list)
    
    if not extractions:
        print("ERROR: No books were successfully extracted!")
        return False
    
    print(f"\n✓ Successfully extracted {len(extractions)} books")
    
    # Step 2: Organize by topic
    print_banner("STEP 2: TOPIC ORGANIZATION")
    organizer = TopicOrganizer(str(extraction_output), output_dir)
    organizer.generate_all_documents()
    
    print("\n✓ Topic organization complete")
    
    # Step 3: Generate summary report
    print_banner("EXTRACTION COMPLETE")
    print(f"Books Processed: {len(extractions)}")
    print(f"Output Directory: {output_dir}")
    print(f"\nGenerated Files:")
    print(f"  - extracted_content/: Raw extractions (JSON + summaries)")
    print(f"  - 00-foundations/: Foundation topic documents")
    print(f"  - 01-marriage/: Marriage analysis documents")
    print(f"  - 02-career/: Career analysis documents")
    print(f"  - ... and more topic folders")
    print(f"  - MASTER_INDEX.md: Complete book index")
    print(f"  - TOPIC_INDEX.md: Complete topic index")
    
    return True


def main():
    """Main execution with command line options"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Extract and organize content from Vedic astrology books"
    )
    parser.add_argument(
        '--tier',
        type=int,
        choices=[1, 2, 3],
        help='Process specific tier of books (1=Foundation, 2=+Modern, 3=+Specialized)'
    )
    parser.add_argument(
        '--books-dir',
        type=str,
        default='../../Books',
        help='Path to Books directory'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='..',
        help='Path to output directory (logy-learning folder)'
    )
    
    args = parser.parse_args()
    
    # Resolve paths
    script_dir = Path(__file__).parent
    
    # Handle Books as separate workspace folder
    if args.books_dir == '../../Books':
        # Check if Books is a sibling workspace folder
        books_dir = script_dir.parent.parent.parent / 'Books'
        if not books_dir.exists():
            # Try original path
            books_dir = (script_dir / args.books_dir).resolve()
    else:
        books_dir = (script_dir / args.books_dir).resolve()
    
    output_dir = (script_dir / args.output_dir).resolve()
    
    if not books_dir.exists():
        print(f"ERROR: Books directory not found: {books_dir}")
        print("Please check the path and try again.")
        sys.exit(1)
    
    # Run extraction
    success = run_full_extraction(str(books_dir), str(output_dir), args.tier)
    
    if success:
        print("\n" + "=" * 70)
        print("SUCCESS! All content extracted and organized.".center(70))
        print("=" * 70)
        sys.exit(0)
    else:
        print("\nERROR: Extraction failed. Check the logs above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
