# UI Guide - Visual Walkthrough

## 🎨 What You'll See

### Desktop View (> 768px)

\`\`\`
┌─────────────────────────────────────────────────────────────────┐
│  ✨ Astro Marriage Analysis              [Vedic Astrology]     │ ← Header
├──────────────┬──────────────────────────────────────────────────┤
│              │                                                  │
│  Contents    │         Marriage Analysis                        │
│  10 files    │    Comprehensive Vedic astrology insights...    │
│              │                                                  │
│ ┌──────────┐ │  ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│ │ README   │ │  │Marriage  │ │Most Likely│ │ Spouse   │       │
│ └──────────┘ │  │Prospects │ │  Period   │ │ Loyalty  │       │
│              │  │ ⭐⭐⭐⭐⭐ │ │2028-2030  │ │  9/10    │       │
│ ┌──────────┐ │  └──────────┘ └──────────┘ └──────────┘       │
│ │START-HERE│ │                                                  │
│ └──────────┘ │         Marriage Timeline                       │
│              │  ┌────────────────────────────────────────┐     │
│ ┌──────────┐ │  │  📊 D3.js Bar Chart                   │     │
│ │01-overview│ │  │  [Animated bars showing years]        │     │
│ └──────────┘ │  └────────────────────────────────────────┘     │
│              │                                                  │
│ ┌──────────┐ │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│ │02-chart  │ │                                                  │
│ │   data   │ │  README                              readme     │
│ └──────────┘ │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│              │                                                  │
│ ┌──────────┐ │  # Marriage Analysis Project                    │
│ │03-marriage│ │                                                  │
│ │  analysis│ │  This project contains comprehensive...         │
│ └──────────┘ │                                                  │
│              │  ## Project Structure                            │
│     ...      │  ...                                             │
│              │                                                  │
└──────────────┴──────────────────────────────────────────────────┘
  Sidebar (280px)           Main Content Area
\`\`\`

### Mobile View (< 768px)

\`\`\`
┌─────────────────────────────────┐
│ ✨ Astro Marriage Analysis      │ ← Header
│                    [Vedic]      │
├─────────────────────────────────┤
│                                 │
│    Marriage Analysis            │
│  Comprehensive Vedic astrology  │
│                                 │
│ ┌─────────────────────────────┐ │
│ │ Marriage Prospects          │ │
│ │ ⭐⭐⭐⭐⭐                    │ │
│ └─────────────────────────────┘ │
│                                 │
│ ┌─────────────────────────────┐ │
│ │ Most Likely Period          │ │
│ │ 2028-2030                   │ │
│ └─────────────────────────────┘ │
│                                 │
│    Marriage Timeline            │
│ ┌─────────────────────────────┐ │
│ │ 📊 Chart (responsive)       │ │
│ └─────────────────────────────┘ │
│                                 │
│  README                         │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│  # Marriage Analysis Project    │
│  ...                            │
│                                 │
│                                 │
│                          ┌────┐ │
│                          │ ☰  │ │ ← Floating Menu Button
│                          └────┘ │
└─────────────────────────────────┘

When menu button clicked:
┌─────────────────────────────────┐
│ [Overlay - dark background]     │
│  ┌─────────────────────────┐   │
│  │ Contents         10 files│   │
│  │                          │   │
│  │ 📄 README                │   │
│  │ 📄 START-HERE            │   │
│  │ 📄 01-overview           │   │
│  │ 📄 02-chart-data         │   │
│  │ 📄 03-marriage-analysis  │   │
│  │ ...                      │   │
│  └─────────────────────────┘   │
└─────────────────────────────────┘
\`\`\`

## 🎨 Color Scheme

### Gradients
\`\`\`
Primary:    Purple → Violet   [#667eea → #764ba2]
Secondary:  Pink → Red        [#f093fb → #f5576c]
Accent:     Blue → Cyan       [#4facfe → #00f2fe]
Success:    Green → Teal      [#43e97b → #38f9d7]
\`\`\`

### Base Colors
\`\`\`
Background:         #000000 (Pure Black)
Surface:            #111111 (Dark Gray)
Surface Elevated:   #1a1a1a (Lighter Gray)
Border:             #2a2a2a (Border Gray)
Text Primary:       #ffffff (White)
Text Secondary:     #a0a0a0 (Light Gray)
Text Tertiary:      #666666 (Medium Gray)
Accent:             #667eea (Purple)
\`\`\`

## 📐 Layout Measurements

### Spacing Scale
\`\`\`
xs:  0.25rem (4px)
sm:  0.5rem  (8px)
md:  1rem    (16px)
lg:  1.5rem  (24px)
xl:  2rem    (32px)
2xl: 3rem    (48px)
\`\`\`

### Border Radius
\`\`\`
sm: 0.375rem (6px)
md: 0.5rem   (8px)
lg: 0.75rem  (12px)
xl: 1rem     (16px)
\`\`\`

### Component Sizes
\`\`\`
Header Height:        64px
Sidebar Width:        280px
Max Content Width:    900px
Stats Card Height:    ~120px
Timeline Height:      300px
Mobile Menu Button:   56px (diameter)
\`\`\`

## 🎯 Interactive Elements

### Header
- **Logo**: Gradient background with Sparkles icon
- **Title**: "Astro Marriage Analysis"
- **Badge**: "Vedic Astrology" in monospace font
- **Sticky**: Stays at top when scrolling

### Sidebar (Desktop)
- **File List**: All markdown files
- **Active State**: Highlighted with accent border
- **Hover Effect**: Background change + border
- **Icons**: FileText icon for each file
- **Chevron**: Appears on active item

### Sidebar (Mobile)
- **Hidden by default**
- **Floating Button**: Bottom-right corner
- **Slide Animation**: Smooth 0.3s transition
- **Overlay**: Dark backdrop when open
- **Close**: Tap overlay or select file

### Stats Cards
- **Gradient Top Border**: Different color per card
- **Hover Effect**: Lifts up 2px
- **Shadow**: Appears on hover
- **Content**: Label + large value

### Timeline Chart
- **Animated Entrance**: Bars grow from bottom
- **Staggered**: Each bar animates in sequence
- **Gradient Fill**: Custom color per bar
- **Labels**: Year + description
- **Responsive**: Adjusts to container width

### Content Sections
- **Card Style**: Border + rounded corners
- **Spacing**: Generous padding
- **Typography**: Clear hierarchy
- **Markdown**: Fully styled

## 🎨 Typography Styles

### Headings
\`\`\`
Hero Title:     3.5rem (56px) - Gradient text
Hero Subtitle:  1.25rem (20px) - Secondary color
Section Title:  1.75rem (28px) - Primary color
H1:             2rem (32px)
H2:             1.5rem (24px)
H3:             1.25rem (20px)
H4:             1.125rem (18px)
Body:           1rem (16px)
Small:          0.875rem (14px)
Tiny:           0.75rem (12px)
\`\`\`

### Font Weights
\`\`\`
Regular:  400
Medium:   500
Semibold: 600
Bold:     700
\`\`\`

### Line Heights
\`\`\`
Headings: 1.2
Body:     1.7
Tight:    1.4
\`\`\`

## 🎭 Animations

### Durations
\`\`\`
Fast:     0.2s (hover effects)
Medium:   0.3s (sidebar slide)
Slow:     1s   (chart entrance)
\`\`\`

### Easing
\`\`\`
Standard: ease
Smooth:   ease-in-out
Bounce:   cubic-bezier(0.68, -0.55, 0.265, 1.55)
\`\`\`

### Effects
- **Hover**: Transform translateY(-2px)
- **Active**: Transform scale(0.95)
- **Fade**: Opacity 0 → 1
- **Slide**: TranslateX(-100%) → 0

## 📱 Responsive Breakpoints

### Mobile First Approach
\`\`\`scss
// Base styles: Mobile (< 768px)
.component {
  padding: 1rem;
}

// Tablet and up (≥ 768px)
@media (min-width: 768px) {
  .component {
    padding: 1.5rem;
  }
}

// Desktop (≥ 1024px)
@media (min-width: 1024px) {
  .component {
    padding: 2rem;
  }
}
\`\`\`

## 🎨 Component States

### Sidebar Items
\`\`\`
Default:  Gray text, transparent background
Hover:    White text, elevated background, border
Active:   White text, elevated background, accent border
Focus:    Outline for keyboard navigation
\`\`\`

### Buttons
\`\`\`
Default:  Gradient background
Hover:    Slightly brighter
Active:   Scale down (0.95)
Disabled: Reduced opacity (0.5)
\`\`\`

### Cards
\`\`\`
Default:  Border, no shadow
Hover:    Accent border, shadow, lift up
\`\`\`

## 🔍 Accessibility Features

- **Semantic HTML**: Proper heading hierarchy
- **ARIA Labels**: On interactive elements
- **Keyboard Navigation**: Tab through all elements
- **Focus States**: Visible focus indicators
- **Color Contrast**: WCAG AA compliant
- **Alt Text**: On all images (when added)

## 💡 Visual Hierarchy

### Priority Levels
1. **Hero Title**: Largest, gradient, center
2. **Stats Cards**: Prominent, colorful
3. **Timeline Chart**: Visual focal point
4. **Section Titles**: Clear separators
5. **Body Content**: Readable, secondary
6. **Metadata**: Smallest, tertiary color

## 🎯 User Flow

1. **Land on page** → See hero + stats
2. **Scroll down** → View timeline chart
3. **Read content** → Markdown sections
4. **Navigate** → Click sidebar items
5. **Mobile** → Tap floating button for menu

## 📊 Content Density

- **Desktop**: Comfortable spacing, wide layout
- **Tablet**: Balanced, adaptive grid
- **Mobile**: Compact but readable, single column

---

**The UI is designed to be beautiful, functional, and accessible across all devices!** ✨
