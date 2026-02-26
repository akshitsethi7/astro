#!/usr/bin/env python3
import swisseph as swe
from datetime import datetime, timedelta

# Set ephemeris path
swe.set_ephe_path("/opt/sweph/ephe")

# Your correct birth details
BIRTH_LOCAL = datetime(1994, 12, 26, 22, 50, 0)  # IST
LAT = 26.4499
LON = 80.3319

print("=== TESTING DIFFERENT AYANAMSAS ===")
print(f"Birth time (IST): {BIRTH_LOCAL}")
print(f"Latitude: {LAT}, Longitude: {LON}")
print(f"Target: Leo 23.05°")
print()

# Convert to UTC (IST = UTC+5:30)
ut = BIRTH_LOCAL - timedelta(hours=5, minutes=30)
tjd = swe.julday(ut.year, ut.month, ut.day, ut.hour + ut.minute/60.0 + ut.second/3600.0, swe.GREG_CAL)

print(f"UTC time: {ut}")
print(f"Julian Day: {tjd}")
print()

# Test different ayanamsas
ayanamsas = [
    ("Lahiri", swe.SIDM_LAHIRI),
    ("Raman", swe.SIDM_RAMAN),
    ("Krishnamurti", swe.SIDM_KRISHNAMURTI),
    ("Yukteshwar", swe.SIDM_YUKTESHWAR),
    ("JN Bhasin", swe.SIDM_JN_BHASIN),
]

print("Ayanamsa | Ascendant | Sign | Difference from Leo 23.05°")
print("-" * 60)

for name, sid_mode in ayanamsas:
    try:
        swe.set_sid_mode(sid_mode, 0, 0)
        
        # Calculate ascendant
        try:
            cusps, ascmc = swe.houses_ex(tjd, swe.FLG_SIDEREAL, LAT, LON, b'P')
        except TypeError:
            cusps, ascmc = swe.houses_ex(tjd, LAT, LON, b'P')
        
        asc = ascmc[0] % 360.0
        sign_idx = int(asc // 30)
        sign_deg = asc % 30
        signs = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo",
                 "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
        
        if signs[sign_idx] == "Leo":
            diff = abs(sign_deg - 23.05)
            print(f"{name:15} | {asc:8.2f}° | {signs[sign_idx]:4} {sign_deg:5.2f}° | {diff:5.2f}°")
            if diff < 5:
                print(f"  ✅ CLOSE MATCH!")
        else:
            print(f"{name:15} | {asc:8.2f}° | {signs[sign_idx]:4} {sign_deg:5.2f}° | --")
            
    except Exception as e:
        print(f"{name:15} | ERROR: {e}")

print()
print("Note: We need to find an ayanamsa that gives Leo ascendant close to 23.05°")
