/**
 * Akshit's Chart Data (from vargas_output.json)
 * Birth: Dec 26, 1994, 22:50, Kanpur | Leo Ascendant (Lahiri)
 */

import akshitDashaData from './akshitDashaData.json';

const vargasPlanets = [
  { name: 'Sun', sign: 'Sagittarius', lon: 250.834, house: 5, nakshatra: 'Mula', combust: false, dignity: 'neutral' },
  { name: 'Moon', sign: 'Virgo', lon: 171.577, house: 2, nakshatra: 'Hasta', combust: false, dignity: 'neutral' },
  { name: 'Mercury', sign: 'Sagittarius', lon: 257.978, house: 5, nakshatra: 'Purva Ashadha', combust: true, dignity: 'neutral' },
  { name: 'Venus', sign: 'Libra', lon: 205.333, house: 3, nakshatra: 'Vishakha', combust: false, dignity: 'own' },
  { name: 'Mars', sign: 'Leo', lon: 128.549, house: 1, nakshatra: 'Magha', combust: false, dignity: 'neutral' },
  { name: 'Jupiter', sign: 'Scorpio', lon: 219.852, house: 4, nakshatra: 'Anuradha', combust: false, dignity: 'neutral' },
  { name: 'Saturn', sign: 'Aquarius', lon: 313.773, house: 7, nakshatra: 'Shatabhisha', combust: false, dignity: 'own' },
  { name: 'Rahu', sign: 'Libra', lon: 199.687, house: 3, nakshatra: 'Swati', combust: false, dignity: 'neutral' },
  { name: 'Ketu', sign: 'Aries', lon: 19.687, house: 9, nakshatra: 'Bharani', combust: false, dignity: 'neutral' },
];

const NAKSHATRA_LORDS: Record<string, string> = {
  Mula: 'Ketu', Hasta: 'Moon', 'Purva Ashadha': 'Venus', Vishakha: 'Jupiter', Magha: 'Ketu',
  Anuradha: 'Saturn', Shatabhisha: 'Rahu', Swati: 'Rahu', Bharani: 'Venus',
};

export const akshitChartData = {
  birthDate: new Date('1994-12-26T22:50:00+05:30'),
  birthTime: '22:50:00',
  timezone: 'Asia/Kolkata',
  latitude: 26.4499,
  longitude: 80.3319,
  place: 'Kanpur',
  ayanamsa: 'Lahiri',

  ascendant: {
    sign: 'Leo',
    degree: 20.33,
    absoluteDegree: 140.33,
    nakshatra: 'Purva Phalguni',
    nakshatraLord: 'Venus',
  },

  planets: vargasPlanets.map((p) => ({
    planet: p.name,
    sign: p.sign,
    signLord: p.sign === 'Leo' ? 'Sun' : p.sign === 'Libra' ? 'Venus' : p.sign === 'Aquarius' ? 'Saturn' : 'Jupiter',
    degree: Math.round((p.lon % 30) * 1000) / 1000,
    absoluteDegree: p.lon,
    nakshatra: p.nakshatra,
    nakshatraLord: NAKSHATRA_LORDS[p.nakshatra] || 'Moon',
    pada: 4,
    house: p.house,
    retrograde: false,
    combust: p.combust,
    avastha: 'Kumara',
    dignity: p.dignity,
  })),

  houses: [
    { number: 1, sign: 'Leo', lord: 'Sun', planets: ['Mars'], cuspDegree: 140.33 },
    { number: 2, sign: 'Virgo', lord: 'Mercury', planets: ['Moon'], cuspDegree: 165.95 },
    { number: 3, sign: 'Libra', lord: 'Venus', planets: ['Venus', 'Rahu'], cuspDegree: 195.43 },
    { number: 4, sign: 'Scorpio', lord: 'Mars', planets: ['Jupiter'], cuspDegree: 227.69 },
    { number: 5, sign: 'Sagittarius', lord: 'Jupiter', planets: ['Sun', 'Mercury'], cuspDegree: 260.17 },
    { number: 6, sign: 'Capricorn', lord: 'Saturn', planets: [], cuspDegree: 291.15 },
    { number: 7, sign: 'Aquarius', lord: 'Saturn', planets: ['Saturn'], cuspDegree: 320.33 },
    { number: 8, sign: 'Pisces', lord: 'Jupiter', planets: [], cuspDegree: 345.95 },
    { number: 9, sign: 'Aries', lord: 'Mars', planets: ['Ketu'], cuspDegree: 15.43 },
    { number: 10, sign: 'Taurus', lord: 'Venus', planets: [], cuspDegree: 47.69 },
    { number: 11, sign: 'Gemini', lord: 'Mercury', planets: [], cuspDegree: 80.17 },
    { number: 12, sign: 'Cancer', lord: 'Moon', planets: [], cuspDegree: 111.15 },
  ],

  navamsa: {
    ascendant: { sign: 'Libra', degree: 25.33, nakshatra: 'Vishakha' },
    planets: [
      { planet: 'Sun', sign: 'Sagittarius', degree: 10.83, house: 10 },
      { planet: 'Moon', sign: 'Cancer', degree: 21.58, house: 10 },
      { planet: 'Mercury', sign: 'Sagittarius', degree: 17.98, house: 12 },
      { planet: 'Venus', sign: 'Taurus', degree: 25.33, house: 8 },
      { planet: 'Mars', sign: 'Gemini', degree: 8.55, house: 9 },
      { planet: 'Jupiter', sign: 'Scorpio', degree: 9.85, house: 12 },
      { planet: 'Saturn', sign: 'Aquarius', degree: 13.77, house: 5 },
      { planet: 'Rahu', sign: 'Libra', degree: 19.69, house: 6 },
      { planet: 'Ketu', sign: 'Aries', degree: 19.69, house: 12 },
    ],
  },

  yogas: {
    major: [
      { name: 'Musala Yoga', present: true, description: 'All planets in fixed signs. Brings fame, administrative abilities.' },
      { name: 'Malavya Yoga', present: true, description: 'Venus in own sign (Libra) in Kendra. Brings appreciation of beauty.' },
      { name: 'Sasa Yoga', present: true, description: 'Saturn in own sign (Aquarius) in Kendra. Brings nobility and political success.' },
    ],
    chandra: [
      { name: 'Sunafa Yoga', present: true, description: 'Venus in 2nd house from Moon. Brings wealth and good fortune.' },
      { name: 'Anafa Yoga', present: true, description: 'Mars in 12th house from Moon. Brings good health and charm.' },
    ],
    soorya: [] as { name: string; present: boolean; description: string }[],
    inauspicious: [
      { name: 'Kuja Yoga (Mangal Dosha)', present: true, description: 'Mars in 1st house. Remedies: marry another Manglik, worship Hanuman.' },
    ],
  },

  dashaBalance: {
    lord: akshitDashaData.data.dasha_balance.lord.name,
    duration: akshitDashaData.data.dasha_balance.description.trim(),
    durationDays: 0,
    description: `${akshitDashaData.data.dasha_balance.lord.name} Mahadasha balance at birth`,
  },

  currentDasha: {
    mahadasha: { planet: 'Jupiter', startDate: new Date('2019-01-22'), endDate: new Date('2035-01-22'), durationYears: 16 },
    antardasha: { planet: 'Mercury', startDate: new Date('2023-09-22'), endDate: new Date('2025-12-27') },
  },

  dashaTimeline: akshitDashaData.data.dasha_periods.slice(0, 5).map((p: { name: string; start: string; end: string; antardasha: { name: string; start: string; end: string }[] }) => ({
    planet: p.name,
    startDate: new Date(p.start),
    endDate: new Date(p.end),
    durationYears: Math.round((new Date(p.end).getTime() - new Date(p.start).getTime()) / (365.25 * 24 * 60 * 60 * 1000)),
    antardashas: p.antardasha.slice(0, 9).map((a: { name: string; start: string; end: string }) => ({
      planet: a.name,
      start: a.start.split('T')[0],
      end: a.end.split('T')[0],
    })),
  })),

  strengths: {
    Sun: { shadbala: 385, dignity: 'neutral', strength: 'moderate' },
    Moon: { shadbala: 420, dignity: 'neutral', strength: 'strong' },
    Mars: { shadbala: 365, dignity: 'neutral', strength: 'moderate' },
    Mercury: { shadbala: 340, dignity: 'neutral', strength: 'weak', combust: true },
    Jupiter: { shadbala: 395, dignity: 'neutral', strength: 'moderate' },
    Venus: { shadbala: 450, dignity: 'own', strength: 'very strong' },
    Saturn: { shadbala: 425, dignity: 'own', strength: 'strong' },
  },

  // From TRANSIT_REPORT_2026_2035.md - Feb 2026
  currentTransits: [
    { planet: 'Sun', sign: 'Aquarius', degree: 8.5, house: 7, speed: 1.0, retrograde: false },
    { planet: 'Moon', sign: 'Gemini', degree: 15.2, house: 11, speed: 13.2, retrograde: false },
    { planet: 'Mars', sign: 'Cancer', degree: 22.0, house: 12, speed: 0.5, retrograde: false },
    { planet: 'Mercury', sign: 'Aquarius', degree: 25.0, house: 7, speed: 1.2, retrograde: false },
    { planet: 'Jupiter', sign: 'Gemini', degree: 18.0, house: 11, speed: 0.1, retrograde: false },
    { planet: 'Venus', sign: 'Pisces', degree: 12.0, house: 8, speed: 1.1, retrograde: false },
    { planet: 'Saturn', sign: 'Aquarius', degree: 5.0, house: 6, speed: 0.05, retrograde: false },
    { planet: 'Rahu', sign: 'Pisces', degree: 28.0, house: 8, speed: -0.05, retrograde: true },
    { planet: 'Ketu', sign: 'Virgo', degree: 28.0, house: 2, speed: -0.05, retrograde: true },
  ],

  majorTransits: [
    { planet: 'Jupiter', event: 'Transiting Gemini (11th)', date: new Date('2026-01-01'), significance: 'Jupiter in 11th house brings gains, friendships, fulfillment of desires', impact: 'positive' },
    { planet: 'Saturn', event: 'Transiting Aquarius (7th)', date: new Date('2026-07-30'), significance: 'Saturn in 7th house — marriage timing, commitment', impact: 'mixed' },
    { planet: 'Jupiter', event: 'Double transit 2-7-11 window', date: new Date('2026-07-30'), significance: 'Jupiter in 11th + Saturn in 7th — marriage trigger window', impact: 'positive' },
  ],
};

export const akshitDashaDataForUI = akshitDashaData;
