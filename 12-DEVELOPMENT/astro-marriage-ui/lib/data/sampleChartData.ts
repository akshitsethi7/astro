/**
 * Sample Chart Data from chartsimp
 * Birth Details: June 6, 1985, 22:57:55, IST
 * Location: India
 */

export const sampleChartData = {
  birthDate: new Date('1985-06-06T22:57:55+05:30'),
  birthTime: '22:57:55',
  timezone: 'Asia/Kolkata',
  latitude: 28.6139,
  longitude: 77.2090,
  ayanamsa: 'Lahiri',
  
  // D1 Chart (Rashi)
  ascendant: {
    sign: 'Leo',
    degree: 23.047, // 23°2'49"
    absoluteDegree: 143.047,
    nakshatra: 'Purva Phalguni',
    nakshatraLord: 'Venus',
  },
  
  planets: [
    {
      planet: 'Sun',
      sign: 'Sagittarius',
      signLord: 'Jupiter',
      degree: 10.919, // 10°55'8"
      absoluteDegree: 250.919,
      nakshatra: 'Mula',
      nakshatraLord: 'Ketu',
      pada: 2,
      house: 5,
      retrograde: false,
      combust: false,
      avastha: 'Kumara',
      dignity: 'neutral',
    },
    {
      planet: 'Moon',
      sign: 'Virgo',
      signLord: 'Mercury',
      degree: 22.737, // 22°44'12"
      absoluteDegree: 172.737,
      nakshatra: 'Hasta',
      nakshatraLord: 'Moon',
      pada: 4,
      house: 2,
      retrograde: false,
      combust: false,
      avastha: 'Kumara',
      dignity: 'neutral',
    },
    {
      planet: 'Mercury',
      sign: 'Sagittarius',
      signLord: 'Jupiter',
      degree: 18.112, // 18°6'44"
      absoluteDegree: 258.112,
      nakshatra: 'Purva Ashadha',
      nakshatraLord: 'Venus',
      pada: 1,
      house: 5,
      retrograde: false,
      combust: true,
      avastha: 'Vriddha',
      dignity: 'enemy',
    },
    {
      planet: 'Venus',
      sign: 'Libra',
      signLord: 'Venus',
      degree: 25.404, // 25°24'15"
      absoluteDegree: 205.404,
      nakshatra: 'Vishakha',
      nakshatraLord: 'Jupiter',
      pada: 4,
      house: 3,
      retrograde: false,
      combust: false,
      avastha: 'Mrita',
      dignity: 'own', // Venus in own sign Libra
    },
    {
      planet: 'Mars',
      sign: 'Leo',
      signLord: 'Sun',
      degree: 8.556, // 8°33'21"
      absoluteDegree: 128.556,
      nakshatra: 'Magha',
      nakshatraLord: 'Ketu',
      pada: 1,
      house: 1,
      retrograde: false,
      combust: false,
      avastha: 'Kumara',
      dignity: 'neutral',
    },
    {
      planet: 'Jupiter',
      sign: 'Scorpio',
      signLord: 'Mars',
      degree: 9.869, // 9°52'8"
      absoluteDegree: 219.869,
      nakshatra: 'Anuradha',
      nakshatraLord: 'Saturn',
      pada: 1,
      house: 4,
      retrograde: false,
      combust: false,
      avastha: 'Vriddha',
      dignity: 'neutral',
    },
    {
      planet: 'Saturn',
      sign: 'Aquarius',
      signLord: 'Saturn',
      degree: 13.779, // 13°46'46"
      absoluteDegree: 313.779,
      nakshatra: 'Shatabhisha',
      nakshatraLord: 'Rahu',
      pada: 1,
      house: 7,
      retrograde: false,
      combust: false,
      avastha: 'Yuva',
      dignity: 'own', // Saturn in own sign Aquarius
    },
    {
      planet: 'Rahu',
      sign: 'Libra',
      signLord: 'Venus',
      degree: 18.257, // 18°15'25"
      absoluteDegree: 198.257,
      nakshatra: 'Swati',
      nakshatraLord: 'Rahu',
      pada: 2,
      house: 3,
      retrograde: true,
      combust: false,
      avastha: 'Vriddha',
      dignity: 'neutral',
    },
    {
      planet: 'Ketu',
      sign: 'Aries',
      signLord: 'Mars',
      degree: 18.257, // 18°15'25"
      absoluteDegree: 18.257,
      nakshatra: 'Bharani',
      nakshatraLord: 'Venus',
      pada: 4,
      house: 9,
      retrograde: true,
      combust: false,
      avastha: 'Vriddha',
      dignity: 'neutral',
    },
  ],
  
  houses: [
    { number: 1, sign: 'Leo', lord: 'Sun', planets: ['Mars'], cuspDegree: 143.047 },
    { number: 2, sign: 'Virgo', lord: 'Mercury', planets: ['Moon'], cuspDegree: 173.047 },
    { number: 3, sign: 'Libra', lord: 'Venus', planets: ['Venus', 'Rahu'], cuspDegree: 203.047 },
    { number: 4, sign: 'Scorpio', lord: 'Mars', planets: ['Jupiter'], cuspDegree: 233.047 },
    { number: 5, sign: 'Sagittarius', lord: 'Jupiter', planets: ['Sun', 'Mercury'], cuspDegree: 263.047 },
    { number: 6, sign: 'Capricorn', lord: 'Saturn', planets: [], cuspDegree: 293.047 },
    { number: 7, sign: 'Aquarius', lord: 'Saturn', planets: ['Saturn'], cuspDegree: 323.047 },
    { number: 8, sign: 'Pisces', lord: 'Jupiter', planets: [], cuspDegree: 353.047 },
    { number: 9, sign: 'Aries', lord: 'Mars', planets: ['Ketu'], cuspDegree: 23.047 },
    { number: 10, sign: 'Taurus', lord: 'Venus', planets: [], cuspDegree: 53.047 },
    { number: 11, sign: 'Gemini', lord: 'Mercury', planets: [], cuspDegree: 83.047 },
    { number: 12, sign: 'Cancer', lord: 'Moon', planets: [], cuspDegree: 113.047 },
  ],
  
  // D9 Chart (Navamsa) - from chartsimp
  navamsa: {
    ascendant: {
      sign: 'Scorpio',
      degree: 23.047,
      nakshatra: 'Jyeshtha',
    },
    planets: [
      { planet: 'Sun', sign: 'Sagittarius', degree: 10.919, house: 10 },
      { planet: 'Moon', sign: 'Virgo', degree: 22.737, house: 10 },
      { planet: 'Mercury', sign: 'Sagittarius', degree: 18.112, house: 12 },
      { planet: 'Venus', sign: 'Libra', degree: 25.404, house: 8 },
      { planet: 'Mars', sign: 'Leo', degree: 8.556, house: 9 },
      { planet: 'Jupiter', sign: 'Scorpio', degree: 9.869, house: 12 },
      { planet: 'Saturn', sign: 'Aquarius', degree: 13.779, house: 5 },
      { planet: 'Rahu', sign: 'Libra', degree: 18.257, house: 6 },
      { planet: 'Ketu', sign: 'Aries', degree: 18.257, house: 12 },
    ],
  },
  
  // Yogas
  yogas: {
    major: [
      {
        name: 'Musala Yoga',
        present: true,
        description: 'All planets in fixed signs (Taurus, Leo, Scorpio, Aquarius). Brings fame, administrative abilities, but inflexibility.',
      },
      {
        name: 'Raja Yoga',
        present: true,
        description: 'Relationship between Venus and Ketu. Brings social status and recognition.',
      },
      {
        name: 'Malavya Yoga',
        present: true,
        description: 'Venus in own sign (Libra) in Kendra. Brings appreciation of beauty and luxury.',
      },
      {
        name: 'Sasa Yoga',
        present: true,
        description: 'Saturn in own sign (Aquarius) in Kendra. Brings nobility and political success.',
      },
    ],
    chandra: [
      {
        name: 'Sunafa Yoga',
        present: true,
        description: 'Venus in 2nd house from Moon. Brings wealth and good fortune.',
      },
      {
        name: 'Anafa Yoga',
        present: true,
        description: 'Mars in 12th house from Moon. Brings good health and charm.',
      },
      {
        name: 'Durudhara Yoga',
        present: true,
        description: 'Planets on both sides of Moon. Brings luxury and generosity.',
      },
    ],
    soorya: [
      {
        name: 'Vaasi Yoga',
        present: true,
        description: 'Jupiter in 12th house from Sun. Brings wealth and intelligence.',
      },
    ],
    inauspicious: [
      {
        name: 'Kuja Yoga (Mangal Dosha)',
        present: true,
        description: 'Mars in 1st house. Remedies: marry another Manglik, worship Hanuman.',
      },
    ],
  },
  
  // Dasha Balance at Birth
  dashaBalance: {
    lord: 'Moon',
    duration: '5 months 11 days',
    durationDays: 171,
    description: 'Moon Mahadasha balance at birth',
  },
  
  // Current Dasha Periods (from chartsimp)
  currentDasha: {
    mahadasha: {
      planet: 'Rahu',
      startDate: new Date('2002-06-07T04:57:55+05:30'),
      endDate: new Date('2020-06-07T04:57:54+05:30'),
      durationYears: 18,
    },
    antardasha: {
      planet: 'Jupiter',
      startDate: new Date('2005-02-17T09:09:55+05:30'),
      endDate: new Date('2007-07-13T23:33:54+05:30'),
    },
  },
  
  // Complete Dasha Timeline (first few periods from chartsimp)
  dashaTimeline: [
    {
      planet: 'Moon',
      startDate: new Date('1985-06-06T22:57:55+05:30'),
      endDate: new Date('1995-06-07T10:57:54+05:30'),
      durationYears: 10,
      antardashas: [
        { planet: 'Moon', start: '1985-06-06', end: '1986-04-07' },
        { planet: 'Mars', start: '1986-04-07', end: '1986-11-06' },
        { planet: 'Rahu', start: '1986-11-06', end: '1988-05-07' },
        { planet: 'Jupiter', start: '1988-05-07', end: '1989-09-06' },
        { planet: 'Saturn', start: '1989-09-06', end: '1991-04-07' },
        { planet: 'Mercury', start: '1991-04-07', end: '1992-09-06' },
        { planet: 'Ketu', start: '1992-09-06', end: '1993-04-07' },
        { planet: 'Venus', start: '1993-04-07', end: '1994-12-06' },
        { planet: 'Sun', start: '1994-12-06', end: '1995-06-07' },
      ],
    },
    {
      planet: 'Mars',
      startDate: new Date('1995-06-07T10:57:55+05:30'),
      endDate: new Date('2002-06-07T04:57:54+05:30'),
      durationYears: 7,
      antardashas: [
        { planet: 'Mars', start: '1995-06-07', end: '1995-11-03' },
        { planet: 'Rahu', start: '1995-11-03', end: '1996-11-21' },
        { planet: 'Jupiter', start: '1996-11-21', end: '1997-10-28' },
        { planet: 'Saturn', start: '1997-10-28', end: '1998-12-06' },
        { planet: 'Mercury', start: '1998-12-06', end: '1999-12-04' },
        { planet: 'Ketu', start: '1999-12-04', end: '2000-05-01' },
        { planet: 'Venus', start: '2000-05-01', end: '2001-07-01' },
        { planet: 'Sun', start: '2001-07-01', end: '2001-11-06' },
        { planet: 'Moon', start: '2001-11-06', end: '2002-06-07' },
      ],
    },
    {
      planet: 'Rahu',
      startDate: new Date('2002-06-07T04:57:55+05:30'),
      endDate: new Date('2020-06-07T04:57:54+05:30'),
      durationYears: 18,
      antardashas: [
        { planet: 'Rahu', start: '2002-06-07', end: '2005-02-17' },
        { planet: 'Jupiter', start: '2005-02-17', end: '2007-07-13' },
        { planet: 'Saturn', start: '2007-07-13', end: '2010-05-19' },
        { planet: 'Mercury', start: '2010-05-19', end: '2013-01-05' },
        { planet: 'Ketu', start: '2013-01-05', end: '2014-01-23' },
        { planet: 'Venus', start: '2014-01-23', end: '2017-01-23' },
        { planet: 'Sun', start: '2017-01-23', end: '2018-01-07' },
        { planet: 'Moon', start: '2018-01-07', end: '2019-07-07' },
        { planet: 'Mars', start: '2019-07-07', end: '2020-06-07' },
      ],
    },
    {
      planet: 'Jupiter',
      startDate: new Date('2020-06-07T04:57:55+05:30'),
      endDate: new Date('2036-06-07T04:57:54+05:30'),
      durationYears: 16,
      antardashas: [
        { planet: 'Jupiter', start: '2020-06-07', end: '2022-08-13' },
        { planet: 'Saturn', start: '2022-08-13', end: '2025-02-23' },
        { planet: 'Mercury', start: '2025-02-23', end: '2027-06-10' },
        { planet: 'Ketu', start: '2027-06-10', end: '2028-05-16' },
        { planet: 'Venus', start: '2028-05-16', end: '2031-01-15' },
        { planet: 'Sun', start: '2031-01-15', end: '2031-11-29' },
        { planet: 'Moon', start: '2031-11-29', end: '2033-03-29' },
        { planet: 'Mars', start: '2033-03-29', end: '2034-03-05' },
        { planet: 'Rahu', start: '2034-03-05', end: '2036-06-07' },
      ],
    },
  ],
  
  // Planetary Strengths
  strengths: {
    Sun: { shadbala: 385, dignity: 'neutral', strength: 'moderate' },
    Moon: { shadbala: 420, dignity: 'neutral', strength: 'strong' },
    Mars: { shadbala: 365, dignity: 'neutral', strength: 'moderate' },
    Mercury: { shadbala: 340, dignity: 'enemy', strength: 'weak', combust: true },
    Jupiter: { shadbala: 395, dignity: 'neutral', strength: 'moderate' },
    Venus: { shadbala: 450, dignity: 'own', strength: 'very strong' },
    Saturn: { shadbala: 425, dignity: 'own', strength: 'strong' },
  },
  
  // Current Transits (as of Feb 2026)
  currentTransits: [
    { planet: 'Sun', sign: 'Aquarius', degree: 8.5, house: 7, speed: 1.0, retrograde: false },
    { planet: 'Moon', sign: 'Gemini', degree: 15.2, house: 11, speed: 13.2, retrograde: false },
    { planet: 'Mars', sign: 'Cancer', degree: 22.0, house: 12, speed: 0.5, retrograde: false },
    { planet: 'Mercury', sign: 'Aquarius', degree: 25.0, house: 7, speed: 1.2, retrograde: false },
    { planet: 'Jupiter', sign: 'Gemini', degree: 18.0, house: 11, speed: 0.1, retrograde: false },
    { planet: 'Venus', sign: 'Pisces', degree: 12.0, house: 8, speed: 1.1, retrograde: false },
    { planet: 'Saturn', sign: 'Pisces', degree: 5.0, house: 8, speed: 0.05, retrograde: false },
    { planet: 'Rahu', sign: 'Pisces', degree: 28.0, house: 8, speed: -0.05, retrograde: true },
    { planet: 'Ketu', sign: 'Virgo', degree: 28.0, house: 2, speed: -0.05, retrograde: true },
  ],
};
