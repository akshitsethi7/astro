/**
 * Shadow Planet Service
 * 
 * Analysis of Rahu and Ketu (shadow planets) including positions,
 * aspects, yogas, and life area impacts.
 */

import type { ChartData, Planet, ZodiacSign } from '../types/astrology';

export interface ShadowAnalysis {
  rahu: ShadowPlanetData;
  ketu: ShadowPlanetData;
  opposition: {
    isExact: boolean;
    degrees: number;
  };
  yogas: ShadowYoga[];
  lifeImpact: LifeAreaImpact[];
  remedies: Remedy[];
}

export interface ShadowPlanetData {
  planet: 'Rahu' | 'Ketu';
  sign: ZodiacSign;
  degree: number;
  house: number;
  nakshatra: string;
  interpretation: string;
  strength: number;
  aspects: Planet[];
}

export interface ShadowYoga {
  name: string;
  description: string;
  impact: 'positive' | 'negative' | 'mixed';
  strength: number;
}

export interface LifeAreaImpact {
  area: string;
  planet: 'Rahu' | 'Ketu';
  impact: string;
  intensity: 'high' | 'medium' | 'low';
}

export interface Remedy {
  type: 'mantra' | 'gemstone' | 'donation' | 'ritual' | 'lifestyle';
  planet: 'Rahu' | 'Ketu';
  title: string;
  description: string;
  timing?: string;
  difficulty: 'easy' | 'moderate' | 'advanced';
}

export class ShadowService {
  private chart: ChartData;

  constructor(chart: ChartData) {
    this.chart = chart;
  }

  /**
   * Get complete shadow planet analysis
   */
  getAnalysis(): ShadowAnalysis {
    const rahuData = this.chart.planets.get('Rahu');
    const ketuData = this.chart.planets.get('Ketu');

    if (!rahuData || !ketuData) {
      throw new Error('Shadow planet data not found');
    }

    const rahu = this.analyzeShadowPlanet('Rahu', rahuData);
    const ketu = this.analyzeShadowPlanet('Ketu', ketuData);
    const opposition = this.verifyOpposition(rahuData.absoluteDegree, ketuData.absoluteDegree);
    const yogas = this.detectYogas();
    const lifeImpact = this.analyzeLifeImpact(rahu, ketu);
    const remedies = this.generateRemedies(rahu, ketu);

    return {
      rahu,
      ketu,
      opposition,
      yogas,
      lifeImpact,
      remedies,
    };
  }

  /**
   * Analyze individual shadow planet
   */
  private analyzeShadowPlanet(planet: 'Rahu' | 'Ketu', data: any): ShadowPlanetData {
    const interpretation = this.getInterpretation(planet, data.sign, data.house);
    const strength = this.calculateStrength(planet, data);
    const aspects = this.getAspectedPlanets(planet, data.house);

    return {
      planet,
      sign: data.sign,
      degree: data.degree,
      house: data.house,
      nakshatra: data.nakshatra,
      interpretation,
      strength,
      aspects,
    };
  }

  /**
   * Verify 180-degree opposition between Rahu and Ketu
   */
  private verifyOpposition(rahuDegree: number, ketuDegree: number): { isExact: boolean; degrees: number } {
    let diff = Math.abs(rahuDegree - ketuDegree);
    if (diff > 180) diff = 360 - diff;
    
    const isExact = Math.abs(diff - 180) < 1; // Within 1 degree
    
    return {
      isExact,
      degrees: diff,
    };
  }

  /**
   * Detect shadow planet yogas
   */
  private detectYogas(): ShadowYoga[] {
    const yogas: ShadowYoga[] = [];
    
    // Kala Sarpa Yoga detection
    const kalaSarpa = this.detectKalaSarpaYoga();
    if (kalaSarpa) {
      yogas.push(kalaSarpa);
    }

    // Rahu-Venus conjunction
    const rahuVenus = this.detectRahuVenusYoga();
    if (rahuVenus) {
      yogas.push(rahuVenus);
    }

    // Guru Chandal Yoga (Jupiter-Rahu)
    const guruChandal = this.detectGuruChandalYoga();
    if (guruChandal) {
      yogas.push(guruChandal);
    }

    return yogas;
  }

  /**
   * Detect Kala Sarpa Yoga
   */
  private detectKalaSarpaYoga(): ShadowYoga | null {
    const rahuData = this.chart.planets.get('Rahu');
    const ketuData = this.chart.planets.get('Ketu');
    
    if (!rahuData || !ketuData) return null;

    // Check if all planets are between Rahu and Ketu
    let allBetween = true;
    const planets: Planet[] = ['Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn'];
    
    for (const planet of planets) {
      const planetData = this.chart.planets.get(planet);
      if (!planetData) continue;
      
      // Simplified check - in production, use proper arc calculation
      const degree = planetData.absoluteDegree;
      const rahuDeg = rahuData.absoluteDegree;
      const ketuDeg = ketuData.absoluteDegree;
      
      // Check if planet is in the Rahu-Ketu axis
      const inAxis = this.isBetweenNodes(degree, rahuDeg, ketuDeg);
      if (!inAxis) {
        allBetween = false;
        break;
      }
    }

    if (allBetween) {
      return {
        name: 'Kala Sarpa Yoga',
        description: 'All planets hemmed between Rahu and Ketu, creating intense karmic patterns',
        impact: 'mixed',
        strength: 85,
      };
    }

    return null;
  }

  /**
   * Check if degree is between Rahu and Ketu
   */
  private isBetweenNodes(degree: number, rahuDeg: number, ketuDeg: number): boolean {
    // Simplified logic - in production, handle all cases properly
    if (rahuDeg < ketuDeg) {
      return degree > rahuDeg && degree < ketuDeg;
    } else {
      return degree > rahuDeg || degree < ketuDeg;
    }
  }

  /**
   * Detect Rahu-Venus yoga
   */
  private detectRahuVenusYoga(): ShadowYoga | null {
    const rahuData = this.chart.planets.get('Rahu');
    const venusData = this.chart.planets.get('Venus');
    
    if (!rahuData || !venusData) return null;

    // Check if in same house or conjunct
    if (rahuData.house === venusData.house) {
      return {
        name: 'Rahu-Venus Yoga',
        description: 'Amplifies desires for luxury, relationships, and material pleasures',
        impact: 'mixed',
        strength: 70,
      };
    }

    return null;
  }

  /**
   * Detect Guru Chandal Yoga
   */
  private detectGuruChandalYoga(): ShadowYoga | null {
    const rahuData = this.chart.planets.get('Rahu');
    const jupiterData = this.chart.planets.get('Jupiter');
    
    if (!rahuData || !jupiterData) return null;

    if (rahuData.house === jupiterData.house) {
      return {
        name: 'Guru Chandal Yoga',
        description: 'Jupiter-Rahu conjunction affecting wisdom and spiritual growth',
        impact: 'negative',
        strength: 75,
      };
    }

    return null;
  }

  /**
   * Get interpretation for shadow planet placement
   */
  private getInterpretation(planet: 'Rahu' | 'Ketu', sign: ZodiacSign, house: number): string {
    const interpretations: Record<string, Record<number, string>> = {
      'Rahu': {
        1: 'Strong desire for self-identity and recognition. Unconventional personality.',
        2: 'Unusual sources of wealth. Foreign connections in family matters.',
        3: 'Courage through unconventional means. Innovative communication.',
        4: 'Foreign lands or unusual home environment. Mother may be unique.',
        5: 'Unconventional children or creative pursuits. Speculative gains.',
        6: 'Victory over enemies through unusual means. Health issues from stress.',
        7: 'Foreign spouse or unconventional partnerships. Business abroad.',
        8: 'Interest in occult and mysteries. Sudden transformations.',
        9: 'Foreign travel and spiritual seeking. Unconventional beliefs.',
        10: 'Career in foreign lands or unusual fields. Fame through innovation.',
        11: 'Gains through foreign connections. Unusual friend circles.',
        12: 'Strong spiritual inclinations. Foreign residence or isolation.',
      },
      'Ketu': {
        1: 'Spiritual personality. Detachment from ego. Past life wisdom.',
        2: 'Detachment from wealth. Spiritual family values.',
        3: 'Intuitive communication. Detached from siblings.',
        4: 'Spiritual home environment. Detachment from mother.',
        5: 'Spiritual children. Detachment from romance. Past life creativity.',
        6: 'Spiritual approach to service. Natural healing abilities.',
        7: 'Spiritual partnerships. Detachment in relationships.',
        8: 'Deep occult knowledge. Spiritual transformation.',
        9: 'Strong spiritual wisdom. Detachment from father. Moksha focus.',
        10: 'Spiritual career. Detachment from worldly status.',
        11: 'Detachment from gains. Spiritual friendships.',
        12: 'Strong moksha desire. Natural meditation abilities. Liberation focus.',
      },
    };

    return interpretations[planet][house] || 'Unique karmic influence in this area of life.';
  }

  /**
   * Calculate shadow planet strength
   */
  private calculateStrength(planet: 'Rahu' | 'Ketu', data: any): number {
    let strength = 50;

    // House placement
    const beneficHouses = [1, 3, 6, 10, 11];
    if (beneficHouses.includes(data.house)) {
      strength += 20;
    }

    // Sign placement (Rahu exalted in Taurus, Ketu in Scorpio)
    if (planet === 'Rahu' && data.sign === 'Taurus') strength += 25;
    if (planet === 'Ketu' && data.sign === 'Scorpio') strength += 25;
    if (planet === 'Rahu' && data.sign === 'Scorpio') strength -= 25;
    if (planet === 'Ketu' && data.sign === 'Taurus') strength -= 25;

    return Math.max(0, Math.min(100, strength));
  }

  /**
   * Get planets aspected by shadow planet
   */
  private getAspectedPlanets(planet: 'Rahu' | 'Ketu', house: number): Planet[] {
    const aspected: Planet[] = [];
    
    // Shadow planets aspect 5th, 7th, and 9th houses from themselves
    const aspectHouses = [
      (house + 4) % 12 || 12,
      (house + 6) % 12 || 12,
      (house + 8) % 12 || 12,
    ];

    const planets: Planet[] = ['Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn'];
    
    for (const p of planets) {
      const planetData = this.chart.planets.get(p);
      if (planetData && aspectHouses.includes(planetData.house)) {
        aspected.push(p);
      }
    }

    return aspected;
  }

  /**
   * Analyze life area impacts
   */
  private analyzeLifeImpact(rahu: ShadowPlanetData, ketu: ShadowPlanetData): LifeAreaImpact[] {
    const impacts: LifeAreaImpact[] = [];

    // Rahu impacts
    impacts.push({
      area: this.getHouseArea(rahu.house),
      planet: 'Rahu',
      impact: `Amplifies desires and creates unconventional approaches in ${this.getHouseArea(rahu.house).toLowerCase()}`,
      intensity: rahu.strength > 70 ? 'high' : rahu.strength > 50 ? 'medium' : 'low',
    });

    // Ketu impacts
    impacts.push({
      area: this.getHouseArea(ketu.house),
      planet: 'Ketu',
      impact: `Brings detachment and spiritual wisdom to ${this.getHouseArea(ketu.house).toLowerCase()}`,
      intensity: ketu.strength > 70 ? 'high' : ketu.strength > 50 ? 'medium' : 'low',
    });

    return impacts;
  }

  /**
   * Get house area name
   */
  private getHouseArea(house: number): string {
    const areas: Record<number, string> = {
      1: 'Self & Personality',
      2: 'Wealth & Family',
      3: 'Courage & Siblings',
      4: 'Home & Mother',
      5: 'Children & Creativity',
      6: 'Health & Service',
      7: 'Marriage & Partnership',
      8: 'Transformation & Occult',
      9: 'Fortune & Spirituality',
      10: 'Career & Status',
      11: 'Gains & Friends',
      12: 'Liberation & Losses',
    };
    return areas[house] || 'Unknown';
  }

  /**
   * Generate remedies
   */
  private generateRemedies(rahu: ShadowPlanetData, ketu: ShadowPlanetData): Remedy[] {
    const remedies: Remedy[] = [];

    // Rahu remedies
    if (rahu.strength < 60) {
      remedies.push({
        type: 'mantra',
        planet: 'Rahu',
        title: 'Rahu Beej Mantra',
        description: 'Om Bhram Bhreem Bhroum Sah Rahave Namah (108 times daily)',
        timing: 'Saturday evenings or Rahu Kaal',
        difficulty: 'easy',
      });

      remedies.push({
        type: 'gemstone',
        planet: 'Rahu',
        title: 'Hessonite (Gomed)',
        description: 'Wear hessonite gemstone in silver on middle finger',
        timing: 'Saturday during Rahu hora',
        difficulty: 'moderate',
      });

      remedies.push({
        type: 'donation',
        planet: 'Rahu',
        title: 'Saturday Donations',
        description: 'Donate black sesame seeds, blankets, or iron items to the needy',
        timing: 'Saturdays',
        difficulty: 'easy',
      });
    }

    // Ketu remedies
    if (ketu.strength < 60) {
      remedies.push({
        type: 'mantra',
        planet: 'Ketu',
        title: 'Ketu Beej Mantra',
        description: 'Om Shram Shreem Shroum Sah Ketave Namah (108 times daily)',
        timing: 'Tuesday evenings',
        difficulty: 'easy',
      });

      remedies.push({
        type: 'gemstone',
        planet: 'Ketu',
        title: "Cat's Eye (Lehsunia)",
        description: "Wear cat's eye gemstone in silver on middle finger",
        timing: 'Tuesday during Ketu hora',
        difficulty: 'moderate',
      });

      remedies.push({
        type: 'lifestyle',
        planet: 'Ketu',
        title: 'Meditation Practice',
        description: 'Regular meditation and spiritual practices to balance Ketu energy',
        difficulty: 'moderate',
      });
    }

    return remedies;
  }
}
