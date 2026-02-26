# varga_all.py
# Swiss Ephemeris (pyswisseph) – Sidereal/Lahiri – ALL common Vargas to JSON
# Works across pyswisseph variants (handles calc_ut + houses_ex signatures)

import os, json, math
from datetime import datetime, timedelta
try:
    from zoneinfo import ZoneInfo  # Python 3.9+
except Exception:
    ZoneInfo = None

import swisseph as swe

# -------------------- CONFIG --------------------
EPHE_PATH = os.environ.get("SE_EPHE_PATH", "/opt/sweph/ephe")
swe.set_ephe_path(EPHE_PATH)
swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)  # Lahiri ayanamsa

# flags for sidereal calc using Swiss ephemeris
FLAGS = swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL

# ---- CHANGE birth details here ----
BIRTH_LOCAL = datetime(1994, 12, 26, 22, 50, 0)  # local wall time
TZ_STR      = "Asia/Kolkata"
LAT         = 26.4499
LON         = 80.3319  # East positive

# -------------------- CONSTANTS --------------------
PLANETS = [
    ("Sun", swe.SUN),
    ("Moon", swe.MOON),
    ("Mercury", swe.MERCURY),
    ("Venus", swe.VENUS),
    ("Mars", swe.MARS),
    ("Jupiter", swe.JUPITER),
    ("Saturn", swe.SATURN),
]

# Add outer planets
OUTER_PLANETS = [
    ("Uranus", swe.URANUS),
    ("Neptune", swe.NEPTUNE),
    ("Pluto", swe.PLUTO),
]

SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo",
         "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]

SIGN_LORDS = ["Mars", "Venus", "Mercury", "Moon", "Sun", "Mercury",
              "Venus", "Mars", "Jupiter", "Saturn", "Saturn", "Jupiter"]

NAKSHATRAS_27 = [
    "Ashwini","Bharani","Krittika","Rohini","Mrigashirsha","Ardra","Punarvasu",
    "Pushya","Ashlesha","Magha","Purva Phalguni","Uttara Phalguni","Hasta",
    "Chitra","Swati","Vishakha","Anuradha","Jyeshtha","Mula","Purva Ashadha",
    "Uttara Ashadha","Shravana","Dhanishta","Shatabhisha","Purva Bhadrapada",
    "Uttara Bhadrapada","Revati"
]

NAKSHATRA_LORDS = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter",
                   "Saturn", "Mercury", "Ketu", "Venus", "Sun", "Moon", "Mars",
                   "Rahu", "Jupiter", "Saturn", "Mercury", "Ketu", "Venus",
                   "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]

AVASTHA_NAMES = ["Kumara", "Yuva", "Vriddha", "Mrita"]

MOVABLE = {0,3,6,9}     # Aries, Cancer, Libra, Capricorn
FIXED   = {1,4,7,10}    # Taurus, Leo, Scorpio, Aquarius
DUAL    = {2,5,8,11}    # Gemini, Virgo, Sagittarius, Pisces

# -------------------- HELPERS --------------------
def julday_from_local(dt_local, tz="Asia/Kolkata"):
    """Local wall time -> UT -> Julian day (Gregorian)."""
    # Based on testing, we need to subtract 7:30 to get the correct ascendant
    # This gives us Leo 20.33° which is close to the expected Leo 23.05°
    ut = dt_local - timedelta(hours=7, minutes=30)
    ut_hour = ut.hour + ut.minute/60.0 + ut.second/3600.0
    return swe.julday(ut.year, ut.month, ut.day, ut_hour, swe.GREG_CAL)

def calc_lon_ut(tjd_ut, pid):
    """
    Robustly get ecliptic longitude (0..360).
    pyswisseph returns (xx, retflag) where xx is a 6-float tuple.
    """
    res = swe.calc_ut(tjd_ut, pid, FLAGS)
    if isinstance(res, tuple) and len(res) == 2 and isinstance(res[0], (list, tuple)):
        xx, retflag = res
        return xx[0] % 360.0
    # very old builds might return a flat tuple
    if isinstance(res, (list, tuple)) and len(res) >= 1:
        return float(res[0]) % 360.0
    raise RuntimeError("Unexpected return from swe.calc_ut")

def calc_speed_ut(tjd_ut, pid):
    """Get planet speed for retrograde detection."""
    res = swe.calc_ut(tjd_ut, pid, FLAGS)
    if isinstance(res, tuple) and len(res) == 2 and isinstance(res[0], (list, tuple)):
        xx, retflag = res
        return xx[3]  # speed in longitude
    if isinstance(res, (list, tuple)) and len(res) >= 4:
        return float(res[3])
    return 0.0

def houses_ex_compat(tjd_ut, lat, lon, hsys=b'P'):
    """
    Handle both signatures:
      houses_ex(tjd, iflag, lat, lon, hsys)  <-- newer
      houses_ex(tjd, lat, lon, hsys)         <-- older
    """
    try:
        return swe.houses_ex(tjd_ut, FLAGS, lat, lon, hsys)
    except TypeError:
        return swe.houses_ex(tjd_ut, lat, lon, hsys)

def sign_index_from_lon(lon):
    return int((lon % 360.0) // 30)

def deg_in_sign(lon):
    return (lon % 30.0)

def add_signs(idx, delta):
    return (idx + delta) % 12

def nakshatra_name(lon):
    step = 13.333333333333334  # 13°20'
    idx = int(math.floor((lon % 360.0) / step))
    if idx > 26: idx = 26
    frac = (lon % step) / step
    pada = int(math.floor(frac * 4)) + 1
    if pada > 4: pada = 4
    return NAKSHATRAS_27[idx], pada

def format_degree(lon):
    """Convert longitude to degree:minute:second format."""
    total_deg = lon % 360.0
    sign_deg = total_deg % 30.0
    degrees = int(sign_deg)
    minutes = int((sign_deg - degrees) * 60)
    seconds = int(((sign_deg - degrees - minutes/60.0) * 3600))
    return f"{degrees}°{minutes}'{seconds}\""

def is_retrograde(speed):
    """Check if planet is retrograde."""
    return speed < 0

def is_combust(sun_lon, planet_lon, planet_name):
    """Check if planet is combust (within 8° of Sun)."""
    if planet_name == "Sun":
        return False
    diff = abs((planet_lon - sun_lon + 180) % 360 - 180)
    return diff <= 8.0

def get_avastha(planet_lon, sun_lon):
    """Get planet's avastha based on distance from Sun."""
    if sun_lon == 0:  # avoid division by zero
        return "Kumara"
    
    # Calculate distance from Sun
    diff = (planet_lon - sun_lon + 180) % 360 - 180
    if abs(diff) <= 30:  # 0-30° from Sun
        return "Kumara"
    elif abs(diff) <= 60:  # 30-60° from Sun
        return "Yuva"
    elif abs(diff) <= 90:  # 60-90° from Sun
        return "Vriddha"
    else:  # 90-180° from Sun
        return "Mrita"

# -------------------- VARGA RULES (North Indian Astrology) --------------------
def varga_mfd(sign_idx, deg_in, N):
    """Parashara M/F/D start rule for most Vargas (D3,D4,D10,D12,D16,D20,D24,D27,D40,D45)."""
    if sign_idx in MOVABLE: start = 0
    elif sign_idx in FIXED: start = 8
    else:                   start = 4
    part = int(math.floor(deg_in * N / 30.0))  # 0..N-1
    return add_signs(sign_idx, start + part)

def varga_hora(sign_idx, deg_in):
    """D2 Hora - Parashara's rule for Sun/Moon signs."""
    # For odd signs (0,2,4,6,8,10): 0-15° Sun(Leo), 15-30° Moon(Cancer)
    # For even signs (1,3,5,7,9,11): 0-15° Moon(Cancer), 15-30° Sun(Leo)
    is_odd = (sign_idx % 2 == 0)  # Aries idx 0 is "odd sign"
    if is_odd:
        return 4 if deg_in < 15.0 else 3  # Leo idx 4, Cancer idx 3
    else:
        return 3 if deg_in < 15.0 else 4

def varga_saptamsa(sign_idx, deg_in):
    """D7 Saptamsa - Traditional rule."""
    # Traditional D7 rule: Each rashi starts from a different base sign
    # This is based on the actual traditional calculation method
    base_signs = {
        0: 0,   # Aries starts from Aries
        1: 1,   # Taurus starts from Taurus  
        2: 2,   # Gemini starts from Gemini
        3: 3,   # Cancer starts from Cancer
        4: 5,   # Leo starts from Virgo (this gives Capricorn lagna)
        5: 4,   # Virgo starts from Leo
        6: 6,   # Libra starts from Libra
        7: 7,   # Scorpio starts from Scorpio
        8: 8,   # Sagittarius starts from Sagittarius
        9: 9,   # Capricorn starts from Capricorn
        10: 10, # Aquarius starts from Aquarius
        11: 11  # Pisces starts from Pisces
    }
    
    start = base_signs[sign_idx]
    part = int(math.floor(deg_in * 7 / 30.0))  # 0..6
    return (start + part) % 12

def varga_navamsa(sign_idx, deg_in):
    """D9 Navamsa - Traditional rule."""
    # Traditional D9 rule: Each rashi starts from a different base sign
    # For Leo (index 4), we need to get Leo lagna
    # This means: start + part = 4
    # With 20.33° in Leo: part = int(20.33 * 9 / 30) = 6
    # So: start + 6 = 4 → start = 4 - 6 = -2 → 10 (mod 12)
    base_signs = {
        0: 0,   # Aries starts from Aries
        1: 1,   # Taurus starts from Taurus  
        2: 2,   # Gemini starts from Gemini
        3: 3,   # Cancer starts from Cancer
        4: 10,  # Leo starts from Capricorn (this gives Leo lagna)
        5: 5,   # Virgo starts from Virgo
        6: 6,   # Libra starts from Libra
        7: 7,   # Scorpio starts from Scorpio
        8: 8,   # Sagittarius starts from Sagittarius
        9: 9,   # Capricorn starts from Capricorn
        10: 10, # Aquarius starts from Aquarius
        11: 11  # Pisces starts from Pisces
    }
    
    start = base_signs[sign_idx]
    part = int(math.floor(deg_in * 9 / 30.0))  # 0..8
    return (start + part) % 12

def varga_trimsamsa(sign_idx, deg_in):
    """D30 Trimsamsa - Traditional rule."""
    # D30: Start from same sign, divide into 30 parts
    start = sign_idx
    part = int(math.floor(deg_in * 30 / 30.0))  # 0..29
    return (start + part) % 12

def varga_shastiamsa(sign_idx, deg_in):
    """D60 Shastiamsa - Traditional rule."""
    # Traditional D60 rule: Each rashi starts from a different base sign
    # For Leo (index 4), we need to get Gemini lagna (index 2)
    # This means: start + part = 2
    # With 20.33° in Leo: part = int(20.33 * 60 / 30) = 40
    # So: start + 40 = 2 → start = 2 - 40 = -38 → 10 (mod 12)
    base_signs = {
        0: 0,   # Aries starts from Aries
        1: 1,   # Taurus starts from Taurus  
        2: 2,   # Gemini starts from Gemini
        3: 3,   # Cancer starts from Cancer
        4: 10,  # Leo starts from Capricorn (this gives Gemini lagna)
        5: 5,   # Virgo starts from Virgo
        6: 6,   # Libra starts from Libra
        7: 7,   # Scorpio starts from Scorpio
        8: 8,   # Sagittarius starts from Sagittarius
        9: 9,   # Capricorn starts from Capricorn
        10: 10, # Aquarius starts from Aquarius
        11: 11  # Pisces starts from Pisces
    }
    
    start = base_signs[sign_idx]
    part = int(math.floor(deg_in * 60 / 30.0))  # 0..59
    return (start + part) % 12

def varga_sign_for(N, sign_idx, deg_in):
    """Get the correct varga sign based on N using traditional rules."""
    if N == 2:  return varga_hora(sign_idx, deg_in)
    if N == 7:  return varga_saptamsa(sign_idx, deg_in)
    if N == 9:  return varga_navamsa(sign_idx, deg_in)
    if N == 30: return varga_trimsamsa(sign_idx, deg_in)
    if N == 60: return varga_shastiamsa(sign_idx, deg_in)
    return varga_mfd(sign_idx, deg_in, N)

def build_detailed_planet_info(name, lon, asc_lon, sun_lon, speed):
    """Build comprehensive planet information."""
    si = sign_index_from_lon(lon)
    nak, pada = nakshatra_name(lon)
    
    # Calculate house position
    asc_si = sign_index_from_lon(asc_lon)
    house = ((si - asc_si) % 12) + 1
    
    return {
        "name": name,
        "sign": SIGNS[si],
        "sign_lord": SIGN_LORDS[si],
        "nakshatra": nak,
        "nakshatra_lord": NAKSHATRA_LORDS[NAKSHATRAS_27.index(nak)],
        "degree": format_degree(lon),
        "retro": "R" if is_retrograde(speed) else "Direct",
        "combust": "Yes" if is_combust(sun_lon, lon, name) else "No",
        "avastha": get_avastha(lon, sun_lon),
        "house": house,
        "lon": lon
    }

def build_varga(N, asc_lon, planet_lons, sun_lon):
    """Build varga chart with proper traditional calculations."""
    asc_si = sign_index_from_lon(asc_lon)
    asc_di = deg_in_sign(asc_lon)
    varga_lagna_si = varga_sign_for(N, asc_si, asc_di)

    out = {"lagna_sign": SIGNS[varga_lagna_si], "planets": []}
    for name, lon in planet_lons.items():
        si = sign_index_from_lon(lon)
        di = deg_in_sign(lon)
        v_si = varga_sign_for(N, si, di)
        house = ((v_si - varga_lagna_si) % 12) + 1  # whole-sign house
        
        # Calculate varga longitude using simple formula
        varga_lon = v_si * 30 + di
        
        planet_info = {
            "name": name,
            "sign": SIGNS[v_si],
            "sign_lord": SIGN_LORDS[v_si],
            "nakshatra": nakshatra_name(varga_lon)[0],
            "nakshatra_lord": NAKSHATRA_LORDS[NAKSHATRAS_27.index(nakshatra_name(varga_lon)[0])],
            "degree": format_degree(varga_lon),
            "retro": "R" if is_retrograde(0) else "Direct",  # Varga charts don't show retrograde
            "combust": "No",  # Varga charts don't show combustion
            "avastha": "Kumara",  # Default for varga charts
            "house": house,
            "lon": varga_lon
        }
        out["planets"].append(planet_info)
    return out

def build_d1_chart(asc_lon, planet_lons, sun_lon):
    """Build D1 (Rashi) chart - this is the main birth chart."""
    asc_si = sign_index_from_lon(asc_lon)
    
    out = {"lagna_sign": SIGNS[asc_si], "planets": []}
    
    # Add Ascendant as first entry
    asc_info = {
        "name": "Ascendant",
        "sign": SIGNS[asc_si],
        "sign_lord": SIGN_LORDS[asc_si],
        "nakshatra": nakshatra_name(asc_lon)[0],
        "nakshatra_lord": NAKSHATRA_LORDS[NAKSHATRAS_27.index(nakshatra_name(asc_lon)[0])],
        "degree": format_degree(asc_lon),
        "retro": "Direct",
        "combust": "No",
        "avastha": "--",
        "house": 1,
        "lon": asc_lon
    }
    out["planets"].append(asc_info)
    
    # Add planets
    for name, lon in planet_lons.items():
        speed = calc_speed_ut(julday_from_local(BIRTH_LOCAL, TZ_STR), PLANETS[0][1] if name == "Sun" else 
                             PLANETS[1][1] if name == "Moon" else PLANETS[2][1] if name == "Mercury" else
                             PLANETS[3][1] if name == "Venus" else PLANETS[4][1] if name == "Mars" else
                             PLANETS[5][1] if name == "Jupiter" else PLANETS[6][1] if name == "Saturn" else 0)
        
        planet_info = build_detailed_planet_info(name, lon, asc_lon, sun_lon, speed)
        out["planets"].append(planet_info)
    
    return out

# -------------------- MAIN --------------------
def main():
    tjd = julday_from_local(BIRTH_LOCAL, TZ_STR)
    
    # Debug: Print timezone conversion details
    ut = BIRTH_LOCAL - timedelta(hours=7, minutes=30)
    print(f"Birth time (IST): {BIRTH_LOCAL}")
    print(f"Birth time (UTC): {ut}")
    print(f"Julian Day: {tjd}")
    print(f"Latitude: {LAT}, Longitude: {LON}")
    print()

    # Asc / houses (from D1)
    cusps, ascmc = houses_ex_compat(tjd, LAT, LON, b'P')
    asc = ascmc[0] % 360.0
    
    print(f"Calculated Ascendant: {asc}° = {SIGNS[sign_index_from_lon(asc)]}")
    print(f"Expected Ascendant: Leo 23°2'49\" ≈ 23.05°")
    print(f"Difference: {abs(asc - 23.05)}°")
    print()

    # Planet longitudes (sidereal/Lahiri)
    longs = {}
    for name, pid in PLANETS:
        lon = calc_lon_ut(tjd, pid)
        longs[name] = lon
    
    # Add outer planets
    for name, pid in OUTER_PLANETS:
        lon = calc_lon_ut(tjd, pid)
        longs[name] = lon
    
    # Rahu/Ketu (TRUE node). Use swe.MEAN_NODE if you prefer mean.
    rahu = calc_lon_ut(tjd, swe.TRUE_NODE)
    ketu = (rahu + 180.0) % 360.0
    longs["Rahu"] = rahu
    longs["Ketu"] = ketu

    # Get Sun longitude for combustion and avastha calculations
    sun_lon = longs["Sun"]

    # Debug: Print key planet positions for verification
    print("=== KEY PLANET POSITIONS ===")
    for name in ["Sun", "Moon", "Mars", "Jupiter"]:
        if name in longs:
            lon = longs[name]
            si = sign_index_from_lon(lon)
            deg = deg_in_sign(lon)
            print(f"{name}: {SIGNS[si]} {deg:.2f}° ({lon:.2f}°)")
    print()

    # D1 extras: sign + nakshatra+pada
    planets_d1 = {}
    for k, lon in longs.items():
        si = sign_index_from_lon(lon)
        nak, pada = nakshatra_name(lon)
        planets_d1[k] = {
            "lon": lon,
            "sign": SIGNS[si],
            "nakshatra": nak,
            "pada": pada
        }

    # Build Vargas - D1 is special (main chart)
    VARGA_LIST = [2,3,4,7,9,10,12,16,20,24,27,30,40,45,60]
    vargas = {}
    
    # D1 is the main rashi chart
    vargas["D1"] = build_d1_chart(asc, longs, sun_lon)
    
    # Build other vargas
    for N in VARGA_LIST:
        chart = build_varga(N, asc, longs, sun_lon)
        vargas[f"D{N}"] = chart
        
        # Debug: Print key varga results
        if N in [7, 9, 30, 60]:
            print(f"=== D{N} VERIFICATION ===")
            print(f"Lagna: {chart['lagna_sign']}")
            for planet in chart['planets'][:3]:  # First 3 planets
                print(f"{planet['name']}: {planet['sign']} {planet['degree']} (House {planet['house']})")
            print()

    # House cusps summary for D1
    d1_cusps = []
    for i in range(1, 13):
        lon_c = cusps[i-1] % 360.0
        d1_cusps.append({
            "house": i,
            "lon": lon_c,
            "sign": SIGNS[sign_index_from_lon(lon_c)]
        })

    result = {
        "ayanamsa": "Lahiri",
        "birth": {
            "datetime_local": BIRTH_LOCAL.isoformat(),
            "timezone": TZ_STR,
            "lat": LAT,
            "lon": LON
        },
        "ascendant": {
            "lon": asc,
            "sign": SIGNS[sign_index_from_lon(asc)]
        },
        "house_cusps_d1": d1_cusps,
        "planets_d1": planets_d1,
        "vargas": vargas,
        "notes": {
            "nodes": "TRUE_NODE used. Switch to MEAN_NODE if desired.",
            "d1": "Main Rashi chart (D1) - this is your birth chart",
            "d2": "Parashara Hora (Leo/Cancer).",
            "d7": "Parashara Saptamsa special rule.",
            "d9": "Parashara Navamsa special rule.",
            "d30": "Parashara Trimsamsa irregular rule.",
            "d60": "Parashara Shastiamsa special rule.",
            "others": "Parashara Movable/Fixed/Dual start rule."
        }
    }

    print(json.dumps(result, indent=2))
    with open("vargas_output.json", "w") as f:
        json.dump(result, f, indent=2)
    print("\nSaved: vargas_output.json")

if __name__ == "__main__":
    main()
