# PDF EXTRACTION SYSTEM

**Purpose**: Tools for extracting content from classical astrology texts  
**Last Updated**: February 27, 2026  
**Status**: Fully Functional ✅

---

## 📁 WHAT'S IN THIS FOLDER

This folder contains 30+ Python scripts for extracting, processing, and analyzing content from classical astrology PDF books.

### Key Scripts:
- `pdf_extractor.py` - Main PDF extraction tool
- `run_extraction.py` - Automated extraction runner
- `extract_all_books.py` - Batch extraction for all books
- `content_processor.py` - Process extracted content
- `analyze_akshit_from_pdfs.py` - Analyze Akshit's chart using extracted content

### Documentation:
- `START_HERE.md` - Quick start guide
- `README.md` - Detailed extraction system guide
- `WORKFLOW.md` - Complete workflow documentation
- `USAGE_GUIDE.md` - Usage instructions
- `SYSTEM_OVERVIEW.md` - System architecture

---

## 🚀 QUICK START

### To Extract a Single Book:
```bash
cd astro/15-EXTRACTION-SYSTEM
python pdf_extractor.py --book "BPHS - 1 RSanthanam.pdf"
```

### To Extract All Books:
```bash
python extract_all_books.py
```

### To Analyze Akshit's Chart:
```bash
python analyze_akshit_from_pdfs.py
```

---

## 📊 STATISTICS

**Total Scripts**: 30+ Python scripts
**Extraction Capacity**: 33 classical texts
**Output Format**: JSON + Markdown
**Source Books**: Located in `../../Books/`
**Output Location**: `../16-EXTRACTED-BOOKS/`

---

## 🔧 SCRIPT CATEGORIES

### Extraction Scripts:
- `pdf_extractor.py` - Core extraction
- `extract_all_books.py` - Batch extraction
- `extract_real_content.py` - Real content extraction
- `full_extraction.py` - Full extraction pipeline

### Processing Scripts:
- `content_processor.py` - Content processing
- `enhanced_processor.py` - Enhanced processing
- `content_distributor.py` - Content distribution
- `topic_organizer.py` - Topic organization

### Analysis Scripts:
- `analyze_akshit_from_pdfs.py` - Chart analysis
- `deep_analysis_with_refs.py` - Deep analysis with references
- `search_marriage_content.py` - Marriage content search

### Knowledge Building:
- `build_knowledge_base.py` - Build knowledge base
- `knowledge_synthesizer.py` - Synthesize knowledge
- `create_high_quality_docs.py` - Create quality docs

### Utilities:
- `find_books.py` - Find available books
- `test_extraction.py` - Test extraction
- `progress_tracker.py` - Track progress
- `batch_generator.py` - Generate batches

---

## 📦 OUTPUT

All extracted content goes to: `../16-EXTRACTED-BOOKS/`

Output includes:
- JSON files with structured content
- Markdown summaries
- Classification data
- Extraction logs

---

## 🛠️ REQUIREMENTS

Install dependencies:
```bash
pip install -r requirements.txt
```

Required packages:
- PyPDF2
- pdfplumber
- json
- re
- pathlib

---

## 🔍 RELATED FOLDERS

### Source Books:
- Location: `../../Books/`
- Total: 46 PDF files
- Classical astrology texts

### Extracted Content:
- Location: `../16-EXTRACTED-BOOKS/`
- Format: JSON + Markdown
- Total: 33 books extracted

### Learning Materials:
- Location: `../14-LEARNING-MATERIALS/`
- Uses extracted content for learning

### Main Analysis:
- Location: `../01-AKSHIT-ANALYSIS/`
- Uses extracted content for analysis

---

## 📝 NOTES

- All scripts are Python 3.8+
- Source PDFs must be in `../../Books/` folder
- Output automatically goes to `../16-EXTRACTED-BOOKS/`
- Extraction logs are saved for tracking
- Some scripts have subdirectories (extracted_content, test_output, __pycache__)

---

## 🙏 ACKNOWLEDGMENTS

**Books Extracted**: 33 classical texts
**Total Quotes**: 14,069+ quotes extracted
**System Type**: Python-based PDF extraction
**Output Size**: 34MB+ of structured content

---

**For detailed documentation, check**: `START_HERE.md` or `README.md`

**For extracted books, go to**: `../16-EXTRACTED-BOOKS/`

**For learning materials, go to**: `../14-LEARNING-MATERIALS/`

🔧 **Happy Extracting!** 🔧
