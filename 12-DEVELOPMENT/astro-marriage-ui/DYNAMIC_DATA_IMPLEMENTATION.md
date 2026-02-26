# Dynamic Data Implementation Guide

## Overview
This guide shows how to update all UI pages to consume real chart data from ChartContext instead of mock data.

## Chart Data Structure (from chartsimp)

The birth chart contains:
- **D1 Chart**: Main birth chart with planetary positions
- **D9 Chart**: Navamsa (divisional chart)
- **D60 Chart**: Shashtiamsa (divisional chart)
- **Yogas**: Major yogas, Chandra yogas, Soorya yogas, Inauspicious yogas
- **Dasha Periods**: Complete Vimshottari Dasha timeline with Mahadasha, Antardasha, Pratyantar

### Example Planetary Data (D1):
```
Planet: Sun
- Sign: Sagittarius
- Sign Lord: Jupiter
- Nakshatra: Mula
- Nakshatra Lord: Ketu
- Degree: 10°55'8"
- House: 5
- Retro: Direct
- Combust: No
- Avastha: Kumara
```

## Implementation Steps

### 1. Update Dasha Page (`app/dasha/page.tsx`)

**Current**: Uses mock data
**Update**: Use ChartContext

```typescript
'use client';

import { useChart } from '@/lib/context/ChartContext';
import { Calendar, Clock, TrendingUp } from 'lucide-react';
import styles from './page.module.scss';

export default function DashaPage() {
  const { chartData, isLoading } = useChart();

  if (isLoading) {
    return <div className={styles.loading}>Calculating...</div>;
  }

  if (!chartData) {
    return (
      <div className={styles.noData}>
        <p>Please enter birth details on the home page.</p>
      </div>
    );
  }

  const moonData = chartData.planets.get('Moon');
  
  return (
    <div className={styles.dashaPage}>
      <header className={styles.header}>
        <h1>Vimshottari Dasha</h1>
        <div className={styles.stats}>
          <div>Birth: {chartData.birthDate.toLocaleDateString()}</div>
          <div>Time: {chartData.birthTime}</div>
          <div>Nakshatra: {moonData?.nakshatra}</div>
        </div>
      </header>
      
      {/* Display Dasha periods */}
      <section>
        <h2>Current Period</h2>
        <p>Mahadasha Lord: {moonData?.nakshatraLord}</p>
        <p>Nakshatra Pada: {moonData?.nakshatraPada}</p>
      </section>
    </div>
  );
}
```

### 2. Update Chart Page (`app/chart/page.tsx`)

**Display**:
- Ascendant with sign and degree
- All 9 planets with positions
- Houses with occupants
- Aspects between planets

```typescript
'use client';

import { useChart } from '@/lib/context/ChartContext';
import styles from './page.module.scss';

export default function ChartPage() {
  const { chartData } = useChart();

  if (!chartData) {
    return <div>No chart data</div>;
  }

  return (
    <div className={styles.chartPage}>
      <h1>Birth Chart (D1)</h1>
      
      {/* Ascendant */}
      <div className={styles.ascendant}>
        <h2>Ascendant</h2>
        <p>{chartData.ascendant.sign} {chartData.ascendant.degree.toFixed(2)}°</p>
      </div>

      {/* Planets */}
      <div className={styles.planets}>
        <h2>Planetary Positions</h2>
        <table>
          <thead>
            <tr>
              <th>Planet</th>
              <th>Sign</th>
              <th>Degree</th>
              <th>House</th>
              <th>Nakshatra</th>
              <th>Pada</th>
            </tr>
          </thead>
          <tbody>
            {Array.from(chartData.planets.entries()).map(([planet, data]) => (
              <tr key={planet}>
                <td>{planet}</td>
                <td>{data.sign}</td>
                <td>{data.degree.toFixed(2)}°</td>
                <td>{data.house}</td>
                <td>{data.nakshatra}</td>
                <td>{data.nakshatraPada}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Houses */}
      <div className={styles.houses}>
        <h2>Houses</h2>
        {chartData.houses.map((house) => (
          <div key={house.number} className={styles.house}>
            <h3>House {house.number}</h3>
            <p>Sign: {house.sign}</p>
            <p>Lord: {house.lord}</p>
            <p>Planets: {house.planets.join(', ') || 'Empty'}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
```

### 3. Update Shadows Page (`app/shadows/page.tsx`)

**Display**:
- Rahu position, sign, house, nakshatra
- Ketu position (always 180° opposite)
- Yogas involving Rahu/Ketu
- Remedies

```typescript
'use client';

import { useChart } from '@/lib/context/ChartContext';
import styles from './page.module.scss';

export default function ShadowsPage() {
  const { chartData } = useChart();

  if (!chartData) return <div>No data</div>;

  const rahuData = chartData.planets.get('Rahu');
  const ketuData = chartData.planets.get('Ketu');

  return (
    <div className={styles.shadowsPage}>
      <h1>Shadow Planets</h1>
      
      <div className={styles.grid}>
        {/* Rahu */}
        <div className={styles.card}>
          <h2>Rahu (North Node)</h2>
          <p>Sign: {rahuData?.sign}</p>
          <p>Degree: {rahuData?.degree.toFixed(2)}°</p>
          <p>House: {rahuData?.house}</p>
          <p>Nakshatra: {rahuData?.nakshatra}</p>
          <p>Pada: {rahuData?.nakshatraPada}</p>
        </div>

        {/* Ketu */}
        <div className={styles.card}>
          <h2>Ketu (South Node)</h2>
          <p>Sign: {ketuData?.sign}</p>
          <p>Degree: {ketuData?.degree.toFixed(2)}°</p>
          <p>House: {ketuData?.house}</p>
          <p>Nakshatra: {ketuData?.nakshatra}</p>
          <p>Pada: {ketuData?.nakshatraPada}</p>
        </div>
      </div>

      {/* Opposition */}
      <div className={styles.opposition}>
        <p>Rahu and Ketu are always 180° apart</p>
        <p>Difference: {Math.abs((rahuData?.absoluteDegree || 0) - (ketuData?.absoluteDegree || 0)).toFixed(2)}°</p>
      </div>
    </div>
  );
}
```

### 4. Update Transits Page (`app/transits/page.tsx`)

**Display**:
- Current planetary positions
- Comparison with birth chart
- Sade Sati status (Saturn transit)
- Major transits

```typescript
'use client';

import { useChart } from '@/lib/context/ChartContext';
import { calculatePlanetaryPositions } from '@/lib/calculations/ephemeris';
import styles from './page.module.scss';

export default function TransitsPage() {
  const { chartData } = useChart();
  
  if (!chartData) return <div>No data</div>;

  // Calculate current positions
  const currentPositions = calculatePlanetaryPositions(new Date());
  
  // Get Moon sign from birth chart
  const birthMoon = chartData.planets.get('Moon');
  
  // Find current Saturn position
  const currentSaturn = currentPositions.find(p => p.planet === 'Saturn');
  
  return (
    <div className={styles.transitsPage}>
      <h1>Current Transits</h1>
      
      {/* Current Positions */}
      <section>
        <h2>Current Planetary Positions</h2>
        <table>
          <thead>
            <tr>
              <th>Planet</th>
              <th>Longitude</th>
              <th>Speed</th>
              <th>Retrograde</th>
            </tr>
          </thead>
          <tbody>
            {currentPositions.map((pos) => (
              <tr key={pos.planet}>
                <td>{pos.planet}</td>
                <td>{pos.longitude.toFixed(2)}°</td>
                <td>{pos.speed.toFixed(4)}°/day</td>
                <td>{pos.isRetrograde ? 'Yes' : 'No'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>

      {/* Sade Sati */}
      <section>
        <h2>Sade Sati Status</h2>
        <p>Birth Moon: {birthMoon?.sign}</p>
        <p>Current Saturn: {currentSaturn?.longitude.toFixed(2)}°</p>
      </section>
    </div>
  );
}
```

### 5. Update Home Page (`app/page.tsx`)

**Display**:
- Birth chart form (already done)
- Quick summary when data is available
- Links to detailed pages

```typescript
'use client';

import { useState } from 'react';
import { useChart } from '@/lib/context/ChartContext';
import BirthChartForm from '@/components/BirthChartForm';
import Link from 'next/link';
import styles from './page.module.scss';

export default function HomePage() {
  const { chartData } = useChart();
  const [showForm, setShowForm] = useState(!chartData);

  return (
    <div className={styles.homePage}>
      <header className={styles.hero}>
        <h1>Vedic Astrology Dashboard</h1>
        <p>Advanced birth chart analysis and predictions</p>
      </header>

      {!chartData || showForm ? (
        <BirthChartForm onClose={() => setShowForm(false)} />
      ) : (
        <div className={styles.dashboard}>
          <h2>Your Birth Chart</h2>
          
          {/* Quick Summary */}
          <div className={styles.summary}>
            <div>Ascendant: {chartData.ascendant.sign}</div>
            <div>Moon: {chartData.planets.get('Moon')?.sign}</div>
            <div>Sun: {chartData.planets.get('Sun')?.sign}</div>
          </div>

          {/* Navigation */}
          <div className={styles.nav}>
            <Link href="/chart">View Full Chart</Link>
            <Link href="/dasha">Dasha Periods</Link>
            <Link href="/shadows">Shadow Planets</Link>
            <Link href="/transits">Current Transits</Link>
          </div>

          <button onClick={() => setShowForm(true)}>
            Edit Birth Details
          </button>
        </div>
      )}
    </div>
  );
}
```

## Key Points

1. **Always check for data**: Use `if (!chartData) return ...` pattern
2. **Handle loading states**: Show loading indicator while calculating
3. **Use Map methods**: `chartData.planets.get('Moon')` to access planet data
4. **Format numbers**: Use `.toFixed(2)` for degrees
5. **Display all fields**: Show sign, degree, house, nakshatra, pada, dignity, etc.

## Testing

Test with sample birth data:
- Date: January 1, 1995
- Time: 10:30 AM
- Location: New Delhi (28.6139°N, 77.2090°E)
- Timezone: Asia/Kolkata

Expected results:
- Ascendant should be calculated accurately
- All 9 planets should have positions
- Moon should have nakshatra and pada
- Houses should show occupants

## Next Steps

1. Update each page one by one
2. Test with real birth data
3. Add error handling for edge cases
4. Style the data displays beautifully
5. Add loading animations
6. Implement data persistence (already done in ChartContext)
