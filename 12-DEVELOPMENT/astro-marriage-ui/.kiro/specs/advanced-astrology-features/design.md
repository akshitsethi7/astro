# Design Document - Advanced Astrology Features

## Overview

This design document outlines the technical architecture for implementing advanced Vedic astrology features including Dasha analysis, Shadow planet (Rahu/Ketu) analysis, and Transit predictions. The system will provide professional-grade astrological calculations and visualizations similar to Lagna360.

### Goals
- Provide accurate Vimshottari Dasha calculations with multi-level periods
- Offer comprehensive Rahu/Ketu analysis with interpretations
- Display real-time transit positions and predictions
- Create interactive, responsive visualizations
- Ensure calculation accuracy using established ephemeris data
- Maintain performance with complex astronomical calculations

### Non-Goals
- Horary astrology (Prashna)
- Muhurta (electional astrology) 
- KP system calculations
- Ashtakavarga detailed scoring (future enhancement)

---

## Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Presentation Layer                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Dasha View   │  │ Shadow View  │  │ Transit View │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            │
┌─────────────────────────────────────────────────────────────┐
│                    Component Layer                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ DashaTimeline│  │ ShadowChart  │  │ TransitChart │     │
│  │ DashaPeriods │  │ ShadowTable  │  │ TransitTable │     │
│  │ DashaDetails │  │ RemedyCard   │  │ AlertPanel   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            │
┌─────────────────────────────────────────────────────────────┐
│                     Service Layer                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │DashaService  │  │ShadowService │  │TransitService│     │
│  │              │  │              │  │              │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            │
┌─────────────────────────────────────────────────────────────┐
│                  Calculation Engine                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Vimshottari  │  │  Ephemeris   │  │   Aspects    │     │
│  │ Calculator   │  │  Calculator  │  │  Calculator  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            │
┌─────────────────────────────────────────────────────────────┐
│                      Data Layer                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Birth Chart  │  │  Ephemeris   │  │Interpretation│     │
│  │    Data      │  │    Data      │  │    Rules     │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

### Technology Stack

**Frontend:**
- Next.js 15 (React framework)
- TypeScript (type safety)
- D3.js (visualizations)
- date-fns (date manipulation)
- SCSS Modules (styling)

**Calculation Libraries:**
- astronomy-engine (planetary positions) OR
- swisseph (Swiss Ephemeris - more accurate)
- Custom Vimshottari Dasha calculator

**State Management:**
- React Context for global state
- Local component state for UI interactions
- Server-side calculations where possible

---

## Components and Interfaces

### 1. Dasha Components

#### DashaTimeline Component
```typescript
interface DashaTimelineProps {
  birthDate: Date
  birthTime: string
  timezone: string
  startDate?: Date
  endDate?: Date
  onPeriodSelect?: (period: DashaPeriod) => void
}

interface DashaPeriod {
  planet: Planet
  startDate: Date
  endDate: Date
  level: 'mahadasha' | 'antardasha' | 'pratyantar'
  subPeriods?: DashaPeriod[]
  predictions?: Prediction[]
  strength: number // 0-100
  favorability: 'excellent' | 'good' | 'neutral' | 'challenging' | 'difficult'
}
```

#### DashaPeriodCard Component
```typescript
interface DashaPeriodCardProps {
  period: DashaPeriod
  isExpanded: boolean
  onToggle: () => void
  showPredictions: boolean
}
```

#### DashaPredictions Component
```typescript
interface DashaPredictionsProps {
  mahadasha: Planet
  antardasha: Planet
  pratyantar?: Planet
  natalChart: ChartData
  categories: PredictionCategory[]
}

interface Prediction {
  category: 'marriage' | 'career' | 'health' | 'finance' | 'spiritual'
  title: string
  description: string
  confidence: number // 0-100
  timing?: DateRange
  remedies?: Remedy[]
}
```

### 2. Shadow Planet Components

#### ShadowAnalysis Component
```typescript
interface ShadowAnalysisProps {
  rahuPosition: PlanetPosition
  ketuPosition: PlanetPosition
  natalChart: ChartData
  navamsaChart: ChartData
}

interface PlanetPosition {
  planet: 'Rahu' | 'Ketu'
  sign: ZodiacSign
  degree: number
  house: number
  nakshatra: Nakshatra
  pada: number
  retrograde: boolean
}

interface ShadowInterpretation {
  planet: 'Rahu' | 'Ketu'
  houseEffects: string[]
  signEffects: string[]
  nakshatraEffects: string[]
  aspects: AspectInfo[]
  yogas: Yoga[]
  lifeAreas: {
    marriage: string
    career: string
    spiritual: string
  }
}
```

#### ShadowRemedies Component
```typescript
interface ShadowRemediesProps {
  planet: 'Rahu' | 'Ketu'
  affliction: AfflictionLevel
  chartStrength: number
}

interface Remedy {
  type: 'mantra' | 'gemstone' | 'donation' | 'ritual' | 'lifestyle'
  title: string
  description: string
  timing: RemedyTiming
  difficulty: 'easy' | 'moderate' | 'advanced'
  cost: 'free' | 'low' | 'medium' | 'high'
  effectiveness: number // 0-100
}

interface RemedyTiming {
  days?: string[] // ['Monday', 'Saturday']
  hours?: string[] // ['Sunrise', 'Sunset']
  duration?: string // '40 days', '108 days'
}
```

### 3. Transit Components

#### TransitChart Component
```typescript
interface TransitChartProps {
  natalChart: ChartData
  transitDate: Date
  showAspects: boolean
  highlightSignificant: boolean
}

interface TransitPosition {
  planet: Planet
  sign: ZodiacSign
  degree: number
  house: number // natal house being transited
  speed: number // degrees per day
  retrograde: boolean
  aspects: TransitAspect[]
}

interface TransitAspect {
  transitPlanet: Planet
  natalPlanet: Planet
  aspectType: AspectType
  orb: number
  applying: boolean
  significance: number // 0-100
}
```

#### TransitPredictions Component
```typescript
interface TransitPredictionsProps {
  transits: TransitPosition[]
  natalChart: ChartData
  dateRange: DateRange
}

interface TransitPrediction {
  planet: Planet
  transitingHouse: number
  startDate: Date
  endDate: Date
  effects: string[]
  significance: 'major' | 'moderate' | 'minor'
  category: PredictionCategory
}
```

#### SadeSatiIndicator Component
```typescript
interface SadeSatiIndicatorProps {
  natalMoonSign: ZodiacSign
  currentSaturnSign: ZodiacSign
}

interface SadeSatiInfo {
  isActive: boolean
  phase: 'rising' | 'peak' | 'setting' | null
  startDate: Date
  endDate: Date
  currentPhaseStart: Date
  currentPhaseEnd: Date
  effects: string[]
  remedies: Remedy[]
}
```

### 4. Shared Components

#### AspectLines Component (D3.js)
```typescript
interface AspectLinesProps {
  aspects: Aspect[]
  planetPositions: Map<Planet, Position>
  chartRadius: number
}

interface Aspect {
  planet1: Planet
  planet2: Planet
  type: AspectType
  orb: number
  strength: number
}

type AspectType = 'conjunction' | 'opposition' | 'trine' | 'square' | 'sextile'
```

---

## Data Models

### Core Data Structures

```typescript
// Birth Chart Data
interface ChartData {
  birthDate: Date
  birthTime: string
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

interface PlanetData {
  sign: ZodiacSign
  degree: number
  house: number
  nakshatra: Nakshatra
  pada: number
  retrograde: boolean
  dignity: Dignity
  speed: number
}

type Planet = 'Sun' | 'Moon' | 'Mars' | 'Mercury' | 'Jupiter' | 'Venus' | 'Saturn' | 'Rahu' | 'Ketu'
type ZodiacSign = 'Aries' | 'Taurus' | 'Gemini' | 'Cancer' | 'Leo' | 'Virgo' | 
                  'Libra' | 'Scorpio' | 'Sagittarius' | 'Capricorn' | 'Aquarius' | 'Pisces'
type Dignity = 'own' | 'exalted' | 'debilitated' | 'friend' | 'enemy' | 'neutral'

// Dasha System
interface VimshottariDasha {
  birthDate: Date
  moonNakshatra: Nakshatra
  moonDegree: number
  mahadashas: MahadashaPeriod[]
}

interface MahadashaPeriod {
  planet: Planet
  startDate: Date
  endDate: Date
  balance: number // years remaining at birth
  antardashas: AntardashaPeriod[]
}

interface AntardashaPeriod {
  planet: Planet
  startDate: Date
  endDate: Date
  pratyantars: PratyanterPeriod[]
}

interface PratyanterPeriod {
  planet: Planet
  startDate: Date
  endDate: Date
}

// Nakshatra System
interface Nakshatra {
  name: string
  number: number // 1-27
  lord: Planet
  deity: string
  symbol: string
  startDegree: number
  endDegree: number
}

// Yoga (Combinations)
interface Yoga {
  name: string
  type: 'raja' | 'dhana' | 'marriage' | 'spiritual' | 'negative'
  planets: Planet[]
  houses: number[]
  strength: number // 0-100
  effects: string[]
}
```

---

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Dasha Calculation Properties

**Property 1: Dasha period continuity**
*For any* birth chart, the end date of one Dasha period should equal the start date of the next period with no gaps or overlaps
**Validates: Requirements 1.1, 1.7**

**Property 2: Dasha duration accuracy**
*For any* Mahadasha, the sum of all Antardasha durations within it should equal the Mahadasha duration
**Validates: Requirements 1.4, 1.7**

**Property 3: Dasha hierarchy consistency**
*For any* Antardasha, all Pratyantar Dashas within it should fall within the Antardasha's date range
**Validates: Requirements 1.8**

**Property 4: Current period identification**
*For any* given date and birth chart, exactly one Mahadasha, one Antardasha, and one Pratyantar Dasha should be active
**Validates: Requirements 1.1, 1.6**

**Property 5: Balance calculation accuracy**
*For any* birth chart, the balance of the first Mahadasha should be correctly calculated based on Moon's nakshatra position
**Validates: Requirements 1.6**

### Shadow Planet Properties

**Property 6: Rahu-Ketu opposition**
*For any* chart, Rahu and Ketu should always be exactly 180 degrees apart
**Validates: Requirements 2.1**

**Property 7: Shadow planet data completeness**
*For any* shadow planet position, all required fields (house, sign, nakshatra, degree) should be present and valid
**Validates: Requirements 2.2, 2.3**

**Property 8: Aspect calculation correctness**
*For any* shadow planet, aspects to other planets should be calculated based on standard Vedic aspect rules
**Validates: Requirements 2.4**

**Property 9: Yoga detection accuracy**
*For any* chart with Rahu or Ketu in specific positions, relevant yogas should be correctly identified
**Validates: Requirements 2.8**

### Transit Calculation Properties

**Property 10: Transit position accuracy**
*For any* given date, planetary positions should match ephemeris data within acceptable tolerance (< 1 arc minute)
**Validates: Requirements 3.1**

**Property 11: House transit mapping**
*For any* transit planet and natal chart, the transited house should be correctly calculated based on natal ascendant
**Validates: Requirements 3.2**

**Property 12: Sade Sati detection**
*For any* natal Moon sign and Saturn position, Sade Sati phase should be correctly identified when Saturn is within 3 signs of Moon
**Validates: Requirements 3.4**

**Property 13: Transit aspect calculation**
*For any* transit planet and natal planet, aspects should be calculated with correct orbs and aspect types
**Validates: Requirements 3.6**

**Property 14: Date range transit calculation**
*For any* date range, all planetary transits should be calculated for each day in the range
**Validates: Requirements 3.7**

### Visualization Properties

**Property 15: Timeline date ordering**
*For any* Dasha timeline, all periods should be displayed in chronological order from left to right
**Validates: Requirements 4.1**

**Property 16: Current date centering**
*For any* timeline view, the current date should be visible in the viewport on initial load
**Validates: Requirements 4.2**

**Property 17: Color uniqueness**
*For any* set of planetary periods, each planet should have a distinct, consistent color across all visualizations
**Validates: Requirements 4.6**

**Property 18: Hierarchical expansion**
*For any* Dasha period, clicking should toggle expansion state and show/hide sub-periods
**Validates: Requirements 4.4, 4.5**

**Property 19: Dual-circle chart structure**
*For any* transit chart, natal positions should be in inner circle and transit positions in outer circle
**Validates: Requirements 5.4**

**Property 20: Aspect line rendering**
*For any* pair of aspecting planets, a line should be drawn between them with correct styling based on aspect type
**Validates: Requirements 5.3, 5.6**

### Prediction Generation Properties

**Property 21: Prediction categorization**
*For any* Dasha period, predictions should be generated for all specified life areas (marriage, career, health, finance, spiritual)
**Validates: Requirements 6.3**

**Property 22: Strength-based favorability**
*For any* Dasha period, favorability rating should be based on planetary dignity, house placement, and aspects
**Validates: Requirements 6.5**

**Property 23: Combined Dasha effects**
*For any* Antardasha, predictions should consider both Mahadasha lord and Antardasha lord effects
**Validates: Requirements 6.2**

### Remedy Generation Properties

**Property 24: Affliction-based remedies**
*For any* afflicted shadow planet, remedies should be generated appropriate to the affliction level
**Validates: Requirements 7.1, 7.2**

**Property 25: Remedy timing specification**
*For any* remedy, timing information (days, hours) should be specified based on planetary rulership
**Validates: Requirements 7.3**

**Property 26: Remedy alternatives**
*For any* planetary affliction, multiple remedy options should be provided across different difficulty and cost levels
**Validates: Requirements 7.6**

### Alert Generation Properties

**Property 27: Major transit detection**
*For any* significant transit (Saturn sign change, Jupiter 7th house entry), an alert should be generated
**Validates: Requirements 8.1, 8.2, 8.3**

**Property 28: Retrograde notification**
*For any* planet entering retrograde motion, a notification should be generated with appropriate guidance
**Validates: Requirements 8.4**

**Property 29: Alert categorization**
*For any* generated alert, it should be assigned a priority level (critical, important, informational) based on transit significance
**Validates: Requirements 8.5**

### Export Properties

**Property 30: Export completeness**
*For any* export request, the generated document should include all selected sections with complete data
**Validates: Requirements 10.1, 10.2, 10.4**

**Property 31: Date range filtering**
*For any* export with date range, only periods/transits within that range should be included
**Validates: Requirements 10.4**

---

## Error Handling

### Calculation Errors
- Invalid birth data → Show user-friendly error message
- Ephemeris data unavailable → Fall back to approximate calculations
- Date out of range → Limit to supported date range (1900-2100)

### UI Errors
- Chart rendering failure → Show placeholder with error message
- Timeline overflow → Implement virtual scrolling
- Aspect line collision → Implement smart line routing

### Data Errors
- Missing planetary position → Use default/interpolated value
- Invalid timezone → Convert to UTC
- Corrupted chart data → Validate and sanitize input

---

## Testing Strategy

### Unit Testing
- Test Dasha calculation algorithms with known birth charts
- Test ephemeris calculations against Swiss Ephemeris reference data
- Test aspect calculations with various planetary positions
- Test yoga detection with specific chart configurations
- Test remedy generation logic
- Test prediction generation algorithms

### Property-Based Testing
Using **fast-check** (JavaScript property testing library):

- Generate random birth dates and verify Dasha continuity
- Generate random planetary positions and verify aspect calculations
- Generate random transit dates and verify house mappings
- Generate random chart data and verify all properties hold

**Configuration:** Each property test should run minimum 100 iterations

### Integration Testing
- Test complete Dasha timeline rendering with real chart data
- Test transit chart with live ephemeris data
- Test shadow planet analysis with various chart configurations
- Test export functionality with different options

### Visual Regression Testing
- Snapshot testing for chart visualizations
- Compare rendered output against reference images
- Test responsive layouts at different breakpoints

---

## Performance Considerations

### Calculation Optimization
- Cache Dasha calculations (rarely change)
- Memoize ephemeris lookups
- Use Web Workers for heavy calculations
- Implement progressive loading for large date ranges

### Rendering Optimization
- Virtual scrolling for long timelines
- Canvas rendering for complex charts (fallback to SVG)
- Lazy load sub-periods
- Debounce zoom/pan operations

### Data Loading
- Server-side calculation where possible
- Client-side caching of ephemeris data
- Incremental loading of predictions
- Optimize bundle size (code splitting)

---

## Security Considerations

- Validate all user inputs (dates, times, coordinates)
- Sanitize chart data before storage
- Rate limit calculation requests
- Secure API endpoints for ephemeris data
- No sensitive data in client-side code

---

## Accessibility

- Keyboard navigation for all interactive elements
- ARIA labels for chart elements
- Screen reader support for predictions
- High contrast mode support
- Focus indicators on all interactive elements
- Alternative text descriptions for visualizations

---

## Future Enhancements

- Ashtakavarga scoring system
- Multiple Dasha system support (Yogini, Chara)
- Varshaphal (annual predictions)
- Muhurta (electional astrology)
- Compatibility analysis
- Progressive Web App features
- Offline mode with cached calculations

---

*This design document provides the technical foundation for implementing advanced astrology features. Refer to requirements.md for detailed acceptance criteria and tasks.md for implementation steps.*
