/**
 * Dasha Service
 * 
 * High-level service for Vimshottari Dasha calculations and analysis.
 * Provides methods for calculating, evaluating, and interpreting Dasha periods.
 */

import { 
  calculateVimshottariDasha, 
  getCurrentPeriods,
  getMahadashasInRange,
} from '../calculations/vimshottari';
import type { Planet, ChartData, Favorability, VimshottariDasha, MahadashaPeriod, AntardashaPeriod } from '../types/astrology';

/**
 * Dasha period with strength evaluation
 */
export interface EvaluatedDashaPeriod {
  planet: Planet;
  startDate: Date;
  endDate: Date;
  durationYears: number;
  strength: number; // 0-100
  favorability: Favorability;
  predictions: string[];
  lifeAreas: Record<string, string>;
}

/**
 * Current Dasha status
 */
export interface CurrentDashaStatus {
  mahadasha: EvaluatedDashaPeriod | null;
  antardasha: EvaluatedDashaPeriod | null;
  pratyantar: EvaluatedDashaPeriod | null;
  remainingDays: {
    mahadasha: number;
    antardasha: number;
    pratyantar: number;
  };
  percentComplete: {
    mahadasha: number;
    antardasha: number;
    pratyantar: number;
  };
}

/**
 * Dasha Service Class
 */
export class DashaService {
  private chart: ChartData;
  private dasha: VimshottariDasha;

  constructor(chart: ChartData) {
    this.chart = chart;
    
    // Get Moon's position for Dasha calculation
    const moonData = chart.planets.get('Moon');
    if (!moonData) {
      throw new Error('Moon position not found in chart');
    }
    
    this.dasha = calculateVimshottariDasha(
      chart.birthDate,
      moonData.absoluteDegree
    );
  }

  /**
   * Get complete Dasha system
   */
  getDasha(): VimshottariDasha {
    return this.dasha;
  }

  /**
   * Get current Dasha periods with evaluation
   */
  getCurrentStatus(date: Date = new Date()): CurrentDashaStatus {
    const current = getCurrentPeriods(this.dasha, date);
    
    return {
      mahadasha: current.mahadasha ? this.evaluatePeriod(current.mahadasha) : null,
      antardasha: current.antardasha ? this.evaluatePeriod(current.antardasha) : null,
      pratyantar: current.pratyantar ? this.evaluatePeriod(current.pratyantar) : null,
      remainingDays: {
        mahadasha: current.mahadasha ? this.getRemainingDays(current.mahadasha, date) : 0,
        antardasha: current.antardasha ? this.getRemainingDays(current.antardasha, date) : 0,
        pratyantar: current.pratyantar ? this.getRemainingDays(current.pratyantar, date) : 0,
      },
      percentComplete: {
        mahadasha: current.mahadasha ? this.getPercentComplete(current.mahadasha, date) : 0,
        antardasha: current.antardasha ? this.getPercentComplete(current.antardasha, date) : 0,
        pratyantar: current.pratyantar ? this.getPercentComplete(current.pratyantar, date) : 0,
      },
    };
  }

  /**
   * Get Dasha periods for a date range
   */
  getPeriodsInRange(startDate: Date, endDate: Date): MahadashaPeriod[] {
    return getMahadashasInRange(this.dasha, startDate, endDate);
  }

  /**
   * Evaluate planetary strength and favorability
   */
  private evaluatePeriod(period: MahadashaPeriod | AntardashaPeriod | any): EvaluatedDashaPeriod {
    const planetData = this.chart.planets.get(period.planet);
    if (!planetData) {
      return {
        planet: period.planet,
        startDate: period.startDate,
        endDate: period.endDate,
        durationYears: 0,
        strength: 50,
        favorability: 'neutral',
        predictions: [],
        lifeAreas: {},
      };
    }

    const strength = this.calculatePlanetaryStrength(period.planet, planetData);
    const favorability = this.determineFavorability(strength);
    const predictions = this.generatePredictions(period.planet, planetData);
    const lifeAreas = this.analyzeLifeAreas(period.planet, planetData);

    return {
      ...period,
      strength,
      favorability,
      predictions,
      lifeAreas,
    };
  }

  /**
   * Calculate planetary strength (0-100)
   */
  private calculatePlanetaryStrength(planet: Planet, planetData: any): number {
    let strength = 50; // Base strength

    // Dignity bonus/penalty
    switch (planetData.dignity) {
      case 'exalted':
        strength += 30;
        break;
      case 'own':
        strength += 20;
        break;
      case 'friend':
        strength += 10;
        break;
      case 'enemy':
        strength -= 10;
        break;
      case 'debilitated':
        strength -= 30;
        break;
    }

    // House placement (angular houses are strong)
    const angularHouses = [1, 4, 7, 10];
    const trineHouses = [1, 5, 9];
    
    if (angularHouses.includes(planetData.house)) {
      strength += 15;
    } else if (trineHouses.includes(planetData.house)) {
      strength += 10;
    }

    // Retrograde penalty (except for Jupiter and Saturn)
    if (planetData.retrograde && !['Jupiter', 'Saturn'].includes(planet)) {
      strength -= 5;
    }

    return Math.max(0, Math.min(100, strength));
  }

  /**
   * Determine favorability from strength
   */
  private determineFavorability(strength: number): Favorability {
    if (strength >= 80) return 'excellent';
    if (strength >= 65) return 'good';
    if (strength >= 45) return 'neutral';
    if (strength >= 30) return 'challenging';
    return 'difficult';
  }

  /**
   * Generate predictions for a planet period
   */
  private generatePredictions(planet: Planet, planetData: any): string[] {
    const predictions: string[] = [];
    
    // Base predictions by planet
    const basePredictions: Record<Planet, string[]> = {
      'Sun': ['Leadership opportunities', 'Recognition and authority', 'Government matters'],
      'Moon': ['Emotional growth', 'Public relations', 'Travel and changes'],
      'Mars': ['Energy and action', 'Property matters', 'Courage and initiative'],
      'Mercury': ['Communication skills', 'Business and trade', 'Learning and education'],
      'Jupiter': ['Wisdom and knowledge', 'Spiritual growth', 'Prosperity and expansion'],
      'Venus': ['Relationships and marriage', 'Luxury and comfort', 'Arts and creativity'],
      'Saturn': ['Hard work and discipline', 'Delays but lasting results', 'Karmic lessons'],
      'Rahu': ['Unconventional paths', 'Foreign connections', 'Material desires'],
      'Ketu': ['Spiritual insights', 'Detachment', 'Past life karma'],
    };

    predictions.push(...basePredictions[planet]);

    // Modify based on dignity
    if (planetData.dignity === 'exalted' || planetData.dignity === 'own') {
      predictions.push('Strong positive results expected');
    } else if (planetData.dignity === 'debilitated') {
      predictions.push('Challenges may arise, remedies recommended');
    }

    return predictions;
  }

  /**
   * Analyze life areas affected by planet
   */
  private analyzeLifeAreas(planet: Planet, planetData: any): Record<string, string> {
    const areas: Record<string, string> = {};
    
    // House-based analysis
    const houseSignifications: Record<number, string[]> = {
      1: ['Self', 'Personality', 'Health'],
      2: ['Wealth', 'Family', 'Speech'],
      3: ['Siblings', 'Courage', 'Communication'],
      4: ['Mother', 'Home', 'Happiness'],
      5: ['Children', 'Education', 'Creativity'],
      6: ['Health', 'Enemies', 'Service'],
      7: ['Marriage', 'Partnership', 'Business'],
      8: ['Longevity', 'Transformation', 'Occult'],
      9: ['Fortune', 'Father', 'Spirituality'],
      10: ['Career', 'Status', 'Authority'],
      11: ['Gains', 'Friends', 'Aspirations'],
      12: ['Losses', 'Spirituality', 'Foreign lands'],
    };

    const house = planetData.house;
    const significations = houseSignifications[house] || [];
    
    significations.forEach((area, index) => {
      areas[area] = `Influenced by ${planet} in house ${house}`;
    });

    return areas;
  }

  /**
   * Get remaining days in period
   */
  private getRemainingDays(period: any, currentDate: Date): number {
    const remaining = period.endDate.getTime() - currentDate.getTime();
    return Math.max(0, Math.ceil(remaining / (1000 * 60 * 60 * 24)));
  }

  /**
   * Get percent complete of period
   */
  private getPercentComplete(period: any, currentDate: Date): number {
    const total = period.endDate.getTime() - period.startDate.getTime();
    const elapsed = currentDate.getTime() - period.startDate.getTime();
    return Math.max(0, Math.min(100, (elapsed / total) * 100));
  }

  /**
   * Get next major Dasha change
   */
  getNextMajorChange(date: Date = new Date()): { type: string; planet: Planet; date: Date } | null {
    const current = getCurrentPeriods(this.dasha, date);
    
    if (current.antardasha) {
      return {
        type: 'Antardasha',
        planet: current.antardasha.planet,
        date: current.antardasha.endDate,
      };
    }
    
    if (current.mahadasha) {
      return {
        type: 'Mahadasha',
        planet: current.mahadasha.planet,
        date: current.mahadasha.endDate,
      };
    }
    
    return null;
  }
}
