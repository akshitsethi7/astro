# PDF Extraction System for Vedic Astrology Books

## 🎯 What This Does

Automatically extracts and organizes content from 45 Vedic astrology books into 100+ structured, topic-based markdown documents for systematic learning.

**Time Investment**: 20 minutes setup + extraction  
**Return**: Organized knowledge from 10,000+ pages worth months of manual work

## 📚 Overview

This system extracts content from 45+ Vedic astrology PDF books and organizes it into structured markdown documents by topic. It's designed to support the 6-month learning project outlined in MASTER_PLAN.md.

## 🚀 Quick Start (5 Minutes)

```bash
# Navigate to extraction system
cd astro/logy-learning/extraction-system

# Option 1: Use the interactive menu (easiest)
chmod +x run.sh
./run.sh

# Option 2: Run directly with your venv Python
../../venv/bin/python3 test_extraction.py
../../venv/bin/python3 run_extraction.py --tier 1

# Option 3: View results
cat ../TOPIC_INDEX.md
ls ../00-foundations/
```

**Done!** You now have organized content from 10 classical texts.

**Note**: The scripts will auto-install PyPDF2 and pdfplumber if needed.

## Features

- **Intelligent PDF Extraction**: Extracts text from PDFs with chapter detection
- **Topic Categorization**: Automatically categorizes content by 15+ topics
- **Sutra Detection**: Identifies and extracts Sanskrit sutras and principles
- **Example Extraction**: Finds and extracts case studies and examples
- **Multi-Book Synthesis**: Combines content from multiple sources by topic
- **Structured Output**: Creates organized markdown documents ready for study

## System Components

### 1. pdf_extractor.py
Core extraction engine that:
- Reads PDF files using PyPDF2 and pdfplumber
- Detects chapter boundaries
- Categorizes content by topic (planets, houses, marriage, career, etc.)
- Extracts sutras and examples
- Generates JSON data and markdown summaries

### 2. topic_organizer.py
Content organization system that:
- Loads all extracted content
- Organizes by topic across all books
- Creates comprehensive topic documents
- Generates cross-references
- Produces master topic index

### 3. run_extraction.py
Master runner script that:
- Orchestrates the complete pipeline
- Supports tiered processing (Tier 1, 2, 3, or all books)
- Generates summary reports
- Provides command-line interface

## Installation

### Prerequisites

```bash
# Python 3.7 or higher required
python3 --version

# Install required packages
pip install PyPDF2 pdfplumber
```

Or let the scripts auto-install dependencies (they will attempt to install if missing).

## Usage

### Quick Start - Process Tier 1 Books (Foundation Texts)

```bash
cd astro/logy-learning/extraction-system
python3 run_extraction.py --tier 1
```

This processes the 10 most important foundation texts:
- BPHS Volumes 1 & 2
- Brihat Jataka
- Jataka Parijata Volumes 1 & 2
- Phaladeepika
- Jaimini Sutras
- And more

### Process Tier 1 + 2 (Foundation + Modern Masters)

```bash
python3 run_extraction.py --tier 2
```

Adds 5 modern master texts:
- Sanjay Rath's Introduction
- C.S. Patel's Navamsa
- K.N. Rao's Marriage Timing
- KK Pathak's Vimshottari Dasha
- 300 Important Combinations

### Process All Books

```bash
python3 run_extraction.py
```

Processes all 45 books in the Books folder.

### Custom Paths

```bash
python3 run_extraction.py --books-dir /path/to/Books --output-dir /path/to/output
```

## Output Structure

```
logy-learning/
├── extraction-system/
│   ├── extracted_content/          # Raw extractions
│   │   ├── BPHS_extraction.json
│   │   ├── BPHS_summary.md
│   │   └── ... (one per book)
│   └── MASTER_INDEX.md             # Index of all books
│
├── 00-foundations/                  # Foundation topics
│   ├── planets.md
│   ├── houses.md
│   ├── signs.md
│   └── ...
│
├── 01-marriage/                     # Marriage analysis
│   ├── marriage.md
│   ├── 7th-house.md
│   ├── venus.md
│   └── ...
│
├── 02-career/                       # Career analysis
├── 03-finance/                      # Wealth analysis
├── 04-children/                     # Children analysis
├── 05-health-longevity/            # Health analysis
├── 06-dashas/                       # Dasha systems
├── 07-transits/                     # Transit analysis
├── 08-divisional-charts/           # Varga charts
├── 09-yogas/                        # Yogas & combinations
├── 10-remedies/                     # Remedial measures
│
└── TOPIC_INDEX.md                   # Master topic index
```

## What Gets Extracted

### For Each Book:
- **Total pages**: Complete page count
- **Chapters**: Detected chapter boundaries
- **Topic coverage**: Pages per topic (planets, houses, marriage, etc.)
- **Sutras**: Classical principles and Sanskrit verses
- **Examples**: Case studies and chart examples
- **Page references**: Specific pages for each topic

### For Each Topic:
- **Source books**: Which books cover this topic
- **Classical principles**: Sutras from all sources
- **Examples**: Case studies from all sources
- **Page references**: Where to find more in original books
- **Cross-references**: Related topics

## Topic Categories

The system recognizes and organizes content into these categories:

1. **Foundations**: planets, houses, signs, nakshatras, aspects
2. **Marriage**: 7th house, Venus, Jupiter, Navamsa, spouse characteristics
3. **Career**: 10th house, profession indicators, career timing
4. **Wealth**: 2nd/11th houses, Dhana yogas, financial timing
5. **Children**: 5th house, Jupiter, Saptamsa, progeny timing
6. **Health**: 6th/8th houses, disease indicators, longevity
7. **Dashas**: Vimshottari, Yogini, Chara, Narayana
8. **Transits**: Jupiter, Saturn, Rahu-Ketu transits
9. **Divisional Charts**: All 16 vargas (D1-D60)
10. **Yogas**: Raja, Dhana, and other combinations
11. **Remedies**: Mantras, gemstones, pujas

## Advanced Usage

### Extract Specific Books Only

Edit `run_extraction.py` and modify the book lists, or use the extractor directly:

```python
from pdf_extractor import AstrologyPDFExtractor

extractor = AstrologyPDFExtractor("../../Books", "extracted_content")
book_list = ["BPHS - 1 RSanthanam.pdf", "Brihat Jataka 2nd Ed. by V Subrahmanya Sastri.pdf"]
extractions = extractor.process_all_books(book_list)
```

### Extract Topic-Specific Content

```python
from topic_organizer import TopicOrganizer

organizer = TopicOrganizer("extracted_content", "..")
extractions = organizer.load_all_extractions()
organized = organizer.organize_by_topic(extractions)

# Access specific topic
marriage_content = organized['marriage']
print(f"Marriage covered in {len(marriage_content['books'])} books")
```

## Workflow Integration

This extraction system integrates with the MASTER_PLAN workflow:

1. **Phase 1**: Run Tier 1 extraction for foundation texts
2. **Phase 2**: Run Tier 2 extraction for modern masters
3. **Phase 3**: Run full extraction for all books
4. **Review**: Read generated markdown documents
5. **Enhance**: Add your own notes and insights
6. **Apply**: Use with AKSHIT-LEARNING-APPLICATION.md

## Troubleshooting

### "PyPDF2 not found"
```bash
pip install PyPDF2 pdfplumber
```

### "Books directory not found"
Check that the Books folder is at `../../Books` relative to the script, or use `--books-dir` flag.

### "No text extracted from PDF"
Some PDFs may be scanned images. These require OCR (not included). Try with other books first.

### "Memory error"
Process books in tiers rather than all at once:
```bash
python3 run_extraction.py --tier 1
python3 run_extraction.py --tier 2
```

## Performance

- **Tier 1 (10 books)**: ~10-20 minutes
- **Tier 2 (15 books)**: ~20-30 minutes
- **All books (45)**: ~60-90 minutes

Depends on PDF size and system performance.

## Next Steps After Extraction

1. Review `MASTER_INDEX.md` to see what was extracted
2. Review `TOPIC_INDEX.md` to see topic coverage
3. Read generated topic documents in each folder
4. Cross-reference with original PDFs using page numbers
5. Add your own notes and insights
6. Create practice exercises
7. Apply to personal chart analysis

## Contributing

To improve the extraction:

1. Add more topic keywords in `pdf_extractor.py`
2. Improve chapter detection patterns
3. Enhance sutra extraction regex
4. Add more topic categories
5. Improve document templates

## License

This extraction system is for personal educational use. The extracted content belongs to the original book authors and publishers.

---

**Created for the Vedic Astrology 6-Month Learning Project**  
**See MASTER_PLAN.md for the complete learning roadmap**
