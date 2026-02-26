/**
 * Nakshatra Calculation Utilities
 * 
 * Functions for working with the 27 Nakshatras (lunar mansions) in Vedic astrology.
 * Each Nakshatra spans 13°20' (13.333...°) of the zodiac.
 */

import { Nakshatra, NAKSHATRAS, Planet } from '@/lib/types/astrology'

/**
 * Find which Nakshatra a given degree falls into
 * @param absoluteDegree - Degree in the zodiac (0-360)
 * @returns Nakshatra information including name, lord, and pada
 */
export function getNakshatraFromDegree(absoluteDegree: number): {
  nakshatra: string
  nakshatraNumber: number
  lord: Planet
  pada: number
  degreeInNakshatra: number
} {
  // Normalize degree to 0-360 range
  const normalizedDegree = ((absoluteDegree % 360) + 360) % 360
  
  // Each Nakshatra is 13.333... degrees (13°20')
  const nakshatraSpan = 360 / 27 // 13.333...
  
  // Find which Nakshatra (0-26)
  const nakshatraIndex = Math.floor(normalizedDegree / nakshatraSpan)
  
  // Get the Nakshatra data
  const nakshatraData = NAKSHATRAS[nakshatraIndex]
  
  // Calculate degree within the Nakshatra (0-13.333...)
  const degreeInNakshatra = normalizedDegree % nakshatraSpan
  
  // Calculate pada (1-4) - each pada is 1/4 of the Nakshatra (3.333... degrees)
  const padaSpan = nakshatraSpan / 4 // 3.333...
  const pada = Math.floor(degreeInNakshatra / padaSpan) + 1
  
  return {
    nakshatra: nakshatraData.name,
    nakshatraNumber: nakshatraData.number,
    lord: nakshatraData.lord,
    pada: Math.min(pada, 4), // Ensure pada is 1-4
    degreeInNakshatra
  }
}

/**
 * Get Nakshatra by number (1-27)
 * @param number - Nakshatra number (1-27)
 * @returns Nakshatra data
 */
export function getNakshatraByNumber(number: number): Nakshatra | null {
  if (number < 1 || number > 27) {
    return null
  }
  return NAKSHATRAS[number - 1]
}

/**
 * Get Nakshatra by name
 * @param name - Nakshatra name
 * @returns Nakshatra data
 */
export function getNakshatraByName(name: string): Nakshatra | null {
  return NAKSHATRAS.find(n => n.name.toLowerCase() === name.toLowerCase()) || null
}

/**
 * Calculate the balance of Dasha at birth based on Moon's position in Nakshatra
 * @param moonDegree - Moon's absolute degree (0-360)
 * @param mahadashaDuration - Duration of the Mahadasha in years
 * @returns Balance remaining in years
 */
export function calculateDashaBalance(moonDegree: number, mahadashaDuration: number): number {
  const { degreeInNakshatra } = getNakshatraFromDegree(moonDegree)
  
  // Each Nakshatra is 13.333... degrees
  const nakshatraSpan = 360 / 27
  
  // Calculate how much of the Nakshatra has been traversed (0-1)
  const fractionTraversed = degreeInNakshatra / nakshatraSpan
  
  // Balance is the remaining portion of the Mahadasha
  const balance = mahadashaDuration * (1 - fractionTraversed)
  
  return balance
}

/**
 * Get all Nakshatras ruled by a specific planet
 * @param planet - Planet lord
 * @returns Array of Nakshatras ruled by the planet
 */
export function getNakshatrasByLord(planet: Planet): Nakshatra[] {
  return NAKSHATRAS.filter(n => n.lord === planet)
}

/**
 * Convert sign and degree to absolute degree
 * @param signNumber - Sign number (0-11, where 0=Aries)
 * @param degreeInSign - Degree within the sign (0-30)
 * @returns Absolute degree (0-360)
 */
export function signDegreeToAbsolute(signNumber: number, degreeInSign: number): number {
  return (signNumber * 30) + degreeInSign
}

/**
 * Convert absolute degree to sign and degree
 * @param absoluteDegree - Absolute degree (0-360)
 * @returns Object with sign number and degree in sign
 */
export function absoluteDegreeToSign(absoluteDegree: number): {
  signNumber: number
  degreeInSign: number
} {
  const normalizedDegree = ((absoluteDegree % 360) + 360) % 360
  const signNumber = Math.floor(normalizedDegree / 30)
  const degreeInSign = normalizedDegree % 30
  
  return { signNumber, degreeInSign }
}

/**
 * Get the starting degree of a Nakshatra
 * @param nakshatraNumber - Nakshatra number (1-27)
 * @returns Starting degree (0-360)
 */
export function getNakshatraStartDegree(nakshatraNumber: number): number {
  if (nakshatraNumber < 1 || nakshatraNumber > 27) {
    throw new Error('Nakshatra number must be between 1 and 27')
  }
  
  const nakshatraSpan = 360 / 27
  return (nakshatraNumber - 1) * nakshatraSpan
}

/**
 * Get the ending degree of a Nakshatra
 * @param nakshatraNumber - Nakshatra number (1-27)
 * @returns Ending degree (0-360)
 */
export function getNakshatraEndDegree(nakshatraNumber: number): number {
  if (nakshatraNumber < 1 || nakshatraNumber > 27) {
    throw new Error('Nakshatra number must be between 1 and 27')
  }
  
  const nakshatraSpan = 360 / 27
  return nakshatraNumber * nakshatraSpan
}

/**
 * Check if a degree falls within a specific Nakshatra
 * @param absoluteDegree - Degree to check (0-360)
 * @param nakshatraNumber - Nakshatra number (1-27)
 * @returns True if degree is in the Nakshatra
 */
export function isInNakshatra(absoluteDegree: number, nakshatraNumber: number): boolean {
  const { nakshatraNumber: actualNumber } = getNakshatraFromDegree(absoluteDegree)
  return actualNumber === nakshatraNumber
}

/**
 * Get the pada (quarter) boundaries for a Nakshatra
 * @param nakshatraNumber - Nakshatra number (1-27)
 * @returns Array of 4 pada boundaries [start1, start2, start3, start4, end4]
 */
export function getNakshatraPadaBoundaries(nakshatraNumber: number): number[] {
  const startDegree = getNakshatraStartDegree(nakshatraNumber)
  const nakshatraSpan = 360 / 27
  const padaSpan = nakshatraSpan / 4
  
  return [
    startDegree,                    // Pada 1 start
    startDegree + padaSpan,         // Pada 2 start
    startDegree + (padaSpan * 2),   // Pada 3 start
    startDegree + (padaSpan * 3),   // Pada 4 start
    startDegree + nakshatraSpan     // Pada 4 end (Nakshatra end)
  ]
}

/**
 * Format Nakshatra information as a readable string
 * @param absoluteDegree - Degree in the zodiac (0-360)
 * @returns Formatted string with Nakshatra details
 */
export function formatNakshatraInfo(absoluteDegree: number): string {
  const info = getNakshatraFromDegree(absoluteDegree)
  return `${info.nakshatra} (${info.nakshatraNumber}) - Pada ${info.pada} - Lord: ${info.lord}`
}

/**
 * Get Nakshatra compatibility score (simplified)
 * Used for basic compatibility analysis
 * @param nakshatra1 - First Nakshatra number
 * @param nakshatra2 - Second Nakshatra number
 * @returns Compatibility score (0-10)
 */
export function getNakshatraCompatibility(nakshatra1: number, nakshatra2: number): number {
  // This is a simplified version. Full compatibility uses Kuta system
  // with 8 factors (Varna, Vashya, Tara, Yoni, Graha Maitri, Gana, Bhakoot, Nadi)
  
  // Same Nakshatra
  if (nakshatra1 === nakshatra2) return 7
  
  // Calculate distance
  const distance = Math.abs(nakshatra1 - nakshatra2)
  
  // Trine (9 apart) - very good
  if (distance === 9 || distance === 18) return 9
  
  // Opposite (14 apart) - challenging
  if (distance === 13 || distance === 14) return 4
  
  // Adjacent - neutral
  if (distance === 1 || distance === 26) return 6
  
  // Default moderate compatibility
  return 6
}

/**
 * Get the Nakshatra sequence starting from a given Nakshatra
 * Useful for Dasha calculations
 * @param startNakshatra - Starting Nakshatra number (1-27)
 * @param count - Number of Nakshatras to return
 * @returns Array of Nakshatra numbers in sequence
 */
export function getNakshatraSequence(startNakshatra: number, count: number): number[] {
  const sequence: number[] = []
  
  for (let i = 0; i < count; i++) {
    const nakshatraNumber = ((startNakshatra - 1 + i) % 27) + 1
    sequence.push(nakshatraNumber)
  }
  
  return sequence
}

/**
 * Validate if a degree is within valid range
 * @param degree - Degree to validate
 * @returns True if valid (0-360)
 */
export function isValidDegree(degree: number): boolean {
  return degree >= 0 && degree < 360
}

/**
 * Normalize degree to 0-360 range
 * @param degree - Any degree value
 * @returns Normalized degree (0-360)
 */
export function normalizeDegree(degree: number): number {
  return ((degree % 360) + 360) % 360
}
