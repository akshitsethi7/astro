#!/usr/bin/env python3
import swisseph as swe
from datetime import datetime, timedelta

# Set ephemeris path
swe.set_ephe_path("/opt/sweph/ephe")
swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)

# Birth details
BIRTH_DATE = datetime(1994, 12, 26, 22, 50, 0)  # IST
LAT = 26.4499
LON = 80.3319

print("=== FINDING CORRECT BIRTH TIME ===")
print(f"Target: Leo 23.05° ascendant")
print(f"Birth date: {BIRTH_DATE.date()}")
print(f"Latitude: {LAT}, Longitude: {LON}")

# Test different times around 22:50
target_asc = 23.05  # Leo 23.05°
base_time = datetime(1994, 12, 26, 22, 50, 0)

print(f"\nTesting times around {base_time.time()}:")
print("Time (IST) | UTC | Ascendant | Sign | Difference")

for minute_offset in range(-30, 31, 5):  # Test ±30 minutes
    test_time = base_time + timedelta(minutes=minute_offset)
    
    # Convert to UTC (subtract 7:30 based on our testing)
    ut = test_time - timedelta(hours=7, minutes=30)
    tjd = swe.julday(ut.year, ut.month, ut.day, ut.hour + ut.minute/60.0 + ut.second/3600.0, swe.GREG_CAL)
    
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
        diff = abs(sign_deg - target_asc)
        print(f"{test_time.time()} | {ut.time()} | {asc:.2f}° | {signs[sign_idx]} {sign_deg:.2f}° | {diff:.2f}°")
        
        if diff < 1.0:  # Within 1 degree
            print(f"  🎯 EXCELLENT MATCH!")
        elif diff < 5.0:  # Within 5 degrees
            print(f"  ✅ Good match")
    else:
        print(f"{test_time.time()} | {ut.time()} | {asc:.2f}° | {signs[sign_idx]} {sign_deg:.2f}° | --")

print(f"\nNote: Target is Leo {target_asc}°")
print("We need to find a time that gives Leo ascendant close to this degree.")
