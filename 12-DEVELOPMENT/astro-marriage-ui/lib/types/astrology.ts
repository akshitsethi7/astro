/**
 * Core Astrology Types and Interfaces
 * 
 * This file contains all TypeScript type definitions for Vedic astrology calculations
 * including birth charts, dashas, transits, and predictions.
 */

// ============================================================================
// Basic Types
// ============================================================================

export type Planet = 'Sun' | 'Moon' | 'Mars' | 'Mercury' | 'Jupiter' | 'Venus' | 'Saturn' | 'Rahu' | 'Ketu'

export type ZodiacSign = 
  | 'Aries' | 'Taurus' | 'Gemini' | 'Cancer' 
  | 'Leo' | 'Virgo' | 'Libra' | 'Scorpio' 
  | 'Sagittarius' | 'Capricorn' | 'Aquarius' | 'Pisces'

export type Dignity = 'own' | 'exalted' | 'debilitated' | 'friend' | 'enemy' | 'neutral'

export type AspectType = 'conjunction' | 'opposition' | 'trine' | 'square' | 'sextile'

export type PredictionCategory = 'marriage' | 'career' | 'health' | 'finance' | 'spiritual'

export type DashaLevel = 'mahadasha' | 'antardasha' | 'pratyantar'

export type Favorability = 'excellent' | 'good' | 'neutral' | 'challenging' | 'difficult'

export type AfflictionLevel = 'none' | 'mild' | 'moderate' | 'severe'

export type RemedyType = 'mantra' | 'gemstone' | 'donation' | 'ritual' | 'lifestyle'

export type AlertPriority = 'critical' | 'important' | 'informational'

export type SadeSatiPhase = 'rising' | 'peak' | 'setting'

// ============================================================================
// Nakshatra System
// ============================================================================

export interface Nakshatra {
  name: string
  number: number // 1-27
  lord: Planet
  deity: string
  symbol: string
  startDegree: number // 0-360
  endDegree: number
  pada: number // 1-4
}

export const NAKSHATRAS: readonly Nakshatra[] = [
  { name: 'Ashwini', number: 1, lord: 'Ketu', deity: 'Ashwini Kumaras', symbol: 'Horse Head', startDegree: 0, endDegree: 13.33, pada: 1 },
  { name: 'Bharani', number: 2, lord: 'Venus', deity: 'Yama', symbol: 'Yoni', startDegree: 13.33, endDegree: 26.67, pada: 1 },
  { name: 'Krittika', number: 3, lord: 'Sun', deity: 'Agni', symbol: 'Razor', startDegree: 26.67, endDegree: 40, pada: 1 },
  { name: 'Rohini', number: 4, lord: 'Moon', deity: 'Brahma', symbol: 'Cart', startDegree: 40, endDegree: 53.33, pada: 1 },
  { name: 'Mrigashira', number: 5, lord: 'Mars', deity: 'Soma', symbol: 'Deer Head', startDegree: 53.33, endDegree: 66.67, pada: 1 },
  { name: 'Ardra', number: 6, lord: 'Rahu', deity: 'Rudra', symbol: 'Teardrop', startDegree: 66.67, endDegree: 80, pada: 1 },
  { name: 'Punarvasu', number: 7, lord: 'Jupiter', deity: 'Aditi', symbol: 'Bow', startDegree: 80, endDegree: 93.33, pada: 1 },
  { name: 'Pushya', number: 8, lord: 'Saturn', deity: 'Brihaspati', symbol: 'Flower', startDegree: 93.33, endDegree: 106.67, pada: 1 },
  { name: 'Ashlesha', number: 9, lord: 'Mercury', deity: 'Nagas', symbol: 'Serpent', startDegree: 106.67, endDegree: 120, pada: 1 },
  { name: 'Magha', number: 10, lord: 'Ketu', deity: 'Pitris', symbol: 'Throne', startDegree: 120, endDegree: 133.33, pada: 1 },
  { name: 'Purva Phalguni', number: 11, lord: 'Venus', deity: 'Bhaga', symbol: 'Hammock', startDegree: 133.33, endDegree: 146.67, pada: 1 },
  { name: 'Uttara Phalguni', number: 12, lord: 'Sun', deity: 'Aryaman', symbol: 'Bed', startDegree: 146.67, endDegree: 160, pada: 1 },
  { name: 'Hasta', number: 13, lord: 'Moon', deity: 'Savitar', symbol: 'Hand', startDegree: 160, endDegree: 173.33, pada: 1 },
  { name: 'Chitra', number: 14, lord: 'Mars', deity: 'Tvashtar', symbol: 'Pearl', startDegree: 173.33, endDegree: 186.67, pada: 1 },
  { name: 'Swati', number: 15, lord: 'Rahu', deity: 'Vayu', symbol: 'Coral', startDegree: 186.67, endDegree: 200, pada: 1 },
  { name: 'Vishakha', number: 16, lord: 'Jupiter', deity: 'Indra-Agni', symbol: 'Archway', startDegree: 200, endDegree: 213.33, pada: 1 },
  { name: 'Anuradha', number: 17, lord: 'Saturn', deity: 'Mitra', symbol: 'Lotus', startDegree: 213.33, endDegree: 226.67, pada: 1 },
  { name: 'Jyeshtha', number: 18, lord: 'Mercury', deity: 'Indra', symbol: 'Earring', startDegree: 226.67, endDegree: 240, pada: 1 },
  { name: 'Mula', number: 19, lord: 'Ketu', deity: 'Nirriti', symbol: 'Root', startDegree: 240, endDegree: 253.33, pada: 1 },
  { name: 'Purva Ashadha', number: 20, lord: 'Venus', deity: 'Apas', symbol: 'Fan', startDegree: 253.33, endDegree: 266.67, pada: 1 },
  { name: 'Uttara Ashadha', number: 21, lord: 'Sun', deity: 'Vishvadevas', symbol: 'Elephant Tusk', startDegree: 266.67, endDegree: 280, pada: 1 },
  { name: 'Shravana', number: 22, lord: 'Moon', deity: 'Vishnu', symbol: 'Ear', startDegree: 280, endDegree: 293.33, pada: 1 },
  { name: 'Dhanishta', number: 23, lord: 'Mars', deity: 'Vasus', symbol: 'Drum', startDegree: 293.33, endDegree: 306.67, pada: 1 },
  { name: 'Shatabhisha', number: 24, lord: 'Rahu', deity: 'Varuna', symbol: 'Circle', startDegree: 306.67, endDegree: 320, pada: 1 },
  { name: 'Purva Bhadrapada', number: 25, lord: 'Jupiter', deity: 'Aja Ekapada', symbol: 'Sword', startDegree: 320, endDegree: 333.33, pada: 1 },
  { name: 'Uttara Bhadrapada', number: 26, lord: 'Saturn', deity: 'Ahir Budhnya', symbol: 'Twins', startDegree: 333.33, endDegree: 346.67, pada: 1 },
  { name: 'Revati', number: 27, lord: 'Mercury', deity: 'Pushan', symbol: 'Fish', startDegree: 346.67, endDegree: 360, pada: 1 },
] as const

// ============================================================================
// Chart Data
// ============================================================================

export interface ChartData {
  birthDate: Date
  birthTime: string // HH:MM format
  timezone: string
  latitude: number
  longitude: number
  ayanamsa: 'Lahiri' | 'Raman' | 'KP'
  ascendant: {
    sign: ZodiacSign
    degree: number
  }
  planets: Map<Planet, PlanetData>
  houses: House[]
}

export interface PlanetData {
  sign: ZodiacSign
  degree: number // 0-30 within sign
  absoluteDegree: number // 0-360 in zodiac
  house: number // 1-12
  nakshatra: string
  nakshatraPada: number // 1-4
  nakshatraLord: Planet
  retrograde: boolean
  dignity: Dignity
  speed: number // degrees per day
}

export interface House {
  number: number // 1-12
  sign: ZodiacSign
  degree: number // cusp degree
  lord: Planet
  planets: Planet[]
}

// ============================================================================
// Dasha System
// ============================================================================

export interface VimshottariDasha {
  birthDate: Date
  moonNakshatra: string
  moonDegree: number
  moonNakshatraLord: Planet
  balance: number // years remaining at birth
  mahadashas: MahadashaPeriod[]
}

export interface MahadashaPeriod {
  planet: Planet
  startDate: Date
  endDate: Date
  durationYears: number
  balance: number // years remaining at birth (only for first)
  antardashas: AntardashaPeriod[]
  strength: number // 0-100
  favorability: Favorability
}

export interface AntardashaPeriod {
  planet: Planet
  startDate: Date
  endDate: Date
  durationMonths: number
  pratyantars: PratyanterPeriod[]
  strength: number // 0-100
  favorability: Favorability
}

export interface PratyanterPeriod {
  planet: Planet
  startDate: Date
  endDate: Date
  durationDays: number
  strength: number // 0-100
  favorability: Favorability
}

export interface DashaPeriod {
  planet: Planet
  startDate: Date
  endDate: Date
  level: DashaLevel
  subPeriods?: DashaPeriod[]
  predictions?: Prediction[]
  strength: number // 0-100
  favorability: Favorability
}

// Vimshottari Dasha durations in years
export const MAHADASHA_YEARS: Record<Planet, number> = {
  Sun: 6,
  Moon: 10,
  Mars: 7,
  Rahu: 18,
  Jupiter: 16,
  Saturn: 19,
  Mercury: 17,
  Ketu: 7,
  Venus: 20,
}

// Dasha sequence
export const DASHA_SEQUENCE: Planet[] = [
  'Ketu', 'Venus', 'Sun', 'Moon', 'Mars', 'Rahu', 'Jupiter', 'Saturn', 'Mercury'
]

// ============================================================================
// Predictions
// ============================================================================

export interface Prediction {
  category: PredictionCategory
  title: string
  description: string
  confidence: number // 0-100
  timing?: DateRange
  remedies?: Remedy[]
  favorability: Favorability
}

export interface DateRange {
  start: Date
  end: Date
}

// ============================================================================
// Transits
// ============================================================================

export interface TransitPosition {
  planet: Planet
  sign: ZodiacSign
  degree: number
  absoluteDegree: number
  house: number // natal house being transited
  speed: number // degrees per day
  retrograde: boolean
  aspects: TransitAspect[]
}

export interface TransitAspect {
  transitPlanet: Planet
  natalPlanet: Planet
  aspectType: AspectType
  orb: number // degrees
  applying: boolean // true if aspect is getting closer
  significance: number // 0-100
}

export interface TransitPrediction {
  planet: Planet
  transitingHouse: number
  startDate: Date
  endDate: Date
  effects: string[]
  significance: 'major' | 'moderate' | 'minor'
  category: PredictionCategory
}

export interface SadeSatiInfo {
  isActive: boolean
  phase: SadeSatiPhase | null
  startDate: Date | null
  endDate: Date | null
  currentPhaseStart: Date | null
  currentPhaseEnd: Date | null
  effects: string[]
  remedies: Remedy[]
}

// ============================================================================
// Aspects
// ============================================================================

export interface Aspect {
  planet1: Planet
  planet2: Planet
  type: AspectType
  orb: number
  strength: number // 0-100
  applying: boolean
}

// Standard aspect orbs (in degrees)
export const ASPECT_ORBS: Record<AspectType, number> = {
  conjunction: 8,
  opposition: 8,
  trine: 8,
  square: 7,
  sextile: 6,
}

// ============================================================================
// Yogas (Combinations)
// ============================================================================

export interface Yoga {
  name: string
  type: 'raja' | 'dhana' | 'marriage' | 'spiritual' | 'negative'
  planets: Planet[]
  houses: number[]
  strength: number // 0-100
  effects: string[]
  description: string
}

// ============================================================================
// Remedies
// ============================================================================

export interface Remedy {
  type: RemedyType
  title: string
  description: string
  timing: RemedyTiming
  difficulty: 'easy' | 'moderate' | 'advanced'
  cost: 'free' | 'low' | 'medium' | 'high'
  effectiveness: number // 0-100
  instructions: string[]
}

export interface RemedyTiming {
  days?: string[] // ['Monday', 'Saturday']
  hours?: string[] // ['Sunrise', 'Sunset']
  duration?: string // '40 days', '108 days'
  frequency?: string // 'daily', 'weekly'
}

// ============================================================================
// Alerts
// ============================================================================

export interface Alert {
  id: string
  type: 'transit' | 'dasha' | 'eclipse' | 'retrograde'
  priority: AlertPriority
  title: string
  description: string
  date: Date
  planet?: Planet
  actionable: boolean
  remedies?: Remedy[]
}

// ============================================================================
// Export Options
// ============================================================================

export interface ExportOptions {
  sections: ExportSection[]
  dateRange?: DateRange
  format: 'pdf' | 'json' | 'csv'
  includeCharts: boolean
  includePredictions: boolean
  includeRemedies: boolean
}

export type ExportSection = 
  | 'overview'
  | 'birth-chart'
  | 'dasha'
  | 'transits'
  | 'shadow-planets'
  | 'predictions'
  | 'remedies'

// ============================================================================
// Utility Types
// ============================================================================

export interface Position {
  x: number
  y: number
}

export interface PlanetPosition extends Position {
  planet: Planet
  degree: number
}

// ============================================================================
// Constants
// ============================================================================

export const ZODIAC_SIGNS: readonly ZodiacSign[] = [
  'Aries', 'Taurus', 'Gemini', 'Cancer',
  'Leo', 'Virgo', 'Libra', 'Scorpio',
  'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
] as const

export const PLANETS: readonly Planet[] = [
  'Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn', 'Rahu', 'Ketu'
] as const

export const PLANET_COLORS: Record<Planet, string> = {
  Sun: '#FF6B35',
  Moon: '#F7F7F7',
  Mars: '#E63946',
  Mercury: '#06FFA5',
  Jupiter: '#FFD60A',
  Venus: '#F72585',
  Saturn: '#4361EE',
  Rahu: '#8338EC',
  Ketu: '#FB5607',
}

// Sign lords
export const SIGN_LORDS: Record<ZodiacSign, Planet> = {
  Aries: 'Mars',
  Taurus: 'Venus',
  Gemini: 'Mercury',
  Cancer: 'Moon',
  Leo: 'Sun',
  Virgo: 'Mercury',
  Libra: 'Venus',
  Scorpio: 'Mars',
  Sagittarius: 'Jupiter',
  Capricorn: 'Saturn',
  Aquarius: 'Saturn',
  Pisces: 'Jupiter',
}
