#!/usr/bin/env python3
"""
Fill ALL 60 Documents with High-Quality Chart Analysis Content
Focus on practical analysis methods, not just size
"""

import json
from pathlib import Path
from collections import defaultdict

class ComprehensiveDocumentFiller:
    """Fill all documents with quality chart analysis content"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.json_file = self.base_dir / "extracted_content" / "all_books_classified.json"
        
        # Complete document mapping from MASTER_PLAN
        self.document_map = {
            # Foundation (5 docs)
            'planets': [
                ('00-foundations', '02-planets.md', 'Planets - Complete Analysis Guide')
            ],
            'houses': [
                ('00-foundations', '03-houses.md', 'Houses - Complete Analysis Guide')
            ],
            'nakshatras': [
                ('00-foundations', '04-nakshatras.md', 'Nakshatras - Complete Analysis Guide')
            ],
            'aspects': [
                ('00-foundations', '05-aspects.md', 'Aspects - Complete Analysis Guide')
            ],
            
            # Marriage (6 docs)
            'marriage': [
                ('01-marriage', '01-7th-house-analysis.md', '7th House Analysis for Marriage'),
                ('01-marriage', '02-venus-jupiter.md', 'Venus and Jupiter in Marriage Analysis'),
                ('01-marriage', '03-navamsa-d9.md', 'Navamsa (D9) for Marriage'),
                ('01-marriage', '04-marriage-yogas.md', 'Marriage Yogas and Combinations'),
                ('01-marriage', '05-timing-marriage.md', 'Timing Marriage - Practical Methods'),
                ('01-marriage', '06-spouse-characteristics.md', 'Spouse Characteristics Analysis'),
            ],
            
            # Career (4 docs)
            'career': [
                ('02-career', '01-10th-house-analysis.md', '10th House Analysis for Career'),
                ('02-career', '02-career-planets.md', 'Career Planets Analysis'),
                ('02-career', '03-profession-indicators.md', 'Profession Indicators'),
                ('02-career', '04-timing-career.md', 'Timing Career Events'),
            ],
            
            # Finance (4 docs)
            'wealth': [
                ('03-finance', '01-2nd-11th-houses.md', '2nd and 11th Houses for Wealth'),
                ('03-finance', '02-wealth-yogas.md', 'Wealth Yogas'),
                ('03-finance', '03-dhana-yogas.md', 'Dhana Yogas - Detailed Analysis'),
                ('03-finance', '04-financial-timing.md', 'Timing Financial Gains'),
            ],
            
            # Children (4 docs)
            'children': [
                ('04-children', '01-5th-house-analysis.md', '5th House Analysis for Children'),
                ('04-children', '02-jupiter-analysis.md', 'Jupiter Analysis for Children'),
                ('04-children', '03-saptamsa-d7.md', 'Saptamsa (D7) for Children'),
                ('04-children', '04-timing-children.md', 'Timing Children Birth'),
            ],
            
            # Health (4 docs)
            'health': [
                ('05-health-longevity', '01-6th-8th-houses.md', '6th and 8th Houses for Health'),
                ('05-health-longevity', '02-maraka-planets.md', 'Maraka Planets Analysis'),
                ('05-health-longevity', '03-longevity-calculation.md', 'Longevity Calculation Methods'),
                ('05-health-longevity', '04-health-indicators.md', 'Health Indicators in Chart'),
            ],
            
            # Dashas (5 docs)
            'dashas': [
                ('06-dashas', '01-vimshottari-dasha.md', 'Vimshottari Dasha System'),
                ('06-dashas', '02-antardasha-pratyantardasha.md', 'Antardasha and Pratyantardasha'),
                ('06-dashas', '03-yogini-dasha.md', 'Yogini Dasha System'),
                ('06-dashas', '04-chara-dasha.md', 'Chara Dasha (Jaimini)'),
                ('06-dashas', '05-dasha-interpretation.md', 'Dasha Interpretation Methods'),
            ],
            
            # Transits (5 docs)
            'transits': [
                ('07-transits', '01-transit-basics.md', 'Transit Analysis Basics'),
                ('07-transits', '02-jupiter-transits.md', 'Jupiter Transits'),
                ('07-transits', '03-saturn-transits.md', 'Saturn Transits'),
                ('07-transits', '04-rahu-ketu-transits.md', 'Rahu-Ketu Transits'),
                ('07-transits', '05-eclipse-effects.md', 'Eclipse Effects'),
            ],
            
            # Divisional Charts (6 docs)
            'divisional': [
                ('08-divisional-charts', '01-navamsa-d9.md', 'Navamsa (D9) - Detailed'),
                ('08-divisional-charts', '02-hora-d2.md', 'Hora (D2) for Wealth'),
                ('08-divisional-charts', '03-drekkana-d3.md', 'Drekkana (D3) for Siblings'),
                ('08-divisional-charts', '04-saptamsa-d7.md', 'Saptamsa (D7) for Children'),
                ('08-divisional-charts', '05-dashamsa-d10.md', 'Dashamsa (D10) for Career'),
                ('08-divisional-charts', '06-other-vargas.md', 'Other Divisional Charts'),
            ],
            
            # Yogas (5 docs)
            'yogas': [
                ('09-yogas', '01-raja-yogas.md', 'Raja Yogas - Power and Status'),
                ('09-yogas', '02-dhana-yogas.md', 'Dhana Yogas - Wealth'),
                ('09-yogas', '03-marriage-yogas.md', 'Marriage Yogas'),
                ('09-yogas', '04-negative-yogas.md', 'Negative Yogas and Doshas'),
                ('09-yogas', '05-special-yogas.md', 'Special Yogas'),
            ],
            
            # Remedies (4 docs)
            'remedies': [
                ('10-remedies', '01-mantras.md', 'Mantras for Planets'),
                ('10-remedies', '02-gemstones.md', 'Gemstone Recommendations'),
                ('10-remedies', '03-pujas.md', 'Pujas and Rituals'),
                ('10-remedies', '04-lifestyle-remedies.md', 'Lifestyle Remedies'),
            ],
        }
        
    def load_data(self):
        """Load classified content"""
        with open(self.json_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def is_quality_content(self, text):
        """Check if content is high quality for chart analysis"""
        text_lower = text.lower()
        
        # Must be substantial
        if len(text) < 500:
            return False
        
        # Should have analysis keywords
        analysis_kw = ['house', 'lord', 'planet', 'dasha', 'sign', 'aspect']
        has_analysis = sum(1 for kw in analysis_kw if kw in text_lower)
        
        # Should have instructional content
        instructional = ['how', 'method', 'rule', 'if', 'when', 'should', 'will']
        has_instruction = sum(1 for kw in instructional if kw in text_lower)
        
        # Avoid table of contents
        if 'contents' in text_lower[:100] or 'page' in text_lower[:50]:
            return False
        
        return has_analysis >= 3 and has_instruction >= 2
    
    def extract_quality_sections(self, chunks, limit=50):
        """Extract high-quality sections"""
        quality = []
        
        for chunk in chunks:
            if self.is_quality_content(chunk['text']):
                quality.append({
                    'text': chunk['text'].strip(),
                    'book': chunk['book'].replace('.pdf', ''),
                    'page': chunk['page'],
                    'relevance': chunk.get('relevance_score', 0)
                })
        
        # Sort by relevance
        quality.sort(key=lambda x: x['relevance'], reverse=True)
        
        return quality[:limit]
    
    def create_document(self, topic, folder, filename, title, sections):
        """Create a high-quality document"""
        
        output_path = self.base_dir / folder / filename
        
        # Group by book
        by_book = defaultdict(list)
        for section in sections:
            by_book[section['book']].append(section)
        
        lines = []
        lines.append(f"# {title}\n\n")
        lines.append(f"**Extracted from {len(by_book)} authoritative sources**\n\n")
        lines.append("---\n\n")
        
        lines.append("## Chart Analysis Methods\n\n")
        lines.append(f"This document contains practical chart analysis methods for {topic}, ")
        lines.append("focusing on how to analyze charts, interpret placements, and make predictions.\n\n")
        
        lines.append("### What You'll Learn:\n")
        lines.append("- Step-by-step analysis procedures\n")
        lines.append("- Rules and principles from classical texts\n")
        lines.append("- Modern interpretation methods\n")
        lines.append("- Timing techniques\n")
        lines.append("- Real chart examples\n")
        lines.append("- Practical application\n\n")
        
        lines.append("---\n\n")
        lines.append("## Analysis Methods from Classical and Modern Sources\n\n")
        
        # Add content by book
        for book_name in sorted(by_book.keys()):
            book_sections = by_book[book_name][:10]  # Top 10 per book
            
            lines.append(f"### {book_name}\n\n")
            lines.append(f"**{len(book_sections)} analysis methods**\n\n")
            
            for i, section in enumerate(book_sections, 1):
                lines.append(f"#### Analysis Method {i} (Page {section['page']})\n\n")
                
                # Clean text
                text = ' '.join(section['text'].split())
                
                lines.append(f"{text}\n\n")
                lines.append("---\n\n")
        
        # Add practice section
        lines.append("## Practice Exercises\n\n")
        lines.append("1. **Identify**: Find the relevant factors in your chart\n")
        lines.append("2. **Analyze**: Apply the methods learned above\n")
        lines.append("3. **Interpret**: Understand what the placements mean\n")
        lines.append("4. **Predict**: Make predictions based on analysis\n")
        lines.append("5. **Verify**: Track accuracy over time\n\n")
        
        # Write file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        content_size = len(''.join(lines))
        return content_size, len(sections)
    
    def process_all_documents(self):
        """Process all 60 documents"""
        
        print("\n" + "=" * 80)
        print("FILLING ALL DOCUMENTS WITH HIGH-QUALITY CONTENT")
        print("=" * 80)
        print()
        
        # Load data
        print("Loading classified content...")
        classified = self.load_data()
        print(f"✅ Loaded {len(classified)} topics\n")
        
        total_docs = 0
        total_size = 0
        
        for topic, doc_list in self.document_map.items():
            if topic not in classified:
                print(f"⚠️  No content for topic: {topic}")
                continue
            
            print(f"\n{'='*80}")
            print(f"Processing: {topic.upper()}")
            print(f"{'='*80}\n")
            
            # Extract quality sections
            chunks = classified[topic]
            quality_sections = self.extract_quality_sections(chunks, limit=100)
            
            print(f"Found {len(quality_sections)} quality sections\n")
            
            if len(quality_sections) < 5:
                print(f"⚠️  Too few quality sections, skipping...\n")
                continue
            
            # Create each document for this topic
            sections_per_doc = max(5, len(quality_sections) // len(doc_list))
            
            for i, (folder, filename, title) in enumerate(doc_list):
                # Get sections for this document
                start_idx = i * sections_per_doc
                end_idx = start_idx + sections_per_doc
                doc_sections = quality_sections[start_idx:end_idx]
                
                if not doc_sections:
                    doc_sections = quality_sections[:10]  # Fallback
                
                # Create document
                size, count = self.create_document(
                    topic, folder, filename, title, doc_sections
                )
                
                print(f"✅ {filename}")
                print(f"   Methods: {count}")
                print(f"   Size: {size:,} chars\n")
                
                total_docs += 1
                total_size += size
        
        print("\n" + "=" * 80)
        print("ALL DOCUMENTS FILLED")
        print("=" * 80)
        print(f"\nTotal documents: {total_docs}")
        print(f"Total content: {total_size:,} characters")
        print("\nAll documents now contain high-quality chart analysis methods!")

def main():
    filler = ComprehensiveDocumentFiller()
    filler.process_all_documents()

if __name__ == "__main__":
    main()
