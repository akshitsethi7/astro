/**
 * Planetary Position Calculator
 * 
 * Converts raw ephemeris data into complete planetary information
 * including sign, house, nakshatra, and dignity calculations.
 */

import { calculatePlanetaryPositions, type PlanetPosition } from './ephemeris';
import { getNakshatraFromDegree } from './nakshatra';
import type { 
  Planet, 
  ZodiacSign, 
  PlanetData, 
  Dignity,
  ChartData 
} from '@/lib/types/astrology';

/**
 * Zodiac signs in order
 */
export const ZODIAC_SIGNS: readonly ZodiacSign[] = [
  'Aries', 'Taurus', 'Gemini', 'Cancer',
  'Leo', 'Virgo', 'Libra', 'Scorpio',
  'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
] as const;

/**
 * Sign lords (rulers)
 */
export const SIGN_LORDS: Record<ZodiacSign, Planet> = {
  'Aries': 'Mars',
  'Taurus': 'Venus',
  'Gemini': 'Mercury',
  'Cancer': 'Moon',
  'Leo': 'Sun',
  'Virgo': 'Mercury',
  'Libra': 'Venus',
  'Scorpio': 'Mars',
  'Sagittarius': 'Jupiter',
  'Capricorn': 'Saturn',
  'Aquarius': 'Saturn',
  'Pisces': 'Jupiter',
};

/**
 * Exaltation signs and degrees
 */
const EXALTATION: Record<Planet, { sign: ZodiacSign; degree: number }> = {
  'Sun': { sign: 'Aries', degree: 10 },
  'Moon': { sign: 'Taurus', degree: 3 },
  'Mars': { sign: 'Capricorn', degree: 28 },
  'Mercury': { sign: 'Virgo', degree: 15 },
  'Jupiter': { sign: 'Cancer', degree: 5 },
  'Venus': { sign: 'Pisces', degree: 27 },
  'Saturn': { sign: 'Libra', degree: 20 },
  'Rahu': { sign: 'Taurus', degree: 15 },
  'Ketu': { sign: 'Scorpio', degree: 15 },
};

/**
 * Debilitation signs (opposite to exaltation)
 */
const DEBILITATION: Record<Planet, ZodiacSign> = {
  'Sun': 'Libra',
  'Moon': 'Scorpio',
  'Mars': 'Cancer',
  'Mercury': 'Pisces',
  'Jupiter': 'Capricorn',
  'Venus': 'Virgo',
  'Saturn': 'Aries',
  'Rahu': 'Scorpio',
  'Ketu': 'Taurus',
};

/**
 * Own signs for each planet
 */
const OWN_SIGNS: Record<Planet, ZodiacSign[]> = {
  'Sun': ['Leo'],
  'Moon': ['Cancer'],
  'Mars': ['Aries', 'Scorpio'],
  'Mercury': ['Gemini', 'Virgo'],
  'Jupiter': ['Sagittarius', 'Pisces'],
  'Venus': ['Taurus', 'Libra'],
  'Saturn': ['Capricorn', 'Aquarius'],
  'Rahu': [],
  'Ketu': [],
};

/**
 * Friend signs for each planet
 */
const FRIEND_SIGNS: Record<Planet, ZodiacSign[]> = {
  'Sun': ['Aries', 'Sagittarius', 'Scorpio'],
  'Moon': ['Taurus', 'Cancer'],
  'Mars': ['Leo', 'Sagittarius', 'Pisces'],
  'Mercury': ['Taurus', 'Libra', 'Aquarius'],
  'Jupiter': ['Aries', 'Leo', 'Scorpio'],
  'Venus': ['Gemini', 'Virgo', 'Capricorn', 'Aquarius'],
  'Saturn': ['Taurus', 'Libra', 'Gemini'],
  'Rahu': ['Gemini', 'Virgo', 'Sagittarius', 'Pisces'],
  'Ketu': ['Sagittarius', 'Pisces'],
};

/**
 * Enemy signs for each planet
 */
const ENEMY_SIGNS: Record<Planet, ZodiacSign[]> = {
  'Sun': ['Libra', 'Aquarius'],
  'Moon': ['Capricorn'],
  'Mars': ['Gemini', 'Virgo'],
  'Mercury': ['Sagittarius'],
  'Jupiter': ['Gemini', 'Virgo'],
  'Venus': ['Aries', 'Scorpio'],
  'Saturn': ['Aries', 'Leo', 'Scorpio'],
  'Rahu': ['Cancer', 'Leo'],
  'Ketu': ['Gemini', 'Virgo'],
};

/**
 * Convert absolute degree (0-360) to sign and degree within sign
 */
export function getSignFromDegree(absoluteDegree: number): { sign: ZodiacSign; degree: number } {
  const normalized = ((absoluteDegree % 360) + 360) % 360;
  const signIndex = Math.floor(normalized / 30);
  const degreeInSign = normalized % 30;
  
  return {
    sign: ZODIAC_SIGNS[signIndex],
    degree: degreeInSign,
  };
}

/**
 * Calculate planetary dignity
 */
export function calculateDignity(planet: Planet, sign: ZodiacSign): Dignity {
  // Check exaltation
  if (EXALTATION[planet].sign === sign) {
    return 'exalted';
  }
  
  // Check debilitation
  if (DEBILITATION[planet] === sign) {
    return 'debilitated';
  }
  
  // Check own sign
  if (OWN_SIGNS[planet].includes(sign)) {
    return 'own';
  }
  
  // Check friend sign
  if (FRIEND_SIGNS[planet].includes(sign)) {
    return 'friend';
  }
  
  // Check enemy sign
  if (ENEMY_SIGNS[planet].includes(sign)) {
    return 'enemy';
  }
  
  return 'neutral';
}

/**
 * Calculate which house a planet occupies
 */
export function calculateHouse(
  planetDegree: number,
  ascendantDegree: number,
  houseSystem: 'equal' | 'whole-sign' = 'whole-sign'
): number {
  if (houseSystem === 'whole-sign') {
    // Whole sign houses: each sign is one house
    const planetSign = Math.floor(planetDegree / 30);
    const ascSign = Math.floor(ascendantDegree / 30);
    let house = planetSign - ascSign + 1;
    if (house <= 0) house += 12;
    return house;
  } else {
    // Equal houses: 30° from ascendant degree
    let diff = planetDegree - ascendantDegree;
    if (diff < 0) diff += 360;
    return Math.floor(diff / 30) + 1;
  }
}

/**
 * Calculate complete planetary data from ephemeris position
 */
export function enrichPlanetData(
  position: PlanetPosition,
  ascendantDegree: number
): PlanetData {
  const { sign, degree } = getSignFromDegree(position.longitude);
  const nakshatraInfo = getNakshatraFromDegree(position.longitude);
  const dignity = calculateDignity(position.planet, sign);
  const house = calculateHouse(position.longitude, ascendantDegree);
  
  return {
    sign,
    degree,
    absoluteDegree: position.longitude,
    house,
    nakshatra: nakshatraInfo.nakshatra,
    nakshatraPada: nakshatraInfo.pada,
    nakshatraLord: nakshatraInfo.lord,
    retrograde: position.isRetrograde,
    dignity,
    speed: position.speed,
  };
}

/**
 * Calculate ascendant (Lagna) for a given date, time, and location
 * Uses proper sidereal time calculation
 */
export function calculateAscendant(
  date: Date,
  latitude: number,
  longitude: number
): { sign: ZodiacSign; degree: number; absoluteDegree: number } {
  // Calculate Julian Day
  const year = date.getUTCFullYear();
  const month = date.getUTCMonth() + 1;
  const day = date.getUTCDate();
  const hour = date.getUTCHours() + date.getUTCMinutes() / 60 + date.getUTCSeconds() / 3600;
  
  let a = Math.floor((14 - month) / 12);
  let y = year + 4800 - a;
  let m = month + 12 * a - 3;
  
  let jdn = day + Math.floor((153 * m + 2) / 5) + 365 * y + Math.floor(y / 4) - Math.floor(y / 100) + Math.floor(y / 400) - 32045;
  let jd = jdn + (hour - 12) / 24;
  
  // Calculate Greenwich Sidereal Time (GST)
  const T = (jd - 2451545.0) / 36525;
  let gst = 280.46061837 + 360.98564736629 * (jd - 2451545.0) + 0.000387933 * T * T - T * T * T / 38710000;
  
  // Normalize GST to 0-360
  gst = ((gst % 360) + 360) % 360;
  
  // Calculate Local Sidereal Time (LST)
  let lst = gst + longitude;
  lst = ((lst % 360) + 360) % 360;
  
  // Calculate RAMC (Right Ascension of Midheaven)
  const ramc = lst;
  
  // Convert latitude to radians
  const latRad = latitude * Math.PI / 180;
  
  // Calculate obliquity of ecliptic
  const epsilon = 23.4393 - 0.0000004 * (jd - 2451545.0);
  const epsilonRad = epsilon * Math.PI / 180;
  
  // Calculate ascendant using the formula:
  // tan(ASC) = cos(RAMC) / (-sin(RAMC) * cos(epsilon) - tan(latitude) * sin(epsilon))
  const ramcRad = ramc * Math.PI / 180;
  
  let ascRad = Math.atan2(
    Math.cos(ramcRad),
    -Math.sin(ramcRad) * Math.cos(epsilonRad) - Math.tan(latRad) * Math.sin(epsilonRad)
  );
  
  // Convert to degrees
  let ascDegree = ascRad * 180 / Math.PI;
  
  // Normalize to 0-360
  ascDegree = ((ascDegree % 360) + 360) % 360;
  
  // Apply Lahiri Ayanamsa for sidereal zodiac
  const ayanamsa = calculateLahiriAyanamsa(date);
  let siderealAsc = ascDegree - ayanamsa;
  siderealAsc = ((siderealAsc % 360) + 360) % 360;
  
  const { sign, degree } = getSignFromDegree(siderealAsc);
  
  return {
    sign,
    degree,
    absoluteDegree: siderealAsc,
  };
}

/**
 * Calculate Lahiri Ayanamsa for a given date
 */
function calculateLahiriAyanamsa(date: Date): number {
  // Lahiri Ayanamsa at 2000.0: 23.85°
  // Rate: approximately 50.29 arc seconds per year
  const year = date.getFullYear() + (date.getMonth() / 12) + (date.getDate() / 365.25);
  const yearsSince2000 = year - 2000;
  const ayanamsa = 23.85 + (yearsSince2000 * 50.29 / 3600);
  return ayanamsa;
}

/**
 * Calculate complete chart data
 */
export function calculateChart(
  birthDate: Date,
  birthTime: string,
  timezone: string,
  latitude: number,
  longitude: number,
  ayanamsa: 'Lahiri' | 'Raman' | 'KP' = 'Lahiri'
): ChartData {
  // Parse birth time
  const [hours, minutes] = birthTime.split(':').map(Number);
  const birthDateTime = new Date(birthDate);
  birthDateTime.setHours(hours, minutes, 0, 0);
  
  // Calculate planetary positions
  const positions = calculatePlanetaryPositions(birthDateTime);
  
  // Calculate ascendant
  const ascendant = calculateAscendant(birthDateTime, latitude, longitude);
  
  // Enrich planet data
  const planetsMap = new Map<Planet, PlanetData>();
  for (const position of positions) {
    const enriched = enrichPlanetData(position, ascendant.absoluteDegree);
    planetsMap.set(position.planet, enriched);
  }
  
  // Calculate houses
  const houses = [];
  for (let i = 1; i <= 12; i++) {
    const houseDegree = (ascendant.absoluteDegree + (i - 1) * 30) % 360;
    const { sign } = getSignFromDegree(houseDegree);
    const lord = SIGN_LORDS[sign];
    
    // Find planets in this house
    const planetsInHouse: Planet[] = [];
    for (const [planet, data] of planetsMap.entries()) {
      if (data.house === i) {
        planetsInHouse.push(planet);
      }
    }
    
    houses.push({
      number: i,
      sign,
      degree: houseDegree % 30,
      lord,
      planets: planetsInHouse,
    });
  }
  
  return {
    birthDate: birthDateTime,
    birthTime,
    timezone,
    latitude,
    longitude,
    ayanamsa,
    ascendant,
    planets: planetsMap,
    houses,
  };
}

/**
 * Get planet color for visualization
 */
export function getPlanetColor(planet: Planet): string {
  const colors: Record<Planet, string> = {
    'Sun': '#FF6B35',
    'Moon': '#4ECDC4',
    'Mars': '#E63946',
    'Mercury': '#06FFA5',
    'Jupiter': '#FFD23F',
    'Venus': '#EE6FF8',
    'Saturn': '#1B9AAA',
    'Rahu': '#8338EC',
    'Ketu': '#FB5607',
  };
  return colors[planet];
}

/**
 * Format degree as string (e.g., "15°23'45\"")
 */
export function formatDegree(degree: number, includeSeconds: boolean = false): string {
  const deg = Math.floor(degree);
  const minDecimal = (degree - deg) * 60;
  const min = Math.floor(minDecimal);
  
  if (includeSeconds) {
    const sec = Math.floor((minDecimal - min) * 60);
    return `${deg}°${min}'${sec}"`;
  }
  
  return `${deg}°${min}'`;
}
