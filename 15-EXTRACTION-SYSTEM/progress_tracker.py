#!/usr/bin/env python3
"""
Progress Tracker - Updates MASTER_PLAN.md with extraction progress
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List


class ProgressTracker:
    """Track and update extraction progress in MASTER_PLAN"""
    
    def __init__(self, extraction_dir: str, master_plan_path: str):
        self.extraction_dir = Path(extraction_dir)
        self.master_plan_path = Path(master_plan_path)
    
    def load_extractions(self) -> List[Dict]:
        """Load all extraction data"""
        extractions = []
        for json_file in self.extraction_dir.glob("*_extraction.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    extractions.append(json.load(f))
            except Exception as e:
                print(f"Error loading {json_file.name}: {e}")
        return extractions
    
    def calculate_statistics(self, extractions: List[Dict]) -> Dict:
        """Calculate overall statistics"""
        stats = {
            'books_processed': len(extractions),
            'total_pages': sum(e.get('total_pages', 0) for e in extractions),
            'total_chapters': sum(len(e.get('chapters', [])) for e in extractions),
            'total_sutras': sum(e.get('sutras_count', 0) for e in extractions),
            'total_examples': sum(e.get('examples_count', 0) for e in extractions),
            'books_by_tier': self.categorize_by_tier(extractions),
            'topic_coverage': self.calculate_topic_coverage(extractions)
        }
        return stats
    
    def categorize_by_tier(self, extractions: List[Dict]) -> Dict:
        """Categorize books by tier"""
        tier_1 = ['BPHS', 'Brihat Jataka', 'Jataka Parijata', 'Phaladeepika', 
                  'Jaimini', 'Mantreswara', 'Brihad']
        tier_2 = ['Sanjay Rath', 'Patel', 'K.N. Rao', 'Pathak', 'Combinations']
        tier_3 = ['Marriage', 'Profession', 'Rog Vichar']
        
        tiers = {'tier_1': 0, 'tier_2': 0, 'tier_3': 0, 'other': 0}
        
        for extraction in extractions:
            name = extraction['book_name']
            if any(t in name for t in tier_1):
                tiers['tier_1'] += 1
            elif any(t in name for t in tier_2):
                tiers['tier_2'] += 1
            elif any(t in name for t in tier_3):
                tiers['tier_3'] += 1
            else:
                tiers['other'] += 1
        
        return tiers
    
    def calculate_topic_coverage(self, extractions: List[Dict]) -> Dict:
        """Calculate topic coverage across all books"""
        topics = {}
        for extraction in extractions:
            for topic, count in extraction.get('topic_coverage', {}).items():
                if topic not in topics:
                    topics[topic] = {'books': 0, 'pages': 0}
                topics[topic]['books'] += 1
                topics[topic]['pages'] += count
        return topics
    
    def generate_progress_report(self, stats: Dict) -> str:
        """Generate progress report"""
        report = []
        report.append("# Extraction Progress Report\n")
        report.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        report.append("## Overall Statistics\n\n")
        report.append(f"- **Books Processed**: {stats['books_processed']}/45 ({stats['books_processed']/45*100:.1f}%)\n")
        report.append(f"- **Total Pages Extracted**: {stats['total_pages']:,}\n")
        report.append(f"- **Chapters Detected**: {stats['total_chapters']}\n")
        report.append(f"- **Sutras Found**: {stats['total_sutras']}\n")
        report.append(f"- **Examples Found**: {stats['total_examples']}\n\n")
        
        report.append("## Books by Tier\n\n")
        tiers = stats['books_by_tier']
        report.append(f"- **Tier 1 (Foundation)**: {tiers['tier_1']}/10\n")
        report.append(f"- **Tier 2 (Modern Masters)**: {tiers['tier_2']}/5\n")
        report.append(f"- **Tier 3 (Specialized)**: {tiers['tier_3']}/6\n")
        report.append(f"- **Other Tiers**: {tiers['other']}/24\n\n")
        
        report.append("## Topic Coverage\n\n")
        report.append("| Topic | Books | Pages |\n")
        report.append("|-------|-------|-------|\n")
        
        topics = sorted(stats['topic_coverage'].items(), 
                       key=lambda x: x[1]['pages'], reverse=True)
        for topic, data in topics:
            report.append(f"| {topic.title()} | {data['books']} | {data['pages']} |\n")
        
        report.append("\n## Next Steps\n\n")
        
        if stats['books_processed'] < 10:
            report.append("- Continue with Tier 1 foundation texts\n")
            report.append("- Focus on BPHS, Brihat Jataka, Jataka Parijata\n")
        elif stats['books_processed'] < 15:
            report.append("- Complete Tier 1, then move to Tier 2\n")
            report.append("- Add modern masters (Sanjay Rath, K.N. Rao, etc.)\n")
        elif stats['books_processed'] < 20:
            report.append("- Complete Tier 2, then move to Tier 3\n")
            report.append("- Add specialized texts (Marriage, Career, Health)\n")
        else:
            report.append("- Continue processing remaining books\n")
            report.append("- Review and enhance generated documents\n")
        
        return ''.join(report)
    
    def update_master_plan(self, stats: Dict):
        """Update MASTER_PLAN.md with current progress"""
        if not self.master_plan_path.exists():
            print(f"Warning: MASTER_PLAN.md not found at {self.master_plan_path}")
            return
        
        # Read current plan
        with open(self.master_plan_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update statistics
        # This is a simple replacement - could be more sophisticated
        updated = content.replace(
            '**Total Books** | 45 | 0 | 0%',
            f'**Total Books** | 45 | {stats["books_processed"]} | {stats["books_processed"]/45*100:.0f}%'
        )
        
        # Write back
        with open(self.master_plan_path, 'w', encoding='utf-8') as f:
            f.write(updated)
        
        print(f"✓ Updated MASTER_PLAN.md")
    
    def run(self):
        """Run progress tracking"""
        print("=" * 60)
        print("Progress Tracker")
        print("=" * 60 + "\n")
        
        # Load extractions
        print("Loading extractions...")
        extractions = self.load_extractions()
        
        if not extractions:
            print("No extractions found. Run pdf_extractor.py first.")
            return
        
        print(f"Found {len(extractions)} book extractions\n")
        
        # Calculate statistics
        print("Calculating statistics...")
        stats = self.calculate_statistics(extractions)
        
        # Generate report
        print("Generating report...")
        report = self.generate_progress_report(stats)
        
        # Save report
        report_path = self.extraction_dir / "PROGRESS_REPORT.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✓ Report saved: {report_path}\n")
        
        # Display summary
        print("=" * 60)
        print("PROGRESS SUMMARY")
        print("=" * 60)
        print(f"Books Processed: {stats['books_processed']}/45 ({stats['books_processed']/45*100:.1f}%)")
        print(f"Pages Extracted: {stats['total_pages']:,}")
        print(f"Sutras Found: {stats['total_sutras']}")
        print(f"Examples Found: {stats['total_examples']}")
        print("=" * 60)
        
        # Update master plan
        # self.update_master_plan(stats)  # Uncomment to auto-update


def main():
    """Main execution"""
    script_dir = Path(__file__).parent
    extraction_dir = script_dir / "extracted_content"
    master_plan = script_dir.parent / "MASTER_PLAN.md"
    
    tracker = ProgressTracker(str(extraction_dir), str(master_plan))
    tracker.run()


if __name__ == "__main__":
    main()
