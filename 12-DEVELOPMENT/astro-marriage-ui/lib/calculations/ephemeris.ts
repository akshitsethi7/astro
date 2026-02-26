/**
 * Ephemeris Calculations
 * 
 * Wrapper around astronomy-engine for planetary position calculations.
 * Handles timezone conversions and provides a clean interface for
 * calculating positions of all 9 Vedic planets.
 */

import * as Astronomy from 'astronomy-engine';
import type { Planet } from '@/lib/types/astrology';

/**
 * Configuration for ephemeris calculations
 */
export interface EphemerisConfig {
  /** Ayanamsa value in degrees (default: Lahiri) */
  ayanamsa?: number;
  /** Whether to use tropical (false) or sidereal (true) zodiac */
  useSidereal?: boolean;
}

/**
 * Basic planetary position data from ephemeris
 * This is a simplified version before full chart calculation
 */
export interface PlanetPosition {
  planet: Planet;
  longitude: number; // Absolute degree 0-360
  latitude: number;
  speed: number; // Degrees per day
  isRetrograde: boolean;
}

/**
 * Default Lahiri Ayanamsa for 2000.0 epoch
 * This should be adjusted based on the actual date
 */
const LAHIRI_AYANAMSA_2000 = 23.85;

/**
 * Rate of precession per year (approximately 50.29 arc seconds)
 */
const PRECESSION_RATE_PER_YEAR = 50.29 / 3600; // degrees per year

/**
 * Calculate Lahiri Ayanamsa for a given date
 * 
 * @param date - Date for which to calculate ayanamsa
 * @returns Ayanamsa value in degrees
 */
export function calculateLahiriAyanamsa(date: Date): number {
  const year = date.getFullYear() + (date.getMonth() / 12) + (date.getDate() / 365.25);
  const yearsSince2000 = year - 2000;
  return LAHIRI_AYANAMSA_2000 + (yearsSince2000 * PRECESSION_RATE_PER_YEAR);
}

/**
 * Convert tropical longitude to sidereal longitude
 * 
 * @param tropicalLongitude - Tropical longitude in degrees
 * @param ayanamsa - Ayanamsa value in degrees
 * @returns Sidereal longitude in degrees
 */
export function tropicalToSidereal(tropicalLongitude: number, ayanamsa: number): number {
  let sidereal = tropicalLongitude - ayanamsa;
  
  // Normalize to 0-360 range
  while (sidereal < 0) sidereal += 360;
  while (sidereal >= 360) sidereal -= 360;
  
  return sidereal;
}

/**
 * Calculate planetary position using astronomy-engine
 * 
 * @param body - Astronomy body name
 * @param date - Date and time for calculation
 * @param config - Ephemeris configuration
 * @returns Planetary position data
 */
function calculateBodyPosition(
  body: Astronomy.Body,
  date: Date,
  config: EphemerisConfig = {}
): { longitude: number; latitude: number; speed: number; isRetrograde: boolean } {
  const { ayanamsa, useSidereal = true } = config;
  
  // Calculate ayanamsa if not provided and using sidereal
  const actualAyanamsa = useSidereal 
    ? (ayanamsa ?? calculateLahiriAyanamsa(date))
    : 0;
  
  // Get heliocentric position vector
  const helioVector = Astronomy.HelioVector(body, date);
  
  // Convert to ecliptic coordinates
  const ecliptic = Astronomy.Ecliptic(helioVector);
  
  // Convert to sidereal if needed
  const longitude = useSidereal 
    ? tropicalToSidereal(ecliptic.elon, actualAyanamsa)
    : ecliptic.elon;
  
  // Calculate speed by comparing positions 1 day apart
  const nextDate = new Date(date.getTime() + 24 * 60 * 60 * 1000);
  const nextHelioVector = Astronomy.HelioVector(body, nextDate);
  const nextEcliptic = Astronomy.Ecliptic(nextHelioVector);
  const nextLongitude = useSidereal
    ? tropicalToSidereal(nextEcliptic.elon, actualAyanamsa)
    : nextEcliptic.elon;
  
  // Calculate daily motion (handle 360-degree wrap)
  let dailyMotion = nextLongitude - longitude;
  if (dailyMotion > 180) dailyMotion -= 360;
  if (dailyMotion < -180) dailyMotion += 360;
  
  return {
    longitude,
    latitude: ecliptic.elat,
    speed: dailyMotion,
    isRetrograde: dailyMotion < 0,
  };
}

/**
 * Calculate Rahu (North Node) position
 * Rahu is the ascending node of the Moon
 * 
 * @param date - Date and time for calculation
 * @param config - Ephemeris configuration
 * @returns Rahu position data
 */
function calculateRahuPosition(
  date: Date,
  config: EphemerisConfig = {}
): { longitude: number; latitude: number; speed: number; isRetrograde: boolean } {
  const { ayanamsa, useSidereal = true } = config;
  
  const actualAyanamsa = useSidereal 
    ? (ayanamsa ?? calculateLahiriAyanamsa(date))
    : 0;
  
  // Calculate Moon's ascending node using orbital mechanics
  // The Moon's node regresses approximately 19.3° per year
  const J2000 = new Date('2000-01-01T12:00:00Z');
  const daysSinceJ2000 = (date.getTime() - J2000.getTime()) / (1000 * 60 * 60 * 24);
  
  // Mean longitude of ascending node at J2000: 125.04°
  // Daily motion: -0.0529539° per day
  const meanNode = 125.04 - (0.0529539 * daysSinceJ2000);
  
  // Normalize to 0-360
  let nodeLongitude = ((meanNode % 360) + 360) % 360;
  
  // Convert to sidereal if needed
  const longitude = useSidereal
    ? tropicalToSidereal(nodeLongitude, actualAyanamsa)
    : nodeLongitude;
  
  // Rahu moves retrograde (approximately -3 arc minutes per day)
  const speed = -0.0529539; // degrees per day (retrograde)
  
  return {
    longitude,
    latitude: 0, // Nodes are always on the ecliptic
    speed,
    isRetrograde: true, // Rahu is always retrograde
  };
}

/**
 * Calculate Ketu (South Node) position
 * Ketu is always 180 degrees opposite to Rahu
 * 
 * @param rahuLongitude - Rahu's longitude in degrees
 * @returns Ketu position data
 */
function calculateKetuPosition(
  rahuLongitude: number
): { longitude: number; latitude: number; speed: number; isRetrograde: boolean } {
  let ketuLongitude = rahuLongitude + 180;
  if (ketuLongitude >= 360) ketuLongitude -= 360;
  
  return {
    longitude: ketuLongitude,
    latitude: 0,
    speed: -0.05, // Same retrograde motion as Rahu
    isRetrograde: true,
  };
}

/**
 * Calculate positions for all 9 Vedic planets
 * 
 * @param date - Date and time for calculation (in UTC or with timezone info)
 * @param config - Ephemeris configuration
 * @returns Array of planetary position data
 * 
 * @example
 * ```typescript
 * const date = new Date('1995-01-01T10:30:00Z');
 * const positions = calculatePlanetaryPositions(date);
 * console.log(positions.find(p => p.planet === 'Sun')?.longitude);
 * ```
 */
export function calculatePlanetaryPositions(
  date: Date,
  config: EphemerisConfig = {}
): PlanetPosition[] {
  const positions: PlanetPosition[] = [];
  
  // Calculate positions for the 7 visible planets
  const bodies: Array<{ body: Astronomy.Body; planet: Planet }> = [
    { body: Astronomy.Body.Sun, planet: 'Sun' },
    { body: Astronomy.Body.Moon, planet: 'Moon' },
    { body: Astronomy.Body.Mercury, planet: 'Mercury' },
    { body: Astronomy.Body.Venus, planet: 'Venus' },
    { body: Astronomy.Body.Mars, planet: 'Mars' },
    { body: Astronomy.Body.Jupiter, planet: 'Jupiter' },
    { body: Astronomy.Body.Saturn, planet: 'Saturn' },
  ];
  
  for (const { body, planet } of bodies) {
    const position = calculateBodyPosition(body, date, config);
    positions.push({
      planet,
      longitude: position.longitude,
      latitude: position.latitude,
      speed: position.speed,
      isRetrograde: position.isRetrograde,
    });
  }
  
  // Calculate Rahu and Ketu
  const rahuPosition = calculateRahuPosition(date, config);
  positions.push({
    planet: 'Rahu',
    longitude: rahuPosition.longitude,
    latitude: rahuPosition.latitude,
    speed: rahuPosition.speed,
    isRetrograde: rahuPosition.isRetrograde,
  });
  
  const ketuPosition = calculateKetuPosition(rahuPosition.longitude);
  positions.push({
    planet: 'Ketu',
    longitude: ketuPosition.longitude,
    latitude: ketuPosition.latitude,
    speed: ketuPosition.speed,
    isRetrograde: ketuPosition.isRetrograde,
  });
  
  return positions;
}

/**
 * Calculate position for a single planet
 * 
 * @param planet - Planet name
 * @param date - Date and time for calculation
 * @param config - Ephemeris configuration
 * @returns Planetary position data
 * 
 * @example
 * ```typescript
 * const sunPosition = calculatePlanetPosition('Sun', new Date());
 * console.log(`Sun is at ${sunPosition.longitude.toFixed(2)}°`);
 * ```
 */
export function calculatePlanetPosition(
  planet: Planet,
  date: Date,
  config: EphemerisConfig = {}
): PlanetPosition {
  // Handle shadow planets separately
  if (planet === 'Rahu') {
    const position = calculateRahuPosition(date, config);
    return {
      planet: 'Rahu',
      ...position,
    };
  }
  
  if (planet === 'Ketu') {
    const rahuPosition = calculateRahuPosition(date, config);
    const ketuPosition = calculateKetuPosition(rahuPosition.longitude);
    return {
      planet: 'Ketu',
      ...ketuPosition,
    };
  }
  
  // Map planet name to astronomy-engine body
  const bodyMap: Record<Planet, Astronomy.Body> = {
    'Sun': Astronomy.Body.Sun,
    'Moon': Astronomy.Body.Moon,
    'Mercury': Astronomy.Body.Mercury,
    'Venus': Astronomy.Body.Venus,
    'Mars': Astronomy.Body.Mars,
    'Jupiter': Astronomy.Body.Jupiter,
    'Saturn': Astronomy.Body.Saturn,
    'Rahu': Astronomy.Body.Moon, // Placeholder, handled above
    'Ketu': Astronomy.Body.Moon, // Placeholder, handled above
  };
  
  const body = bodyMap[planet];
  const position = calculateBodyPosition(body, date, config);
  
  return {
    planet,
    ...position,
  };
}

/**
 * Convert local time to UTC for ephemeris calculations
 * 
 * @param localDate - Local date and time
 * @param timezoneOffset - Timezone offset in hours (e.g., +5.5 for IST)
 * @returns UTC date
 * 
 * @example
 * ```typescript
 * // Convert IST to UTC
 * const localDate = new Date('1995-01-01T10:30:00');
 * const utcDate = localToUTC(localDate, 5.5);
 * ```
 */
export function localToUTC(localDate: Date, timezoneOffset: number): Date {
  const utcTime = localDate.getTime() - (timezoneOffset * 60 * 60 * 1000);
  return new Date(utcTime);
}

/**
 * Convert UTC time to local time
 * 
 * @param utcDate - UTC date and time
 * @param timezoneOffset - Timezone offset in hours (e.g., +5.5 for IST)
 * @returns Local date
 */
export function utcToLocal(utcDate: Date, timezoneOffset: number): Date {
  const localTime = utcDate.getTime() + (timezoneOffset * 60 * 60 * 1000);
  return new Date(localTime);
}

/**
 * Get timezone offset for a location (simplified version)
 * In production, use a proper timezone library like date-fns-tz
 * 
 * @param location - Location name or timezone identifier
 * @returns Timezone offset in hours
 */
export function getTimezoneOffset(location: string): number {
  // Common timezone offsets (simplified)
  const timezones: Record<string, number> = {
    'IST': 5.5,
    'India': 5.5,
    'UTC': 0,
    'GMT': 0,
    'EST': -5,
    'PST': -8,
    'CST': -6,
    'MST': -7,
  };
  
  return timezones[location] ?? 0;
}
