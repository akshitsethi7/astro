# Quick Start Guide

## Option 1: Google Sheets (Recommended)

### Setup (One-time)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up Google Cloud credentials:
   - Follow instructions in `README_GOOGLE_SHEET.md`
   - Download `credentials.json` and place it in this directory

3. Run the script:
   ```bash
   python create_google_sheet.py
   ```

The script will create a Google Sheet with all your charts and print the URL.

## Option 2: Excel File (Easier, No API Setup)

### Setup
1. Install dependencies:
   ```bash
   pip install openpyxl
   ```

2. Run the script:
   ```bash
   python create_excel_sheet.py
   ```

This will create `Akshit_Birth_Chart_Analysis.xlsx` in the current directory. You can then:
- Open it in Excel
- Upload it to Google Sheets
- Share it with others

## What You Get

Both options include:

✅ **17 Divisional Charts** (D1, D2, D3, D4, D6, D7, D9, D10, D12, D16, D20, D24, D27, D30, D40, D45, D60)

✅ **4 Dasha Sheets** (Mahadasha, Antardasha, Pratyantardasha, Sookshmadasha)

✅ **Summary Dashboard** with statistics

✅ **Color Coding**:
- 🟢 Green = Exalted
- 🔵 Light Blue = Own Sign
- 🔴 Red = Debilitated
- 🟢 Light Green = Benefic
- 🟠 Orange = Malefic

✅ **Auto-calculated Strengths** (0-100 scale)

✅ **Filters** on all sheets for easy sorting/filtering

## Troubleshooting

### Google Sheets
- **"credentials.json not found"**: See `README_GOOGLE_SHEET.md` for setup instructions
- **Permission errors**: Make sure Google Sheets API and Drive API are enabled

### Excel
- **"openpyxl not found"**: Run `pip install openpyxl`
- **Import errors**: Make sure `create_google_sheet.py` is in the same directory

## Next Steps

After creating your sheet:
1. Review the Dashboard for overall statistics
2. Check each divisional chart for planet positions
3. Use filters to analyze specific planets or signs
4. Review dasha periods for timing predictions

