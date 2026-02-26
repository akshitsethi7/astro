#!/usr/bin/env python3
"""
Extract Chart Analysis Methods from Books
Focus on HOW TO ANALYZE CHARTS, not just general content
"""

import json
import re
from pathlib import Path
from collections import defaultdict

class ChartAnalysisExtractor:
    """Extract practical chart analysis methods from books"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.json_file = self.base_dir / "extracted_content" / "all_books_classified.json"
        
        # Keywords that indicate chart analysis methods
        self.analysis_keywords = [
            'how to', 'method', 'step', 'analyze', 'analysis', 'judge', 'examine',
            'consider', 'note', 'observe', 'find out', 'calculate', 'determine',
            'ascertain', 'identify', 'check', 'see', 'look at', 'study',
            'rule', 'principle', 'if', 'when', 'should', 'must', 'will',
            'house', 'lord', 'planet', 'sign', 'aspect', 'dasha', 'cusp',
            'significator', 'sub-lord', 'constellation', 'nakshatra',
            'example', 'case', 'chart', 'horoscope', 'native'
        ]
        
    def load_data(self):
        """Load classified content"""
        with open(self.json_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def is_analysis_content(self, text):
        """Check if text contains chart analysis methods"""
        text_lower = text.lower()
        
        # Must have analysis keywords
        has_keywords = sum(1 for kw in self.analysis_keywords if kw in text_lower)
        
        # Should have technical terms
        technical_terms = ['house', 'lord', 'planet', 'dasha', 'cusp', 'aspect']
        has_technical = sum(1 for term in technical_terms if term in text_lower)
        
        # Should have instructional language
        instructional = ['how to', 'method', 'step', 'rule', 'if', 'when', 'should']
        has_instructional = sum(1 for inst in instructional if inst in text_lower)
        
        # Scoring
        score = has_keywords + (has_technical * 2) + (has_instructional * 3)
        
        return score >= 8
    
    def extract_analysis_sections(self, chunks):
        """Extract only sections about chart analysis"""
        analysis_sections = []
        
        for chunk in chunks:
            text = chunk['text']
            
            # Filter for analysis content
            if len(text) > 400 and self.is_analysis_content(text):
                analysis_sections.append({
                    'text': text,
                    'book': chunk['book'].replace('.pdf', ''),
                    'page': chunk['page'],
                    'relevance': chunk.get('relevance_score', 0)
                })
        
        # Sort by relevance
        analysis_sections.sort(key=lambda x: x['relevance'], reverse=True)
        
        return analysis_sections
    
    def create_analysis_document(self, topic, sections, output_file):
        """Create document focused on chart analysis methods"""
        
        # Group by book
        by_book = defaultdict(list)
        for section in sections[:80]:  # Top 80 analysis sections
            by_book[section['book']].append(section)
        
        lines = []
        lines.append(f"# {topic.title()} - Chart Analysis Methods\n\n")
        lines.append(f"**Practical techniques extracted from {len(by_book)} authoritative sources**\n\n")
        lines.append("---\n\n")
        
        lines.append("## How to Analyze Charts\n\n")
        lines.append(f"This document contains practical chart analysis methods for {topic}, ")
        lines.append("extracted from classical and modern Vedic astrology texts.\n\n")
        
        lines.append("### Focus Areas:\n")
        lines.append("- Step-by-step analysis methods\n")
        lines.append("- Rules and principles for interpretation\n")
        lines.append("- Calculation techniques\n")
        lines.append("- Prediction methods\n")
        lines.append("- Real chart examples\n\n")
        
        lines.append("---\n\n")
        lines.append("## Analysis Methods by Source\n\n")
        
        # Add content by book
        for book_name in sorted(by_book.keys()):
            book_sections = by_book[book_name][:12]  # Top 12 per book
            
            lines.append(f"### {book_name}\n\n")
            lines.append(f"**{len(book_sections)} analysis methods**\n\n")
            
            for i, section in enumerate(book_sections, 1):
                lines.append(f"#### Method {i} - Page {section['page']}\n\n")
                
                # Clean text
                text = section['text'].strip()
                text = ' '.join(text.split())
                
                lines.append(f"{text}\n\n")
                lines.append("---\n\n")
        
        # Write file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        content_size = len(''.join(lines))
        print(f"✅ {output_file.name}")
        print(f"   Size: {content_size:,} chars")
        print(f"   Books: {len(by_book)}")
        print(f"   Methods: {sum(len(s) for s in by_book.values())}\n")
        
        return content_size
    
    def process_all_topics(self):
        """Process all topics and create analysis documents"""
        
        print("\n" + "=" * 80)
        print("EXTRACTING CHART ANALYSIS METHODS")
        print("=" * 80)
        print()
        
        # Load data
        print("Loading classified content...")
        classified = self.load_data()
        print(f"✅ Loaded {len(classified)} topics\n")
        
        # Topic to file mapping
        topic_files = {
            'planets': ('00-foundations', '02-planets-ANALYSIS.md'),
            'houses': ('00-foundations', '03-houses-ANALYSIS.md'),
            'marriage': ('01-marriage', '01-marriage-analysis-methods.md'),
            'career': ('02-career', '01-career-analysis-methods.md'),
            'wealth': ('03-finance', '01-wealth-analysis-methods.md'),
            'children': ('04-children', '01-children-analysis-methods.md'),
            'health': ('05-health-longevity', '01-health-analysis-methods.md'),
            'dashas': ('06-dashas', '01-dasha-analysis-methods.md'),
            'transits': ('07-transits', '01-transit-analysis-methods.md'),
            'yogas': ('09-yogas', '01-yoga-analysis-methods.md'),
        }
        
        total_size = 0
        total_methods = 0
        
        for topic, (folder, filename) in topic_files.items():
            if topic not in classified:
                continue
            
            print(f"\n{'='*80}")
            print(f"Processing: {topic.upper()}")
            print(f"{'='*80}\n")
            
            # Extract analysis sections
            chunks = classified[topic]
            analysis_sections = self.extract_analysis_sections(chunks)
            
            print(f"Found {len(analysis_sections)} analysis sections")
            
            if len(analysis_sections) < 10:
                print(f"⚠️  Too few analysis sections, skipping...\n")
                continue
            
            # Create document
            output_path = self.base_dir / folder / filename
            size = self.create_analysis_document(topic, analysis_sections, output_path)
            
            total_size += size
            total_methods += len(analysis_sections)
        
        print("\n" + "=" * 80)
        print("CHART ANALYSIS EXTRACTION COMPLETE")
        print("=" * 80)
        print(f"\nTotal content: {total_size:,} characters")
        print(f"Total methods: {total_methods}")
        print("\nDocuments focus on HOW TO ANALYZE CHARTS")

def main():
    extractor = ChartAnalysisExtractor()
    extractor.process_all_topics()

if __name__ == "__main__":
    main()
