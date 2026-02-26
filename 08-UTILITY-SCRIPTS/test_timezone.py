#!/usr/bin/env python3
import swisseph as swe
from datetime import datetime, timedelta

# Set ephemeris path
swe.set_ephe_path("/opt/sweph/ephe")
swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)

# Your correct birth details
BIRTH_LOCAL = datetime(1994, 12, 26, 22, 50, 0)  # IST
LAT = 26.4499
LON = 80.3319

print("=== TESTING DIFFERENT TIMEZONE OFFSETS ===")
print(f"Birth time (IST): {BIRTH_LOCAL}")
print(f"Latitude: {LAT}, Longitude: {LON}")
print(f"Target: Leo 23.05°")
print()

# Test different timezone offsets
offsets = [
    ("UTC+4:30", timedelta(hours=-4, minutes=-30)),
    ("UTC+5:00", timedelta(hours=-5, minutes=0)),
    ("UTC+5:30 (IST)", timedelta(hours=-5, minutes=-30)),
    ("UTC+6:00", timedelta(hours=-6, minutes=0)),
    ("UTC+6:30", timedelta(hours=-6, minutes=-30)),
    ("UTC+7:00", timedelta(hours=-7, minutes=0)),
    ("UTC+7:30", timedelta(hours=-7, minutes=-30)),
    ("UTC+8:00", timedelta(hours=-8, minutes=0)),
]

print("Offset | UTC Time | Julian Day | Ascendant | Sign | Difference from Leo 23.05°")
print("-" * 80)

for name, offset in offsets:
    ut = BIRTH_LOCAL + offset  # Add offset to get UTC
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
        diff = abs(sign_deg - 23.05)
        print(f"{name:12} | {ut.time()} | {tjd:.2f} | {asc:8.2f}° | {signs[sign_idx]:4} {sign_deg:5.2f}° | {diff:5.2f}°")
        if diff < 5:
            print(f"  ✅ CLOSE MATCH!")
    else:
        print(f"{name:12} | {ut.time()} | {tjd:.2f} | {asc:8.2f}° | {signs[sign_idx]:4} {sign_deg:5.2f}° | --")

print()
print("Note: We need to find an offset that gives Leo ascendant close to 23.05°")
print("This will help us understand what timezone your chart was calculated with.")
