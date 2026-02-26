#!/bin/bash
# Simple runner that uses the astro venv

PYTHON="../../venv/bin/python3"

echo "=========================================="
echo "  Vedic Astrology Content Extractor"
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

# Check Books directory
if [ -d "../../../Books" ]; then
    echo "✓ Books directory found (workspace folder)"
elif [ -d "../../Books" ]; then
    echo "✓ Books directory found"
else
    echo "⚠ Warning: Books directory not found at expected location"
    echo "  Will attempt to locate during extraction"
fi
echo ""

# Show menu
echo "Select extraction tier:"
echo "  1) Test system first (recommended)"
echo "  2) Tier 1 - Foundation Texts (10 books, ~15 min)"
echo "  3) Tier 2 - Foundation + Modern Masters (15 books, ~25 min)"
echo "  4) Tier 3 - Foundation + Modern + Specialized (20 books, ~35 min)"
echo "  5) All Books (45 books, ~90 min)"
echo "  6) Process extracted content into learning documents"
echo "  7) Exit"
echo ""
read -p "Enter choice [1-7]: " choice

case $choice in
    1)
        echo ""
        echo "Running test..."
        $PYTHON test_extraction.py
        ;;
    2)
        echo ""
        echo "Processing Tier 1: Foundation Texts..."
        $PYTHON run_extraction.py --tier 1
        ;;
    3)
        echo ""
        echo "Processing Tier 2: Foundation + Modern Masters..."
        $PYTHON run_extraction.py --tier 2
        ;;
    4)
        echo ""
        echo "Processing Tier 3: Foundation + Modern + Specialized..."
        $PYTHON run_extraction.py --tier 3
        ;;
    5)
        echo ""
        echo "Processing All Books..."
        $PYTHON run_extraction.py
        ;;
    6)
        echo ""
        echo "Processing extracted content into learning documents..."
        $PYTHON content_processor.py
        ;;
    7)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid choice. Exiting..."
        exit 1
        ;;
esac

echo ""
echo "=========================================="
echo "  Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "  1. Review ../MASTER_INDEX.md for book summaries"
echo "  2. Review ../TOPIC_INDEX.md for topic coverage"
echo "  3. Read generated documents in topic folders"
echo "  4. Run option 6 to process into learning documents"
echo ""
