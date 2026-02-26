#!/bin/bash
# Quick extraction script for Vedic Astrology books

echo "=========================================="
echo "  Vedic Astrology Content Extractor"
echo "=========================================="
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

echo "Python version:"
python3 --version
echo ""

# Show menu
echo "Select extraction tier:"
echo "  1) Tier 1 - Foundation Texts (10 books, ~15 min)"
echo "  2) Tier 2 - Foundation + Modern Masters (15 books, ~25 min)"
echo "  3) Tier 3 - Foundation + Modern + Specialized (20 books, ~35 min)"
echo "  4) All Books (45 books, ~90 min)"
echo "  5) Exit"
echo ""
read -p "Enter choice [1-5]: " choice

case $choice in
    1)
        echo ""
        echo "Processing Tier 1: Foundation Texts..."
        python3 run_extraction.py --tier 1
        ;;
    2)
        echo ""
        echo "Processing Tier 2: Foundation + Modern Masters..."
        python3 run_extraction.py --tier 2
        ;;
    3)
        echo ""
        echo "Processing Tier 3: Foundation + Modern + Specialized..."
        python3 run_extraction.py --tier 3
        ;;
    4)
        echo ""
        echo "Processing All Books..."
        python3 run_extraction.py
        ;;
    5)
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
echo "  Extraction Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "  1. Review MASTER_INDEX.md for book summaries"
echo "  2. Review TOPIC_INDEX.md for topic coverage"
echo "  3. Read generated documents in topic folders"
echo "  4. Cross-reference with original PDFs"
echo ""
