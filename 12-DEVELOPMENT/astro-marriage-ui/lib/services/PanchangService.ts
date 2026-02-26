import { calculatePlanetPosition } from '../calculations/ephemeris'

export interface PanchangData {
  date: Date
  tithi: string
  tithiEnd: Date
  nakshatra: string
  nakshatraEnd: Date
  yoga: string
  yogaEnd: Date
  karana: string
  karanaEnd: Date
  sunrise: Date
  sunset: Date
  moonrise: Date
  moonset: Date
  rahukaal: { start: Date; end: Date }
  yamaganda: { start: Date; end: Date }
  gulika: { start: Date; end: Date }
  abhijit: { start: Date; end: Date }
  durmuhurtam: Array<{ start: Date; end: Date }>
}

export class PanchangService {
  /**
   * Calculate complete Panchang for a given date and location
   */
  static calculatePanchang(date: Date, latitude: number, longitude: number): PanchangData {
    const sunPos = calculatePlanetPosition('Sun', date)
    const moonPos = calculatePlanetPosition('Moon', date)
    
    return {
      date,
      tithi: this.calculateTithi(sunPos.longitude, moonPos.longitude),
      tithiEnd: this.calculateTithiEnd(date, sunPos.longitude, moonPos.longitude),
      nakshatra: this.calculateNakshatra(moonPos.longitude),
      nakshatraEnd: this.calculateNakshatraEnd(date, moonPos.longitude),
      yoga: this.calculateYoga(sunPos.longitude, moonPos.longitude),
      yogaEnd: this.calculateYogaEnd(date, sunPos.longitude, moonPos.longitude),
      karana: this.calculateKarana(sunPos.longitude, moonPos.longitude),
      karanaEnd: this.calculateKaranaEnd(date, sunPos.longitude, moonPos.longitude),
      sunrise: this.calculateSunrise(date, latitude, longitude),
      sunset: this.calculateSunset(date, latitude, longitude),
      moonrise: this.calculateMoonrise(date, latitude, longitude),
      moonset: this.calculateMoonset(date, latitude, longitude),
      rahukaal: this.calculateRahukaal(date, latitude, longitude),
      yamaganda: this.calculateYamaganda(date, latitude, longitude),
      gulika: this.calculateGulika(date, latitude, longitude),
      abhijit: this.calculateAbhijit(date, latitude, longitude),
      durmuhurtam: this.calculateDurmuhurtam(date, latitude, longitude),
    }
  }

  private static calculateTithi(sunLong: number, moonLong: number): string {
    const diff = (moonLong - sunLong + 360) % 360
    const tithiNumber = Math.floor(diff / 12) + 1
    
    const tithiNames = [
      'Pratipada', 'Dwitiya', 'Tritiya', 'Chaturthi', 'Panchami',
      'Shashthi', 'Saptami', 'Ashtami', 'Navami', 'Dashami',
      'Ekadashi', 'Dwadashi', 'Trayodashi', 'Chaturdashi', 'Purnima',
      'Pratipada', 'Dwitiya', 'Tritiya', 'Chaturthi', 'Panchami',
      'Shashthi', 'Saptami', 'Ashtami', 'Navami', 'Dashami',
      'Ekadashi', 'Dwadashi', 'Trayodashi', 'Chaturdashi', 'Amavasya'
    ]
    
    const paksha = tithiNumber <= 15 ? 'Shukla Paksha' : 'Krishna Paksha'
    return `${paksha} ${tithiNames[tithiNumber - 1]}`
  }

  private static calculateTithiEnd(date: Date, sunLong: number, moonLong: number): Date {
    // Simplified calculation - actual would need precise ephemeris
    const diff = (moonLong - sunLong + 360) % 360
    const tithiProgress = (diff % 12) / 12
    const hoursToEnd = (1 - tithiProgress) * 24
    
    return new Date(date.getTime() + hoursToEnd * 60 * 60 * 1000)
  }

  private static calculateNakshatra(moonLong: number): string {
    const nakshatraNames = [
      'Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra',
      'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'Purva Phalguni', 'Uttara Phalguni',
      'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha', 'Jyeshtha',
      'Mula', 'Purva Ashadha', 'Uttara Ashadha', 'Shravana', 'Dhanishta', 'Shatabhisha',
      'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati'
    ]
    
    const nakshatraIndex = Math.floor(moonLong / 13.333333)
    return nakshatraNames[nakshatraIndex % 27]
  }

  private static calculateNakshatraEnd(date: Date, moonLong: number): Date {
    const nakshatraProgress = (moonLong % 13.333333) / 13.333333
    const hoursToEnd = (1 - nakshatraProgress) * 24
    
    return new Date(date.getTime() + hoursToEnd * 60 * 60 * 1000)
  }

  private static calculateYoga(sunLong: number, moonLong: number): string {
    const yogaNames = [
      'Vishkambha', 'Priti', 'Ayushman', 'Saubhagya', 'Shobhana', 'Atiganda',
      'Sukarma', 'Dhriti', 'Shula', 'Ganda', 'Vriddhi', 'Dhruva',
      'Vyaghata', 'Harshana', 'Vajra', 'Siddhi', 'Vyatipata', 'Variyan',
      'Parigha', 'Shiva', 'Siddha', 'Sadhya', 'Shubha', 'Shukla',
      'Brahma', 'Indra', 'Vaidhriti'
    ]
    
    const sum = (sunLong + moonLong) % 360
    const yogaIndex = Math.floor(sum / 13.333333)
    
    return yogaNames[yogaIndex % 27]
  }

  private static calculateYogaEnd(date: Date, sunLong: number, moonLong: number): Date {
    const sum = (sunLong + moonLong) % 360
    const yogaProgress = (sum % 13.333333) / 13.333333
    const hoursToEnd = (1 - yogaProgress) * 24
    
    return new Date(date.getTime() + hoursToEnd * 60 * 60 * 1000)
  }

  private static calculateKarana(sunLong: number, moonLong: number): string {
    const karanaNames = [
      'Bava', 'Balava', 'Kaulava', 'Taitila', 'Garaja', 'Vanija', 'Vishti',
      'Bava', 'Balava', 'Kaulava', 'Taitila', 'Garaja', 'Vanija', 'Vishti',
      'Bava', 'Balava', 'Kaulava', 'Taitila', 'Garaja', 'Vanija', 'Vishti',
      'Bava', 'Balava', 'Kaulava', 'Taitila', 'Garaja', 'Vanija', 'Vishti',
      'Bava', 'Balava', 'Kaulava', 'Taitila', 'Garaja', 'Vanija', 'Vishti',
      'Bava', 'Balava', 'Kaulava', 'Taitila', 'Garaja', 'Vanija', 'Vishti',
      'Bava', 'Balava', 'Kaulava', 'Taitila', 'Garaja', 'Vanija', 'Vishti',
      'Bava', 'Balava', 'Kaulava', 'Taitila', 'Garaja', 'Vanija', 'Vishti',
      'Shakuni', 'Chatushpada', 'Naga', 'Kimstughna'
    ]
    
    const diff = (moonLong - sunLong + 360) % 360
    const karanaIndex = Math.floor(diff / 6)
    
    return karanaNames[karanaIndex % karanaNames.length]
  }

  private static calculateKaranaEnd(date: Date, sunLong: number, moonLong: number): Date {
    const diff = (moonLong - sunLong + 360) % 360
    const karanaProgress = (diff % 6) / 6
    const hoursToEnd = (1 - karanaProgress) * 24
    
    return new Date(date.getTime() + hoursToEnd * 60 * 60 * 1000)
  }

  private static calculateSunrise(date: Date, latitude: number, longitude: number): Date {
    // Simplified calculation - actual would use proper astronomical algorithms
    const sunrise = new Date(date)
    sunrise.setHours(6, 0, 0, 0)
    return sunrise
  }

  private static calculateSunset(date: Date, latitude: number, longitude: number): Date {
    const sunset = new Date(date)
    sunset.setHours(18, 0, 0, 0)
    return sunset
  }

  private static calculateMoonrise(date: Date, latitude: number, longitude: number): Date {
    const moonrise = new Date(date)
    moonrise.setHours(8, 0, 0, 0)
    return moonrise
  }

  private static calculateMoonset(date: Date, latitude: number, longitude: number): Date {
    const moonset = new Date(date)
    moonset.setHours(20, 0, 0, 0)
    return moonset
  }

  private static calculateRahukaal(date: Date, latitude: number, longitude: number): { start: Date; end: Date } {
    const sunrise = this.calculateSunrise(date, latitude, longitude)
    const sunset = this.calculateSunset(date, latitude, longitude)
    const dayDuration = (sunset.getTime() - sunrise.getTime()) / 8
    
    const dayOfWeek = date.getDay()
    const rahuPeriods = [7, 1, 6, 4, 5, 3, 2] // Sunday to Saturday
    const period = rahuPeriods[dayOfWeek]
    
    const start = new Date(sunrise.getTime() + (period - 1) * dayDuration)
    const end = new Date(sunrise.getTime() + period * dayDuration)
    
    return { start, end }
  }

  private static calculateYamaganda(date: Date, latitude: number, longitude: number): { start: Date; end: Date } {
    const sunrise = this.calculateSunrise(date, latitude, longitude)
    const sunset = this.calculateSunset(date, latitude, longitude)
    const dayDuration = (sunset.getTime() - sunrise.getTime()) / 8
    
    const dayOfWeek = date.getDay()
    const yamagandaPeriods = [5, 4, 3, 2, 1, 7, 6]
    const period = yamagandaPeriods[dayOfWeek]
    
    const start = new Date(sunrise.getTime() + (period - 1) * dayDuration)
    const end = new Date(sunrise.getTime() + period * dayDuration)
    
    return { start, end }
  }

  private static calculateGulika(date: Date, latitude: number, longitude: number): { start: Date; end: Date } {
    const sunrise = this.calculateSunrise(date, latitude, longitude)
    const sunset = this.calculateSunset(date, latitude, longitude)
    const dayDuration = (sunset.getTime() - sunrise.getTime()) / 8
    
    const dayOfWeek = date.getDay()
    const gulikaPeriods = [6, 5, 4, 3, 2, 1, 7]
    const period = gulikaPeriods[dayOfWeek]
    
    const start = new Date(sunrise.getTime() + (period - 1) * dayDuration)
    const end = new Date(sunrise.getTime() + period * dayDuration)
    
    return { start, end }
  }

  private static calculateAbhijit(date: Date, latitude: number, longitude: number): { start: Date; end: Date } {
    const noon = new Date(date)
    noon.setHours(12, 0, 0, 0)
    
    const start = new Date(noon.getTime() - 24 * 60 * 1000)
    const end = new Date(noon.getTime() + 24 * 60 * 1000)
    
    return { start, end }
  }

  private static calculateDurmuhurtam(date: Date, latitude: number, longitude: number): Array<{ start: Date; end: Date }> {
    const sunrise = this.calculateSunrise(date, latitude, longitude)
    const sunset = this.calculateSunset(date, latitude, longitude)
    
    // Two Durmuhurtam periods per day
    const morning = new Date(sunrise.getTime() + 1.5 * 60 * 60 * 1000)
    const afternoon = new Date(sunset.getTime() - 1.5 * 60 * 60 * 1000)
    
    return [
      { start: morning, end: new Date(morning.getTime() + 48 * 60 * 1000) },
      { start: afternoon, end: new Date(afternoon.getTime() + 48 * 60 * 1000) }
    ]
  }
}
