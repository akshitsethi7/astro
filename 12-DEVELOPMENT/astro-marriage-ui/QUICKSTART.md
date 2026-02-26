# Quick Start Guide

## Installation & Setup

1. **Install dependencies:**
   \`\`\`bash
   cd astro/astro-marriage-ui
   npm install
   \`\`\`

2. **Run development server:**
   \`\`\`bash
   npm run dev
   \`\`\`

3. **Open in browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

## What You'll See

- **Header**: Branding with gradient icon
- **Sidebar**: Navigation through all marriage analysis files
- **Main Content**: 
  - Hero section with gradient title
  - Stats cards showing key metrics
  - Interactive D3.js timeline chart
  - All markdown files rendered beautifully

## Features to Try

1. **Navigation**: Click any file in the sidebar to scroll to that section
2. **Mobile Menu**: On mobile, use the floating button to open/close sidebar
3. **Timeline**: Hover over the timeline bars to see the marriage prediction journey
4. **Responsive**: Resize your browser to see the responsive design

## Customization Tips

### Change Colors
Edit \`app/globals.scss\` and modify the gradient variables:
\`\`\`scss
--gradient-primary: linear-gradient(135deg, #YOUR_COLOR_1, #YOUR_COLOR_2);
\`\`\`

### Add More Stats
Edit \`components/ContentViewer.tsx\` and add to the \`stats\` array:
\`\`\`typescript
{ label: 'Your Label', value: 'Your Value', gradient: 'var(--gradient-primary)' }
\`\`\`

### Modify Timeline Data
Edit \`components/TimelineChart.tsx\` and update the \`data\` array with your years and values.

## Build for Production

\`\`\`bash
npm run build
npm start
\`\`\`

## Troubleshooting

**Port already in use?**
\`\`\`bash
npm run dev -- -p 3001
\`\`\`

**Files not loading?**
Make sure the \`marriage\` folder is in the parent directory of \`astro-marriage-ui\`.

**Styling issues?**
Clear Next.js cache:
\`\`\`bash
rm -rf .next
npm run dev
\`\`\`

Enjoy your beautiful astrology UI! ✨
