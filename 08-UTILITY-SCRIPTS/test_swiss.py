#!/usr/bin/env python3
import swisseph as swe
from datetime import datetime, timedelta

# Set ephemeris path
swe.set_ephe_path("/opt/sweph/ephe")
swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)

# Birth details
BIRTH_LOCAL = datetime(1994, 12, 26, 22, 50, 0)  # IST
LAT = 26.4499
LON = 80.3319

print("=== SWISS EPHEMERIS TEST ===")
print(f"Birth time (IST): {BIRTH_LOCAL}")
print(f"Latitude: {LAT}, Longitude: {LON}")

# Test different timezone offsets
offsets = [
    ("UTC-5:30 (IST)", timedelta(hours=5, minutes=30)),
    ("UTC-6:30", timedelta(hours=6, minutes=30)),
    ("UTC-7:30", timedelta(hours=7, minutes=30)),
    ("UTC-8:30", timedelta(hours=8, minutes=30)),
]

for name, offset in offsets:
    ut = BIRTH_LOCAL - offset
    tjd = swe.julday(ut.year, ut.month, ut.day, ut.hour + ut.minute/60.0 + ut.second/3600.0, swe.GREG_CAL)
    
    # Calculate ascendant
    try:
        cusps, ascmc = swe.houses_ex(tjd, swe.FLG_SIDEREAL, LAT, LON, b'P')
    except TypeError:
        # Try older signature
        cusps, ascmc = swe.houses_ex(tjd, LAT, LON, b'P')
    
    asc = ascmc[0] % 360.0
    
    print(f"\n{name}:")
    print(f"  UTC: {ut}")
    print(f"  Julian Day: {tjd}")
    print(f"  Ascendant: {asc}°")
    
    # Convert to sign
    sign_idx = int(asc // 30)
    sign_deg = asc % 30
    signs = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo",
             "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
    
    print(f"  Sign: {signs[sign_idx]} {sign_deg:.2f}°")
    
    # Check if this matches your expected Leo 23.05°
    if signs[sign_idx] == "Leo":
        diff = abs(sign_deg - 23.05)
        print(f"  Difference from expected: {diff:.2f}°")
        if diff < 5:  # Within 5 degrees
            print(f"  ✅ CLOSE MATCH!")
        else:
            print(f"  ❌ Too far off")
