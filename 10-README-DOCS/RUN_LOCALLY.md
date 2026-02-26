# How to Run create_google_sheet.py Locally

## Step-by-Step Instructions

### Step 1: Install Python Dependencies

Open your terminal and navigate to the project directory:

```bash
cd /Users/akshitsethi/Desktop/astro
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install gspread google-auth google-auth-oauthlib google-auth-httplib2 gspread-formatting
```

### Step 2: Set Up Google Cloud Credentials

#### 2.1 Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click on the project dropdown at the top
3. Click "New Project"
4. Name it (e.g., "Astrology Charts")
5. Click "Create"

#### 2.2 Enable Required APIs

1. In the Google Cloud Console, go to **"APIs & Services" > "Library"**
2. Search for **"Google Sheets API"** and click on it
3. Click **"Enable"**
4. Go back to the Library
5. Search for **"Google Drive API"** and click on it
6. Click **"Enable"**

#### 2.3 Create Service Account

1. Go to **"APIs & Services" > "Credentials"**
2. Click **"Create Credentials"** > **"Service Account"**
3. Fill in:
   - **Service account name**: `astrology-sheets` (or any name)
   - **Service account ID**: (auto-generated)
4. Click **"Create and Continue"**
5. Skip the optional steps (click "Continue" and then "Done")

#### 2.4 Create and Download JSON Key

1. Click on the service account you just created
2. Go to the **"Keys"** tab
3. Click **"Add Key"** > **"Create new key"**
4. Select **"JSON"** format
5. Click **"Create"**
6. A JSON file will be downloaded automatically

#### 2.5 Place Credentials File

1. Rename the downloaded JSON file to `credentials.json`
2. Move it to your project directory:
   ```bash
   mv ~/Downloads/your-project-*.json /Users/akshitsethi/Desktop/astro/credentials.json
   ```

   Or manually:
   - Copy the downloaded file
   - Paste it in `/Users/akshitsethi/Desktop/astro/`
   - Rename it to `credentials.json`

### Step 3: Run the Script

Now you can run the script:

```bash
python create_google_sheet.py
```

Or if you're using Python 3:

```bash
python3 create_google_sheet.py
```

### Step 4: Access Your Google Sheet

After running the script, you'll see output like:

```
Creating Google Sheet with all astrological charts...
Created spreadsheet: https://docs.google.com/spreadsheets/d/xxxxx/edit
✅ Success! Spreadsheet created: https://docs.google.com/spreadsheets/d/xxxxx/edit
```

1. Copy the URL from the output
2. Open it in your browser
3. The spreadsheet will be owned by the service account

### Step 5: Share the Sheet with Your Personal Account (Optional)

Since the sheet is created by a service account, you may want to share it with your personal Google account:

1. Open the spreadsheet URL
2. Click the **"Share"** button (top right)
3. Add your personal Gmail address
4. Give yourself "Editor" access
5. Click **"Send"**

Alternatively, you can make it publicly viewable (not recommended for personal data) or share it with specific people.

## Troubleshooting

### Error: "credentials.json not found"

**Solution**: Make sure the `credentials.json` file is in the same directory as the script:
```bash
ls -la /Users/akshitsethi/Desktop/astro/credentials.json
```

If it's not there, check where you downloaded it and move it to the correct location.

### Error: "Permission denied" or "API not enabled"

**Solution**: 
1. Go back to Google Cloud Console
2. Make sure both **Google Sheets API** and **Google Drive API** are enabled
3. Wait a few minutes for the APIs to propagate

### Error: "ModuleNotFoundError: No module named 'gspread'"

**Solution**: Install the dependencies:
```bash
pip install -r requirements.txt
```

If you're using Python 3, try:
```bash
pip3 install -r requirements.txt
```

### Error: "403 Forbidden" or "Insufficient permissions"

**Solution**: 
1. Make sure the service account has the correct permissions
2. Try creating a new service account and downloading a new credentials file
3. Make sure the JSON key file is valid (not corrupted)

### Script runs but no spreadsheet is created

**Solution**:
1. Check the terminal output for error messages
2. Make sure you have internet connectivity
3. Verify the credentials.json file is valid JSON:
   ```bash
   python -m json.tool credentials.json
   ```

## Alternative: Use Excel Instead

If you're having trouble with Google Sheets setup, you can use the Excel version instead:

```bash
pip install openpyxl
python create_excel_sheet.py
```

This creates a local Excel file (`Akshit_Birth_Chart_Analysis.xlsx`) that you can:
- Open in Excel
- Upload to Google Sheets manually
- Share with others

## Quick Test

To verify everything is set up correctly, you can test the imports:

```bash
python -c "import gspread; from google.oauth2.service_account import Credentials; print('✅ All imports successful!')"
```

If this works, your dependencies are installed correctly.

## Need Help?

If you encounter any issues:
1. Check the error message in the terminal
2. Verify all steps above were completed
3. Make sure your `credentials.json` file is valid
4. Try the Excel alternative if Google Sheets setup is too complex



