/**
 * Vimshottari Dasha Calculator
 * 
 * Implements the Vimshottari Dasha system - the most widely used predictive system
 * in Vedic astrology. Calculates Mahadasha, Antardasha, and Pratyantar Dasha periods.
 * 
 * The system is based on a 120-year cycle divided among 9 planets.
 */

import { addYears, addMonths, addDays } from 'date-fns'
import {
  Planet,
  VimshottariDasha,
  MahadashaPeriod,
  AntardashaPeriod,
  PratyanterPeriod,
  MAHADASHA_YEARS,
  DASHA_SEQUENCE,
  Favorability
} from '@/lib/types/astrology'
import { getNakshatraFromDegree, calculateDashaBalance } from './nakshatra'

/**
 * Calculate complete Vimshottari Dasha system from birth data
 * @param birthDate - Date of birth
 * @param moonDegree - Moon's absolute degree at birth (0-360)
 * @returns Complete Vimshottari Dasha structure
 */
export function calculateVimshottariDasha(
  birthDate: Date,
  moonDegree: number
): VimshottariDasha {
  // Get Moon's Nakshatra
  const { nakshatra, lord } = getNakshatraFromDegree(moonDegree)
  
  // Calculate balance of first Mahadasha
  const firstMahadashaDuration = MAHADASHA_YEARS[lord]
  const balance = calculateDashaBalance(moonDegree, firstMahadashaDuration)
  
  // Find starting position in Dasha sequence
  const startIndex = DASHA_SEQUENCE.indexOf(lord)
  
  // Calculate all Mahadashas
  const mahadashas = calculateAllMahadashas(birthDate, startIndex, balance)
  
  return {
    birthDate,
    moonNakshatra: nakshatra,
    moonDegree,
    moonNakshatraLord: lord,
    balance,
    mahadashas
  }
}

/**
 * Calculate all Mahadasha periods
 * @param birthDate - Date of birth
 * @param startIndex - Starting index in DASHA_SEQUENCE
 * @param balance - Balance of first Mahadasha in years
 * @returns Array of Mahadasha periods
 */
function calculateAllMahadashas(
  birthDate: Date,
  startIndex: number,
  balance: number
): MahadashaPeriod[] {
  const mahadashas: MahadashaPeriod[] = []
  let currentDate = birthDate
  
  // Calculate for at least 120 years (full cycle) + some extra
  const totalPlanets = DASHA_SEQUENCE.length
  const cycles = 2 // Calculate 2 full cycles to cover long lifespans
  
  for (let cycle = 0; cycle < cycles; cycle++) {
    for (let i = 0; i < totalPlanets; i++) {
      const planetIndex = (startIndex + i) % totalPlanets
      const planet = DASHA_SEQUENCE[planetIndex]
      const durationYears = MAHADASHA_YEARS[planet]
      
      // For the first Mahadasha, use the balance
      const actualDuration = (cycle === 0 && i === 0) ? balance : durationYears
      
      const startDate = currentDate
      const endDate = addYears(startDate, actualDuration)
      
      // Calculate Antardashas for this Mahadasha
      const antardashas = calculateAntardashas(planet, startDate, endDate)
      
      mahadashas.push({
        planet,
        startDate,
        endDate,
        durationYears: actualDuration,
        balance: (cycle === 0 && i === 0) ? balance : 0,
        antardashas,
        strength: 50, // Default, will be calculated based on chart
        favorability: 'neutral' // Default, will be calculated based on chart
      })
      
      currentDate = endDate
    }
  }
  
  return mahadashas
}

/**
 * Calculate all Antardasha periods within a Mahadasha
 * @param mahadashaPlanet - Planet ruling the Mahadasha
 * @param startDate - Mahadasha start date
 * @param endDate - Mahadasha end date
 * @returns Array of Antardasha periods
 */
function calculateAntardashas(
  mahadashaPlanet: Planet,
  startDate: Date,
  endDate: Date
): AntardashaPeriod[] {
  const antardashas: AntardashaPeriod[] = []
  
  // Find starting position (Antardasha starts with Mahadasha lord)
  const startIndex = DASHA_SEQUENCE.indexOf(mahadashaPlanet)
  const mahadashaDuration = MAHADASHA_YEARS[mahadashaPlanet]
  
  let currentDate = startDate
  
  // Calculate all 9 Antardashas
  for (let i = 0; i < DASHA_SEQUENCE.length; i++) {
    const planetIndex = (startIndex + i) % DASHA_SEQUENCE.length
    const planet = DASHA_SEQUENCE[planetIndex]
    const antardashaDuration = MAHADASHA_YEARS[planet]
    
    // Antardasha duration = (Mahadasha years × Antardasha years) / 120
    const durationYears = (mahadashaDuration * antardashaDuration) / 120
    const durationMonths = durationYears * 12
    
    const antStartDate = currentDate
    const antEndDate = addMonths(antStartDate, durationMonths)
    
    // Don't exceed Mahadasha end date
    const actualEndDate = antEndDate > endDate ? endDate : antEndDate
    
    // Calculate Pratyantars for this Antardasha
    const pratyantars = calculatePratyantars(planet, antStartDate, actualEndDate)
    
    antardashas.push({
      planet,
      startDate: antStartDate,
      endDate: actualEndDate,
      durationMonths,
      pratyantars,
      strength: 50, // Default
      favorability: 'neutral' // Default
    })
    
    currentDate = actualEndDate
    
    // Stop if we've reached the Mahadasha end
    if (currentDate >= endDate) break
  }
  
  return antardashas
}

/**
 * Calculate all Pratyantar Dasha periods within an Antardasha
 * @param antardashaPlanet - Planet ruling the Antardasha
 * @param startDate - Antardasha start date
 * @param endDate - Antardasha end date
 * @returns Array of Pratyantar periods
 */
function calculatePratyantars(
  antardashaPlanet: Planet,
  startDate: Date,
  endDate: Date
): PratyanterPeriod[] {
  const pratyantars: PratyanterPeriod[] = []
  
  // Find starting position (Pratyantar starts with Antardasha lord)
  const startIndex = DASHA_SEQUENCE.indexOf(antardashaPlanet)
  const antardashaDuration = MAHADASHA_YEARS[antardashaPlanet]
  
  let currentDate = startDate
  
  // Calculate all 9 Pratyantars
  for (let i = 0; i < DASHA_SEQUENCE.length; i++) {
    const planetIndex = (startIndex + i) % DASHA_SEQUENCE.length
    const planet = DASHA_SEQUENCE[planetIndex]
    const pratyanterDuration = MAHADASHA_YEARS[planet]
    
    // Pratyantar duration = (Antardasha years × Pratyantar years) / 120
    const durationYears = (antardashaDuration * pratyanterDuration) / 120
    const durationDays = durationYears * 365.25
    
    const pratStartDate = currentDate
    const pratEndDate = addDays(pratStartDate, durationDays)
    
    // Don't exceed Antardasha end date
    const actualEndDate = pratEndDate > endDate ? endDate : pratEndDate
    
    pratyantars.push({
      planet,
      startDate: pratStartDate,
      endDate: actualEndDate,
      durationDays,
      strength: 50, // Default
      favorability: 'neutral' // Default
    })
    
    currentDate = actualEndDate
    
    // Stop if we've reached the Antardasha end
    if (currentDate >= endDate) break
  }
  
  return pratyantars
}

/**
 * Find the current Mahadasha for a given date
 * @param dasha - Complete Vimshottari Dasha structure
 * @param date - Date to check
 * @returns Current Mahadasha or null
 */
export function getCurrentMahadasha(
  dasha: VimshottariDasha,
  date: Date = new Date()
): MahadashaPeriod | null {
  return dasha.mahadashas.find(
    m => date >= m.startDate && date < m.endDate
  ) || null
}

/**
 * Find the current Antardasha for a given date
 * @param mahadasha - Mahadasha period
 * @param date - Date to check
 * @returns Current Antardasha or null
 */
export function getCurrentAntardasha(
  mahadasha: MahadashaPeriod,
  date: Date = new Date()
): AntardashaPeriod | null {
  return mahadasha.antardashas.find(
    a => date >= a.startDate && date < a.endDate
  ) || null
}

/**
 * Find the current Pratyantar Dasha for a given date
 * @param antardasha - Antardasha period
 * @param date - Date to check
 * @returns Current Pratyantar or null
 */
export function getCurrentPratyantar(
  antardasha: AntardashaPeriod,
  date: Date = new Date()
): PratyanterPeriod | null {
  return antardasha.pratyantars.find(
    p => date >= p.startDate && date < p.endDate
  ) || null
}

/**
 * Get all current periods (Mahadasha, Antardasha, Pratyantar) for a date
 * @param dasha - Complete Vimshottari Dasha structure
 * @param date - Date to check
 * @returns Object with current periods at all levels
 */
export function getCurrentPeriods(
  dasha: VimshottariDasha,
  date: Date = new Date()
): {
  mahadasha: MahadashaPeriod | null
  antardasha: AntardashaPeriod | null
  pratyantar: PratyanterPeriod | null
} {
  const mahadasha = getCurrentMahadasha(dasha, date)
  const antardasha = mahadasha ? getCurrentAntardasha(mahadasha, date) : null
  const pratyantar = antardasha ? getCurrentPratyantar(antardasha, date) : null
  
  return { mahadasha, antardasha, pratyantar }
}

/**
 * Calculate remaining time in a period
 * @param endDate - Period end date
 * @param currentDate - Current date
 * @returns Object with years, months, days remaining
 */
export function calculateRemainingTime(
  endDate: Date,
  currentDate: Date = new Date()
): {
  years: number
  months: number
  days: number
  totalDays: number
} {
  const diffMs = endDate.getTime() - currentDate.getTime()
  const totalDays = Math.floor(diffMs / (1000 * 60 * 60 * 24))
  
  const years = Math.floor(totalDays / 365.25)
  const remainingDays = totalDays - (years * 365.25)
  const months = Math.floor(remainingDays / 30.44)
  const days = Math.floor(remainingDays - (months * 30.44))
  
  return { years, months, days, totalDays }
}

/**
 * Get Mahadashas within a date range
 * @param dasha - Complete Vimshottari Dasha structure
 * @param startDate - Range start date
 * @param endDate - Range end date
 * @returns Array of Mahadashas that overlap with the date range
 */
export function getMahadashasInRange(
  dasha: VimshottariDasha,
  startDate: Date,
  endDate: Date
): MahadashaPeriod[] {
  return dasha.mahadashas.filter(m =>
    (m.startDate >= startDate && m.startDate <= endDate) ||
    (m.endDate >= startDate && m.endDate <= endDate) ||
    (m.startDate <= startDate && m.endDate >= endDate)
  )
}

/**
 * Format Dasha period as readable string
 * @param mahadasha - Mahadasha planet
 * @param antardasha - Antardasha planet (optional)
 * @param pratyantar - Pratyantar planet (optional)
 * @returns Formatted string
 */
export function formatDashaPeriod(
  mahadasha: Planet,
  antardasha?: Planet,
  pratyantar?: Planet
): string {
  let result = mahadasha
  
  if (antardasha) {
    result += `-${antardasha}`
  }
  
  if (pratyantar) {
    result += `-${pratyantar}`
  }
  
  return result
}

/**
 * Check if a date falls within a specific Dasha period
 * @param date - Date to check
 * @param startDate - Period start date
 * @param endDate - Period end date
 * @returns True if date is within period
 */
export function isDateInPeriod(date: Date, startDate: Date, endDate: Date): boolean {
  return date >= startDate && date < endDate
}

/**
 * Get the next Mahadasha after a given date
 * @param dasha - Complete Vimshottari Dasha structure
 * @param date - Reference date
 * @returns Next Mahadasha or null
 */
export function getNextMahadasha(
  dasha: VimshottariDasha,
  date: Date = new Date()
): MahadashaPeriod | null {
  return dasha.mahadashas.find(m => m.startDate > date) || null
}

/**
 * Get the previous Mahadasha before a given date
 * @param dasha - Complete Vimshottari Dasha structure
 * @param date - Reference date
 * @returns Previous Mahadasha or null
 */
export function getPreviousMahadasha(
  dasha: VimshottariDasha,
  date: Date = new Date()
): MahadashaPeriod | null {
  const previous = dasha.mahadashas
    .filter(m => m.endDate <= date)
    .pop()
  
  return previous || null
}

/**
 * Calculate percentage completed for a period
 * @param startDate - Period start date
 * @param endDate - Period end date
 * @param currentDate - Current date
 * @returns Percentage completed (0-100)
 */
export function calculatePercentageCompleted(
  startDate: Date,
  endDate: Date,
  currentDate: Date = new Date()
): number {
  if (currentDate < startDate) return 0
  if (currentDate >= endDate) return 100
  
  const totalDuration = endDate.getTime() - startDate.getTime()
  const elapsed = currentDate.getTime() - startDate.getTime()
  
  return (elapsed / totalDuration) * 100
}
