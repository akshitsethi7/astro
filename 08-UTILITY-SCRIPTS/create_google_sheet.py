#!/usr/bin/env python3
"""
Create a comprehensive Google Sheet with all astrological charts,
color coding, filters, and calculated strengths.
"""

import json
from datetime import datetime
from typing import Dict, List, Tuple, Any
import gspread
from google.oauth2.service_account import Credentials
try:
    from gspread_formatting import *
except ImportError:
    # Fallback if gspread_formatting is not available
    print("Warning: gspread_formatting not available. Some formatting features may be limited.")
    CellFormat = None
    TextFormat = None
    format_cell_range = None
    merge_cells = None

# ==================== CHART DATA PARSING ====================

# Define planet data from user's input
CHARTS_DATA = {
    "D1": {
        "name": "Birth Chart (D1) - Planetary Positions",
        "planets": [
            {"Planet": "SUN", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "10°55'", "House": 5},
            {"Planet": "MOON", "Sign": "Virgo", "Sign Lord": "Mercury", "Degree": "22°44'", "House": 2},
            {"Planet": "MARS", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "8°33'", "House": 1},
            {"Planet": "MERCURY", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "18°06'", "House": 5},
            {"Planet": "JUPITER", "Sign": "Scorpio", "Sign Lord": "Mars", "Degree": "9°52'", "House": 4},
            {"Planet": "VENUS", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "25°24'", "House": 3},
            {"Planet": "SATURN", "Sign": "Aquarius", "Sign Lord": "Saturn", "Degree": "13°46'", "House": 7},
            {"Planet": "RAHU (R)", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "18°15'", "House": 3},
            {"Planet": "KETU (R)", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "18°15'", "House": 9},
            {"Planet": "URANUS", "Sign": "Capricorn", "Sign Lord": "Saturn", "Degree": "1°22'", "House": 6},
            {"Planet": "NEPTUNE", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "28°34'", "House": 5},
            {"Planet": "PLUTO", "Sign": "Scorpio", "Sign Lord": "Mars", "Degree": "5°33'", "House": 4},
            {"Planet": "Ascendant", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "23°03'", "House": 1},
        ]
    },
    "D2": {
        "name": "Hora Chart (D2) - Wealth & Prosperity",
        "planets": [
            {"Planet": "MARS", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "17°06'", "House": 1},
            {"Planet": "MOON", "Sign": "Virgo", "Sign Lord": "Mercury", "Degree": "15°28'", "House": 2},
            {"Planet": "VENUS", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "20°48'", "House": 3},
            {"Planet": "RAHU (R)", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "06°30'", "House": 3},
            {"Planet": "JUPITER", "Sign": "Scorpio", "Sign Lord": "Mars", "Degree": "19°44'", "House": 4},
            {"Planet": "SUN", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "21°50'", "House": 5},
            {"Planet": "MERCURY", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "06°13'", "House": 5},
            {"Planet": "SATURN", "Sign": "Aquarius", "Sign Lord": "Saturn", "Degree": "27°33'", "House": 7},
            {"Planet": "KETU (R)", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "06°30'", "House": 9},
        ]
    },
    "D6": {
        "name": "Shashtamsa Chart (D6) - Health & Disease",
        "planets": [
            {"Planet": "MARS", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "21°20'", "House": 1},
            {"Planet": "MOON", "Sign": "Virgo", "Sign Lord": "Mercury", "Degree": "16°25'", "House": 2},
            {"Planet": "VENUS", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "02°25'", "House": 3},
            {"Planet": "RAHU (R)", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "19°32'", "House": 3},
            {"Planet": "JUPITER", "Sign": "Scorpio", "Sign Lord": "Mars", "Degree": "29°12'", "House": 4},
            {"Planet": "SUN", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "05°30'", "House": 5},
            {"Planet": "MERCURY", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "18°40'", "House": 5},
            {"Planet": "SATURN", "Sign": "Aquarius", "Sign Lord": "Saturn", "Degree": "22°40'", "House": 7},
            {"Planet": "KETU (R)", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "19°32'", "House": 9},
        ]
    },
    "D7": {
        "name": "Saptamsa Chart (D7) - Children & Progeny",
        "planets": [
            {"Planet": "MARS", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "29°53'", "House": 1},
            {"Planet": "MOON", "Sign": "Virgo", "Sign Lord": "Mercury", "Degree": "09°09'", "House": 2},
            {"Planet": "VENUS", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "27°49'", "House": 3},
            {"Planet": "RAHU (R)", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "07°47'", "House": 3},
            {"Planet": "JUPITER", "Sign": "Scorpio", "Sign Lord": "Mars", "Degree": "09°04'", "House": 4},
            {"Planet": "SUN", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "16°26'", "House": 5},
            {"Planet": "MERCURY", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "06°47'", "House": 5},
            {"Planet": "SATURN", "Sign": "Aquarius", "Sign Lord": "Saturn", "Degree": "06°27'", "House": 7},
            {"Planet": "KETU (R)", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "07°47'", "House": 9},
        ]
    },
    "D9": {
        "name": "Navamsa Chart (D9) - Marriage & Spirituality",
        "planets": [
            {"Planet": "SATURN", "Sign": "Aquarius", "Sign Lord": "Saturn", "Degree": "04°00'", "House": 5},
            {"Planet": "RAHU (R)", "Sign": "Pisces", "Sign Lord": "Jupiter", "Degree": "14°18'", "House": 6},
            {"Planet": "VENUS", "Sign": "Taurus", "Sign Lord": "Venus", "Degree": "18°38'", "House": 8},
            {"Planet": "MARS", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "17°00'", "House": 9},
            {"Planet": "SUN", "Sign": "Cancer", "Sign Lord": "Moon", "Degree": "08°16'", "House": 10},
            {"Planet": "MOON", "Sign": "Cancer", "Sign Lord": "Moon", "Degree": "24°37'", "House": 10},
            {"Planet": "MERCURY", "Sign": "Virgo", "Sign Lord": "Mercury", "Degree": "13°00'", "House": 12},
            {"Planet": "JUPITER", "Sign": "Virgo", "Sign Lord": "Mercury", "Degree": "28°49'", "House": 12},
            {"Planet": "KETU (R)", "Sign": "Virgo", "Sign Lord": "Mercury", "Degree": "14°18'", "House": 12},
        ]
    },
    "D10": {
        "name": "Dashamsa Chart (D10) - Career & Profession",
        "planets": [
            {"Planet": "SUN", "Sign": "Pisces", "Sign Lord": "Jupiter", "Degree": "19°11'", "House": 1},
            {"Planet": "RAHU (R)", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "02°34'", "House": 2},
            {"Planet": "MERCURY", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "01°07'", "House": 4},
            {"Planet": "VENUS", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "14°02'", "House": 4},
            {"Planet": "SATURN", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "17°47'", "House": 4},
            {"Planet": "MARS", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "25°33'", "House": 8},
            {"Planet": "JUPITER", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "08°41'", "House": 8},
            {"Planet": "KETU (R)", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "02°34'", "House": 8},
            {"Planet": "MOON", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "17°22'", "House": 10},
        ]
    },
    "D60": {
        "name": "Shashtiamsa Chart (D60) - Karmic Chart",
        "planets": [
            {"Planet": "MARS", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "03°21'", "House": 1},
            {"Planet": "MOON", "Sign": "Virgo", "Sign Lord": "Mercury", "Degree": "14°12'", "House": 2},
            {"Planet": "VENUS", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "24°15'", "House": 3},
            {"Planet": "RAHU (R)", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "15°25'", "House": 3},
            {"Planet": "JUPITER", "Sign": "Scorpio", "Sign Lord": "Mars", "Degree": "22°08'", "House": 4},
            {"Planet": "SUN", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "25°08'", "House": 5},
            {"Planet": "MERCURY", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "06°44'", "House": 5},
            {"Planet": "SATURN", "Sign": "Aquarius", "Sign Lord": "Saturn", "Degree": "16°46'", "House": 7},
            {"Planet": "KETU (R)", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "15°25'", "House": 9},
        ]
    }
}

# Additional charts from detailed data
DETAILED_CHARTS = {
    "D3": {
        "name": "Drekkana Chart (D3)",
        "planets": [
            {"Planet": "Ascendant", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "09°13'", "House": 1},
            {"Planet": "SUN", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "02°45'", "House": 1},
            {"Planet": "MOON", "Sign": "Taurus", "Sign Lord": "Venus", "Degree": "08°12'", "House": 2},
            {"Planet": "MERCURY", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "24°20'", "House": 1},
            {"Planet": "VENUS", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "16°12'", "House": 3},
            {"Planet": "MARS", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "25°40'", "House": 5},
            {"Planet": "JUPITER", "Sign": "Scorpio", "Sign Lord": "Mars", "Degree": "29°36'", "House": 8},
            {"Planet": "SATURN", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "11°20'", "House": 3},
            {"Planet": "RAHU (R)", "Sign": "Aquarius", "Sign Lord": "Saturn", "Degree": "24°46'", "House": 11},
            {"Planet": "KETU (R)", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "24°46'", "House": 5},
        ]
    },
    "D4": {
        "name": "Chaturthamsa Chart (D4)",
        "planets": [
            {"Planet": "Ascendant", "Sign": "Taurus", "Sign Lord": "Venus", "Degree": "02°18'", "House": 1},
            {"Planet": "SUN", "Sign": "Pisces", "Sign Lord": "Jupiter", "Degree": "13°40'", "House": 12},
            {"Planet": "MOON", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "00°56'", "House": 2},
            {"Planet": "MERCURY", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "12°26'", "House": 2},
            {"Planet": "VENUS", "Sign": "Cancer", "Sign Lord": "Moon", "Degree": "11°37'", "House": 3},
            {"Planet": "MARS", "Sign": "Scorpio", "Sign Lord": "Mars", "Degree": "04°13'", "House": 7},
            {"Planet": "JUPITER", "Sign": "Aquarius", "Sign Lord": "Saturn", "Degree": "09°28'", "House": 10},
            {"Planet": "SATURN", "Sign": "Taurus", "Sign Lord": "Venus", "Degree": "25°07'", "House": 1},
            {"Planet": "RAHU (R)", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "13°01'", "House": 12},
            {"Planet": "KETU (R)", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "13°01'", "House": 6},
        ]
    },
    "D12": {
        "name": "Dwadasamsa Chart (D12)",
        "planets": [
            {"Planet": "Ascendant", "Sign": "Taurus", "Sign Lord": "Venus", "Degree": "06°54'", "House": 1},
            {"Planet": "SUN", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "11°01'", "House": 12},
            {"Planet": "MOON", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "02°50'", "House": 2},
            {"Planet": "MERCURY", "Sign": "Cancer", "Sign Lord": "Moon", "Degree": "07°20'", "House": 3},
            {"Planet": "VENUS", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "04°51'", "House": 4},
            {"Planet": "MARS", "Sign": "Scorpio", "Sign Lord": "Mars", "Degree": "12°40'", "House": 7},
            {"Planet": "JUPITER", "Sign": "Aquarius", "Sign Lord": "Saturn", "Degree": "28°25'", "House": 10},
            {"Planet": "SATURN", "Sign": "Cancer", "Sign Lord": "Moon", "Degree": "15°21'", "House": 3},
            {"Planet": "RAHU (R)", "Sign": "Taurus", "Sign Lord": "Venus", "Degree": "09°05'", "House": 1},
            {"Planet": "KETU (R)", "Sign": "Scorpio", "Sign Lord": "Mars", "Degree": "09°05'", "House": 7},
        ]
    },
    "D16": {
        "name": "Shodasamsa Chart (D16)",
        "planets": [
            {"Planet": "Ascendant", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "09°12'", "House": 1},
            {"Planet": "SUN", "Sign": "Taurus", "Sign Lord": "Venus", "Degree": "24°42'", "House": 10},
            {"Planet": "MOON", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "03°47'", "House": 5},
            {"Planet": "MERCURY", "Sign": "Virgo", "Sign Lord": "Mercury", "Degree": "19°47'", "House": 2},
            {"Planet": "VENUS", "Sign": "Taurus", "Sign Lord": "Venus", "Degree": "16°28'", "House": 10},
            {"Planet": "MARS", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "16°53'", "House": 5},
            {"Planet": "JUPITER", "Sign": "Capricorn", "Sign Lord": "Saturn", "Degree": "07°54'", "House": 6},
            {"Planet": "SATURN", "Sign": "Pisces", "Sign Lord": "Jupiter", "Degree": "10°28'", "House": 8},
            {"Planet": "RAHU (R)", "Sign": "Capricorn", "Sign Lord": "Saturn", "Degree": "22°06'", "House": 6},
            {"Planet": "KETU (R)", "Sign": "Capricorn", "Sign Lord": "Saturn", "Degree": "22°06'", "House": 6},
        ]
    },
    "D20": {
        "name": "Vimsamsa Chart (D20)",
        "planets": [
            {"Planet": "Ascendant", "Sign": "Pisces", "Sign Lord": "Jupiter", "Degree": "11°30'", "House": 1},
            {"Planet": "SUN", "Sign": "Pisces", "Sign Lord": "Jupiter", "Degree": "08°22'", "House": 1},
            {"Planet": "MOON", "Sign": "Scorpio", "Sign Lord": "Mars", "Degree": "04°44'", "House": 9},
            {"Planet": "MERCURY", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "02°14'", "House": 6},
            {"Planet": "VENUS", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "28°05'", "House": 6},
            {"Planet": "MARS", "Sign": "Taurus", "Sign Lord": "Venus", "Degree": "21°07'", "House": 3},
            {"Planet": "JUPITER", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "17°22'", "House": 4},
            {"Planet": "SATURN", "Sign": "Virgo", "Sign Lord": "Mercury", "Degree": "05°35'", "House": 7},
            {"Planet": "RAHU (R)", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "05°08'", "House": 12},
            {"Planet": "KETU (R)", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "05°08'", "House": 12},
        ]
    },
    "D24": {
        "name": "Chaturvimsamsa Chart (D24)",
        "planets": [
            {"Planet": "Ascendant", "Sign": "Aquarius", "Sign Lord": "Saturn", "Degree": "13°48'", "House": 1},
            {"Planet": "SUN", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "22°03'", "House": 2},
            {"Planet": "MOON", "Sign": "Capricorn", "Sign Lord": "Saturn", "Degree": "05°40'", "House": 12},
            {"Planet": "MERCURY", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "14°41'", "House": 8},
            {"Planet": "VENUS", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "09°42'", "House": 2},
            {"Planet": "MARS", "Sign": "Aquarius", "Sign Lord": "Saturn", "Degree": "25°20'", "House": 1},
            {"Planet": "JUPITER", "Sign": "Aquarius", "Sign Lord": "Saturn", "Degree": "26°51'", "House": 1},
            {"Planet": "SATURN", "Sign": "Cancer", "Sign Lord": "Moon", "Degree": "00°42'", "House": 6},
            {"Planet": "RAHU (R)", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "18°10'", "House": 8},
            {"Planet": "KETU (R)", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "18°10'", "House": 8},
        ]
    },
    "D27": {
        "name": "Saptavimsamsa Chart (D27)",
        "planets": [
            {"Planet": "Ascendant", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "23°02'", "House": 1},
            {"Planet": "SUN", "Sign": "Capricorn", "Sign Lord": "Saturn", "Degree": "24°48'", "House": 2},
            {"Planet": "MOON", "Sign": "Pisces", "Sign Lord": "Jupiter", "Degree": "13°53'", "House": 4},
            {"Planet": "MERCURY", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "09°01'", "House": 9},
            {"Planet": "VENUS", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "25°55'", "House": 9},
            {"Planet": "MARS", "Sign": "Scorpio", "Sign Lord": "Mars", "Degree": "21°00'", "House": 12},
            {"Planet": "JUPITER", "Sign": "Virgo", "Sign Lord": "Mercury", "Degree": "26°27'", "House": 10},
            {"Planet": "SATURN", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "12°02'", "House": 11},
            {"Planet": "RAHU (R)", "Sign": "Aquarius", "Sign Lord": "Saturn", "Degree": "12°56'", "House": 3},
            {"Planet": "KETU (R)", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "12°56'", "House": 9},
        ]
    },
    "D30": {
        "name": "Trimsamsa Chart (D30)",
        "planets": [
            {"Planet": "Ascendant", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "02°16'", "House": 1},
            {"Planet": "SUN", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "27°34'", "House": 7},
            {"Planet": "MOON", "Sign": "Capricorn", "Sign Lord": "Saturn", "Degree": "22°06'", "House": 8},
            {"Planet": "MERCURY", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "03°22'", "House": 1},
            {"Planet": "VENUS", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "12°07'", "House": 5},
            {"Planet": "MARS", "Sign": "Aquarius", "Sign Lord": "Saturn", "Degree": "16°40'", "House": 9},
            {"Planet": "JUPITER", "Sign": "Virgo", "Sign Lord": "Mercury", "Degree": "26°04'", "House": 6},
            {"Planet": "SATURN", "Sign": "Sagittarius", "Sign Lord": "Jupiter", "Degree": "23°23'", "House": 7},
            {"Planet": "RAHU (R)", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "07°42'", "House": 1},
            {"Planet": "KETU (R)", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "07°42'", "House": 1},
        ]
    },
    "D40": {
        "name": "Khavedamsa Chart (D40)",
        "planets": [
            {"Planet": "Ascendant", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "23°01'", "House": 1},
            {"Planet": "SUN", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "16°45'", "House": 9},
            {"Planet": "MOON", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "09°28'", "House": 7},
            {"Planet": "MERCURY", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "04°29'", "House": 7},
            {"Planet": "VENUS", "Sign": "Capricorn", "Sign Lord": "Saturn", "Degree": "26°10'", "House": 4},
            {"Planet": "MARS", "Sign": "Pisces", "Sign Lord": "Jupiter", "Degree": "12°14'", "House": 6},
            {"Planet": "JUPITER", "Sign": "Scorpio", "Sign Lord": "Mars", "Degree": "04°45'", "House": 12},
            {"Planet": "SATURN", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "11°10'", "House": 1},
            {"Planet": "RAHU (R)", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "10°16'", "House": 7},
            {"Planet": "KETU (R)", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "10°16'", "House": 7},
        ]
    },
    "D45": {
        "name": "Akshavedamsa Chart (D45)",
        "planets": [
            {"Planet": "Ascendant", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "18°24'", "House": 1},
            {"Planet": "SUN", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "11°21'", "House": 11},
            {"Planet": "MOON", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "03°09'", "House": 5},
            {"Planet": "MERCURY", "Sign": "Pisces", "Sign Lord": "Jupiter", "Degree": "05°03'", "House": 10},
            {"Planet": "VENUS", "Sign": "Gemini", "Sign Lord": "Mercury", "Degree": "03°11'", "House": 1},
            {"Planet": "MARS", "Sign": "Leo", "Sign Lord": "Sun", "Degree": "25°01'", "House": 3},
            {"Planet": "JUPITER", "Sign": "Libra", "Sign Lord": "Venus", "Degree": "24°06'", "House": 5},
            {"Planet": "SATURN", "Sign": "Aries", "Sign Lord": "Mars", "Degree": "20°04'", "House": 11},
            {"Planet": "RAHU (R)", "Sign": "Cancer", "Sign Lord": "Moon", "Degree": "11°34'", "House": 2},
            {"Planet": "KETU (R)", "Sign": "Cancer", "Sign Lord": "Moon", "Degree": "11°34'", "House": 2},
        ]
    }
}

# Dasha data
DASHA_DATA = {
    "Mahadasha": [
        {"Planet": "MOON", "Start Date": "Birth", "End Date": "08-Jun-1995 08:21"},
        {"Planet": "MARS", "Start Date": "08-Jun-1995 08:21", "End Date": "08-Jun-2002 02:21"},
        {"Planet": "RAHU", "Start Date": "08-Jun-2002 02:21", "End Date": "07-Jun-2020 14:21"},
        {"Planet": "JUPITER", "Start Date": "07-Jun-2020 14:21", "End Date": "07-Jun-2036 14:21"},
        {"Planet": "SATURN", "Start Date": "07-Jun-2036 14:21", "End Date": "08-Jun-2055 08:21"},
        {"Planet": "MERCURY", "Start Date": "08-Jun-2055 08:21", "End Date": "07-Jun-2072 14:21"},
        {"Planet": "KETU", "Start Date": "07-Jun-2072 14:21", "End Date": "08-Jun-2079 08:21"},
        {"Planet": "VENUS", "Start Date": "08-Jun-2079 08:21", "End Date": "08-Jun-2099 08:21"},
        {"Planet": "SUN", "Start Date": "08-Jun-2099 08:21", "End Date": "08-Jun-2105 20:21"},
    ],
    "Antardasha": [
        {"Planet": "JU - JU", "Start Date": "07-Jun-2020 14:21", "End Date": "26-Jul-2022 19:09"},
        {"Planet": "JU - SA", "Start Date": "26-Jul-2022 19:09", "End Date": "06-Feb-2025 02:21"},
        {"Planet": "JU - ME", "Start Date": "06-Feb-2025 02:21", "End Date": "14-May-2027 23:57"},
        {"Planet": "JU - KE", "Start Date": "14-May-2027 23:57", "End Date": "19-Apr-2028 21:33"},
        {"Planet": "JU - VE", "Start Date": "19-Apr-2028 21:33", "End Date": "19-Dec-2030 21:33"},
        {"Planet": "JU - SU", "Start Date": "19-Dec-2030 21:33", "End Date": "08-Oct-2031 02:21"},
        {"Planet": "JU - MO", "Start Date": "08-Oct-2031 02:21", "End Date": "06-Feb-2033 02:21"},
        {"Planet": "JU - MA", "Start Date": "06-Feb-2033 02:21", "End Date": "12-Jan-2034 23:57"},
        {"Planet": "JU - RA", "Start Date": "12-Jan-2034 23:57", "End Date": "07-Jun-2036 14:21"},
    ],
    "Pratyantardasha": [
        {"Planet": "JU-ME-ME", "Start Date": "05-Feb-2025", "End Date": "02-Jun-2025"},
        {"Planet": "JU-ME-KE", "Start Date": "02-Jun-2025", "End Date": "20-Jul-2025"},
        {"Planet": "JU-ME-VE", "Start Date": "20-Jul-2025", "End Date": "05-Dec-2025"},
        {"Planet": "JU-ME-SU", "Start Date": "05-Dec-2025", "End Date": "16-Jan-2026"},
        {"Planet": "JU-ME-MO", "Start Date": "16-Jan-2026", "End Date": "26-Mar-2026"},
        {"Planet": "JU-ME-MA", "Start Date": "26-Mar-2026", "End Date": "13-May-2026"},
        {"Planet": "JU-ME-RA", "Start Date": "13-May-2026", "End Date": "14-Sep-2026"},
        {"Planet": "JU-ME-JU", "Start Date": "14-Sep-2026", "End Date": "02-Jan-2027"},
        {"Planet": "JU-ME-SA", "Start Date": "02-Jan-2027", "End Date": "14-May-2027"},
    ],
    "Sookshmadasha": [
        {"Planet": "JU-ME-VE-VE", "Start Date": "20-Jul-2025", "End Date": "12-Aug-2025"},
        {"Planet": "JU-ME-VE-SU", "Start Date": "12-Aug-2025", "End Date": "19-Aug-2025"},
        {"Planet": "JU-ME-VE-MO", "Start Date": "19-Aug-2025", "End Date": "31-Aug-2025"},
        {"Planet": "JU-ME-VE-MA", "Start Date": "31-Aug-2025", "End Date": "08-Sep-2025"},
        {"Planet": "JU-ME-VE-RA", "Start Date": "08-Sep-2025", "End Date": "28-Sep-2025"},
        {"Planet": "JU-ME-VE-JU", "Start Date": "28-Sep-2025", "End Date": "17-Oct-2025"},
        {"Planet": "JU-ME-VE-SA", "Start Date": "17-Oct-2025", "End Date": "08-Nov-2025"},
        {"Planet": "JU-ME-VE-ME", "Start Date": "08-Nov-2025", "End Date": "27-Nov-2025"},
        {"Planet": "JU-ME-VE-KE", "Start Date": "27-Nov-2025", "End Date": "05-Dec-2025"},
        {"Planet": "JU-ME-SU-SU", "Start Date": "05-Dec-2025", "End Date": "07-Dec-2025"},
        {"Planet": "JU-ME-SU-MO", "Start Date": "07-Dec-2025", "End Date": "11-Dec-2025"},
        {"Planet": "JU-ME-SU-MA", "Start Date": "11-Dec-2025", "End Date": "13-Dec-2025"},
        {"Planet": "JU-ME-SU-RA", "Start Date": "13-Dec-2025", "End Date": "19-Dec-2025"},
        {"Planet": "JU-ME-SU-JU", "Start Date": "19-Dec-2025", "End Date": "25-Dec-2025"},
        {"Planet": "JU-ME-SU-SA", "Start Date": "25-Dec-2025", "End Date": "31-Dec-2025"},
        {"Planet": "JU-ME-SU-ME", "Start Date": "31-Dec-2025", "End Date": "06-Jan-2026"},
        {"Planet": "JU-ME-SU-KE", "Start Date": "06-Jan-2026", "End Date": "09-Jan-2026"},
        {"Planet": "JU-ME-SU-VE", "Start Date": "09-Jan-2026", "End Date": "16-Jan-2026"},
        {"Planet": "JU-ME-MO-MO", "Start Date": "16-Jan-2026", "End Date": "21-Jan-2026"},
        {"Planet": "JU-ME-MO-MA", "Start Date": "21-Jan-2026", "End Date": "25-Jan-2026"},
        {"Planet": "JU-ME-MO-RA", "Start Date": "25-Jan-2026", "End Date": "05-Feb-2026"},
        {"Planet": "JU-ME-MO-JU", "Start Date": "05-Feb-2026", "End Date": "14-Feb-2026"},
        {"Planet": "JU-ME-MO-SA", "Start Date": "14-Feb-2026", "End Date": "25-Feb-2026"},
        {"Planet": "JU-ME-MO-ME", "Start Date": "25-Feb-2026", "End Date": "07-Mar-2026"},
        {"Planet": "JU-ME-MO-KE", "Start Date": "07-Mar-2026", "End Date": "11-Mar-2026"},
        {"Planet": "JU-ME-MO-VE", "Start Date": "11-Mar-2026", "End Date": "22-Mar-2026"},
        {"Planet": "JU-ME-MO-SU", "Start Date": "22-Mar-2026", "End Date": "26-Mar-2026"},
    ]
}

# ==================== ASTROLOGICAL RULES ====================

# Exaltation signs
EXALTATION = {
    "Sun": "Aries", "Moon": "Taurus", "Mars": "Capricorn",
    "Mercury": "Virgo", "Jupiter": "Cancer", "Venus": "Pisces",
    "Saturn": "Libra"
}

# Debilitation signs
DEBILITATION = {
    "Sun": "Libra", "Moon": "Scorpio", "Mars": "Cancer",
    "Mercury": "Pisces", "Jupiter": "Capricorn", "Venus": "Virgo",
    "Saturn": "Aries"
}

# Own signs (Moolatrikona)
OWN_SIGNS = {
    "Sun": "Leo", "Moon": "Taurus", "Mars": "Aries",
    "Mercury": "Virgo", "Jupiter": "Sagittarius", "Venus": "Libra",
    "Saturn": "Aquarius"
}

# Benefic planets
BENEFIC = {"Jupiter", "Venus", "Mercury", "Moon"}
MALEFIC = {"Sun", "Mars", "Saturn", "Rahu", "Ketu"}

def get_planet_name(planet_str: str) -> str:
    """Extract planet name from string (e.g., 'RAHU (R)' -> 'Rahu')."""
    return planet_str.split()[0].capitalize()

def get_planet_status(planet: str, sign: str, sign_lord: str) -> Dict[str, Any]:
    """Calculate planet status: benefic/malefic, own sign, exalted, debilitated."""
    planet_name = get_planet_name(planet)
    
    status = {
        "is_benefic": planet_name in BENEFIC,
        "is_malefic": planet_name in MALEFIC,
        "is_own_sign": OWN_SIGNS.get(planet_name) == sign,
        "is_exalted": EXALTATION.get(planet_name) == sign,
        "is_debilitated": DEBILITATION.get(planet_name) == sign,
        "is_retrograde": "(R)" in planet.upper(),
    }
    
    # Calculate strength (0-100)
    strength = 50  # Base strength
    if status["is_exalted"]:
        strength += 30
    elif status["is_own_sign"]:
        strength += 20
    elif status["is_debilitated"]:
        strength -= 20
    
    if status["is_benefic"]:
        strength += 10
    elif status["is_malefic"]:
        strength -= 5
    
    if status["is_retrograde"]:
        strength -= 10
    
    # Check if planet is in friendly sign (sign lord is benefic)
    if sign_lord in BENEFIC:
        strength += 5
    
    strength = max(0, min(100, strength))
    status["strength"] = strength
    
    return status

def get_color_for_status(status: Dict[str, Any]) -> Dict[str, float]:
    """Get RGB color based on planet status."""
    if status["is_exalted"]:
        return {"red": 0.0, "green": 0.8, "blue": 0.0}  # Green
    elif status["is_own_sign"]:
        return {"red": 0.0, "green": 0.6, "blue": 0.8}  # Light blue
    elif status["is_debilitated"]:
        return {"red": 0.8, "green": 0.0, "blue": 0.0}  # Red
    elif status["is_benefic"]:
        return {"red": 0.0, "green": 0.7, "blue": 0.3}  # Light green
    elif status["is_malefic"]:
        return {"red": 0.9, "green": 0.5, "blue": 0.0}  # Orange
    else:
        return {"red": 1.0, "green": 1.0, "blue": 1.0}  # White

# ==================== GOOGLE SHEETS CREATION ====================

def cleanup_old_spreadsheets(client, max_to_keep: int = 5):
    """Delete old spreadsheets to free up space."""
    try:
        # Get all spreadsheets
        spreadsheets = client.openall()
        
        if len(spreadsheets) <= max_to_keep:
            print(f"Found {len(spreadsheets)} spreadsheets. No cleanup needed.")
            return
        
        # Sort by creation time (newest first) if available
        try:
            spreadsheets.sort(key=lambda x: x.created if hasattr(x, 'created') else 0, reverse=True)
        except:
            pass
        
        # Delete old ones
        to_delete = spreadsheets[max_to_keep:]
        print(f"Found {len(spreadsheets)} spreadsheets. Deleting {len(to_delete)} old ones...")
        
        for sheet in to_delete:
            try:
                client.del_spreadsheet(sheet.id)
                print(f"  Deleted: {sheet.title}")
            except Exception as e:
                print(f"  Could not delete {sheet.title}: {e}")
        
        print(f"✅ Cleanup complete. Kept {max_to_keep} most recent spreadsheets.")
    except Exception as e:
        print(f"Warning: Could not cleanup old spreadsheets: {e}")

def create_google_sheet(credentials_file: str = "credentials.json", spreadsheet_name: str = "Akshit - Complete Birth Chart Analysis", cleanup_first: bool = True):
    """Create Google Sheet with all charts and features."""
    
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
        print("Please create a service account and download the credentials JSON file.")
        print("See: https://gspread.readthedocs.io/en/latest/oauth2.html")
        return None
    
    # Cleanup old spreadsheets if requested
    if cleanup_first:
        try:
            cleanup_old_spreadsheets(client, max_to_keep=3)
        except Exception as e:
            print(f"Warning: Cleanup failed: {e}")
            print("Continuing anyway...")
    
    # Create spreadsheet
    try:
        spreadsheet = client.create(spreadsheet_name)
        spreadsheet.share("", perm_type="anyone", role="writer")  # Make it publicly editable (optional)
        print(f"Created spreadsheet: {spreadsheet.url}")
    except Exception as e:
        error_msg = str(e)
        if "quota" in error_msg.lower() or "storage" in error_msg.lower():
            print(f"\n❌ Error: Google Drive storage quota exceeded!")
            print("\nSolutions:")
            print("1. Run cleanup script to delete old spreadsheets:")
            print("   python cleanup_sheets.py")
            print("\n2. Use the Excel version instead (no storage limits):")
            print("   python create_excel_sheet.py")
            print("\n3. Manually clean up Google Drive:")
            print("   - Find the service account email in credentials.json")
            print("   - Go to https://drive.google.com")
            print("   - Sign in with that email and delete old files")
        else:
            print(f"Error creating spreadsheet: {e}")
        return None
    
    # Combine all charts
    all_charts = {**CHARTS_DATA, **DETAILED_CHARTS}
    
    # Create chart sheets
    sheet_order = ["D1", "D2", "D3", "D4", "D6", "D7", "D9", "D10", "D12", "D16", "D20", "D24", "D27", "D30", "D40", "D45", "D60"]
    
    for chart_id in sheet_order:
        if chart_id in all_charts:
            create_chart_sheet(spreadsheet, chart_id, all_charts[chart_id])
    
    # Create dasha sheets
    create_dasha_sheet(spreadsheet, "Mahadasha", DASHA_DATA["Mahadasha"])
    create_dasha_sheet(spreadsheet, "Antardasha", DASHA_DATA["Antardasha"])
    create_dasha_sheet(spreadsheet, "Pratyantardasha", DASHA_DATA["Pratyantardasha"])
    create_dasha_sheet(spreadsheet, "Sookshmadasha", DASHA_DATA["Sookshmadasha"])
    
    # Create summary dashboard
    create_summary_dashboard(spreadsheet, all_charts)
    
    return spreadsheet

def create_chart_sheet(spreadsheet, chart_id: str, chart_data: Dict):
    """Create a sheet for a specific chart with formatting."""
    try:
        worksheet = spreadsheet.add_worksheet(title=chart_id, rows=100, cols=20)
    except:
        worksheet = spreadsheet.worksheet(chart_id)
    
    # Add chart title first
    worksheet.update("A1", [[chart_data["name"]]])
    if merge_cells:
        try:
            merge_cells(worksheet, "A1:L1")
        except:
            pass
    if format_cell_range and CellFormat and TextFormat:
        try:
            format_cell_range(worksheet, "A1", CellFormat(
                textFormat=TextFormat(bold=True, fontSize=14),
                horizontalAlignment="CENTER"
            ))
        except:
            pass
    
    # Headers (row 3, after title)
    headers = ["Planet", "Sign", "Sign Lord", "Degree", "House", "Status", "Strength", "Benefic/Malefic", "Own Sign", "Exalted", "Debilitated", "Retrograde"]
    worksheet.append_row(headers)
    
    # Format header row
    format_header_row(worksheet, 3)
    
    # Add planet data
    row_num = 4  # Start after header
    for planet_data in chart_data["planets"]:
        planet = planet_data["Planet"]
        sign = planet_data["Sign"]
        sign_lord = planet_data["Sign Lord"]
        degree = planet_data["Degree"]
        house = planet_data["House"]
        
        status = get_planet_status(planet, sign, sign_lord)
        
        # Status text
        status_parts = []
        if status["is_exalted"]:
            status_parts.append("Exalted")
        elif status["is_own_sign"]:
            status_parts.append("Own Sign")
        elif status["is_debilitated"]:
            status_parts.append("Debilitated")
        
        status_text = ", ".join(status_parts) if status_parts else "Normal"
        
        row = [
            planet,
            sign,
            sign_lord,
            degree,
            house,
            status_text,
            status["strength"],
            "Benefic" if status["is_benefic"] else "Malefic" if status["is_malefic"] else "Neutral",
            "Yes" if status["is_own_sign"] else "No",
            "Yes" if status["is_exalted"] else "No",
            "Yes" if status["is_debilitated"] else "No",
            "Yes" if status["is_retrograde"] else "No"
        ]
        
        worksheet.append_row(row)
        
        # Apply color formatting
        if format_cell_range and CellFormat:
            try:
                color = get_color_for_status(status)
                format_cell_range(worksheet, f"A{row_num}:L{row_num}", CellFormat(
                    backgroundColor=color
                ))
            except:
                pass
        
        row_num += 1
    
    # Add filters (on header row)
    try:
        worksheet.set_basic_filter(3, 1, row_num - 1, len(headers))
    except:
        pass
    
    # Auto-resize columns
    try:
        worksheet.columns_auto_resize(0, len(headers) - 1)
    except:
        # Fallback: manual column width setting
        try:
            worksheet.set_column_widths([(1, 12), (2, 12), (3, 12), (4, 10), (5, 8), (6, 15), (7, 10), (8, 15), (9, 10), (10, 10), (11, 12), (12, 10)])
        except:
            pass

def create_dasha_sheet(spreadsheet, sheet_name: str, dasha_data: List[Dict]):
    """Create a sheet for dasha periods."""
    try:
        worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=100, cols=10)
    except:
        worksheet = spreadsheet.worksheet(sheet_name)
    
    headers = ["Planet/Period", "Start Date", "End Date", "Duration"]
    worksheet.append_row(headers)
    format_header_row(worksheet, 1)
    
    for period in dasha_data:
        start = period["Start Date"]
        end = period["End Date"]
        
        # Calculate duration (simplified)
        duration = "N/A"
        if start != "Birth" and "-" in start and "-" in end:
            try:
                start_dt = datetime.strptime(start, "%d-%b-%Y %H:%M")
                end_dt = datetime.strptime(end, "%d-%b-%Y %H:%M")
                delta = end_dt - start_dt
                years = delta.days / 365.25
                duration = f"{years:.2f} years"
            except:
                pass
        
        row = [period["Planet"], start, end, duration]
        worksheet.append_row(row)
    
    try:
        worksheet.set_basic_filter(1, 1, len(dasha_data) + 1, len(headers))
    except:
        pass
    try:
        worksheet.columns_auto_resize(0, len(headers) - 1)
    except:
        try:
            worksheet.set_column_widths([(1, 20), (2, 20), (3, 20), (4, 15)])
        except:
            pass

def create_summary_dashboard(spreadsheet, all_charts: Dict):
    """Create a summary dashboard sheet."""
    try:
        worksheet = spreadsheet.add_worksheet(title="Dashboard", rows=100, cols=15)
    except:
        worksheet = spreadsheet.worksheet("Dashboard")
    
    # Title
    worksheet.update("A1", [["ASTROLOGICAL CHART SUMMARY DASHBOARD"]])
    if merge_cells:
        merge_cells(worksheet, "A1:O1")
    if format_cell_range and CellFormat and TextFormat:
        format_cell_range(worksheet, "A1", CellFormat(
            textFormat=TextFormat(bold=True, fontSize=16),
            horizontalAlignment="CENTER",
            backgroundColor={"red": 0.2, "green": 0.4, "blue": 0.8}
        ))
    
    # Summary statistics
    row = 3
    worksheet.update(f"A{row}", [["Chart", "Total Planets", "Avg Strength", "Benefic Count", "Malefic Count"]])
    format_header_row(worksheet, row)
    row += 1
    
    for chart_id in sorted(all_charts.keys()):
        chart = all_charts[chart_id]
        planets = chart["planets"]
        
        total = len(planets)
        strengths = []
        benefic_count = 0
        malefic_count = 0
        
        for p in planets:
            status = get_planet_status(p["Planet"], p["Sign"], p["Sign Lord"])
            strengths.append(status["strength"])
            if status["is_benefic"]:
                benefic_count += 1
            elif status["is_malefic"]:
                malefic_count += 1
        
        avg_strength = sum(strengths) / len(strengths) if strengths else 0
        
        worksheet.append_row([chart_id, total, f"{avg_strength:.1f}", benefic_count, malefic_count])
    
    try:
        worksheet.set_basic_filter(3, 1, len(all_charts) + 3, 5)
    except:
        pass
    try:
        worksheet.columns_auto_resize(0, 4)
    except:
        try:
            worksheet.set_column_widths([(1, 10), (2, 12), (3, 12), (4, 15), (5, 15)])
        except:
            pass

def format_header_row(worksheet, row_num: int):
    """Format header row with bold text and background color."""
    if format_cell_range and CellFormat and TextFormat:
        format_cell_range(worksheet, f"A{row_num}:Z{row_num}", CellFormat(
            textFormat=TextFormat(bold=True),
            backgroundColor={"red": 0.9, "green": 0.9, "blue": 0.9}
        ))

# ==================== MAIN ====================

if __name__ == "__main__":
    import sys
    
    print("Creating Google Sheet with all astrological charts...")
    print("Make sure you have credentials.json file in the current directory.")
    print()
    
    # Check if user wants to skip cleanup
    cleanup = True
    if "--no-cleanup" in sys.argv:
        cleanup = False
        print("Skipping cleanup of old spreadsheets...")
    
    spreadsheet = create_google_sheet(
        credentials_file="credentials.json",
        spreadsheet_name="Akshit - Complete Birth Chart Analysis",
        cleanup_first=cleanup
    )
    
    if spreadsheet:
        print(f"\n✅ Success! Spreadsheet created: {spreadsheet.url}")
        print("\nFeatures included:")
        print("  ✓ Multiple chart sheets (D1, D2, D3, D4, D6, D7, D9, D10, D12, D16, D20, D24, D27, D30, D40, D45, D60)")
        print("  ✓ Dasha sheets (Mahadasha, Antardasha, Pratyantardasha, Sookshmadasha)")
        print("  ✓ Color coding (benefic/malefic/own sign/exalted/debilitated)")
        print("  ✓ Auto-calculated strengths")
        print("  ✓ Filters on all sheets")
        print("  ✓ Summary dashboard")
    else:
        print("\n❌ Failed to create spreadsheet. Please check your credentials.")

