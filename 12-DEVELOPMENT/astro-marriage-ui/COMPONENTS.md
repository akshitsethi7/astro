# Component Reference

Complete guide to all components in the Astro Marriage UI.

## Layout Components

### Header
**File:** `components/Header.tsx`

Top navigation bar with branding.

**Features:**
- Gradient icon with Sparkles
- App title
- "Vedic Astrology" badge
- Sticky positioning

**Props:** None

**Usage:**
```tsx
import { Header } from '@/components/Header'

<Header />
```

---

### Sidebar
**File:** `components/Sidebar.tsx`

File navigation sidebar with collapsible mobile view.

**Props:**
```typescript
interface SidebarProps {
  files: MarriageFile[]
}
```

**Features:**
- File list navigation
- Active state tracking
- Smooth scroll-to-section
- Mobile drawer with overlay
- File count display

**Usage:**
```tsx
import { Sidebar } from '@/components/Sidebar'

<Sidebar files={files} />
```

---

### Dashboard
**File:** `components/Dashboard.tsx`

Tab-based navigation wrapper.

**Props:**
```typescript
interface DashboardProps {
  children: React.ReactNode
}
```

**Features:**
- 6 navigation tabs
- Icon-based tabs
- Active state
- Responsive scrolling

**Tabs:**
- Overview
- Birth Chart
- Marriage
- Timing
- Spouse
- Analysis

**Usage:**
```tsx
import { Dashboard } from '@/components/Dashboard'

<Dashboard>
  <YourContent />
</Dashboard>
```

---

## Visualization Components

### BirthChart
**File:** `components/BirthChart.tsx`

Interactive circular birth chart (D1 - Rashi).

**Features:**
- 12 houses in circular layout
- Planetary positions with colors
- Hover tooltips
- Sign names and house numbers
- Responsive sizing

**Data:**
- Hardcoded planetary positions
- Can be modified in component

**Usage:**
```tsx
import { BirthChart } from '@/components/BirthChart'

<BirthChart />
```

**Customization:**
```typescript
// Edit planets array in component
const planets: Planet[] = [
  { name: 'Sun', sign: 'Sagittarius', degree: 10.92, house: 5, color: '#FF6B35' },
  // ... more planets
]
```

---

### PlanetaryTable
**File:** `components/PlanetaryTable.tsx`

Detailed table of planetary positions.

**Features:**
- All planetary data
- Color-coded planet dots
- Nakshatra information
- Dignity status
- Hover row highlighting
- Responsive scrolling

**Usage:**
```tsx
import { PlanetaryTable } from '@/components/PlanetaryTable'

<PlanetaryTable />
```

---

### DashaTimeline
**File:** `components/DashaTimeline.tsx`

Interactive timeline of dasha periods.

**Features:**
- Jupiter Mahadasha periods
- Clickable bars
- Current date indicator
- Info panel on selection
- Color-coded periods
- Responsive

**Usage:**
```tsx
import { DashaTimeline } from '@/components/DashaTimeline'

<DashaTimeline />
```

**Customization:**
```typescript
// Edit dashaData array
const dashaData: DashaPeriod[] = [
  { 
    planet: 'Jupiter-Mercury', 
    start: new Date('2025-02-06'), 
    end: new Date('2027-05-14'), 
    color: '#FFD60A', 
    significance: 'Good period' 
  },
  // ... more periods
]
```

---

### TimelineChart
**File:** `components/TimelineChart.tsx`

Marriage probability timeline chart.

**Features:**
- D3.js bar chart
- Gradient fills
- Animated entrance
- Year labels
- Responsive

**Usage:**
```tsx
import { TimelineChart } from '@/components/TimelineChart'

<TimelineChart />
```

---

## UI Components

### StatsCard
**File:** `components/StatsCard.tsx`

Simple statistics display card.

**Props:**
```typescript
interface StatsCardProps {
  label: string
  value: string
  gradient: string
}
```

**Features:**
- Gradient top border
- Hover lift effect
- Monospace values

**Usage:**
```tsx
import { StatsCard } from '@/components/StatsCard'

<StatsCard 
  label="Marriage Prospects" 
  value="⭐⭐⭐⭐⭐" 
  gradient="var(--gradient-success)" 
/>
```

---

### InfoCard
**File:** `components/InfoCard.tsx`

Advanced metric card with icons and trends.

**Props:**
```typescript
interface InfoCardProps {
  title: string
  value: string | number
  subtitle?: string
  icon?: LucideIcon
  gradient?: string
  trend?: 'up' | 'down' | 'neutral'
  trendValue?: string
}
```

**Features:**
- Icon support
- Trend indicators
- Gradient top border
- Hover animations
- Optional subtitle

**Usage:**
```tsx
import { InfoCard } from '@/components/InfoCard'
import { Heart } from 'lucide-react'

<InfoCard
  title="Spouse Loyalty"
  value="9/10"
  subtitle="Very high commitment"
  icon={Heart}
  gradient="var(--gradient-accent)"
  trend="up"
  trendValue="Excellent"
/>
```

---

## Content Components

### ContentViewer
**File:** `components/ContentViewer.tsx`

Main content area with markdown rendering.

**Props:**
```typescript
interface ContentViewerProps {
  files: MarriageFile[]
}
```

**Features:**
- Markdown to HTML conversion
- Syntax highlighting
- Custom styling
- Section anchors

**Usage:**
```tsx
import { ContentViewer } from '@/components/ContentViewer'

<ContentViewer files={files} />
```

---

### OverviewDashboard
**File:** `components/OverviewDashboard.tsx`

Comprehensive overview dashboard.

**Features:**
- 4 info cards
- Birth chart
- Key highlights
- Planetary table
- Both timelines
- Spouse profile grid

**Sections:**
1. Quick Stats Grid
2. Birth Chart + Highlights
3. Planetary Table
4. Timelines
5. Spouse Profile

**Usage:**
```tsx
import { OverviewDashboard } from '@/components/OverviewDashboard'

<OverviewDashboard />
```

---

## Utility Functions

### getMarriageFiles
**File:** `lib/markdown.ts`

Reads and parses markdown files.

**Returns:**
```typescript
interface MarriageFile {
  slug: string
  title: string
  content: string
  order: number
}
```

**Usage:**
```typescript
import { getMarriageFiles } from '@/lib/markdown'

const files = await getMarriageFiles()
```

---

## Styling

### CSS Modules
All components use SCSS modules for scoped styling.

**Pattern:**
```
ComponentName.tsx
ComponentName.module.scss
```

### Global Styles
**File:** `app/globals.scss`

**Variables:**
```scss
--gradient-primary
--gradient-secondary
--gradient-accent
--gradient-success
--color-bg
--color-surface
--color-text-primary
--spacing-md
--radius-lg
// ... and more
```

---

## Component Hierarchy

```
App
├── Header
└── Main
    ├── Sidebar
    └── Dashboard
        └── ContentViewer
            ├── OverviewDashboard
            │   ├── InfoCard (x4)
            │   ├── BirthChart
            │   ├── Highlights
            │   ├── PlanetaryTable
            │   ├── TimelineChart
            │   ├── DashaTimeline
            │   └── Spouse Profile
            └── Markdown Sections
```

---

## Creating New Components

### Template

```tsx
'use client'

import styles from './YourComponent.module.scss'

interface YourComponentProps {
  // Define props
}

export function YourComponent({ }: YourComponentProps) {
  return (
    <div className={styles.container}>
      {/* Your content */}
    </div>
  )
}
```

### SCSS Template

```scss
.container {
  padding: var(--spacing-lg);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  
  @media (max-width: 768px) {
    padding: var(--spacing-md);
  }
}
```

---

## Best Practices

### Component Design
1. Use TypeScript interfaces for props
2. Add 'use client' for interactive components
3. Use CSS modules for styling
4. Make components responsive
5. Add hover states for interactivity

### Styling
1. Use CSS variables for colors
2. Use spacing scale for consistency
3. Add transitions for smooth UX
4. Test on mobile devices
5. Use semantic class names

### Performance
1. Lazy load heavy components
2. Optimize D3.js renders
3. Use React.memo for expensive components
4. Minimize re-renders
5. Use Next.js Image for images

---

## Troubleshooting

### Component Not Rendering
- Check imports
- Verify props are passed correctly
- Check console for errors
- Ensure 'use client' for interactive components

### Styling Issues
- Clear Next.js cache: `rm -rf .next`
- Check CSS module syntax
- Verify class names match
- Check responsive breakpoints

### D3.js Issues
- Ensure SVG ref is attached
- Check data format
- Verify scales are correct
- Test in browser console

---

**For more help, see [TIPS_AND_TRICKS.md](./TIPS_AND_TRICKS.md)**
