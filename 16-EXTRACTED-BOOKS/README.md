# EXTRACTED CLASSICAL TEXTS

**Purpose**: Extracted content from 33 classical astrology books  
**Last Updated**: February 27, 2026  
**Status**: Complete ✅

---

## 📁 WHAT'S IN THIS FOLDER

This folder contains extracted and processed content from 33 classical Vedic astrology texts in structured JSON and Markdown formats.

### Key Files:
- `MASTER_INDEX.md` - Index of all extracted books
- `all_books_classified.json` - All books content (34MB)
- `bphs_full_content.json` - Complete BPHS content (2.3MB)
- `bphs_full_classified.json` - BPHS classified content (108KB)
- `extraction_log.json` - Extraction logs and statistics

### BPHS Extractions:
- `BPHS - 1 RSanthanam_extraction.json` (298KB)
- `BPHS - 1 RSanthanam_summary.md` (25KB)
- `BPHS - 2 RSanthanam_extraction.json` (269KB)
- `BPHS - 2 RSanthanam_summary.md` (17KB)

---

## 📊 STATISTICS

**Total Books Extracted**: 33 classical texts
**Total Size**: 34MB+ of structured content
**Total Quotes**: 14,069+ quotes
**Format**: JSON (structured) + Markdown (readable)
**Source Location**: `../../Books/` (46 PDFs)

---

## 🔍 CONTENT STRUCTURE

### JSON Files:
Structured data with:
- Book metadata (title, author, pages)
- Chapter/section organization
- Classified content by topic
- Searchable quotes and references

### Markdown Files:
Human-readable summaries with:
- Book overview
- Key concepts
- Chapter summaries
- Important quotes

---

## 📚 EXTRACTED BOOKS

Check `MASTER_INDEX.md` for complete list of extracted books including:
- Brihat Parashara Hora Shastra (BPHS) Vol 1 & 2
- Brihat Jataka
- Jataka Parijata
- Phaladeepika
- Uttara Kalamrita
- And 28 more classical texts

---

## 🚀 USAGE

### For Programmatic Access:
```python
import json

# Load all books
with open('all_books_classified.json', 'r') as f:
    all_books = json.load(f)

# Search for specific content
marriage_content = [
    quote for quote in all_books 
    if 'marriage' in quote['text'].lower()
]
```

### For Human Reading:
1. Check `MASTER_INDEX.md` for book list
2. Open specific `*_summary.md` files
3. Read chapter summaries and key quotes

### For Analysis:
1. Use `all_books_classified.json` for comprehensive search
2. Use topic-specific JSON files for focused analysis
3. Cross-reference with `../14-LEARNING-MATERIALS/`

---

## 🔧 EXTRACTION TOOLS

All extraction was done using scripts in: `../15-EXTRACTION-SYSTEM/`

To extract more books:
```bash
cd ../15-EXTRACTION-SYSTEM
python pdf_extractor.py --book "BookName.pdf"
```

---

## 🔍 RELATED FOLDERS

### Source Books:
- Location: `../../Books/`
- Total: 46 PDF files
- Classical astrology texts

### Extraction Tools:
- Location: `../15-EXTRACTION-SYSTEM/`
- 30+ Python scripts
- Automated extraction pipeline

### Learning Materials:
- Location: `../14-LEARNING-MATERIALS/`
- Uses this extracted content
- Organized by topic

### Main Analysis:
- Location: `../01-AKSHIT-ANALYSIS/`
- Uses this extracted content
- 14,069 quotes in `AKSHIT_MAXIMUM_EXTRACTION.md`

---

## 📝 FILE FORMATS

### JSON Structure:
```json
{
  "book": "Book Title",
  "author": "Author Name",
  "topic": "marriage/career/wealth/etc",
  "chapter": "Chapter Name",
  "text": "Actual quote or content",
  "page": 123
}
```

### Markdown Structure:
```markdown
# Book Title

## Overview
Brief description

## Chapter 1: Name
Summary and key quotes

## Key Concepts
Important teachings
```

---

## 🎯 SEARCH TIPS

### To Find Marriage Content:
```bash
grep -r "marriage" *.json
```

### To Find Career Content:
```bash
grep -r "career\|profession\|10th house" *.json
```

### To Find Dasha Content:
```bash
grep -r "dasha\|mahadasha\|antardasha" *.json
```

### To Find Specific Book:
Check `MASTER_INDEX.md` for book list and filenames

---

## 🛠️ MAINTENANCE

### To Add New Extractions:
1. Place PDF in `../../Books/`
2. Run extraction script from `../15-EXTRACTION-SYSTEM/`
3. Output will appear in this folder
4. Update `MASTER_INDEX.md`

### To Update Existing:
1. Delete old extraction files
2. Re-run extraction script
3. Verify output

---

## 📊 CONTENT BREAKDOWN

**By Topic**:
- Marriage: 2,500+ quotes
- Career: 1,800+ quotes
- Wealth: 2,200+ quotes
- Health: 1,500+ quotes
- Dashas: 2,000+ quotes
- Yogas: 1,900+ quotes
- Other: 2,169+ quotes

**By Book Type**:
- Classical texts: 25 books
- Modern commentaries: 5 books
- Specialized topics: 3 books

---

## 🙏 ACKNOWLEDGMENTS

**Books Extracted**: 33 classical texts
**Extraction Method**: Python-based PDF extraction
**Total Effort**: Comprehensive extraction system
**Output Quality**: Structured, searchable, classified

---

**For extraction tools, go to**: `../15-EXTRACTION-SYSTEM/`

**For learning materials, go to**: `../14-LEARNING-MATERIALS/`

**For main analysis, go to**: `../01-AKSHIT-ANALYSIS/`

📦 **All classical wisdom, digitized and structured!** 📦
