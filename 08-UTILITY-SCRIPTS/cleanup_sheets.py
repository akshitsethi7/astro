#!/usr/bin/env python3
"""
Cleanup old Google Sheets to free up storage space.
"""

import gspread
from google.oauth2.service_account import Credentials
import sys

def cleanup_old_spreadsheets(credentials_file: str = "credentials.json", max_to_keep: int = 3):
    """Delete old spreadsheets to free up space."""
    
    # Authenticate
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    
    try:
        creds = Credentials.from_service_account_file(credentials_file, scopes=scope)
        client = gspread.authorize(creds)
    except FileNotFoundError:
        print(f"Error: {credentials_file} not found!")
        return False
    
    try:
        # Get all spreadsheets
        print("Fetching all spreadsheets...")
        spreadsheets = client.openall()
        
        if len(spreadsheets) == 0:
            print("No spreadsheets found.")
            return True
        
        print(f"Found {len(spreadsheets)} spreadsheets.")
        
        if len(spreadsheets) <= max_to_keep:
            print(f"Only {len(spreadsheets)} spreadsheets found. Keeping all (max_to_keep={max_to_keep}).")
            print("\nCurrent spreadsheets:")
            for i, sheet in enumerate(spreadsheets, 1):
                print(f"  {i}. {sheet.title} (ID: {sheet.id})")
            return True
        
        # Sort by creation time (newest first)
        try:
            spreadsheets.sort(key=lambda x: x.created if hasattr(x, 'created') else 0, reverse=True)
        except:
            # If created attribute doesn't exist, just use the order
            pass
        
        # Show what will be kept
        print(f"\nKeeping {max_to_keep} most recent spreadsheets:")
        for i, sheet in enumerate(spreadsheets[:max_to_keep], 1):
            print(f"  {i}. {sheet.title}")
        
        # Show what will be deleted
        to_delete = spreadsheets[max_to_keep:]
        print(f"\nDeleting {len(to_delete)} old spreadsheets:")
        for i, sheet in enumerate(to_delete, 1):
            print(f"  {i}. {sheet.title}")
        
        # Ask for confirmation
        response = input(f"\nDelete {len(to_delete)} spreadsheets? (yes/no): ").strip().lower()
        if response not in ['yes', 'y']:
            print("Cancelled.")
            return False
        
        # Delete old ones
        deleted_count = 0
        for sheet in to_delete:
            try:
                client.del_spreadsheet(sheet.id)
                print(f"  ✅ Deleted: {sheet.title}")
                deleted_count += 1
            except Exception as e:
                print(f"  ❌ Could not delete {sheet.title}: {e}")
        
        print(f"\n✅ Cleanup complete! Deleted {deleted_count} spreadsheets.")
        print(f"Kept {max_to_keep} most recent spreadsheets.")
        return True
        
    except Exception as e:
        print(f"Error during cleanup: {e}")
        return False

if __name__ == "__main__":
    max_to_keep = 3
    if len(sys.argv) > 1:
        try:
            max_to_keep = int(sys.argv[1])
        except ValueError:
            print(f"Invalid number: {sys.argv[1]}. Using default: 3")
    
    print(f"Cleaning up old Google Sheets (keeping {max_to_keep} most recent)...")
    print()
    
    success = cleanup_old_spreadsheets(max_to_keep=max_to_keep)
    
    if success:
        print("\n✅ You can now try creating a new spreadsheet:")
        print("   python create_google_sheet.py")
    else:
        print("\n❌ Cleanup failed. Check the error messages above.")



