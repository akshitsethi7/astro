import { PanchangService, PanchangData } from './PanchangService'

export interface MuhurataResult {
  date: Date
  startTime: Date
  endTime: Date
  score: number
  factors: {
    tithi: string
    nakshatra: string
    yoga: string
    karana: string
    weekday: string
  }
  suitability: string
  notes: string[]
}

export type EventType = 'marriage' | 'business' | 'housewarming' | 'travel' | 'education'

export class MuhurataService {
  /**
   * Find auspicious timings for a specific event type
   */
  static findMuhurata(
    eventType: EventType,
    startDate: Date,
    endDate: Date,
    latitude: number,
    longitude: number
  ): MuhurataResult[] {
    const results: MuhurataResult[] = []
    const currentDate = new Date(startDate)
    
    while (currentDate <= endDate) {
      const panchang = PanchangService.calculatePanchang(currentDate, latitude, longitude)
      const muhuratas = this.analyzeDayForMuhurata(eventType, panchang, latitude, longitude)
      results.push(...muhuratas)
      
      currentDate.setDate(currentDate.getDate() + 1)
    }
    
    return results.sort((a, b) => b.score - a.score).slice(0, 10)
  }

  private static analyzeDayForMuhurata(
    eventType: EventType,
    panchang: PanchangData,
    latitude: number,
    longitude: number
  ): MuhurataResult[] {
    const results: MuhurataResult[] = []
    
    // Check if day is suitable
    if (!this.isDaySuitable(eventType, panchang)) {
      return results
    }
    
    // Find good time windows
    const timeWindows = this.findGoodTimeWindows(panchang)
    
    for (const window of timeWindows) {
      const score = this.calculateMuhurataScore(eventType, panchang, window)
      
      if (score >= 70) {
        results.push({
          date: panchang.date,
          startTime: window.start,
          endTime: window.end,
          score,
          factors: {
            tithi: panchang.tithi,
            nakshatra: panchang.nakshatra,
            yoga: panchang.yoga,
            karana: panchang.karana,
            weekday: this.getWeekdayName(panchang.date.getDay()),
          },
          suitability: this.getSuitabilityLevel(score),
          notes: this.generateNotes(eventType, panchang),
        })
      }
    }
    
    return results
  }

  private static isDaySuitable(eventType: EventType, panchang: PanchangData): boolean {
    const weekday = panchang.date.getDay()
    
    // Marriage specific checks
    if (eventType === 'marriage') {
      // Avoid Tuesdays and Saturdays for marriage
      if (weekday === 2 || weekday === 6) return false
      
      // Avoid certain Tithis
      const avoidTithis = ['Amavasya', 'Chaturthi', 'Navami', 'Chaturdashi']
      if (avoidTithis.some(t => panchang.tithi.includes(t))) return false
      
      // Avoid certain Nakshatras
      const avoidNakshatras = ['Bharani', 'Ashlesha', 'Jyeshtha', 'Mula']
      if (avoidNakshatras.includes(panchang.nakshatra)) return false
    }
    
    // Business specific checks
    if (eventType === 'business') {
      // Prefer certain weekdays
      const goodDays = [1, 3, 4, 5] // Monday, Wednesday, Thursday, Friday
      if (!goodDays.includes(weekday)) return false
    }
    
    return true
  }

  private static findGoodTimeWindows(panchang: PanchangData): Array<{ start: Date; end: Date }> {
    const windows: Array<{ start: Date; end: Date }> = []
    
    // Morning window (after sunrise)
    const morningStart = new Date(panchang.sunrise.getTime() + 30 * 60 * 1000)
    const morningEnd = new Date(panchang.sunrise.getTime() + 3 * 60 * 60 * 1000)
    
    // Check if not in inauspicious periods
    if (!this.isInInauspiciousPeriod(morningStart, panchang)) {
      windows.push({ start: morningStart, end: morningEnd })
    }
    
    // Abhijit Muhurta (always auspicious)
    windows.push(panchang.abhijit)
    
    // Afternoon window
    const afternoonStart = new Date(panchang.sunrise.getTime() + 6 * 60 * 60 * 1000)
    const afternoonEnd = new Date(panchang.sunrise.getTime() + 8 * 60 * 60 * 1000)
    
    if (!this.isInInauspiciousPeriod(afternoonStart, panchang)) {
      windows.push({ start: afternoonStart, end: afternoonEnd })
    }
    
    return windows
  }

  private static isInInauspiciousPeriod(time: Date, panchang: PanchangData): boolean {
    const timeMs = time.getTime()
    
    // Check Rahukaal
    if (timeMs >= panchang.rahukaal.start.getTime() && 
        timeMs <= panchang.rahukaal.end.getTime()) {
      return true
    }
    
    // Check Yamaganda
    if (timeMs >= panchang.yamaganda.start.getTime() && 
        timeMs <= panchang.yamaganda.end.getTime()) {
      return true
    }
    
    // Check Gulika
    if (timeMs >= panchang.gulika.start.getTime() && 
        timeMs <= panchang.gulika.end.getTime()) {
      return true
    }
    
    // Check Durmuhurtam
    for (const period of panchang.durmuhurtam) {
      if (timeMs >= period.start.getTime() && timeMs <= period.end.getTime()) {
        return true
      }
    }
    
    return false
  }

  private static calculateMuhurataScore(
    eventType: EventType,
    panchang: PanchangData,
    window: { start: Date; end: Date }
  ): number {
    let score = 50 // Base score
    
    // Tithi score
    score += this.getTithiScore(eventType, panchang.tithi)
    
    // Nakshatra score
    score += this.getNakshatraScore(eventType, panchang.nakshatra)
    
    // Yoga score
    score += this.getYogaScore(panchang.yoga)
    
    // Weekday score
    score += this.getWeekdayScore(eventType, panchang.date.getDay())
    
    // Abhijit bonus
    if (window.start.getTime() === panchang.abhijit.start.getTime()) {
      score += 10
    }
    
    return Math.min(100, score)
  }

  private static getTithiScore(eventType: EventType, tithi: string): number {
    const auspiciousTithis = ['Dwitiya', 'Tritiya', 'Panchami', 'Saptami', 
                              'Dashami', 'Ekadashi', 'Trayodashi', 'Purnima']
    
    for (const good of auspiciousTithis) {
      if (tithi.includes(good)) return 15
    }
    
    return 5
  }

  private static getNakshatraScore(eventType: EventType, nakshatra: string): number {
    const marriageNakshatras = ['Rohini', 'Mrigashira', 'Uttara Phalguni', 
                                'Hasta', 'Swati', 'Anuradha', 'Uttara Ashadha', 
                                'Uttara Bhadrapada', 'Revati']
    
    const businessNakshatras = ['Ashwini', 'Pushya', 'Hasta', 'Chitra', 
                                'Shravana', 'Dhanishta', 'Revati']
    
    if (eventType === 'marriage' && marriageNakshatras.includes(nakshatra)) {
      return 15
    }
    
    if (eventType === 'business' && businessNakshatras.includes(nakshatra)) {
      return 15
    }
    
    return 5
  }

  private static getYogaScore(yoga: string): number {
    const auspiciousYogas = ['Siddhi', 'Sadhya', 'Shubha', 'Shukla', 
                             'Brahma', 'Indra', 'Dhruva', 'Ayushman']
    
    return auspiciousYogas.includes(yoga) ? 10 : 5
  }

  private static getWeekdayScore(eventType: EventType, weekday: number): number {
    if (eventType === 'marriage') {
      const goodDays = [0, 1, 3, 4, 5] // Sunday, Monday, Wednesday, Thursday, Friday
      return goodDays.includes(weekday) ? 10 : 0
    }
    
    if (eventType === 'business') {
      const goodDays = [1, 3, 4, 5] // Monday, Wednesday, Thursday, Friday
      return goodDays.includes(weekday) ? 10 : 5
    }
    
    return 5
  }

  private static getSuitabilityLevel(score: number): string {
    if (score >= 90) return 'Excellent'
    if (score >= 80) return 'Very Good'
    if (score >= 70) return 'Good'
    return 'Fair'
  }

  private static getWeekdayName(day: number): string {
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days[day]
  }

  private static generateNotes(eventType: EventType, panchang: PanchangData): string[] {
    const notes: string[] = []
    
    if (panchang.yoga === 'Siddhi') {
      notes.push('Siddhi Yoga is highly auspicious for all activities')
    }
    
    if (panchang.nakshatra === 'Pushya') {
      notes.push('Pushya Nakshatra is considered one of the best for new beginnings')
    }
    
    if (eventType === 'marriage' && panchang.nakshatra === 'Rohini') {
      notes.push('Rohini is excellent for marriage ceremonies')
    }
    
    return notes
  }
}
