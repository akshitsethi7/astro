# Implementation Plan - Advanced Astrology Features

This implementation plan breaks down the advanced astrology features into discrete, manageable coding tasks. Each task builds incrementally on previous work, with testing integrated throughout.

---

## Phase 1: Foundation & Core Calculation Engine

### 1. Set up project dependencies and types

- [ ] 1.1 Install required dependencies
  - Add `astronomy-engine` or `swisseph` for ephemeris calculations
  - Add `date-fns` for date manipulation
  - Add `fast-check` for property-based testing
  - _Requirements: All_

- [ ] 1.2 Create core TypeScript types and interfaces
  - Define `ChartData`, `PlanetData`, `DashaPeriod` interfaces
  - Define `Planet`, `ZodiacSign`, `Nakshatra` types
  - Define `TransitPosition`, `Aspect`, `Yoga` interfaces
  - Create `lib/types/astrology.ts` file
  - _Requirements: 1.1, 2.1, 3.1_

- [ ]* 1.3 Write property test for type validation
  - **Property 7: Shadow planet data completeness**
  - **Validates: Requirements 2.2, 2.3**

### 2. Implement Vimshottari Dasha calculation engine

- [ ] 2.1 Create Nakshatra data and utilities
  - Define 27 Nakshatras with lords, degrees, and properties
  - Implement function to find Nakshatra from Moon degree
  - Create `lib/calculations/nakshatra.ts`
  - _Requirements: 1.1, 1.4_

- [ ] 2.2 Implement Vimshottari Dasha calculator
  - Calculate Mahadasha periods from birth date and Moon position
  - Calculate balance of first Mahadasha based on Moon's nakshatra position
  - Generate all Mahadasha periods for 120-year cycle
  - Create `lib/calculations/vimshottari.ts`
  - _Requirements: 1.1, 1.4, 1.6_

- [ ]* 2.3 Write property test for Dasha continuity
  - **Property 1: Dasha period continuity**
  - **Validates: Requirements 1.1, 1.7**

- [ ]* 2.4 Write property test for Dasha duration
  - **Property 2: Dasha duration accuracy**
  - **Validates: Requirements 1.4, 1.7**

- [ ] 2.5 Implement Antardasha calculator
  - Calculate all Antardashas within each Mahadasha
  - Ensure proper date ranges and proportions
  - Add to `lib/calculations/vimshottari.ts`
  - _Requirements: 1.7, 1.8_

- [ ]* 2.6 Write property test for Dasha hierarchy
  - **Property 3: Dasha hierarchy consistency**
  - **Validates: Requirements 1.8**

- [ ] 2.7 Implement Pratyantar Dasha calculator
  - Calculate all Pratyantar Dashas within each Antardasha
  - Complete the three-level hierarchy
  - _Requirements: 1.8_

- [ ] 2.8 Implement current period finder
  - Function to find active Mahadasha/Antardasha/Pratyantar for any date
  - Calculate remaining balance for current periods
  - _Requirements: 1.1, 1.6_

- [ ]* 2.9 Write property test for current period identification
  - **Property 4: Current period identification**
  - **Validates: Requirements 1.1, 1.6**

- [ ]* 2.10 Write property test for balance calculation
  - **Property 5: Balance calculation accuracy**
  - **Validates: Requirements 1.6**

### 3. Implement ephemeris and planetary calculations

- [ ] 3.1 Set up ephemeris library integration
  - Configure astronomy-engine or swisseph
  - Create wrapper functions for planetary positions
  - Handle timezone conversions
  - Create `lib/calculations/ephemeris.ts`
  - _Requirements: 3.1_

- [ ] 3.2 Implement planetary position calculator
  - Calculate positions for all 9 planets for any date/time
  - Include retrograde detection
  - Calculate planetary speed
  - _Requirements: 3.1, 3.2_

- [ ]* 3.3 Write property test for transit position accuracy
  - **Property 10: Transit position accuracy**
  - **Validates: Requirements 3.1**

- [ ] 3.4 Implement house calculation
  - Calculate which natal house a transit planet occupies
  - Handle different house systems (Placidus, Equal, Whole Sign)
  - _Requirements: 3.2_

- [ ]* 3.5 Write property test for house transit mapping
  - **Property 11: House transit mapping**
  - **Validates: Requirements 3.2**

- [ ] 3.6 Implement aspect calculator
  - Calculate aspects between planets (conjunction, opposition, trine, square, sextile)
  - Calculate orbs and determine applying/separating
  - Support both natal-natal and transit-natal aspects
  - Create `lib/calculations/aspects.ts`
  - _Requirements: 2.4, 3.6, 5.3_

- [ ]* 3.7 Write property test for aspect calculation
  - **Property 8: Aspect calculation correctness**
  - **Validates: Requirements 2.4**

- [ ]* 3.8 Write property test for transit aspects
  - **Property 13: Transit aspect calculation**
  - **Validates: Requirements 3.6**

### 4. Checkpoint - Core calculations complete
- Ensure all tests pass, ask the user if questions arise.

---

## Phase 2: Dasha System Implementation

### 5. Create Dasha data service

- [ ] 5.1 Implement DashaService class
  - Method to calculate complete Dasha system from birth chart
  - Method to get current periods
  - Method to get periods for date range
  - Method to evaluate period strength and favorability
  - Create `lib/services/DashaService.ts`
  - _Requirements: 1.1, 1.4, 1.5_

- [ ] 5.2 Implement Dasha strength evaluator
  - Evaluate planetary dignity (own sign, exalted, debilitated)
  - Consider house placement
  - Factor in aspects from benefics/malefics
  - Calculate strength score (0-100)
  - _Requirements: 1.5, 6.5_

- [ ]* 5.3 Write property test for strength-based favorability
  - **Property 22: Strength-based favorability**
  - **Validates: Requirements 6.5**

### 6. Build Dasha prediction engine

- [ ] 6.1 Create prediction templates
  - Define prediction templates for each planet
  - Categorize by life area (marriage, career, health, finance, spiritual)
  - Create `lib/data/dasha-predictions.ts`
  - _Requirements: 6.1, 6.3_

- [ ] 6.2 Implement prediction generator
  - Generate predictions based on Mahadasha lord
  - Combine effects for Mahadasha + Antardasha
  - Adjust predictions based on planetary strength
  - Create `lib/services/PredictionService.ts`
  - _Requirements: 6.1, 6.2, 6.3_

- [ ]* 6.3 Write property test for prediction categorization
  - **Property 21: Prediction categorization**
  - **Validates: Requirements 6.3**

- [ ]* 6.4 Write property test for combined Dasha effects
  - **Property 23: Combined Dasha effects**
  - **Validates: Requirements 6.2**

- [ ] 6.5 Implement confidence level calculator
  - Calculate confidence based on chart strength
  - Factor in multiple indicators
  - _Requirements: 6.8_

### 7. Build Dasha Timeline component

- [ ] 7.1 Create DashaTimeline component structure
  - Set up component with D3.js
  - Define props interface
  - Create basic SVG structure
  - Create `components/dasha/DashaTimeline.tsx`
  - _Requirements: 1.2, 4.1_

- [ ] 7.2 Implement timeline rendering
  - Render horizontal timeline with date scale
  - Display Mahadasha periods as colored bars
  - Add current date indicator
  - _Requirements: 4.1, 4.2_

- [ ]* 7.3 Write property test for timeline date ordering
  - **Property 15: Timeline date ordering**
  - **Validates: Requirements 4.1**

- [ ]* 7.4 Write property test for current date centering
  - **Property 16: Current date centering**
  - **Validates: Requirements 4.2**

- [ ] 7.5 Implement color coding
  - Assign unique color to each planet
  - Apply colors consistently across timeline
  - _Requirements: 4.6_

- [ ]* 7.6 Write property test for color uniqueness
  - **Property 17: Color uniqueness**
  - **Validates: Requirements 4.6**

- [ ] 7.7 Add hover interactions
  - Show tooltip on hover with period details
  - Highlight hovered period
  - _Requirements: 4.3_

- [ ] 7.8 Implement click-to-expand functionality
  - Click Mahadasha bar to show Antardashas
  - Click Antardasha to show Pratyantars
  - Smooth expand/collapse animations
  - _Requirements: 4.4, 4.5_

- [ ]* 7.9 Write property test for hierarchical expansion
  - **Property 18: Hierarchical expansion**
  - **Validates: Requirements 4.4, 4.5**

- [ ] 7.10 Add zoom and pan controls
  - Implement zoom in/out functionality
  - Add pan/scroll for navigation
  - _Requirements: 4.7_

- [ ] 7.11 Implement favorable period indicators
  - Mark favorable periods with visual indicators
  - Use green/gold colors for positive periods
  - _Requirements: 4.8, 1.5_

### 8. Build Dasha period detail components

- [ ] 8.1 Create DashaPeriodCard component
  - Display period information (planet, dates, duration)
  - Show strength and favorability indicators
  - Add expand/collapse functionality
  - Create `components/dasha/DashaPeriodCard.tsx`
  - _Requirements: 1.3, 1.4_

- [ ] 8.2 Create DashaPredictions component
  - Display predictions by category
  - Show confidence levels
  - Include remedies for challenging periods
  - Create `components/dasha/DashaPredictions.tsx`
  - _Requirements: 1.3, 6.1, 6.3, 6.7_

- [ ] 8.3 Create DashaBalance component
  - Show remaining time in current period
  - Display as progress bar or countdown
  - Create `components/dasha/DashaBalance.tsx`
  - _Requirements: 1.6_

### 9. Build Dasha page and integration

- [ ] 9.1 Create Dasha page
  - Set up page structure with sections
  - Integrate DashaTimeline component
  - Add period selection state management
  - Create `app/dasha/page.tsx`
  - _Requirements: 1.1, 1.2_

- [ ] 9.2 Implement period selection flow
  - Click timeline → show period details
  - Display predictions for selected period
  - Show sub-periods in sidebar
  - _Requirements: 1.3, 1.7, 1.8_

- [ ] 9.3 Add navigation to Dashboard
  - Update Dashboard component with Dasha tab
  - Ensure proper routing
  - _Requirements: 1.1_

### 10. Checkpoint - Dasha system complete
- Ensure all tests pass, ask the user if questions arise.

---

## Phase 3: Shadow Planet (Rahu/Ketu) Implementation

### 11. Implement Shadow planet analysis engine

- [ ] 11.1 Create ShadowService class
  - Extract Rahu and Ketu positions from chart
  - Calculate positions in D1 and D9 charts
  - Verify 180-degree opposition
  - Create `lib/services/ShadowService.ts`
  - _Requirements: 2.1_

- [ ]* 11.2 Write property test for Rahu-Ketu opposition
  - **Property 6: Rahu-Ketu opposition**
  - **Validates: Requirements 2.1**

- [ ] 11.3 Implement shadow planet interpretation generator
  - Generate interpretations based on house placement
  - Generate interpretations based on sign placement
  - Generate interpretations based on nakshatra
  - _Requirements: 2.2, 2.3, 2.5, 2.6_

- [ ] 11.4 Implement yoga detector for shadow planets
  - Detect Kala Sarpa Yoga
  - Detect Rahu-Venus combinations
  - Detect other shadow planet yogas
  - Create `lib/calculations/yogas.ts`
  - _Requirements: 2.8_

- [ ]* 11.5 Write property test for yoga detection
  - **Property 9: Yoga detection accuracy**
  - **Validates: Requirements 2.8**

- [ ] 11.6 Implement life area impact analyzer
  - Analyze impact on marriage
  - Analyze impact on career
  - Analyze impact on spiritual growth
  - _Requirements: 2.7_

### 12. Build Shadow planet visualization components

- [ ] 12.1 Create ShadowAnalysis component
  - Display Rahu and Ketu positions
  - Show house, sign, nakshatra, degree
  - Display interpretations
  - Create `components/shadow/ShadowAnalysis.tsx`
  - _Requirements: 2.1, 2.2, 2.3_

- [ ] 12.2 Create ShadowChart component
  - Visualize Rahu and Ketu on birth chart
  - Highlight aspected planets
  - Show aspect lines
  - Create `components/shadow/ShadowChart.tsx`
  - _Requirements: 2.4_

- [ ] 12.3 Create ShadowYogas component
  - Display detected yogas
  - Show yoga effects and significance
  - Create `components/shadow/ShadowYogas.tsx`
  - _Requirements: 2.8_

- [ ] 12.4 Create ShadowLifeAreas component
  - Display impact on different life areas
  - Categorize by marriage, career, spiritual
  - Create `components/shadow/ShadowLifeAreas.tsx`
  - _Requirements: 2.7_

### 13. Implement Shadow planet remedies

- [ ] 13.1 Create remedy database
  - Define remedies for Rahu afflictions
  - Define remedies for Ketu afflictions
  - Include mantras, gemstones, donations, rituals
  - Create `lib/data/shadow-remedies.ts`
  - _Requirements: 7.1, 7.2_

- [ ] 13.2 Implement remedy generator
  - Generate remedies based on affliction level
  - Provide alternatives for different budgets
  - Include timing information
  - Create `lib/services/RemedyService.ts`
  - _Requirements: 7.1, 7.2, 7.3, 7.6_

- [ ]* 13.3 Write property test for affliction-based remedies
  - **Property 24: Affliction-based remedies**
  - **Validates: Requirements 7.1, 7.2**

- [ ]* 13.4 Write property test for remedy timing
  - **Property 25: Remedy timing specification**
  - **Validates: Requirements 7.3**

- [ ]* 13.5 Write property test for remedy alternatives
  - **Property 26: Remedy alternatives**
  - **Validates: Requirements 7.6**

- [ ] 13.6 Create ShadowRemedies component
  - Display recommended remedies
  - Categorize by type and difficulty
  - Show timing and instructions
  - Create `components/shadow/ShadowRemedies.tsx`
  - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8_

### 14. Build Shadow planets page

- [ ] 14.1 Create Shadow planets page
  - Set up page layout
  - Integrate all shadow components
  - Create `app/shadows/page.tsx`
  - _Requirements: 2.1_

- [ ] 14.2 Add navigation to Dashboard
  - Update Dashboard with Shadows tab
  - Ensure proper routing
  - _Requirements: 2.1_

### 15. Checkpoint - Shadow planets complete
- Ensure all tests pass, ask the user if questions arise.

---

## Phase 4: Transit System Implementation

### 16. Implement transit calculation engine

- [ ] 16.1 Create TransitService class
  - Calculate current planetary positions
  - Map transits to natal houses
  - Calculate transit-natal aspects
  - Create `lib/services/TransitService.ts`
  - _Requirements: 3.1, 3.2, 3.6_

- [ ] 16.2 Implement Sade Sati detector
  - Detect if Saturn is within 3 signs of natal Moon
  - Identify Sade Sati phase (rising, peak, setting)
  - Calculate phase start and end dates
  - _Requirements: 3.4_

- [ ]* 16.3 Write property test for Sade Sati detection
  - **Property 12: Sade Sati detection**
  - **Validates: Requirements 3.4**

- [ ] 16.4 Implement transit significance evaluator
  - Identify major transits (Saturn sign change, Jupiter 7th house)
  - Calculate significance scores
  - _Requirements: 3.3, 3.5_

- [ ] 16.5 Implement date range transit calculator
  - Calculate transits for any date range
  - Identify important transit events
  - _Requirements: 3.7_

- [ ]* 16.6 Write property test for date range calculation
  - **Property 14: Date range transit calculation**
  - **Validates: Requirements 3.7**

### 17. Build transit prediction engine

- [ ] 17.1 Create transit prediction templates
  - Define predictions for each planet transiting each house
  - Categorize by life area
  - Create `lib/data/transit-predictions.ts`
  - _Requirements: 3.8_

- [ ] 17.2 Implement transit prediction generator
  - Generate predictions based on transit positions
  - Consider natal chart context
  - Adjust for planetary strength
  - _Requirements: 3.8_

### 18. Build Transit Chart component

- [ ] 18.1 Create TransitChart component structure
  - Set up dual-circle chart with D3.js
  - Inner circle for natal, outer for transits
  - Create `components/transit/TransitChart.tsx`
  - _Requirements: 5.1, 5.4_

- [ ]* 18.2 Write property test for dual-circle structure
  - **Property 19: Dual-circle chart structure**
  - **Validates: Requirements 5.4**

- [ ] 18.3 Implement natal and transit rendering
  - Render natal planets in inner circle
  - Render transit planets in outer circle
  - Use different colors/styles for distinction
  - _Requirements: 5.2, 5.4_

- [ ] 18.4 Implement aspect line rendering
  - Draw lines between aspecting planets
  - Color-code by aspect type
  - Show degree information
  - _Requirements: 5.3, 5.6_

- [ ]* 18.5 Write property test for aspect line rendering
  - **Property 20: Aspect line rendering**
  - **Validates: Requirements 5.3, 5.6**

- [ ] 18.6 Add hover interactions
  - Highlight affected planets on hover
  - Show tooltip with transit details
  - _Requirements: 5.5_

- [ ] 18.7 Implement date selector
  - Allow selection of past/future dates
  - Update chart when date changes
  - _Requirements: 5.7_

- [ ] 18.8 Add significant transit highlighting
  - Visually emphasize important transits
  - Use special styling for major events
  - _Requirements: 5.8_

### 19. Build transit information components

- [ ] 19.1 Create TransitTable component
  - Display all current transit positions
  - Show house being transited
  - Include speed and retrograde status
  - Create `components/transit/TransitTable.tsx`
  - _Requirements: 3.1, 3.2_

- [ ] 19.2 Create SadeSatiIndicator component
  - Display Sade Sati status
  - Show current phase if active
  - Display phase timeline
  - Create `components/transit/SadeSatiIndicator.tsx`
  - _Requirements: 3.4_

- [ ] 19.3 Create TransitPredictions component
  - Display predictions for current transits
  - Categorize by life area
  - Show timing and duration
  - Create `components/transit/TransitPredictions.tsx`
  - _Requirements: 3.8_

- [ ] 19.4 Create TransitHighlights component
  - Show most significant current transits
  - Highlight Jupiter and Saturn transits
  - Display upcoming important transits
  - Create `components/transit/TransitHighlights.tsx`
  - _Requirements: 3.3, 3.5_

### 20. Implement transit alerts system

- [ ] 20.1 Create AlertService class
  - Detect major transit events
  - Generate alerts with priority levels
  - Create `lib/services/AlertService.ts`
  - _Requirements: 8.1, 8.2, 8.3, 8.4_

- [ ]* 20.2 Write property test for major transit detection
  - **Property 27: Major transit detection**
  - **Validates: Requirements 8.1, 8.2, 8.3**

- [ ]* 20.3 Write property test for retrograde notification
  - **Property 28: Retrograde notification**
  - **Validates: Requirements 8.4**

- [ ]* 20.4 Write property test for alert categorization
  - **Property 29: Alert categorization**
  - **Validates: Requirements 8.5**

- [ ] 20.5 Create TransitAlerts component
  - Display active alerts
  - Categorize by priority
  - Show upcoming alerts
  - Create `components/transit/TransitAlerts.tsx`
  - _Requirements: 8.1, 8.5, 8.6_

- [ ] 20.6 Implement alert preferences
  - Allow users to customize alert types
  - Set notification preferences
  - _Requirements: 8.8_

### 21. Build Transits page

- [ ] 21.1 Create Transits page
  - Set up page layout with sections
  - Integrate TransitChart component
  - Add TransitTable and predictions
  - Create `app/transits/page.tsx`
  - _Requirements: 3.1_

- [ ] 21.2 Add date range selector
  - Allow viewing past/future transits
  - Update all components when date changes
  - _Requirements: 3.7, 5.7_

- [ ] 21.3 Add navigation to Dashboard
  - Update Dashboard with Transits tab
  - Ensure proper routing
  - _Requirements: 3.1_

### 22. Checkpoint - Transit system complete
- Ensure all tests pass, ask the user if questions arise.

---

## Phase 5: Advanced Features & Polish

### 23. Implement comparative Dasha systems

- [ ] 23.1 Implement Yogini Dasha calculator
  - Calculate Yogini Dasha periods
  - Create `lib/calculations/yogini.ts`
  - _Requirements: 9.2_

- [ ] 23.2 Create comparative view component
  - Display multiple Dasha systems side-by-side
  - Highlight convergences
  - Create `components/dasha/ComparativeDasha.tsx`
  - _Requirements: 9.3, 9.4_

- [ ] 23.3 Add system selector
  - Allow switching between Dasha systems
  - Remember user preference
  - _Requirements: 9.8_

### 24. Implement export functionality

- [ ] 24.1 Create ExportService class
  - Generate PDF reports
  - Include charts and predictions
  - Create `lib/services/ExportService.ts`
  - _Requirements: 10.1, 10.2_

- [ ]* 24.2 Write property test for export completeness
  - **Property 30: Export completeness**
  - **Validates: Requirements 10.1, 10.2, 10.4**

- [ ]* 24.3 Write property test for date range filtering
  - **Property 31: Date range filtering**
  - **Validates: Requirements 10.4**

- [ ] 24.4 Implement PDF generation
  - Use library like jsPDF or react-pdf
  - Format professionally with branding
  - _Requirements: 10.5_

- [ ] 24.5 Create export options UI
  - Allow section selection
  - Date range selection
  - Format options
  - _Requirements: 10.4, 10.7_

- [ ] 24.6 Implement shareable links
  - Generate secure shareable URLs
  - Add privacy controls
  - _Requirements: 10.6_

### 25. Performance optimization

- [ ] 25.1 Implement calculation caching
  - Cache Dasha calculations
  - Cache ephemeris lookups
  - Use React.memo for expensive components
  - _Requirements: All_

- [ ] 25.2 Add Web Workers for calculations
  - Move heavy calculations to Web Workers
  - Implement progress indicators
  - _Requirements: All_

- [ ] 25.3 Implement virtual scrolling
  - Add virtual scrolling for long timelines
  - Optimize rendering performance
  - _Requirements: 4.1_

- [ ] 25.4 Optimize bundle size
  - Code splitting for each feature
  - Lazy load components
  - Tree-shake unused code
  - _Requirements: All_

### 26. Accessibility improvements

- [ ] 26.1 Add keyboard navigation
  - Implement keyboard shortcuts
  - Ensure all interactive elements are keyboard accessible
  - _Requirements: All_

- [ ] 26.2 Add ARIA labels
  - Label all chart elements
  - Provide screen reader descriptions
  - _Requirements: All_

- [ ] 26.3 Implement high contrast mode
  - Support high contrast themes
  - Ensure color contrast ratios meet WCAG AA
  - _Requirements: All_

### 27. Documentation and examples

- [ ] 27.1 Create component documentation
  - Document all new components
  - Add usage examples
  - Update COMPONENTS.md
  - _Requirements: All_

- [ ] 27.2 Create user guide
  - Write guide for Dasha features
  - Write guide for Shadow planet analysis
  - Write guide for Transit tracking
  - _Requirements: All_

- [ ] 27.3 Update README and changelog
  - Document new features
  - Update installation instructions
  - Add to CHANGELOG.md
  - _Requirements: All_

### 28. Final checkpoint - All features complete
- Ensure all tests pass, ask the user if questions arise.

---

## Summary

**Total Tasks:** 28 major tasks with 100+ sub-tasks
**Estimated Timeline:** 8-12 weeks for full implementation
**Testing:** 31 property-based tests integrated throughout

**Phase Breakdown:**
- Phase 1: Foundation (Tasks 1-4) - 2 weeks
- Phase 2: Dasha System (Tasks 5-10) - 3 weeks
- Phase 3: Shadow Planets (Tasks 11-15) - 2 weeks
- Phase 4: Transits (Tasks 16-22) - 3 weeks
- Phase 5: Polish & Advanced (Tasks 23-28) - 2 weeks

**Key Milestones:**
1. Core calculations working (Task 4)
2. Dasha system complete (Task 10)
3. Shadow planets complete (Task 15)
4. Transits complete (Task 22)
5. All features polished (Task 28)

---

*This implementation plan follows an incremental approach with testing integrated throughout. Each checkpoint ensures stability before moving to the next phase.*
