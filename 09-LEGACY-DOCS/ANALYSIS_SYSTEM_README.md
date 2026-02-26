# Chart Analysis System

A comprehensive astrological chart analysis system that uses your knowledge base to provide detailed insights.

## 📁 Files Created

### Core Analysis Modules

1. **chart_analyzer.py** - Main chart analysis engine
   - Loads and parses chart data
   - Analyzes marriage prospects
   - Analyzes career prospects
   - Planetary strength analysis
   - Dasha timeline generation

2. **knowledge_analyzer.py** - Knowledge-based analysis
   - Uses your learning documents
   - Detailed marriage analysis with interpretations
   - Career analysis with profession suggestions
   - Spouse characteristics analysis
   - Timing predictions

3. **report_generator.py** - Report generation
   - Comprehensive text reports
   - Formatted output
   - Multiple sections (overview, yogas, marriage, career, dashas)

4. **data_validator.py** - Data validation
   - Validates chart data integrity
   - Checks planetary positions
   - Validates houses and signs
   - Cross-validates divisional charts

5. **analyze_chart.py** - Master script
   - Interactive analysis workflow
   - Runs all modules
   - Generates multiple report formats

## 🚀 Quick Start

### Basic Usage

```bash
cd astro
python3 analyze_chart.py
```

This will:
1. Validate your chart data
2. Run comprehensive analysis
3. Generate detailed reports
4. Create JSON outputs for further processing

### Individual Module Usage

#### 1. Basic Chart Analysis
```python
from chart_analyzer import ChartAnalyzer

analyzer = ChartAnalyzer('chartsall', 'chartsimp')

# Get D1 chart
d1 = analyzer.get_d1_chart()

# Analyze marriage
marriage = analyzer.analyze_marriage_prospects()

# Analyze career
career = analyzer.analyze_career_prospects()

# Get current dasha
current_dasha = analyzer.get_current_dasha()
```

#### 2. Knowledge-Based Analysis
```python
from chart_analyzer import ChartAnalyzer
from knowledge_analyzer import KnowledgeAnalyzer

analyzer = ChartAnalyzer('chartsall', 'chartsimp')
kb_analyzer = KnowledgeAnalyzer(analyzer)

# Detailed marriage analysis
marriage = kb_analyzer.analyze_marriage_with_knowledge()

# Detailed career analysis
career = kb_analyzer.analyze_career_with_knowledge()
```

#### 3. Generate Reports
```python
from chart_analyzer import ChartAnalyzer
from report_generator import ReportGenerator

analyzer = ChartAnalyzer('chartsall', 'chartsimp')
generator = ReportGenerator(analyzer)

# Generate complete report
report = generator.generate_complete_report('my_report.txt')
```

#### 4. Validate Data
```python
from data_validator import DataValidator

validator = DataValidator('chartsall', 'chartsimp')
errors, warnings = validator.validate_all()
validator.print_report()
```

## 📊 Output Files

When you run `analyze_chart.py`, it generates:

1. **COMPLETE_CHART_REPORT.txt** - Full text report with:
   - Chart overview
   - Planetary positions
   - Yoga analysis
   - Marriage analysis
   - Career analysis
   - Dasha timeline
   - Divisional charts summary
   - Recommendations

2. **marriage_analysis.json** - Detailed marriage analysis:
   - 7th house analysis
   - Venus analysis
   - Jupiter analysis
   - Navamsa analysis
   - Marriage yogas
   - Timing indicators
   - Spouse characteristics

3. **career_analysis.json** - Detailed career analysis:
   - 10th house analysis
   - Sun analysis
   - Saturn analysis
   - D10 analysis
   - Suitable professions
   - Career timing

4. **dasha_timeline.json** - 10-year dasha timeline:
   - Mahadasha periods
   - Antardasha periods
   - Dates and durations

## 🔍 What the System Analyzes

### Marriage Analysis
- 7th house (marriage house) and its lord
- Venus (karaka for marriage)
- Jupiter (karaka for husband)
- Navamsa chart (D9)
- Marriage yogas (Raja Yoga, etc.)
- Kuja Dosha (Manglik)
- Timing of marriage from dashas
- Spouse characteristics

### Career Analysis
- 10th house (career house) and its lord
- Sun (karaka for authority)
- Saturn (karaka for service)
- Dasamsa chart (D10)
- Career yogas
- Suitable professions based on planetary positions
- Career timing from dashas

### Planetary Analysis
- Strength (exalted, own sign, etc.)
- Weakness (debilitated, enemy sign)
- Combustion status
- Retrograde status
- House placement
- Sign placement
- Nakshatra placement

### Yoga Analysis
- Major yogas (Gajakesari, Raja, Pancha Mahapurusha)
- Chandra yogas (Sunafa, Anafa, Durudhara)
- Surya yogas (Veshi, Vaasi)
- Inauspicious yogas (Kuja, Kemadruma)

### Dasha Analysis
- Current running dasha
- Upcoming dasha periods
- Favorable periods for marriage
- Favorable periods for career
- 10-year timeline

## 🎯 Key Features

### 1. Knowledge-Based Interpretations
The system uses your learning documents to provide contextual interpretations:
- Classical principles from BPHS, Jataka Parijata, etc.
- Modern interpretations
- Practical guidance

### 2. Multi-Level Analysis
- D1 (Rashi) - Overall life
- D9 (Navamsa) - Marriage
- D10 (Dasamsa) - Career
- D7 (Saptamsa) - Children
- Other divisional charts

### 3. Timing Predictions
- Uses Vimshottari dasha system
- Identifies favorable periods
- Connects planetary periods to life events

### 4. Data Validation
- Ensures data integrity
- Checks calculations
- Identifies inconsistencies

## 🔧 Customization

### Add Custom Analysis

Edit `knowledge_analyzer.py` to add custom interpretations:

```python
def _interpret_custom_factor(self, planet):
    """Add your custom interpretation"""
    # Your logic here
    return interpretation
```

### Modify Report Format

Edit `report_generator.py` to customize report sections:

```python
def _generate_custom_section(self):
    """Add custom report section"""
    lines = []
    # Your report logic
    return lines
```

### Add New Validations

Edit `data_validator.py` to add custom validations:

```python
def _validate_custom_rule(self):
    """Add custom validation"""
    # Your validation logic
    pass
```

## 📚 Integration with Knowledge Base

The system automatically loads knowledge from:
- `logy-learning/01-marriage/` - Marriage analysis methods
- `logy-learning/02-career/` - Career analysis methods
- `logy-learning/00-foundations/` - Foundational concepts

To add more knowledge:
1. Add markdown files to appropriate folders
2. System will automatically load them
3. Use the knowledge in interpretations

## 🐛 Troubleshooting

### File Not Found
```bash
# Make sure you're in the astro directory
cd astro
python3 analyze_chart.py
```

### Import Errors
```bash
# Ensure all files are in the same directory
ls -la *.py
```

### Data Issues
```bash
# Run validator separately
python3 data_validator.py
```

## 🚀 Next Steps

1. **Run the analysis**:
   ```bash
   python3 analyze_chart.py
   ```

2. **Review the reports**:
   - Read `COMPLETE_CHART_REPORT.txt`
   - Examine JSON files for detailed data

3. **Customize**:
   - Add your own interpretations
   - Modify report formats
   - Add new analysis modules

4. **Integrate**:
   - Use with your astro-marriage-ui
   - Create API endpoints
   - Build visualization tools

## 💡 Tips

- Run validation first to ensure data quality
- Use JSON outputs for programmatic access
- Customize interpretations based on your knowledge
- Add more divisional chart analysis as needed
- Integrate with your UI for interactive analysis

## 📖 Further Reading

- Check your `logy-learning/` folder for detailed astrological knowledge
- Review `marriage-analysis/` for marriage-specific insights
- See `astro-marriage-ui/` for UI integration examples

---

**Created**: 2026-02-23
**System**: Comprehensive Chart Analysis v1.0
