#!/usr/bin/env python3
"""
Topic-Based Content Organizer
Organizes extracted content by topic and creates structured markdown documents
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict


class TopicOrganizer:
    """Organize extracted content by topics"""
    
    def __init__(self, extraction_dir: str, output_dir: str):
        self.extraction_dir = Path(extraction_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Topic structure from MASTER_PLAN
        self.topic_structure = {
            'foundations': {
                'folder': '00-foundations',
                'topics': ['planets', 'houses', 'signs', 'nakshatras', 'aspects'],
                'priority': 1
            },
            'marriage': {
                'folder': '01-marriage',
                'topics': ['marriage', '7th house', 'venus', 'jupiter', 'navamsa'],
                'priority': 2
            },
            'career': {
                'folder': '02-career',
                'topics': ['career', '10th house', 'profession', 'occupation'],
                'priority': 2
            },
            'wealth': {
                'folder': '03-finance',
                'topics': ['wealth', 'money', 'finance', 'dhana', '2nd house', '11th house'],
                'priority': 2
            },
            'children': {
                'folder': '04-children',
                'topics': ['children', 'progeny', '5th house', 'putra'],
                'priority': 2
            },
            'health': {
                'folder': '05-health-longevity',
                'topics': ['health', 'disease', '6th house', 'longevity', 'maraka'],
                'priority': 2
            },
            'dashas': {
                'folder': '06-dashas',
                'topics': ['dasha', 'mahadasha', 'antardasha', 'vimshottari'],
                'priority': 3
            },
            'transits': {
                'folder': '07-transits',
                'topics': ['transit', 'gochara'],
                'priority': 3
            },
            'divisional': {
                'folder': '08-divisional-charts',
                'topics': ['divisional', 'varga', 'navamsa', 'D9', 'D10'],
                'priority': 4
            },
            'yogas': {
                'folder': '09-yogas',
                'topics': ['yoga', 'combination', 'raja yoga', 'dhana yoga'],
                'priority': 4
            },
            'remedies': {
                'folder': '10-remedies',
                'topics': ['remedy', 'upaya', 'mantra', 'gemstone'],
                'priority': 5
            }
        }
    
    def load_all_extractions(self) -> List[Dict]:
        """Load all extraction JSON files"""
        extractions = []
        json_files = list(self.extraction_dir.glob("*_extraction.json"))
        
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    extractions.append(data)
            except Exception as e:
                print(f"Error loading {json_file.name}: {e}")
        
        return extractions
    
    def organize_by_topic(self, extractions: List[Dict]) -> Dict:
        """Organize all content by topic"""
        organized = defaultdict(lambda: {
            'books': [],
            'total_pages': 0,
            'sutras': [],
            'examples': [],
            'page_references': []
        })
        
        for extraction in extractions:
            book_name = extraction['book_name']
            
            # Process topic pages
            for topic, pages in extraction.get('topic_pages', {}).items():
                if pages:
                    organized[topic]['books'].append(book_name)
                    organized[topic]['total_pages'] += len(pages)
                    organized[topic]['page_references'].extend([
                        {'book': book_name, 'page': p['page'], 'preview': p['preview']}
                        for p in pages
                    ])
            
            # Add sutras with topic tags
            for sutra in extraction.get('sutras', []):
                # Categorize sutra
                sutra_text = sutra['text'].lower()
                for topic in organized.keys():
                    if topic in sutra_text:
                        organized[topic]['sutras'].append({
                            'book': book_name,
                            'page': sutra['page'],
                            'text': sutra['text']
                        })
            
            # Add examples with topic tags
            for example in extraction.get('examples', []):
                example_text = example['text'].lower()
                for topic in organized.keys():
                    if topic in example_text:
                        organized[topic]['examples'].append({
                            'book': book_name,
                            'page': example['page'],
                            'text': example['text']
                        })
        
        return dict(organized)
    
    def create_topic_document(self, topic: str, content: Dict, category: str) -> str:
        """Create a comprehensive markdown document for a topic"""
        doc = []
        
        # Header
        doc.append(f"# {topic.title()} - Comprehensive Analysis\n")
        doc.append(f"**Category**: {category}\n")
        doc.append(f"**Sources**: {len(set(content['books']))} books\n")
        doc.append(f"**Total Pages**: {content['total_pages']}\n")
        doc.append(f"**Sutras Found**: {len(content['sutras'])}\n")
        doc.append(f"**Examples Found**: {len(content['examples'])}\n\n")
        
        # Source books
        doc.append("## Source Books\n\n")
        unique_books = sorted(set(content['books']))
        for book in unique_books:
            page_count = sum(1 for ref in content['page_references'] if ref['book'] == book)
            doc.append(f"- **{book}**: {page_count} pages\n")
        doc.append("\n")
        
        # Classical principles (sutras)
        if content['sutras']:
            doc.append("## Classical Principles & Sutras\n\n")
            doc.append("*Extracted from classical texts*\n\n")
            
            # Group by book
            sutras_by_book = defaultdict(list)
            for sutra in content['sutras']:
                sutras_by_book[sutra['book']].append(sutra)
            
            for book, sutras in sutras_by_book.items():
                doc.append(f"### From {book}\n\n")
                for i, sutra in enumerate(sutras[:10], 1):  # Limit to 10 per book
                    doc.append(f"**{i}. (Page {sutra['page']})**\n")
                    doc.append(f"{sutra['text']}\n\n")
        
        # Examples and case studies
        if content['examples']:
            doc.append("## Examples & Case Studies\n\n")
            
            examples_by_book = defaultdict(list)
            for example in content['examples']:
                examples_by_book[example['book']].append(example)
            
            for book, examples in examples_by_book.items():
                doc.append(f"### From {book}\n\n")
                for i, example in enumerate(examples[:5], 1):  # Limit to 5 per book
                    doc.append(f"**Example {i} (Page {example['page']})**\n")
                    doc.append(f"{example['text']}\n\n")
        
        # Page references for further study
        doc.append("## Page References for Deep Study\n\n")
        doc.append("*Refer to these pages in the original books for complete context*\n\n")
        
        # Group by book
        refs_by_book = defaultdict(list)
        for ref in content['page_references']:
            refs_by_book[ref['book']].append(ref)
        
        for book, refs in sorted(refs_by_book.items()):
            pages = sorted(set(ref['page'] for ref in refs))
            doc.append(f"**{book}**: Pages {', '.join(map(str, pages[:20]))}")
            if len(pages) > 20:
                doc.append(f" ... and {len(pages) - 20} more")
            doc.append("\n\n")
        
        # Practice exercises placeholder
        doc.append("## Practice Exercises\n\n")
        doc.append("*To be developed based on extracted principles*\n\n")
        doc.append("1. Identify this concept in your birth chart\n")
        doc.append("2. Analyze the strength and placement\n")
        doc.append("3. Make predictions based on classical principles\n")
        doc.append("4. Compare with actual life events\n\n")
        
        # Next steps
        doc.append("## Next Steps\n\n")
        doc.append("- Review all page references in source books\n")
        doc.append("- Study sutras in detail with commentary\n")
        doc.append("- Practice with example charts\n")
        doc.append("- Apply to personal chart analysis\n\n")
        
        doc.append("---\n")
        doc.append(f"*Extracted from {len(unique_books)} classical and modern texts*\n")
        
        return ''.join(doc)
    
    def generate_all_documents(self):
        """Generate all topic documents"""
        print("Loading extractions...")
        extractions = self.load_all_extractions()
        print(f"Loaded {len(extractions)} book extractions")
        
        print("\nOrganizing by topic...")
        organized = self.organize_by_topic(extractions)
        print(f"Organized into {len(organized)} topics")
        
        # Create documents by category
        for category, config in self.topic_structure.items():
            category_dir = self.output_dir / config['folder']
            category_dir.mkdir(parents=True, exist_ok=True)
            
            print(f"\nProcessing {category}...")
            
            # Find relevant topics
            for topic in config['topics']:
                if topic in organized:
                    content = organized[topic]
                    
                    # Create document
                    doc_content = self.create_topic_document(topic, content, category)
                    
                    # Save
                    filename = f"{topic.replace(' ', '-').replace('/', '-')}.md"
                    filepath = category_dir / filename
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(doc_content)
                    
                    print(f"  Created: {filepath.name} ({content['total_pages']} pages from {len(set(content['books']))} books)")
        
        # Create master topic index
        self.create_topic_index(organized)
    
    def create_topic_index(self, organized: Dict):
        """Create master index of all topics"""
        index_path = self.output_dir / "TOPIC_INDEX.md"
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write("# Topic Index - Organized Content\n\n")
            f.write("## All Topics by Coverage\n\n")
            f.write("| Topic | Books | Pages | Sutras | Examples |\n")
            f.write("|-------|-------|-------|--------|----------|\n")
            
            for topic, content in sorted(organized.items(), key=lambda x: x[1]['total_pages'], reverse=True):
                books = len(set(content['books']))
                pages = content['total_pages']
                sutras = len(content['sutras'])
                examples = len(content['examples'])
                
                f.write(f"| {topic.title()} | {books} | {pages} | {sutras} | {examples} |\n")
            
            f.write("\n## Topics by Category\n\n")
            
            for category, config in self.topic_structure.items():
                f.write(f"### {category.title()} ({config['folder']})\n\n")
                
                for topic in config['topics']:
                    if topic in organized:
                        content = organized[topic]
                        f.write(f"- **{topic.title()}**: {content['total_pages']} pages from {len(set(content['books']))} books\n")
                
                f.write("\n")
        
        print(f"\nTopic index created: {index_path}")


def main():
    """Main execution"""
    script_dir = Path(__file__).parent
    extraction_dir = script_dir / "extracted_content"
    output_dir = script_dir.parent
    
    print("=" * 60)
    print("Topic-Based Content Organizer")
    print("=" * 60)
    
    if not extraction_dir.exists():
        print(f"ERROR: Extraction directory not found: {extraction_dir}")
        print("Please run pdf_extractor.py first!")
        return
    
    organizer = TopicOrganizer(str(extraction_dir), str(output_dir))
    organizer.generate_all_documents()
    
    print("\n" + "=" * 60)
    print("Organization complete!")
    print(f"Documents created in: {output_dir}")
    print("=" * 60)


if __name__ == "__main__":
    main()
