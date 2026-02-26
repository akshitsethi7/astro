#!/bin/bash
# Generate all phase documents with high quality

PYTHON="../../venv/bin/python3"

echo "=========================================="
echo "  Complete Phase Generator"
echo "  Generating ALL Learning Documents"
echo "=========================================="
echo ""
echo "This will generate 60+ comprehensive documents"
echo "covering all phases of the MASTER_PLAN:"
echo ""
echo "  Phase 1: Foundation (5 docs) ✅"
echo "  Phase 2: Life Areas (22 docs)"
echo "  Phase 3: Timing (10 docs)"
echo "  Phase 4: Advanced (15 docs)"
echo "  Phase 5: Practical (7 docs)"
echo ""
echo "Total: 59 documents"
echo ""
read -p "Continue? (y/n): " confirm

if [ "$confirm" != "y" ]; then
    echo "Cancelled."
    exit 0
fi

echo ""
echo "Generating all documents..."
echo ""

$PYTHON << 'PYTHON_SCRIPT'
import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Import and run the comprehensive generator
exec(open('comprehensive_generator.py').read())
PYTHON_SCRIPT

echo ""
echo "=========================================="
echo "  Generation Complete!"
echo "=========================================="
echo ""
echo "Generated documents in:"
echo "  - 00-foundations/ (5 docs)"
echo "  - 01-marriage/ (6 docs)"
echo "  - 02-career/ (4 docs)"
echo "  - 03-finance/ (4 docs)"
echo "  - 04-children/ (4 docs)"
echo "  - 05-health-longevity/ (4 docs)"
echo "  - 06-dashas/ (5 docs)"
echo "  - 07-transits/ (5 docs)"
echo "  - 08-divisional-charts/ (6 docs)"
echo "  - 09-yogas/ (5 docs)"
echo "  - 10-remedies/ (4 docs)"
echo "  - 11-case-studies/ (3 docs)"
echo "  - 12-reference/ (4 docs)"
echo ""
