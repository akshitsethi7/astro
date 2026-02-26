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

print("=== ASCENDANT DEBUG ===")
print(f"Birth time (IST): {BIRTH_LOCAL}")
print(f"Latitude: {LAT}, Longitude: {LON}")

# Test different UTC times
test_times = [
    ("IST (UTC+5:30)", BIRTH_LOCAL - timedelta(hours=5, minutes=30)),
    ("IST (UTC+5:30) - 1 hour", BIRTH_LOCAL - timedelta(hours=6, minutes=30)),
    ("IST (UTC+5:30) + 1 hour", BIRTH_LOCAL - timedelta(hours=4, minutes=30)),
    ("IST (UTC+5:30) - 2 hours", BIRTH_LOCAL - timedelta(hours=7, minutes=30)),
    ("IST (UTC+5:30) + 2 hours", BIRTH_LOCAL - timedelta(hours=3, minutes=30)),
]

for desc, ut_time in test_times:
    print(f"\n--- {desc} ---")
    print(f"UTC time: {ut_time}")
    
    # Calculate Julian Day
    ut_hour = ut_time.hour + ut_time.minute/60.0 + ut_time.second/3600.0
    tjd = swe.julday(ut_time.year, ut_time.month, ut_time.day, ut_hour, swe.GREG_CAL)
    print(f"Julian Day: {tjd}")
    
    # Calculate houses - try different signatures
    try:
        # Try the newer signature first
        cusps, ascmc = swe.houses_ex(tjd, swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL, LAT, LON, b'P')
        asc = ascmc[0] % 360.0
        print(f"Ascendant: {asc}°")
        
        # Convert to sign
        sign_idx = int(asc // 30)
        signs = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo",
                "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
        sign = signs[sign_idx]
        deg_in_sign = asc % 30
        print(f"Sign: {sign} {deg_in_sign:.2f}°")
        
        # Check if this matches expected Leo 23°
        if sign == "Leo" and abs(deg_in_sign - 23.05) < 5:
            print("✅ MATCHES EXPECTED LEO ASCENDANT!")
        
    except TypeError:
        try:
            # Try the older signature
            cusps, ascmc = swe.houses_ex(tjd, LAT, LON, b'P')
            asc = ascmc[0] % 360.0
            print(f"Ascendant: {asc}°")
            
            # Convert to sign
            sign_idx = int(asc // 30)
            signs = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo",
                    "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
            sign = signs[sign_idx]
            deg_in_sign = asc % 30
            print(f"Sign: {sign} {deg_in_sign:.2f}°")
            
            # Check if this matches expected Leo 23°
            if sign == "Leo" and abs(deg_in_sign - 23.05) < 5:
                print("✅ MATCHES EXPECTED LEO ASCENDANT!")
                
        except Exception as e:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

print("\n=== END DEBUG ===")
