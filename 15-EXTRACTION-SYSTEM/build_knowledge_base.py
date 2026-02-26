#!/usr/bin/env python3
"""
Build High-Quality Knowledge Base
Reads extracted content and creates comprehensive, well-structured documents
with actual teachings, principles, and practical knowledge
"""

import json
import os
from pathlib import Path
from collections import defaultdict

def load_extracted_content():
    """Load the classified content"""
    base_dir = Path(__file__).parent.parent
    json_file = base_dir / "extracted_content" / "all_books_classified.json"
    
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_content_quality(classified_data):
    """Analyze what we actually have"""
    
    print("=" * 80)
    print("CONTENT QUALITY ANALYSIS")
    print("=" * 80)
    print()
    
    for topic, chunks in classified_data.items():
        print(f"\n{topic.upper()}")
        print("-" * 40)
        print(f"Total chunks: {len(chunks)}")
        
        # Analyze chunk quality
        substantial_chunks = [c for c in chunks if len(c['text']) > 500]
        print(f"Substantial chunks (>500 chars): {len(substantial_chunks)}")
        
        # Show sample
        if substantial_chunks:
            sample = substantial_chunks[0]
            print(f"\nSample from {sample['book']} (Page {sample['page']}):")
            print(f"{sample['text'][:300]}...")
        
        # Count unique books
        books = set(c['book'] for c in chunks)
        print(f"Unique books: {len(books)}")

def create_structured_document(topic, chunks, output_file):
    """Create a well-structured knowledge document"""
    
    # Filter for quality content
    quality_chunks = [c for c in chunks if len(c['text']) > 300]
    quality_chunks.sort(key=lambda x: x.get('relevance_score', 0), reverse=True)
    
    # Group by book
    by_book = defaultdict(list)
    for chunk in quality_chunks[:100]:  # Top 100 chunks
        by_book[chunk['book']].append(chunk)
    
    # Build document
    lines = []
    lines.append(f"# {topic.title()} - Knowledge Base\n")
    lines.append(f"**Compiled from {len(by_book)} authoritative sources**\n")
    lines.append(f"**{len(quality_chunks)} high-quality extractions**\n\n")
    
    lines.append("---\n\n")
    lines.append("## Overview\n\n")
    lines.append(f"This document contains comprehensive knowledge about {topic} ")
    lines.append(f"extracted from classical and modern Vedic astrology texts.\n\n")
    
    lines.append("---\n\n")
    lines.append("## Teachings by Source\n\n")
    
    # Add content by book
    for book_name in sorted(by_book.keys()):
        book_chunks = by_book[book_name][:15]  # Top 15 per book
        
        lines.append(f"### {book_name.replace('.pdf', '')}\n\n")
        lines.append(f"**{len(book_chunks)} key sections**\n\n")
        
        for i, chunk in enumerate(book_chunks, 1):
            lines.append(f"#### Extract {i} - Page {chunk['page']}\n\n")
            
            # Clean and format text
            text = chunk['text'].strip()
            # Remove excessive whitespace
            text = ' '.join(text.split())
            
            lines.append(f"{text}\n\n")
            lines.append("---\n\n")
    
    # Write file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"✅ Created: {output_file}")
    print(f"   Size: {len(''.join(lines))} characters")
    print(f"   Books: {len(by_book)}")
    print(f"   Sections: {sum(len(chunks) for chunks in by_book.values())}\n")

def main():
    """Main execution"""
    
    print("\n" + "=" * 80)
    print("BUILDING HIGH-QUALITY KNOWLEDGE BASE")
    print("=" * 80)
    print()
    
    # Load data
    print("Loading extracted content...")
    classified = load_extracted_content()
    print(f"✅ Loaded {len(classified)} topics\n")
    
    # Analyze quality
    analyze_content_quality(classified)
    
    print("\n" + "=" * 80)
    print("CREATING KNOWLEDGE DOCUMENTS")
    print("=" * 80)
    print()
    
    # Create documents
    base_dir = Path(__file__).parent.parent
    
    # Map topics to files
    topic_mapping = {
        'planets': ('00-foundations', '02-planets-KNOWLEDGE.md'),
        'houses': ('00-foundations', '03-houses-KNOWLEDGE.md'),
        'marriage': ('01-marriage', '00-MARRIAGE-KNOWLEDGE.md'),
        'career': ('02-career', '00-CAREER-KNOWLEDGE.md'),
        'wealth': ('03-finance', '00-WEALTH-KNOWLEDGE.md'),
        'children': ('04-children', '00-CHILDREN-KNOWLEDGE.md'),
        'health': ('05-health-longevity', '00-HEALTH-KNOWLEDGE.md'),
        'dashas': ('06-dashas', '00-DASHAS-KNOWLEDGE.md'),
        'yogas': ('09-yogas', '00-YOGAS-KNOWLEDGE.md'),
    }
    
    for topic, (folder, filename) in topic_mapping.items():
        if topic in classified:
            output_path = base_dir / folder / filename
            create_structured_document(topic, classified[topic], output_path)
    
    print("\n" + "=" * 80)
    print("KNOWLEDGE BASE CREATION COMPLETE")
    print("=" * 80)
    print("\nNew high-quality knowledge documents created with actual content!")
    print("These contain the real teachings extracted from the books.")

if __name__ == "__main__":
    main()
