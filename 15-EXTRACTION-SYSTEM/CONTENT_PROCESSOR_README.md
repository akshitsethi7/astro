# Content Processor - Transform Raw Extractions into Learning Documents

## Overview

The Content Processor is the second stage of the extraction system. It transforms raw PDF extractions into structured, comprehensive learning documents that follow the MASTER_PLAN format.

## What It Does

### Input
- Raw JSON extractions from PDF books
- Chapter text, titles, and page numbers
- Unstructured content dumps

### Output
- Structured learning documents with:
  - Clear introductions and learning objectives
  - Classical principles from source texts
  - Modern application guidelines
  - Practice exercises
  - Personal chart application sections
  - Summaries and next steps

## Two-Stage Workflow

### Stage 1: PDF Extraction (Already Done)
```bash
bash run.sh
# Select option 1-5 to extract PDFs
```

This creates:
- `extracted_content/*_extraction.json` - Raw chapter data
- `extracted_content/*_summary.md` - Book summaries
- Raw topic files (planets.md, houses.md, etc.)

### Stage 2: Content Processing (This Script)
```bash
bash process_content.sh
# OR
bash run.sh
# Select option 6
```

This creates:
- `00-foundations/02-planets.md` - Structured learning document
- `00-foundations/03-houses.md` - Structured learning document
- `00-foundations/04-nakshatras.md` - Structured learning document
- `00-foundations/05-aspects.md` - Structured learning document

## Document Structure

Each generated document follows this structure:

### 1. Header & Metadata
- Title and learning phase
- Status and last updated date
- Source books referenced

### 2. Learning Objectives
- Clear goals for the document
- What you'll be able to do after reading

### 3. Introduction
- Context and importance
- Overview of the topic
- Why it matters for chart reading

### 4. Classical Principles
- Direct quotes from source texts
- Sutras and principles from BPHS, Brihat Jataka, etc.
- Proper attribution with book, chapter, page

### 5. Modern Application
- Step-by-step analysis methods
- How to apply in practice
- Common mistakes to avoid
- Practical tips

### 6. Practice Exercises
- Hands-on exercises
- Chart analysis tasks
- Skill-building activities
- Comparative analysis

### 7. Personal Chart Application
- Apply to your own chart
- Step-by-step guidance
- Learning checkpoints
- Questions to answer

### 8. Summary
- Key takeaways
- Next steps
- Related documents
- Further study resources

## Customization

### Adding More Documents

Edit `content_processor.py` and add to `document_structure`:

```python
self.document_structure = {
    "foundations": {
        "02-planets.md": {...},
        "03-houses.md": {...},
        # Add more here
    },
    "marriage": {
        "01-7th-house-analysis.md": {...},
        # Add marriage documents
    }
}
```

### Modifying Templates

Each section has a template function:
- `create_introduction()` - Customize intro text
- `create_modern_application()` - Add application guidelines
- `create_practice_exercises()` - Add exercises
- `create_personal_chart_section()` - Customize chart application

### Adding More Topics

The processor searches for relevant content based on topics:

```python
"02-planets.md": {
    "topics": ["planets", "planetary characteristics", "benefics", "malefics"],
    # Add more search terms
}
```

## Current Status

### Completed
✅ Foundation documents (4 documents)
- 02-planets.md
- 03-houses.md
- 04-nakshatras.md
- 05-aspects.md

### To Be Added
⚪ Marriage documents (6 documents)
⚪ Career documents (4 documents)
⚪ Finance documents (4 documents)
⚪ Children documents (4 documents)
⚪ Health documents (4 documents)
⚪ Dasha documents (5 documents)
⚪ Transit documents (5 documents)
⚪ Divisional chart documents (6 documents)
⚪ Yoga documents (5 documents)
⚪ Remedy documents (4 documents)

## Next Steps

1. **Review Generated Documents**
   - Check 00-foundations/ folder
   - Read through each document
   - Verify content quality

2. **Enhance Content**
   - Add more classical references
   - Expand modern application sections
   - Add more practice exercises
   - Include real chart examples

3. **Expand to Other Topics**
   - Add marriage document templates
   - Add career document templates
   - Continue through MASTER_PLAN phases

4. **Apply to Your Chart**
   - Complete practice exercises
   - Apply to your birth chart
   - Track predictions and insights

## Integration with MASTER_PLAN

This processor aligns with the MASTER_PLAN by:

1. **Following the Structure**
   - Documents match MASTER_PLAN naming
   - Content follows quality standards
   - Includes all required sections

2. **Supporting Learning Goals**
   - Theory + Practice + Application
   - Classical + Modern synthesis
   - Personal chart integration

3. **Enabling Progress Tracking**
   - Clear document completion
   - Practice exercises for validation
   - Learning checkpoints

## Technical Details

### Requirements
- Python 3.7+
- JSON extraction files in `extracted_content/`
- Write access to parent directory

### File Locations
- Script: `extraction-system/content_processor.py`
- Input: `extracted_content/*_extraction.json`
- Output: `00-foundations/*.md` (and other folders)

### Error Handling
- Skips None/empty chapters
- Handles missing fields gracefully
- Continues on individual document errors
- Reports all errors at end

## Troubleshooting

### "No extracted content found"
Run extraction first:
```bash
bash run.sh
# Select option 2 (Tier 1)
```

### "No extraction JSON files found"
Check that extraction completed successfully:
```bash
ls -la ../extracted_content/*.json
```

### Documents not generated
Check Python errors in output and verify:
- JSON files are valid
- Write permissions exist
- Python version is 3.7+

## Future Enhancements

1. **AI Enhancement** (Optional)
   - Use LLM to expand explanations
   - Generate more examples
   - Create better exercises

2. **Cross-Referencing**
   - Auto-link related documents
   - Create topic index
   - Build knowledge graph

3. **Quality Validation**
   - Check completeness
   - Verify classical references
   - Validate examples

4. **Interactive Elements**
   - Chart calculation tools
   - Interactive exercises
   - Progress tracking

---

**Created**: February 21, 2026  
**Last Updated**: February 21, 2026  
**Status**: Active Development
