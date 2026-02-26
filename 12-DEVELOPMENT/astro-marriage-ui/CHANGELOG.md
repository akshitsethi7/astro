# Changelog

## Version 2.0.0 - Lagna360-Inspired Dashboard (2024)

### 🎉 Major Features Added

#### Interactive Visualizations
- **Birth Chart Component** - Circular D1 chart with 12 houses and planetary positions
- **Planetary Table** - Comprehensive table with all planetary data
- **Dasha Timeline** - Interactive timeline showing Jupiter Mahadasha periods
- **Marriage Timeline** - Probability chart across years
- **Overview Dashboard** - Comprehensive dashboard with all key metrics

#### New Components
1. `BirthChart.tsx` - Interactive circular birth chart
2. `PlanetaryTable.tsx` - Detailed planetary positions table
3. `DashaTimeline.tsx` - Interactive dasha period timeline
4. `Dashboard.tsx` - Tab-based navigation system
5. `InfoCard.tsx` - Metric cards with trends and icons
6. `OverviewDashboard.tsx` - Main dashboard view

#### Design Improvements
- Lagna360-inspired professional layout
- Tab-based navigation (Overview, Chart, Marriage, Timing, Spouse, Analysis)
- Interactive hover effects on all charts
- Click-to-select functionality on dasha timeline
- Color-coded planetary positions
- Gradient-based design system
- Smooth animations and transitions

#### User Experience
- Hover tooltips on birth chart planets
- Clickable dasha periods with info panel
- Responsive grid layouts
- Touch-optimized for mobile
- Improved navigation flow

### 🐛 Bug Fixes
- Fixed SCSS `:global` selector syntax for CSS modules
- Corrected component imports
- Fixed responsive breakpoints

### 📚 Documentation
- Updated README with new features
- Added component documentation
- Updated installation instructions

---

## Version 1.0.0 - Initial Release

### Features
- Basic Next.js setup with TypeScript
- Markdown file rendering
- Sidebar navigation
- Stats cards
- Simple timeline chart
- Responsive design
- Dark theme

---

## Upcoming Features

### Planned for v2.1.0
- [ ] Navamsa (D9) chart visualization
- [ ] Divisional charts (D7, D10, D60)
- [ ] Aspect lines on birth chart
- [ ] Export to PDF functionality
- [ ] Print-friendly styles
- [ ] Search functionality
- [ ] Filter by category
- [ ] Light/Dark theme toggle

### Planned for v3.0.0
- [ ] User authentication
- [ ] Save custom notes
- [ ] Multiple chart comparison
- [ ] Transit predictions
- [ ] Remedies tracker
- [ ] Calendar integration
- [ ] Notification system
- [ ] Mobile app (React Native)

---

## Breaking Changes

### v2.0.0
- Restructured component hierarchy
- Changed ContentViewer to use OverviewDashboard
- Updated styling system with new CSS modules
- Modified file structure for better organization

---

## Migration Guide

### From v1.0.0 to v2.0.0

No migration needed for existing markdown files. The new version is backward compatible with v1.0.0 content.

If you customized components:
1. Update imports to include new components
2. Check SCSS module syntax (use `.container :global(.class)` instead of `:global { .class }`)
3. Review new Dashboard wrapper component

---

## Credits

- Design inspiration: Lagna360, Linear.app, Vercel
- Icons: Lucide React
- Charts: D3.js
- Framework: Next.js 15
- Fonts: IBM Plex Sans & Mono

---

**For detailed documentation, see [INDEX.md](./INDEX.md)**
