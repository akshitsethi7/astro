# Requirements Document - Advanced Astrology Features

## Introduction

This specification outlines the addition of advanced Vedic astrology features to the Astro Marriage UI, inspired by Lagna360's professional dashboard. The goal is to provide comprehensive astrological analysis tools including detailed Dasha analysis, Shadow planet (Rahu/Ketu) analysis, and Transit predictions.

## Glossary

- **Dasha System**: Vedic astrology's planetary period system that predicts timing of events
- **Vimshottari Dasha**: 120-year cycle system, most commonly used dasha system
- **Mahadasha**: Major planetary period (6-20 years)
- **Antardasha**: Sub-period within a Mahadasha (months to years)
- **Pratyantar Dasha**: Sub-sub-period within an Antardasha
- **Shadow Planets**: Rahu (North Node) and Ketu (South Node) - lunar nodes
- **Transits**: Current planetary positions and their effects on natal chart
- **Gochara**: Sanskrit term for planetary transits
- **Sade Sati**: 7.5 year Saturn transit period
- **Ashtakavarga**: Point system for transit strength analysis
- **D1 Chart**: Rashi chart (birth chart)
- **D9 Chart**: Navamsa chart (marriage/spiritual chart)
- **Divisional Charts**: Various charts for specific life areas

---

## Requirements

### Requirement 1: Dasha Analysis System

**User Story:** As a user, I want to view detailed Dasha periods with predictions, so that I can understand the timing of events in my life.

#### Acceptance Criteria

1. WHEN a user navigates to the Dasha section THEN the system SHALL display the current Mahadasha, Antardasha, and Pratyantar Dasha with start and end dates
2. WHEN viewing Dasha periods THEN the system SHALL show a visual timeline with color-coded periods for easy identification
3. WHEN a user clicks on a Dasha period THEN the system SHALL display detailed predictions and effects for that period
4. WHEN displaying Dasha information THEN the system SHALL include the ruling planet, duration, and significance for marriage/career/health
5. WHEN showing future Dashas THEN the system SHALL highlight favorable and challenging periods with visual indicators
6. WHEN a user views Dasha details THEN the system SHALL show the balance of current period remaining
7. WHEN displaying Mahadasha THEN the system SHALL show all Antardashas within that period in a hierarchical view
8. WHEN a user selects an Antardasha THEN the system SHALL display all Pratyantar Dashas within it

### Requirement 2: Shadow Planet Analysis (Rahu/Ketu)

**User Story:** As a user, I want to understand Rahu and Ketu's influence in my chart, so that I can work with their karmic lessons and opportunities.

#### Acceptance Criteria

1. WHEN a user views Shadow planet analysis THEN the system SHALL display Rahu and Ketu positions in both D1 and D9 charts
2. WHEN showing Rahu position THEN the system SHALL indicate the house, sign, nakshatra, and degree with interpretation
3. WHEN showing Ketu position THEN the system SHALL indicate the house, sign, nakshatra, and degree with interpretation
4. WHEN displaying shadow planets THEN the system SHALL show their aspects on other planets and houses
5. WHEN analyzing Rahu THEN the system SHALL explain material desires, obsessions, and worldly ambitions indicated
6. WHEN analyzing Ketu THEN the system SHALL explain spiritual inclinations, detachment areas, and past life karma
7. WHEN showing shadow planet effects THEN the system SHALL indicate their impact on marriage, career, and spiritual growth
8. WHEN Rahu or Ketu are in significant positions THEN the system SHALL highlight special yogas (combinations) formed

### Requirement 3: Transit Analysis System

**User Story:** As a user, I want to see current planetary transits and their effects, so that I can make informed decisions about timing.

#### Acceptance Criteria

1. WHEN a user views Transits THEN the system SHALL display current positions of all planets in real-time
2. WHEN showing transits THEN the system SHALL indicate which natal houses each planet is transiting
3. WHEN a planet transits a significant house THEN the system SHALL highlight the transit with predictions
4. WHEN displaying Saturn transit THEN the system SHALL indicate if user is in Sade Sati period with phase information
5. WHEN showing Jupiter transit THEN the system SHALL highlight beneficial periods and houses being activated
6. WHEN analyzing transits THEN the system SHALL show aspects between transiting planets and natal planets
7. WHEN a user selects a date range THEN the system SHALL show future transits and their timing
8. WHEN displaying transit effects THEN the system SHALL provide specific predictions for marriage, career, and health

### Requirement 4: Interactive Dasha Timeline Visualization

**User Story:** As a user, I want an interactive visual timeline of Dasha periods, so that I can easily navigate through different time periods.

#### Acceptance Criteria

1. WHEN viewing the Dasha timeline THEN the system SHALL display a horizontal timeline spanning past, present, and future periods
2. WHEN the timeline loads THEN the system SHALL center on the current date with a clear indicator
3. WHEN a user hovers over a Dasha period THEN the system SHALL show a tooltip with period details
4. WHEN a user clicks a Dasha bar THEN the system SHALL expand to show sub-periods (Antardashas)
5. WHEN viewing expanded Antardashas THEN the system SHALL allow clicking to see Pratyantar Dashas
6. WHEN the timeline displays periods THEN the system SHALL use distinct colors for each planetary period
7. WHEN a user zooms the timeline THEN the system SHALL maintain smooth transitions and readability
8. WHEN displaying favorable periods THEN the system SHALL mark them with positive indicators (green/gold)

### Requirement 5: Transit Chart Visualization

**User Story:** As a user, I want to see a visual representation of current transits overlaid on my birth chart, so that I can understand planetary movements.

#### Acceptance Criteria

1. WHEN viewing transit chart THEN the system SHALL display natal chart with current planetary positions overlaid
2. WHEN showing transits THEN the system SHALL use different colors/styles to distinguish natal vs transit planets
3. WHEN a transit planet aspects a natal planet THEN the system SHALL draw aspect lines with degree information
4. WHEN displaying the chart THEN the system SHALL show both inner circle (natal) and outer circle (transit) positions
5. WHEN a user hovers over a transit planet THEN the system SHALL highlight affected natal planets and houses
6. WHEN showing aspects THEN the system SHALL indicate aspect type (conjunction, opposition, trine, square, sextile)
7. WHEN displaying the chart THEN the system SHALL update in real-time or allow date selection for future/past transits
8. WHEN a significant transit occurs THEN the system SHALL highlight it with visual emphasis

### Requirement 6: Dasha Predictions and Interpretations

**User Story:** As a user, I want detailed interpretations of Dasha periods, so that I can understand what to expect during each period.

#### Acceptance Criteria

1. WHEN viewing a Mahadasha THEN the system SHALL provide general predictions for that planetary period
2. WHEN viewing an Antardasha THEN the system SHALL show combined effects of Mahadasha lord and Antardasha lord
3. WHEN displaying predictions THEN the system SHALL categorize effects by life area (marriage, career, health, finances, spirituality)
4. WHEN a Dasha involves 7th house lord THEN the system SHALL highlight marriage-related predictions
5. WHEN showing Dasha effects THEN the system SHALL indicate strength based on planetary dignity and placement
6. WHEN a favorable Dasha period is shown THEN the system SHALL suggest optimal activities and decisions
7. WHEN a challenging Dasha is displayed THEN the system SHALL provide remedies and precautions
8. WHEN predictions are shown THEN the system SHALL include confidence levels based on chart strength

### Requirement 7: Shadow Planet Remedies

**User Story:** As a user, I want specific remedies for Rahu and Ketu, so that I can mitigate negative effects and enhance positive influences.

#### Acceptance Criteria

1. WHEN Rahu is afflicted THEN the system SHALL suggest specific mantras, gemstones, and practices
2. WHEN Ketu is afflicted THEN the system SHALL provide appropriate remedies and spiritual practices
3. WHEN showing remedies THEN the system SHALL indicate timing (days, hours) for maximum effectiveness
4. WHEN Rahu/Ketu cause doshas THEN the system SHALL explain the dosha and provide comprehensive remedies
5. WHEN displaying remedies THEN the system SHALL include both simple daily practices and advanced rituals
6. WHEN remedies are suggested THEN the system SHALL provide alternatives for different budgets and lifestyles
7. WHEN showing gemstone recommendations THEN the system SHALL specify weight, metal, and wearing instructions
8. WHEN remedies are displayed THEN the system SHALL explain the reasoning and expected benefits

### Requirement 8: Transit Alerts and Notifications

**User Story:** As a user, I want to be notified of important transits, so that I can prepare for significant astrological events.

#### Acceptance Criteria

1. WHEN a major transit begins THEN the system SHALL display an alert with transit details
2. WHEN Saturn enters a new sign THEN the system SHALL notify about Sade Sati phases if applicable
3. WHEN Jupiter transits 7th house THEN the system SHALL alert about marriage opportunities
4. WHEN a retrograde period starts THEN the system SHALL notify with precautions and guidance
5. WHEN displaying alerts THEN the system SHALL categorize by importance (critical, important, informational)
6. WHEN a user views alerts THEN the system SHALL show upcoming transits for the next 30/60/90 days
7. WHEN an eclipse occurs THEN the system SHALL provide special guidance and remedies
8. WHEN showing notifications THEN the system SHALL allow users to customize alert preferences

### Requirement 9: Comparative Dasha Analysis

**User Story:** As a user, I want to compare different Dasha systems, so that I can get multiple perspectives on timing.

#### Acceptance Criteria

1. WHEN viewing Dasha analysis THEN the system SHALL support Vimshottari Dasha as primary system
2. WHEN a user requests alternative systems THEN the system SHALL display Yogini Dasha as secondary option
3. WHEN comparing systems THEN the system SHALL show both timelines side-by-side for easy comparison
4. WHEN different systems indicate similar timing THEN the system SHALL highlight the convergence
5. WHEN showing multiple systems THEN the system SHALL explain the differences in calculation methods
6. WHEN predictions differ between systems THEN the system SHALL provide guidance on interpretation
7. WHEN displaying comparative analysis THEN the system SHALL indicate which system is more relevant for specific questions
8. WHEN a user selects a system THEN the system SHALL remember the preference for future sessions

### Requirement 10: Data Export and Sharing

**User Story:** As a user, I want to export Dasha and transit information, so that I can share with astrologers or keep records.

#### Acceptance Criteria

1. WHEN a user requests export THEN the system SHALL generate a PDF with complete Dasha timeline
2. WHEN exporting transit data THEN the system SHALL include current positions and predictions
3. WHEN generating reports THEN the system SHALL include visual charts and detailed interpretations
4. WHEN exporting THEN the system SHALL allow selection of date ranges and specific sections
5. WHEN a PDF is generated THEN the system SHALL format it professionally with proper branding
6. WHEN sharing is requested THEN the system SHALL provide a shareable link with privacy controls
7. WHEN exporting data THEN the system SHALL include both graphical and tabular formats
8. WHEN a report is created THEN the system SHALL allow customization of included sections

---

## Technical Considerations

### Data Requirements
- Real-time planetary position calculations (ephemeris data)
- Dasha calculation algorithms (Vimshottari, Yogini)
- Transit calculation engine
- Aspect calculation logic
- Historical and future date support

### Performance Requirements
- Transit positions should update within 1 second
- Dasha timeline should render within 2 seconds
- Chart visualizations should be smooth (60fps)
- Support for date range queries (past 10 years, future 10 years)

### Integration Requirements
- Swiss Ephemeris library or equivalent for accurate calculations
- Date/time handling with timezone support
- Responsive design for all visualizations
- Accessibility compliance for all interactive elements

---

## Success Criteria

- Users can view complete Dasha timeline with predictions
- Shadow planet analysis provides actionable insights
- Transit information is accurate and timely
- All visualizations are interactive and responsive
- Export functionality works across all browsers
- Performance meets specified requirements

---

## Out of Scope

- Horary astrology (Prashna)
- Muhurta (electional astrology)
- Compatibility analysis (separate feature)
- Ashtakavarga detailed calculations (future enhancement)
- Varshaphal (annual predictions)
- KP system (Krishnamurti Paddhati)

---

*This requirements document will guide the design and implementation of advanced astrology features in the Astro Marriage UI.*
