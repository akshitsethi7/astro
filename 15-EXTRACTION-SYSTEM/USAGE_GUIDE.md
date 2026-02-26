# Complete Usage Guide - PDF Extraction System

## Quick Start (5 Minutes)

### Step 1: Install Dependencies

```bash
cd astro/logy-learning/extraction-system
pip install -r requirements.txt
```

### Step 2: Test the System

```bash
python3 test_extraction.py
```

This will:
- Check if all dependencies are installed
- Test extraction on one book
- Verify the system works correctly

### Step 3: Run Extraction

```bash
# Option A: Interactive menu
./extract.sh

# Option B: Direct command
python3 run_extraction.py --tier 1
```

### Step 4: Review Results

```bash
# View master index
cat ../MASTER_INDEX.md

# View topic index
cat ../TOPIC_INDEX.md

# Browse extracted documents
ls -la ../00-foundations/
ls -la ../01-marriage/
```

---

## Detailed Workflow

### Phase 1: Foundation Texts (Week 1-2)

Extract the 10 most important classical texts:

```bash
python3 run_extraction.py --tier 1
```

**Books processed**:
- BPHS Volumes 1 & 2 (Parashara's complete system)
- Brihat Jataka (Varahamihira's principles)
- Jataka Parijata Volumes 1 & 2 (Vaidyanatha's methods)
- Phaladeepika (Mantreswara's predictions)
- Jaimini Sutras (Jaimini's unique system)
- And more classical texts

**Output**: Foundation documents in `00-foundations/`

**Time**: ~15-20 minutes

**Next**: Study the generated foundation documents while reading original texts

### Phase 2: Modern Masters (Week 3-4)

Add modern interpretations and practical applications:

```bash
python3 run_extraction.py --tier 2
```

**Additional books**:
- Sanjay Rath's Introduction to Vedic Astrology
- C.S. Patel's Navamsa in Astrology
- K.N. Rao's Marriage Timing
- KK Pathak's Vimshottari Dasha
- 300 Important Combinations

**Output**: Enhanced documents with modern perspectives

**Time**: ~25-30 minutes total

### Phase 3: Specialized Topics (Week 5-8)

Add specialized books on marriage, career, health:

```bash
python3 run_extraction.py --tier 3
```

**Additional books**:
- Marriage and Married Life
- Astrology of Professions
- Health and Disease analysis
- And more specialized texts

**Output**: Complete topic coverage

**Time**: ~35-40 minutes total

### Phase 4: Complete Library (Month 2+)

Process all 45 books for comprehensive coverage:

```bash
python3 run_extraction.py
```

**All books**: Complete library extraction

**Output**: Exhaustive topic documents

**Time**: ~60-90 minutes

---

## Understanding the Output

### Directory Structure

```
logy-learning/
├── extraction-system/
│   ├── extracted_content/          # Raw data
│   │   ├── BPHS_extraction.json   # Structured data
│   │   ├── BPHS_summary.md        # Human-readable summary
│   │   └── ...
│   └── test_output/                # Test results
│
├── 00-foundations/                  # Generated documents
│   ├── planets.md                  # All planetary knowledge
│   ├── houses.md                   # All house knowledge
│   └── ...
│
├── 01-marriage/
│   ├── marriage.md                 # Complete marriage analysis
│   ├── 7th-house.md               # 7th house deep dive
│   └── ...
│
└── MASTER_INDEX.md                 # Book index
└── TOPIC_INDEX.md                  # Topic index
```

### File Types

**JSON Files** (`*_extraction.json`):
- Structured data for programmatic access
- Contains all extracted content
- Page references and metadata
- Use for custom processing

**Summary Files** (`*_summary.md`):
- Human-readable book summaries
- Chapter listings
- Topic coverage statistics
- Sample sutras and examples

**Topic Documents** (`*.md` in topic folders):
- Comprehensive topic analysis
- Content from multiple books
- Classical principles (sutras)
- Modern interpretations
- Examples and case studies
- Page references for deep study

### Index Files

**MASTER_INDEX.md**:
- Complete list of all processed books
- Statistics per book (pages, chapters, sutras, examples)
- Top topics per book
- Quick reference for which book covers what

**TOPIC_INDEX.md**:
- All topics sorted by coverage
- Which books cover each topic
- How many pages per topic
- Quick reference for topic research

---

## Working with Extracted Content

### Scenario 1: Learning About Planets

1. Open `00-foundations/planets.md`
2. Read the synthesized content from all books
3. Note the page references at the bottom
4. Open original PDFs to those pages for deeper study
5. Add your own notes and insights

### Scenario 2: Marriage Analysis

1. Open `01-marriage/marriage.md`
2. Review classical principles from BPHS, Jataka Parijata, etc.
3. Study modern methods from K.N. Rao
4. Check examples and case studies
5. Apply to your personal chart
6. Cross-reference with `01-marriage/7th-house.md`, `venus.md`, etc.

### Scenario 3: Finding Specific Information

1. Open `TOPIC_INDEX.md`
2. Find your topic (e.g., "dashas")
3. See which books cover it most
4. Open the topic document
5. Use page references to read original text

### Scenario 4: Comparing Classical Texts

1. Open a topic document (e.g., `houses.md`)
2. Read the "Classical Principles & Sutras" section
3. Compare what BPHS says vs. Jataka Parijata vs. Phaladeepika
4. Note agreements (strong principles)
5. Note disagreements (context-dependent)
6. Form your own understanding

---

## Advanced Usage

### Extract Specific Books Only

Create a custom book list:

```python
from pdf_extractor import AstrologyPDFExtractor

books = [
    "BPHS - 1 RSanthanam.pdf",
    "C.S._Patel_-_Navamsa_in_Astrology.pdf"
]

extractor = AstrologyPDFExtractor("../../Books", "extracted_content")
extractions = extractor.process_all_books(books)
```

### Extract Topic-Specific Content

```python
from topic_organizer import TopicOrganizer

organizer = TopicOrganizer("extracted_content", "..")
extractions = organizer.load_all_extractions()
organized = organizer.organize_by_topic(extractions)

# Get all marriage content
marriage = organized['marriage']
print(f"Books: {len(set(marriage['books']))}")
print(f"Pages: {marriage['total_pages']}")
print(f"Sutras: {len(marriage['sutras'])}")
```

### Re-run Organization Only

If you've already extracted but want to reorganize:

```python
from topic_organizer import TopicOrganizer

organizer = TopicOrganizer("extraction-system/extracted_content", ".")
organizer.generate_all_documents()
```

### Add Custom Topics

Edit `topic_organizer.py` and add to `topic_structure`:

```python
'custom_topic': {
    'folder': '11-custom',
    'topics': ['keyword1', 'keyword2'],
    'priority': 6
}
```

---

## Integration with MASTER_PLAN

### Week 1-2: Foundation Phase

```bash
# Extract foundation texts
python3 run_extraction.py --tier 1

# Study generated documents
cat ../00-foundations/01-zodiac-signs.md
cat ../00-foundations/planets.md
cat ../00-foundations/houses.md

# Cross-reference with original books using page numbers
# Add your own notes and insights
```

### Week 3-8: Life Areas Phase

```bash
# Extract modern masters
python3 run_extraction.py --tier 2

# Study marriage documents
ls ../01-marriage/

# Study career documents
ls ../02-career/

# Apply to personal chart (see AKSHIT-LEARNING-APPLICATION.md)
```

### Month 2+: Advanced Topics

```bash
# Extract all books
python3 run_extraction.py

# Study advanced topics
ls ../06-dashas/
ls ../08-divisional-charts/
ls ../09-yogas/
```

---

## Troubleshooting

### Problem: "PyPDF2 not found"

**Solution**:
```bash
pip install PyPDF2 pdfplumber
```

### Problem: "Books directory not found"

**Solution**:
```bash
# Check path
ls ../../Books

# Or specify custom path
python3 run_extraction.py --books-dir /path/to/Books
```

### Problem: "No text extracted"

**Cause**: PDF might be scanned images (requires OCR)

**Solution**: Skip that book for now, process others

### Problem: "Memory error"

**Solution**: Process in tiers instead of all at once
```bash
python3 run_extraction.py --tier 1
# Wait for completion
python3 run_extraction.py --tier 2
```

### Problem: "Extraction is slow"

**Normal**: Large PDFs take time
- Tier 1: 15-20 min
- Tier 2: 25-30 min
- All books: 60-90 min

**Tip**: Run overnight or during breaks

---

## Best Practices

### 1. Start Small
- Begin with Tier 1 (foundation texts)
- Review the output quality
- Adjust if needed
- Then proceed to more books

### 2. Review Regularly
- Check MASTER_INDEX.md after each extraction
- Verify topic coverage in TOPIC_INDEX.md
- Read sample documents to ensure quality

### 3. Cross-Reference
- Don't rely solely on extracted content
- Use page references to read original texts
- Extracted content is a guide, not a replacement

### 4. Add Your Notes
- Edit generated markdown files
- Add your own insights
- Include personal chart examples
- Track predictions and results

### 5. Organize Your Learning
- Follow MASTER_PLAN.md timeline
- Use AKSHIT-LEARNING-APPLICATION.md for practice
- Track progress in MASTER_PLAN.md

---

## Next Steps After Extraction

1. **Review Indexes**
   - Read MASTER_INDEX.md
   - Read TOPIC_INDEX.md
   - Understand what was extracted

2. **Study Foundation**
   - Read all documents in `00-foundations/`
   - Cross-reference with original books
   - Complete practice exercises

3. **Apply to Chart**
   - Use AKSHIT-LEARNING-APPLICATION.md
   - Apply each concept to your birth chart
   - Track predictions

4. **Deep Dive Topics**
   - Choose a life area (marriage, career, etc.)
   - Read all related documents
   - Study original book pages
   - Make detailed notes

5. **Synthesize Knowledge**
   - Compare classical vs. modern views
   - Note agreements and disagreements
   - Form your own understanding
   - Test with real charts

---

## Support and Feedback

### Getting Help

1. Check this guide first
2. Review README.md
3. Run test_extraction.py to diagnose issues
4. Check error messages carefully

### Improving the System

The extraction system can be enhanced:
- Add more topic keywords
- Improve chapter detection
- Better sutra extraction
- More document templates

Edit the Python files to customize for your needs.

---

**Happy Learning! May this system accelerate your journey to mastering Vedic Astrology.**
