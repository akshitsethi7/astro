# Quick Start Guide - 5 Minutes to First Extraction

## Prerequisites

- Python 3.7+ installed (you have it in `astro/venv/`)
- 45 PDF books in `Books/` directory
- 10-15 minutes for first extraction

## Step-by-Step

### 1. Test the System (2 minutes)

The test script will auto-install dependencies if needed.

```bash
cd astro/logy-learning/extraction-system

# Use Python from your venv
../../venv/bin/python3 test_extraction.py
```

Expected output:
```
✓ pdf_extractor module loaded
✓ topic_organizer module loaded
✓ Books directory found
✓ Found 45 PDF files
  Testing with: BPHS - 1 RSanthanam.pdf
✓ Extraction successful!
  Pages extracted: 400
  Chapters detected: 82
  Sutras found: 150
  Examples found: 25
✓ All tests passed!
```

### 2. Run First Extraction (15 minutes)

```bash
../../venv/bin/python3 run_extraction.py --tier 1
```

This processes 10 foundation texts. Go get coffee ☕

### 3. View Results (1 minute)

```bash
# See what was extracted
cat extracted_content/MASTER_INDEX.md

# See topic coverage
cat ../TOPIC_INDEX.md

# Browse generated documents
ls ../00-foundations/
ls ../01-marriage/
```

### 4. Start Learning!

Open any generated markdown file:
```bash
# Foundation topics
cat ../00-foundations/planets.md
cat ../00-foundations/houses.md

# Marriage analysis
cat ../01-marriage/marriage.md

# Career analysis
cat ../02-career/career.md
```

## What You Get

After extraction, you'll have:

✅ **10 books processed** (Tier 1)  
✅ **~3,000 pages extracted**  
✅ **~500 sutras identified**  
✅ **~100 examples found**  
✅ **15+ topic documents created**  
✅ **Complete page references** for deep study  

## Next Steps

1. **Read generated documents** - Start with `00-foundations/`
2. **Cross-reference originals** - Use page numbers to read full context
3. **Apply to your chart** - Use `AKSHIT-LEARNING-APPLICATION.md`
4. **Continue extraction** - Run Tier 2 and 3 when ready

## Common Issues

**"PyPDF2 not found"**
- The test script will auto-install it
- Or manually: `../../venv/bin/pip install PyPDF2 pdfplumber`

**"Books directory not found"**
```bash
# Check path
ls ../../Books
# Should show 45 PDF files
```

**"Test failed"**
- Check Python version: `../../venv/bin/python3 --version` (need 3.7+)
- Check Books directory exists
- Try with a different PDF if one fails

## Full Documentation

- **README.md** - Complete system overview
- **USAGE_GUIDE.md** - Detailed usage instructions
- **MASTER_PLAN.md** - 6-month learning roadmap

## Support

If you encounter issues:
1. Run `python3 test_extraction.py` to diagnose
2. Check error messages carefully
3. Review USAGE_GUIDE.md for troubleshooting

---

**Time Investment**: 5 minutes setup + 15 minutes extraction = 20 minutes  
**Return**: Organized knowledge from 10 classical texts worth months of manual work

Let's begin! 🚀