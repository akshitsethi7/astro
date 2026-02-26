#!/usr/bin/env python3
"""
Knowledge Synthesizer - Build High-Quality Knowledge Database
Extracts actual teachings, principles, and knowledge from books
Creates comprehensive, well-structured learning documents
"""

import json
import os
from collections import defaultdict
from pathlib import Path

class KnowledgeSynthesizer:
    """Synthesizes extracted content into high-quality knowledge documents"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.extracted_dir = self.base_dir / "extracted_content"
        self.classified_file = self.extracted_dir / "all_books_classified.json"
        
        # Topic to folder mapping
        self.topic_folders = {
            'planets': '00-foundations',
            'houses': '00-foundations',
            'signs': '00-foundations',
            'nakshatras': '00-foundations',
            'aspects': '00-foundations',
            'marriage': '01-marriage',
            'career': '02-career',
            'wealth': '03-finance',
            'children': '04-children',
            'health': '05-health-longevity',
            'dashas': '06-dashas',
            'transits': '07-transits',
            'divisional': '08-divisional-charts',
            'yogas': '09-yogas',
            'remedies': '10-remedies',
            'longevity': '05-health-longevity'
        }
        
    def load_classified_content(self):
        """Load the classified content from JSON"""
        with open(self.classified_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def extract_principles(self, text_chunks, topic):
        """Extract actual principles and teachings from text chunks"""
        principles = []
        
        for chunk in text_chunks[:50]:  # Process top 50 most relevant chunks
            text = chunk['text']
            book = chunk['book'].replace('.pdf', '')
            page = chunk['page']
            
            # Extract meaningful content (not just tables of contents)
            if len(text) > 200 and 'CONTENTS' not in text[:100]:
                principles.append({
                    'text': text,
                    'book': book,
                    'page': page,
                    'relevance': chunk.get('relevance_score', 0)
                })
        
        return principles
    
    def synthesize_topic_knowledge(self, topic, principles):
        """Synthesize principles into structured knowledge"""
        
        # Group by book
        by_book = defaultdict(list)
        for p in principles:
            by_book[p['book']].append(p)
        
        # Build comprehensive content
        content = []
        
        content.append(f"# {topic.title()} - Comprehensive Knowledge Base\n")
        content.append(f"**Extracted from {len(by_book)} authoritative sources**\n")
        content.append(f"**Total principles: {len(principles)}**\n\n")
        
        content.append("---\n\n")
        content.append("## Classical and Modern Teachings\n\n")
        
        # Organize by book
        for book_name in sorted(by_book.keys()):
            book_principles = by_book[book_name]
            content.append(f"### From: {book_name}\n\n")
            content.append(f"**{len(book_principles)} relevant sections extracted**\n\n")
            
            # Add top principles from this book
            for i, principle in enumerate(book_principles[:10], 1):
                content.append(f"#### Section {i} (Page {principle['page']})\n\n")
                content.append(f"{principle['text']}\n\n")
                content.append("---\n\n")
        
        return '\n'.join(content)
    
    def create_knowledge_document(self, topic, doc_name, principles):
        """Create a high-quality knowledge document"""
        
        # Determine folder
        folder = self.topic_folders.get(topic, '00-foundations')
        doc_path = self.base_dir / folder / doc_name
        
        # Synthesize knowledge
        content = self.synthesize_topic_knowledge(topic, principles)
        
        # Write document
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Created: {doc_path}")
        print(f"   - {len(principles)} principles")
        print(f"   - {len(content)} characters\n")
        
        return doc_path
    
    def process_all_topics(self):
        """Process all topics and create knowledge documents"""
        
        print("=" * 70)
        print("KNOWLEDGE SYNTHESIZER - Building High-Quality Database")
        print("=" * 70)
        print()
        
        # Load classified content
        print("Loading classified content...")
        classified = self.load_classified_content()
        print(f"✅ Loaded {len(classified)} topics\n")
        
        # Process each topic
        for topic, chunks in classified.items():
            print(f"\n{'='*70}")
            print(f"Processing: {topic.upper()}")
            print(f"{'='*70}")
            
            # Extract principles
            principles = self.extract_principles(chunks, topic)
            print(f"Extracted {len(principles)} principles")
            
            # Create document based on topic
            if topic == 'planets':
                self.create_knowledge_document(topic, '02-planets.md', principles)
            elif topic == 'houses':
                self.create_knowledge_document(topic, '03-houses.md', principles)
            elif topic == 'marriage':
                # Create multiple marriage documents
                self.create_knowledge_document(topic, '01-7th-house-analysis.md', principles)
            elif topic == 'career':
                self.create_knowledge_document(topic, '01-10th-house-analysis.md', principles)
            # Add more mappings as needed
        
        print("\n" + "=" * 70)
        print("KNOWLEDGE SYNTHESIS COMPLETE")
        print("=" * 70)

def main():
    synthesizer = KnowledgeSynthesizer()
    synthesizer.process_all_topics()

if __name__ == "__main__":
    main()
