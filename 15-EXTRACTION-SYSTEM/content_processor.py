#!/usr/bin/env python3
"""
Content Processor - Transform Raw Extractions into Learning Documents

This script takes raw PDF extractions and creates structured learning documents
following the MASTER_PLAN format with:
- Clear structure and explanations
- Classical references with context
- Modern application examples
- Learning aids (tables, checklists, exercises)
- Personal chart application sections
- Cross-references

Author: Akshit Sethi
Date: February 21, 2025
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime


class ContentProcessor:
    """Process raw extractions into structured learning documents"""
    
    def __init__(self, base_dir: str = ".."):
        self.base_dir = Path(base_dir)
        self.extracted_dir = self.base_dir / "extracted_content"
        self.output_dir = self.base_dir
        
        # Document templates based on MASTER_PLAN
        self.document_structure = {
            "foundations": {
                "02-planets.md": {
                    "title": "Planets - The Cosmic Influencers",
                    "topics": ["planets", "planetary characteristics", "benefics", "malefics"],
                    "sections": [
                        "Introduction",
                        "The Nine Planets (Navagrahas)",
                        "Planetary Characteristics",
                        "Natural Benefics and Malefics",
                        "Planetary States",
                        "Planetary Relationships",
                        "Planetary Strengths",
                        "Classical Principles",
                        "Modern Application",
                        "Practice Exercises",
                        "Personal Chart Application",
                        "Summary"
                    ]
                },
                "03-houses.md": {
                    "title": "Houses - The Life Areas",
                    "topics": ["houses", "house significations", "house lordship"],
                    "sections": [
                        "Introduction",
                        "The Twelve Houses",
                        "House Classifications",
                        "House Lordship",
                        "House Strength",
                        "Classical Principles",
                        "Modern Application",
                        "Practice Exercises",
                        "Personal Chart Application",
                        "Summary"
                    ]
                },
                "04-nakshatras.md": {
                    "title": "Nakshatras - The Lunar Mansions",
                    "topics": ["nakshatras", "lunar mansions", "nakshatra lords"],
                    "sections": [
                        "Introduction",
                        "The 27 Nakshatras",
                        "Nakshatra Lords",
                        "Pada Divisions",
                        "Classical Principles",
                        "Modern Application",
                        "Practice Exercises",
                        "Personal Chart Application",
                        "Summary"
                    ]
                },
                "05-aspects.md": {
                    "title": "Aspects - Planetary Influences",
                    "topics": ["aspects", "planetary aspects", "drishti"],
                    "sections": [
                        "Introduction",
                        "The 7th Aspect",
                        "Special Aspects",
                        "Aspect Strength",
                        "Classical Principles",
                        "Modern Application",
                        "Practice Exercises",
                        "Personal Chart Application",
                        "Summary"
                    ]
                }
            }
        }
        
    def load_extractions(self) -> Dict[str, Any]:
        """Load all JSON extractions"""
        extractions = {}
        
        for json_file in self.extracted_dir.glob("*_extraction.json"):
            book_name = json_file.stem.replace("_extraction", "")
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    extractions[book_name] = json.load(f)
                print(f"✓ Loaded: {book_name}")
            except Exception as e:
                print(f"✗ Error loading {book_name}: {e}")
                
        return extractions
    
    def extract_relevant_content(self, extractions: Dict, topics: List[str]) -> Dict[str, List]:
        """Extract content relevant to specific topics"""
        relevant_content = {
            "sutras": [],
            "chapters": [],
            "examples": [],
            "principles": []
        }
        
        for book_name, data in extractions.items():
            chapters = data.get("chapters", [])
            
            for chapter in chapters:
                if not chapter:  # Skip None or empty chapters
                    continue
                    
                chapter_title = chapter.get("title", "").lower() if chapter.get("title") else ""
                chapter_text = chapter.get("text", "").lower() if chapter.get("text") else ""
                
                # Check if chapter is relevant to topics
                is_relevant = any(topic.lower() in chapter_title or topic.lower() in chapter_text 
                                 for topic in topics)
                
                if is_relevant:
                    relevant_content["chapters"].append({
                        "book": book_name,
                        "chapter": chapter.get("chapter_number", "Unknown"),
                        "title": chapter.get("title", "Untitled"),
                        "text": chapter.get("text", ""),
                        "page": chapter.get("page_number", "Unknown")
                    })
        
        return relevant_content
    
    def create_document_header(self, title: str, doc_info: Dict) -> str:
        """Create document header with metadata"""
        header = f"""# {title}

**Part of**: Foundation Phase (Week 1-2)  
**Document**: {doc_info.get('filename', 'Unknown')}  
**Status**: Generated from Classical Texts  
**Last Updated**: {datetime.now().strftime('%B %d, %Y')}  
**Sources**: BPHS, Brihat Jataka, Jataka Parijata, Phaladeepika

---

## 📚 Learning Objectives

By the end of this document, you will be able to:
- Understand the fundamental concepts
- Identify key principles from classical texts
- Apply knowledge to chart reading
- Practice with real examples
- Analyze your own birth chart

---

"""
        return header
    
    def create_introduction(self, topic: str) -> str:
        """Create introduction section"""
        intros = {
            "planets": """## Introduction

Planets (Grahas) are the primary actors in Vedic astrology. The word "Graha" means "to seize" or "to grasp" - planets seize our consciousness and influence our lives through their positions, strengths, and relationships.

The nine planets (Navagrahas) are:
1. **Sun (Surya)** - Soul, authority, father
2. **Moon (Chandra)** - Mind, emotions, mother
3. **Mars (Mangala)** - Energy, courage, siblings
4. **Mercury (Budha)** - Intelligence, communication
5. **Jupiter (Guru)** - Wisdom, expansion, children
6. **Venus (Shukra)** - Love, beauty, spouse
7. **Saturn (Shani)** - Discipline, delays, karma
8. **Rahu** - North Node, obsession, foreign
9. **Ketu** - South Node, spirituality, detachment

Each planet has unique characteristics, significations, and effects that must be understood for accurate chart reading.

---

""",
            "houses": """## Introduction

The twelve houses (Bhavas) represent the twelve major areas of life. While planets are the actors, houses are the stages where the cosmic drama unfolds. Each house governs specific life areas, relationships, and experiences.

Understanding houses is crucial because:
- They show WHERE planetary energies manifest
- They indicate WHICH life areas are emphasized
- They reveal timing of events through dashas
- They connect planets to real-life experiences

The houses are classified into various groups (Kendras, Trikonas, Dusthanas, Upachayas) each with specific characteristics and importance.

---

""",
            "nakshatras": """## Introduction

Nakshatras (Lunar Mansions) are the 27 divisions of the zodiac, each spanning 13°20'. They represent the Moon's daily journey through the sky and provide deeper insight into planetary placements.

Nakshatras are crucial for:
- **Dasha calculations** - Vimshottari dasha starts from Moon's nakshatra
- **Compatibility** - Nakshatra matching for marriage
- **Muhurta** - Selecting auspicious times
- **Deeper interpretation** - Subtle qualities of planets

Each nakshatra has a ruling deity, symbol, and planetary lord that colors the expression of any planet placed in it.

---

""",
            "aspects": """## Introduction

Aspects (Drishti) are the ways planets "see" or influence other planets and houses. The Sanskrit word "Drishti" means "sight" or "glance" - planets cast their influence through their gaze.

Understanding aspects is essential because:
- They show how planets interact
- They modify planetary effects
- They create yogas (combinations)
- They influence house significations

Vedic astrology uses different aspect rules than Western astrology, with special aspects for Mars, Jupiter, and Saturn.

---

"""
        }
        return intros.get(topic, "## Introduction\n\n[Introduction to be added]\n\n---\n\n")
    
    def create_classical_section(self, content: Dict) -> str:
        """Create classical principles section from extracted content"""
        section = """## Classical Principles from Source Texts

*Direct wisdom from the ancient masters*

"""
        
        if content["chapters"]:
            # Group by book
            by_book = {}
            for chapter in content["chapters"]:
                book = chapter["book"]
                if book not in by_book:
                    by_book[book] = []
                by_book[book].append(chapter)
            
            for book, chapters in by_book.items():
                section += f"### From {book}\n\n"
                
                for i, chapter in enumerate(chapters[:5], 1):  # Limit to 5 most relevant
                    section += f"**{i}. {chapter['title']}** (Chapter {chapter['chapter']})\n\n"
                    
                    # Extract key points from text
                    text = chapter['text'][:500]  # First 500 chars
                    section += f"> {text}...\n\n"
                    section += f"*Source: {book}, Chapter {chapter['chapter']}, Page {chapter['page']}*\n\n"
        else:
            section += "*Classical principles to be extracted from source texts*\n\n"
        
        section += "---\n\n"
        return section
    
    def create_modern_application(self, topic: str) -> str:
        """Create modern application section"""
        applications = {
            "planets": """## Modern Application

### How to Analyze Planets in a Chart

**Step 1: Identify Planetary Positions**
- Note which sign each planet occupies
- Check which house each planet is placed in
- Identify the nakshatra of each planet

**Step 2: Assess Planetary Strength**
- Is the planet exalted, debilitated, or in own sign?
- What is the planet's dignity (Shadbala)?
- Is it combust (too close to Sun)?
- Is it retrograde?

**Step 3: Analyze Planetary Relationships**
- Which planets aspect this planet?
- What is the relationship with the sign lord?
- Are there any conjunctions?

**Step 4: Synthesize Significations**
- Combine planet + sign + house + aspects
- Consider dasha periods
- Apply to life areas

### Common Mistakes to Avoid

❌ **Mistake 1**: Judging planets in isolation  
✅ **Correct**: Always consider sign, house, aspects, and dignity

❌ **Mistake 2**: Treating all benefics as good, all malefics as bad  
✅ **Correct**: Functional benefics/malefics depend on ascendant

❌ **Mistake 3**: Ignoring nakshatra placement  
✅ **Correct**: Nakshatra adds crucial nuance to interpretation

---

""",
            "houses": """## Modern Application

### How to Analyze Houses in a Chart

**Step 1: Identify House Cusps**
- Note the sign on each house cusp
- Identify the house lord (ruler of the sign)
- Check if houses are intercepted

**Step 2: Analyze House Occupants**
- Which planets are in each house?
- What are their strengths and dignities?
- How do they aspect other houses?

**Step 3: Assess House Lords**
- Where is each house lord placed?
- What is its strength and condition?
- Which houses does it aspect?

**Step 4: Synthesize House Significations**
- Combine house + planets + lord + aspects
- Consider dasha periods
- Apply to life predictions

### Common Mistakes to Avoid

❌ **Mistake 1**: Only looking at planets in houses  
✅ **Correct**: House lord placement is equally important

❌ **Mistake 2**: Ignoring empty houses  
✅ **Correct**: Empty houses are analyzed through their lords

❌ **Mistake 3**: Not considering house classifications  
✅ **Correct**: Kendra, Trikona, Dusthana nature matters

---

"""
        }
        return applications.get(topic, "## Modern Application\n\n*Modern application guidelines to be added*\n\n---\n\n")
    
    def create_practice_exercises(self, topic: str) -> str:
        """Create practice exercises section"""
        exercises = {
            "planets": """## Practice Exercises

### Exercise 1: Planetary Identification
For each planet in your chart, identify:
1. Sign placement
2. House placement
3. Nakshatra
4. Dignity (exalted/debilitated/neutral)
5. Aspects received

### Exercise 2: Strength Assessment
Rank the planets in your chart from strongest to weakest based on:
- Sign dignity
- House placement (angular/trinal/dusthana)
- Aspects
- Combustion/retrograde status

### Exercise 3: Signification Analysis
Choose one planet and write:
- Its natural significations
- How its sign modifies these
- How its house placement manifests
- What life areas it influences most

### Exercise 4: Comparative Analysis
Compare two charts (yours and a family member):
- How does the same planet behave differently?
- What causes these differences?
- What can you learn from the comparison?

---

""",
            "houses": """## Practice Exercises

### Exercise 1: House Lord Tracking
For each house in your chart:
1. Identify the sign on the cusp
2. Find the house lord
3. Note where the lord is placed
4. Assess the lord's strength

### Exercise 2: Life Area Analysis
Choose three houses and analyze:
- Planets in the house
- House lord placement
- Aspects to the house
- Predicted outcomes for that life area

### Exercise 3: Empty House Analysis
For empty houses in your chart:
- Find the house lord
- Analyze lord's placement and strength
- Determine how this life area manifests
- Compare with occupied houses

### Exercise 4: House Classification
Classify all 12 houses in your chart:
- Kendras (1, 4, 7, 10)
- Trikonas (1, 5, 9)
- Dusthanas (6, 8, 12)
- Upachayas (3, 6, 10, 11)
Note which are strongest in your chart.

---

"""
        }
        return exercises.get(topic, "## Practice Exercises\n\n*Practice exercises to be added*\n\n---\n\n")
    
    def create_personal_chart_section(self, topic: str) -> str:
        """Create personal chart application section"""
        section = f"""## Personal Chart Application

### Applying {topic.title()} to Your Birth Chart

**Your Task**: Analyze your own chart using the principles learned above.

#### Step-by-Step Analysis

1. **Gather Your Data**
   - Open your birth chart
   - Have a notebook ready
   - Reference this document

2. **Systematic Analysis**
   - Follow the modern application steps
   - Take detailed notes
   - Ask questions as you go

3. **Document Your Findings**
   - Write down observations
   - Note patterns and insights
   - Identify areas needing deeper study

4. **Validate Understanding**
   - Can you explain what you found?
   - Does it match your life experience?
   - What predictions can you make?

#### Learning Checkpoints

- [ ] I can identify all relevant placements
- [ ] I understand the classical principles
- [ ] I can apply modern interpretation
- [ ] I see connections to my life
- [ ] I can make basic predictions

#### Questions to Answer

1. What are the strongest placements in my chart?
2. What are the weakest or most challenging?
3. How do these manifest in my life?
4. What patterns do I notice?
5. What questions do I still have?

---

"""
        return section
    
    def create_summary(self, topic: str) -> str:
        """Create summary section"""
        section = f"""## Summary

### Key Takeaways

This document covered the essential principles of {topic} in Vedic astrology, including:

✓ Classical principles from ancient texts  
✓ Modern application techniques  
✓ Practical analysis methods  
✓ Personal chart application  
✓ Practice exercises for mastery

### Next Steps

1. **Review**: Re-read sections that need clarification
2. **Practice**: Complete all exercises with your chart
3. **Apply**: Use these principles in chart reading
4. **Integrate**: Connect with other topics you've learned
5. **Advance**: Move to the next document in the series

### Related Documents

- Previous: [Link to previous document]
- Next: [Link to next document]
- See also: [Related topics]

### Further Study

For deeper understanding, consult:
- BPHS (Brihat Parashara Hora Shastra)
- Brihat Jataka by Varahamihira
- Jataka Parijata by Vaidyanatha
- Phaladeepika by Mantreswara

---

**Document Status**: ✅ Complete  
**Last Updated**: {datetime.now().strftime('%B %d, %Y')}  
**Next Review**: [Schedule next review]

---

*This document is part of the comprehensive Vedic Astrology Learning System based on 45+ classical and modern texts.*
"""
        return section
    
    def process_document(self, doc_key: str, doc_info: Dict, extractions: Dict) -> str:
        """Process a single document"""
        print(f"\nProcessing: {doc_key}")
        
        # Extract relevant content
        content = self.extract_relevant_content(extractions, doc_info["topics"])
        
        # Build document
        document = ""
        document += self.create_document_header(doc_info["title"], {"filename": doc_key})
        
        # Get main topic for context
        main_topic = doc_info["topics"][0] if doc_info["topics"] else "general"
        
        document += self.create_introduction(main_topic)
        document += self.create_classical_section(content)
        document += self.create_modern_application(main_topic)
        document += self.create_practice_exercises(main_topic)
        document += self.create_personal_chart_section(main_topic)
        document += self.create_summary(main_topic)
        
        return document
    
    def process_all_documents(self):
        """Process all documents in the structure"""
        print("=" * 70)
        print("CONTENT PROCESSOR - Transform Raw Extractions to Learning Documents")
        print("=" * 70)
        
        # Load extractions
        print("\nLoading extractions...")
        extractions = self.load_extractions()
        print(f"✓ Loaded {len(extractions)} book extractions")
        
        # Process each category
        for category, documents in self.document_structure.items():
            print(f"\n{'=' * 70}")
            print(f"Processing Category: {category.upper()}")
            print(f"{'=' * 70}")
            
            category_dir = self.output_dir / f"00-{category}"
            category_dir.mkdir(exist_ok=True)
            
            for doc_key, doc_info in documents.items():
                try:
                    # Process document
                    content = self.process_document(doc_key, doc_info, extractions)
                    
                    # Save document
                    output_path = category_dir / doc_key
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"✓ Created: {output_path}")
                    
                except Exception as e:
                    print(f"✗ Error processing {doc_key}: {e}")
        
        print(f"\n{'=' * 70}")
        print("PROCESSING COMPLETE")
        print(f"{'=' * 70}")
        print(f"\nDocuments created in: {self.output_dir}")
        print("\nNext steps:")
        print("1. Review generated documents")
        print("2. Add more detailed content from source texts")
        print("3. Complete practice exercises")
        print("4. Apply to your personal chart")


def main():
    """Main execution"""
    processor = ContentProcessor()
    processor.process_all_documents()


if __name__ == "__main__":
    main()
