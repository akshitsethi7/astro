# Astro Marriage Analysis UI

A modern, responsive web application built with Next.js to visualize Vedic astrology marriage analysis data. Inspired by Lagna360's professional dashboard design with interactive charts and comprehensive data visualization.

## Tech Stack

- **Next.js 15** - React framework with App Router
- **React 18** - UI library
- **TypeScript** - Type safety
- **SCSS** - Styling with CSS modules
- **D3.js** - Data visualization for charts and birth chart
- **Lucide React** - Modern icon library
- **IBM Plex** - Typography (Sans & Mono)
- **Marked** - Markdown parsing
- **Gray Matter** - Frontmatter parsing

## Design Inspiration

- **Lagna360** - Professional astrology dashboard
- **Linear.app** - Clean, modern interface
- **Vercel** - Gradient aesthetics and smooth animations
- Magazine-style layout with responsive grid

## Features

### 🎨 Interactive Visualizations
- **Birth Chart (D1)** - Interactive circular chart with planetary positions
- **Planetary Table** - Detailed positions with color-coded planets
- **Dasha Timeline** - Interactive timeline showing planetary periods
- **Marriage Timeline** - Probability chart across years
- **Stats Cards** - Key metrics with gradients and hover effects

### 📊 Dashboard Components
- **Overview Dashboard** - Comprehensive view with all key information
- **Tab Navigation** - Easy switching between different sections
- **Info Cards** - Highlight cards with trends and icons
- **Spouse Profile** - Detailed characteristics grid
- **Key Highlights** - Important astrological combinations

### 📱 Responsive Design
- Fully responsive (mobile, tablet, desktop)
- Touch-optimized interactions
- Collapsible sidebar on mobile
- Floating action button
- Adaptive layouts

### 🎯 User Experience
- Smooth animations and transitions
- Hover effects on interactive elements
- Click-to-select dasha periods
- Scroll-to-section navigation
- Color-coded planetary positions
- Gradient-based design system

### 🌙 Dark Theme
- Optimized for readability
- Gradient accents
- Proper contrast ratios
- Subtle background effects

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

\`\`\`bash
cd astro-marriage-ui
npm install
\`\`\`

### Development

\`\`\`bash
npm run dev
\`\`\`

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Build

\`\`\`bash
npm run build
npm start
\`\`\`

## Project Structure

\`\`\`
astro-marriage-ui/
├── app/
│   ├── layout.tsx          # Root layout with fonts
│   ├── page.tsx            # Home page
│   ├── globals.scss        # Global styles
│   └── page.module.scss    # Page-specific styles
├── components/
│   ├── Header.tsx          # Top navigation
│   ├── Sidebar.tsx         # File navigation
│   ├── ContentViewer.tsx   # Main content area
│   ├── StatsCard.tsx       # Statistics cards
│   └── TimelineChart.tsx   # D3.js timeline
├── lib/
│   └── markdown.ts         # Markdown file processing
└── public/                 # Static assets
\`\`\`

## Customization

### Colors

Edit gradient variables in \`app/globals.scss\`:

\`\`\`scss
--gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
--gradient-secondary: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
\`\`\`

### Typography

Fonts are configured in \`app/layout.tsx\` using Next.js font optimization.

### Content

The app automatically reads markdown files from \`../marriage/\` directory.

## Responsive Breakpoints

- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

Private project for personal use.
