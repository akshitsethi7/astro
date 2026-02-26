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

print("=== QUICK TEST WITH YOUR CORRECT BIRTH DETAILS ===")
print(f"Birth time (IST): {BIRTH_LOCAL}")
print(f"Latitude: {LAT}, Longitude: {LON}")

# Convert to UTC (IST = UTC+5:30)
ut = BIRTH_LOCAL - timedelta(hours=5, minutes=30)
tjd = swe.julday(ut.year, ut.month, ut.day, ut.hour + ut.minute/60.0 + ut.second/3600.0, swe.GREG_CAL)

print(f"UTC time: {ut}")
print(f"Julian Day: {tjd}")

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

print(f"\nCalculated Ascendant: {asc}° = {signs[sign_idx]} {sign_deg:.2f}°")
print(f"Expected: Leo 23.05°")

if signs[sign_idx] == "Leo":
    diff = abs(sign_deg - 23.05)
    print(f"Difference: {diff:.2f}°")
    if diff < 5:
        print("✅ Close match!")
    else:
        print("❌ Too far off")
else:
    print(f"❌ Wrong sign! Expected Leo, got {signs[sign_idx]}")
