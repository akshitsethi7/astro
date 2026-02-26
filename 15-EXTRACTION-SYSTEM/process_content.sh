#!/bin/bash
# Process extracted content into structured learning documents

PYTHON="../../venv/bin/python3"

echo "=========================================="
echo "  Content Processor"
echo "  Transform Raw Extractions → Learning Documents"
echo "=========================================="
echo ""

# Check if Python is available
if [ ! -f "$PYTHON" ]; then
    echo "ERROR: Python not found at $PYTHON"
    echo "Please ensure the venv exists at astro/venv/"
    exit 1
fi

echo "Using Python from: $PYTHON"
$PYTHON --version
echo ""

# Check if extractions exist
if [ ! -d "../extracted_content" ]; then
    echo "ERROR: No extracted content found!"
    echo "Please run extraction first (option 1-5 in run.sh)"
    exit 1
fi

# Count extraction files
extraction_count=$(ls -1 ../extracted_content/*_extraction.json 2>/dev/null | wc -l)
echo "Found $extraction_count book extractions"
echo ""

if [ $extraction_count -eq 0 ]; then
    echo "ERROR: No extraction JSON files found!"
    echo "Please run extraction first (option 1-5 in run.sh)"
    exit 1
fi

echo "Processing content into structured learning documents..."
echo ""

$PYTHON content_processor.py

echo ""
echo "=========================================="
echo "  Processing Complete!"
echo "=========================================="
echo ""
echo "Generated documents:"
echo "  - 00-foundations/02-planets.md"
echo "  - 00-foundations/03-houses.md"
echo "  - 00-foundations/04-nakshatras.md"
echo "  - 00-foundations/05-aspects.md"
echo ""
echo "Next steps:"
echo "  1. Review generated documents"
echo "  2. Complete practice exercises"
echo "  3. Apply to your personal chart"
echo "  4. Continue with next phase of MASTER_PLAN"
echo ""
