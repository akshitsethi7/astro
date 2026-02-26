/**
 * Aspect Calculations
 * 
 * Calculate aspects between planets including Western and Vedic aspects.
 * Handles both natal-natal and transit-natal aspects.
 */

import type { Planet, AspectType } from '@/lib/types/astrology';

/**
 * Aspect configuration
 */
export interface AspectConfig {
  type: AspectType;
  angle: number;
  orb: number; // Maximum orb in degrees
  isHarmonious: boolean;
}

/**
 * Aspect data
 */
export interface Aspect {
  planet1: Planet;
  planet2: Planet;
  type: AspectType;
  angle: number; // Actual angle between planets
  orb: number; // Difference from exact aspect
  isApplying: boolean; // True if aspect is getting closer
  isHarmonious: boolean;
}

/**
 * Western aspect configurations
 */
export const WESTERN_ASPECTS: readonly AspectConfig[] = [
  { type: 'conjunction', angle: 0, orb: 8, isHarmonious: true },
  { type: 'sextile', angle: 60, orb: 6, isHarmonious: true },
  { type: 'square', angle: 90, orb: 7, isHarmonious: false },
  { type: 'trine', angle: 120, orb: 8, isHarmonious: true },
  { type: 'opposition', angle: 180, orb: 8, isHarmonious: false },
] as const;

/**
 * Vedic aspects (Drishti)
 * All planets aspect the 7th house from themselves
 * Mars aspects 4th, 7th, 8th
 * Jupiter aspects 5th, 7th, 9th
 * Saturn aspects 3rd, 7th, 10th
 */
export const VEDIC_ASPECTS: Record<Planet, number[]> = {
  'Sun': [7],
  'Moon': [7],
  'Mars': [4, 7, 8],
  'Mercury': [7],
  'Jupiter': [5, 7, 9],
  'Venus': [7],
  'Saturn': [3, 7, 10],
  'Rahu': [5, 7, 9], // Similar to Jupiter
  'Ketu': [5, 7, 9], // Similar to Jupiter
};

/**
 * Calculate angular distance between two degrees
 */
export function calculateAngularDistance(degree1: number, degree2: number): number {
  let diff = Math.abs(degree1 - degree2);
  if (diff > 180) diff = 360 - diff;
  return diff;
}

/**
 * Calculate if aspect is applying or separating
 * Requires planetary speeds
 */
export function isAspectApplying(
  degree1: number,
  speed1: number,
  degree2: number,
  speed2: number,
  aspectAngle: number
): boolean {
  // Calculate current distance
  const currentDistance = calculateAngularDistance(degree1, degree2);
  
  // Calculate distance after 1 day
  const futureDistance = calculateAngularDistance(
    degree1 + speed1,
    degree2 + speed2
  );
  
  // If future distance to aspect angle is less, aspect is applying
  return Math.abs(futureDistance - aspectAngle) < Math.abs(currentDistance - aspectAngle);
}

/**
 * Find Western aspect between two planets
 */
export function findWesternAspect(
  planet1: Planet,
  degree1: number,
  speed1: number,
  planet2: Planet,
  degree2: number,
  speed2: number
): Aspect | null {
  const angle = calculateAngularDistance(degree1, degree2);
  
  // Check each aspect type
  for (const aspectConfig of WESTERN_ASPECTS) {
    const orb = Math.abs(angle - aspectConfig.angle);
    
    if (orb <= aspectConfig.orb) {
      const applying = isAspectApplying(degree1, speed1, degree2, speed2, aspectConfig.angle);
      
      return {
        planet1,
        planet2,
        type: aspectConfig.type,
        angle,
        orb,
        isApplying: applying,
        isHarmonious: aspectConfig.isHarmonious,
      };
    }
  }
  
  return null;
}

/**
 * Calculate house distance between two positions
 */
export function calculateHouseDistance(house1: number, house2: number): number {
  let distance = house2 - house1;
  if (distance < 0) distance += 12;
  return distance + 1; // Houses are 1-indexed
}

/**
 * Check if planet aspects another planet using Vedic aspects
 */
export function hasVedicAspect(
  planet: Planet,
  planetHouse: number,
  targetHouse: number
): boolean {
  const aspects = VEDIC_ASPECTS[planet];
  const houseDistance = calculateHouseDistance(planetHouse, targetHouse);
  return aspects.includes(houseDistance);
}

/**
 * Calculate all Western aspects in a chart
 */
export function calculateAllWesternAspects(
  planets: Map<Planet, { degree: number; speed: number }>
): Aspect[] {
  const aspects: Aspect[] = [];
  const planetList = Array.from(planets.keys());
  
  // Check all planet pairs
  for (let i = 0; i < planetList.length; i++) {
    for (let j = i + 1; j < planetList.length; j++) {
      const planet1 = planetList[i];
      const planet2 = planetList[j];
      const data1 = planets.get(planet1)!;
      const data2 = planets.get(planet2)!;
      
      const aspect = findWesternAspect(
        planet1,
        data1.degree,
        data1.speed,
        planet2,
        data2.degree,
        data2.speed
      );
      
      if (aspect) {
        aspects.push(aspect);
      }
    }
  }
  
  return aspects;
}

/**
 * Calculate all Vedic aspects in a chart
 */
export function calculateAllVedicAspects(
  planets: Map<Planet, { house: number }>
): Array<{ planet: Planet; aspects: Planet[] }> {
  const result: Array<{ planet: Planet; aspects: Planet[] }> = [];
  
  for (const [planet, data] of planets.entries()) {
    const aspectedPlanets: Planet[] = [];
    
    for (const [targetPlanet, targetData] of planets.entries()) {
      if (planet === targetPlanet) continue;
      
      if (hasVedicAspect(planet, data.house, targetData.house)) {
        aspectedPlanets.push(targetPlanet);
      }
    }
    
    if (aspectedPlanets.length > 0) {
      result.push({ planet, aspects: aspectedPlanets });
    }
  }
  
  return result;
}

/**
 * Calculate transit aspects (transit planet to natal planet)
 */
export function calculateTransitAspects(
  transitPlanets: Map<Planet, { degree: number; speed: number }>,
  natalPlanets: Map<Planet, { degree: number; speed: number }>
): Aspect[] {
  const aspects: Aspect[] = [];
  
  for (const [transitPlanet, transitData] of transitPlanets.entries()) {
    for (const [natalPlanet, natalData] of natalPlanets.entries()) {
      const aspect = findWesternAspect(
        transitPlanet,
        transitData.degree,
        transitData.speed,
        natalPlanet,
        natalData.degree,
        0 // Natal planets don't move
      );
      
      if (aspect) {
        aspects.push(aspect);
      }
    }
  }
  
  return aspects;
}

/**
 * Get aspect strength (0-100)
 */
export function getAspectStrength(aspect: Aspect): number {
  const aspectConfig = WESTERN_ASPECTS.find(a => a.type === aspect.type);
  if (!aspectConfig) return 0;
  
  // Strength decreases with orb
  const strength = 100 * (1 - aspect.orb / aspectConfig.orb);
  return Math.max(0, Math.min(100, strength));
}

/**
 * Get aspect description
 */
export function getAspectDescription(aspect: Aspect): string {
  const strength = getAspectStrength(aspect);
  const applying = aspect.isApplying ? 'applying' : 'separating';
  const quality = aspect.isHarmonious ? 'harmonious' : 'challenging';
  
  return `${aspect.planet1} ${aspect.type} ${aspect.planet2} (${applying}, ${quality}, ${strength.toFixed(0)}% strength)`;
}

/**
 * Filter aspects by minimum strength
 */
export function filterAspectsByStrength(aspects: Aspect[], minStrength: number): Aspect[] {
  return aspects.filter(aspect => getAspectStrength(aspect) >= minStrength);
}

/**
 * Group aspects by type
 */
export function groupAspectsByType(aspects: Aspect[]): Record<AspectType, Aspect[]> {
  const grouped: Record<AspectType, Aspect[]> = {
    'conjunction': [],
    'opposition': [],
    'trine': [],
    'square': [],
    'sextile': [],
  };
  
  for (const aspect of aspects) {
    grouped[aspect.type].push(aspect);
  }
  
  return grouped;
}
