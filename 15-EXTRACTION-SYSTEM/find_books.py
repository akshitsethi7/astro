#!/usr/bin/env python3
"""Find the Books directory"""

from pathlib import Path

script_dir = Path(__file__).parent
print(f"Script directory: {script_dir.resolve()}")

# Try different paths
paths_to_try = [
    script_dir.parent.parent.parent / "Books",  # Sibling workspace
    script_dir.parent.parent / "Books",  # Under parent
    Path("/Users/akshitsethi/Desktop/Books"),  # Absolute
    Path.home() / "Desktop" / "Books",  # Home relative
]

for path in paths_to_try:
    print(f"\nTrying: {path}")
    print(f"  Resolved: {path.resolve()}")
    print(f"  Exists: {path.exists()}")
    if path.exists():
        pdf_count = len(list(path.glob("*.pdf")))
        print(f"  ✓ FOUND! Contains {pdf_count} PDF files")
        print(f"\n  Use this path: {path.resolve()}")
        break
else:
    print("\n✗ Books directory not found in any expected location")
