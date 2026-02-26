# Google Sheets Astrological Chart Generator

This script creates a comprehensive Google Sheet with all your astrological charts, including color coding, filters, auto-calculated strengths, and a summary dashboard.

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Create Google Cloud Project and Service Account

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use an existing one)
3. Enable the **Google Sheets API** and **Google Drive API**:
   - Go to "APIs & Services" > "Library"
   - Search for "Google Sheets API" and enable it
   - Search for "Google Drive API" and enable it

### 3. Create Service Account

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "Service Account"
3. Give it a name (e.g., "astrology-sheets")
4. Click "Create and Continue"
5. Skip the optional steps and click "Done"

### 4. Create and Download Credentials

1. Click on the service account you just created
2. Go to the "Keys" tab
3. Click "Add Key" > "Create new key"
4. Choose "JSON" format
5. Download the JSON file
6. Rename it to `credentials.json` and place it in the same directory as the script

### 5. Share Your Google Sheet (Optional)

The script will create a new spreadsheet. If you want to access it:
- The script will print the spreadsheet URL
- You can also share the spreadsheet with your Google account email

## Usage

```bash
python create_google_sheet.py
```

The script will:
1. Create a new Google Sheet named "Akshit - Complete Birth Chart Analysis"
2. Add multiple sheets for each divisional chart (D1, D2, D3, D4, D6, D7, D9, D10, D12, D16, D20, D24, D27, D30, D40, D45, D60)
3. Add dasha sheets (Mahadasha, Antardasha, Pratyantardasha, Sookshmadasha)
4. Add a summary dashboard
5. Apply color coding based on planet status
6. Add filters to all sheets
7. Calculate planet strengths automatically

## Features

### Color Coding
- **Green**: Exalted planets
- **Light Blue**: Own sign (Moolatrikona)
- **Red**: Debilitated planets
- **Light Green**: Benefic planets
- **Orange**: Malefic planets
- **White**: Neutral planets

### Auto-Calculated Strengths
Planet strengths are calculated based on:
- Exaltation (+30)
- Own sign (+20)
- Debilitation (-20)
- Benefic nature (+10)
- Malefic nature (-5)
- Retrograde (-10)
- Friendly sign lord (+5)

### Filters
All sheets have filters enabled, allowing you to:
- Sort by planet, sign, house, strength, etc.
- Filter by benefic/malefic status
- Filter by own sign, exalted, or debilitated planets

### Summary Dashboard
The dashboard provides:
- Total planets per chart
- Average strength per chart
- Benefic and malefic planet counts
- Quick overview of all charts

## Sheet Structure

1. **D1** - Birth Chart (Rashi)
2. **D2** - Hora Chart (Wealth & Prosperity)
3. **D3** - Drekkana Chart
4. **D4** - Chaturthamsa Chart
5. **D6** - Shashtamsa Chart (Health & Disease)
6. **D7** - Saptamsa Chart (Children & Progeny)
7. **D9** - Navamsa Chart (Marriage & Spirituality)
8. **D10** - Dashamsa Chart (Career & Profession)
9. **D12** - Dwadasamsa Chart
10. **D16** - Shodasamsa Chart
11. **D20** - Vimsamsa Chart
12. **D24** - Chaturvimsamsa Chart
13. **D27** - Saptavimsamsa Chart
14. **D30** - Trimsamsa Chart
15. **D40** - Khavedamsa Chart
16. **D45** - Akshavedamsa Chart
17. **D60** - Shashtiamsa Chart (Karmic Chart)
18. **Mahadasha** - Major periods
19. **Antardasha** - Sub-periods
20. **Pratyantardasha** - Sub-sub-periods
21. **Sookshmadasha** - Micro-periods
22. **Dashboard** - Summary and statistics

## Troubleshooting

### "credentials.json not found"
- Make sure you've downloaded the service account JSON key
- Rename it to `credentials.json`
- Place it in the same directory as the script

### "Permission denied" errors
- Make sure you've enabled Google Sheets API and Google Drive API
- Check that your service account has the correct permissions

### Formatting not working
- Install `gspread-formatting`: `pip install gspread-formatting`
- The script will still work without it, but formatting will be limited

## Notes

- The spreadsheet will be created in the Google account associated with the service account
- You can share the spreadsheet with your personal Google account for easier access
- All data is based on the chart information you provided
- Planet strengths are calculated using traditional Vedic astrology rules

