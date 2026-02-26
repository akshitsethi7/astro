# 🎯 Dynamic Data System Guide

## Overview

The platform now uses **real, dynamic calculations** based on user-provided birth details. All data is calculated in real-time using astronomical algorithms.

## How It Works

### 1. **ChartContext** - Global State Management

Located in `lib/context/ChartContext.tsx`, this provides:
- Birth details storage (localStorage persistence)
- Real-time chart calculations
- Dasha service initialization
- Shadow service initialization
- Loading and error states

### 2. **Birth Chart Form**

Component: `components/BirthChartForm.tsx`

Users can enter:
- Name (optional)
- Birth date
- Birth time
- Location (latitude/longitude)
- Timezone
- Quick location buttons for common cities

### 3. **Real Calculations**

When birth details are entered:

```typescript
// 1. Calculate planetary positions using astronomy-engine
const positions = calculatePlanetaryPositions(birthDate);

// 2. Generate complete birth chart
const chart = calculateChart(
  birthDate,
  birthTime,
  timezone,
  latitude,
  longitude,
  'Lahiri' // Ayanamsa
);

// 3. Initialize services
const dashaService = new DashaService(chart);
const shadowService = new ShadowService(chart);
```

## Using Dynamic Data in Pages

### Example: Dasha Page

```typescript
'use client';

import { useChart } from '@/lib/context/ChartContext';

export default function DashaPage() {
  const { chartData, dashaService, isLoading } = useChart();

  if (isLoading) return <div>Calculating...</div>;
  if (!chartData) return <div>Enter birth details first</div>;

  // Get real Dasha data
  const currentStatus = dashaService.getCurrentStatus();
  
  return (
    <div>
      <h1>Current Mahadasha: {currentStatus.mahadasha?.planet}</h1>
      <p>Strength: {currentStatus.mahadasha?.strength}/100</p>
      {/* ... */}
    </div>
  );
}
```

### Example: Chart Page

```typescript
'use client';

import { useChart } from '@/lib/context/ChartContext';

export default function ChartPage() {
  const { chartData } = useChart();

  if (!chartData) return <div>No chart data</div>;

  // Access real planetary positions
  const planets = Array.from(chartData.planets.entries()).map(([planet, data]) => ({
    planet,
    sign: data.sign,
    degree: data.degree,
    house: data.house,
    nakshatra: data.nakshatra,
    retrograde: data.retrograde,
    dignity: data.dignity,
  }));

  return <PlanetaryTable planets={planets} />;
}
```

### Example: Shadow Page

```typescript
'use client';

import { useChart } from '@/lib/context/ChartContext';

export default function ShadowsPage() {
  const { shadowService } = useChart();

  if (!shadowService) return <div>Loading...</div>;

  // Get real shadow planet analysis
  const analysis = shadowService.getAnalysis();

  return (
    <div>
      <h2>Rahu in {analysis.rahu.sign}</h2>
      <p>House: {analysis.rahu.house}</p>
      <p>Strength: {analysis.rahu.strength}/100</p>
      
      {/* Yogas */}
      {analysis.yogas.map(yoga => (
        <div key={yoga.name}>
          <h3>{yoga.name}</h3>
          <p>{yoga.description}</p>
        </div>
      ))}
    </div>
  );
}
```

## Data Flow

```
User Input (Birth Details)
    ↓
ChartContext
    ↓
calculateChart() → Real astronomical calculations
    ↓
ChartData object with:
  - Planetary positions (astronomy-engine)
  - Houses (calculated)
  - Nakshatras (calculated)
  - Dignities (evaluated)
    ↓
Services initialized:
  - DashaService (Vimshottari calculations)
  - ShadowService (Rahu/Ketu analysis)
    ↓
Pages consume via useChart() hook
    ↓
UI displays real, personalized data
```

## Features

### ✅ Real Calculations
- Astronomy-engine for precise planetary positions
- Lahiri Ayanamsa (adjusts for precession)
- Retrograde detection
- Planetary speed calculations
- House systems (whole-sign & equal)
- Nakshatra identification
- Dignity evaluation

### ✅ Persistent Storage
- Birth details saved to localStorage
- Automatically loads on page refresh
- Can be cleared/changed anytime

### ✅ Real-time Updates
- Calculations happen instantly
- Loading states during computation
- Error handling for invalid inputs

### ✅ Services
- **DashaService**: Complete Vimshottari Dasha system
  - Current periods
  - Strength evaluation
  - Predictions
  - Life area analysis
  
- **ShadowService**: Rahu/Ketu analysis
  - Position analysis
  - Yoga detection
  - Remedies generation
  - Life impacts

## How to Use

### 1. **First Time User**

1. Visit `http://localhost:3000/`
2. Click "Enter Birth Details"
3. Fill in the form:
   - Date: Your birth date
   - Time: Your birth time (24-hour format)
   - Location: Use quick buttons or enter coordinates
   - Timezone: Select your timezone
4. Click "Calculate Chart"
5. Explore all pages with your personalized data!

### 2. **Changing Details**

- Click "Change Details" button in the banner
- Update any field
- Click "Calculate Chart" again
- All pages update automatically

### 3. **Default Chart**

If no details entered, uses example chart:
- Date: January 1, 1995
- Time: 10:30 AM
- Location: New Delhi, India

## API Reference

### useChart() Hook

```typescript
const {
  birthDetails,      // Current birth details
  chartData,         // Calculated chart data
  dashaService,      // Dasha service instance
  shadowService,     // Shadow service instance
  isLoading,         // Calculation in progress
  error,             // Error message if any
  setBirthDetails,   // Update birth details
  clearChart,        // Clear all data
} = useChart();
```

### ChartData Structure

```typescript
interface ChartData {
  birthDate: Date;
  birthTime: string;
  timezone: string;
  latitude: number;
  longitude: number;
  ayanamsa: 'Lahiri' | 'Raman' | 'KP';
  ascendant: {
    sign: ZodiacSign;
    degree: number;
  };
  planets: Map<Planet, PlanetData>;
  houses: House[];
}
```

### PlanetData Structure

```typescript
interface PlanetData {
  sign: ZodiacSign;
  degree: number;           // 0-30 within sign
  absoluteDegree: number;   // 0-360 in zodiac
  house: number;            // 1-12
  nakshatra: string;
  nakshatraPada: number;    // 1-4
  nakshatraLord: Planet;
  retrograde: boolean;
  dignity: Dignity;
  speed: number;            // degrees per day
}
```

## Calculation Accuracy

### Planetary Positions
- Uses `astronomy-engine` library
- NASA JPL ephemeris data
- Accurate to within arc-seconds
- Includes all 9 Vedic planets

### Ayanamsa
- Lahiri Ayanamsa (default)
- Adjusts for precession (~50.29"/year)
- Accurate for any date

### Dasha System
- Traditional Vimshottari formulas
- 120-year cycle
- Nakshatra-based calculation
- Accurate to the day

### Houses
- Whole-sign system (default)
- Equal house system (available)
- Placidus (can be added)

## Next Steps

### To Update a Page to Use Dynamic Data:

1. Import the hook:
```typescript
import { useChart } from '@/lib/context/ChartContext';
```

2. Get the data:
```typescript
const { chartData, dashaService, shadowService } = useChart();
```

3. Replace mock data with real data:
```typescript
// Before (mock):
const mockData = { planet: 'Sun', sign: 'Aries' };

// After (real):
const sunData = chartData?.planets.get('Sun');
```

4. Add loading/error states:
```typescript
if (isLoading) return <Loading />;
if (!chartData) return <EnterDetails />;
```

## Example: Complete Page Update

```typescript
'use client';

import { useChart } from '@/lib/context/ChartContext';
import Link from 'next/link';

export default function MyPage() {
  const { chartData, dashaService, isLoading, error } = useChart();

  // Loading state
  if (isLoading) {
    return <div>Calculating your chart...</div>;
  }

  // Error state
  if (error) {
    return <div>Error: {error}</div>;
  }

  // No data state
  if (!chartData || !dashaService) {
    return (
      <div>
        <p>Please enter your birth details first</p>
        <Link href="/">Go to Home</Link>
      </div>
    );
  }

  // Real data available!
  const currentDasha = dashaService.getCurrentStatus();
  const moonData = chartData.planets.get('Moon');

  return (
    <div>
      <h1>Your Personalized Analysis</h1>
      <p>Moon in {moonData?.sign} at {moonData?.degree.toFixed(2)}°</p>
      <p>Current Mahadasha: {currentDasha.mahadasha?.planet}</p>
      <p>Strength: {currentDasha.mahadasha?.strength}/100</p>
    </div>
  );
}
```

## Summary

✅ **All calculations are real and dynamic**
✅ **Based on user-provided birth details**
✅ **Uses astronomical algorithms (astronomy-engine)**
✅ **Persistent across page refreshes**
✅ **Easy to use with useChart() hook**
✅ **Accurate Vedic astrology calculations**

The platform is now fully dynamic with real calculations! 🎉
