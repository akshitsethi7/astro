# Tips & Tricks

## ⌨️ Keyboard Shortcuts

### Navigation
- **Tab**: Move between sidebar items
- **Enter**: Select focused sidebar item
- **Space**: Scroll down one page
- **Shift + Space**: Scroll up one page
- **Home**: Jump to top of page
- **End**: Jump to bottom of page
- **Arrow Up/Down**: Scroll smoothly

### Browser
- **Cmd/Ctrl + R**: Refresh page
- **Cmd/Ctrl + Shift + R**: Hard refresh (clear cache)
- **Cmd/Ctrl + +**: Zoom in
- **Cmd/Ctrl + -**: Zoom out
- **Cmd/Ctrl + 0**: Reset zoom

## 🎨 Customization Tips

### Quick Color Changes

Want to change the theme? Edit \`app/globals.scss\`:

\`\`\`scss
// Ocean Theme
--gradient-primary: linear-gradient(135deg, #2E3192 0%, #1BFFFF 100%);
--gradient-secondary: linear-gradient(135deg, #00B4DB 0%, #0083B0 100%);

// Sunset Theme
--gradient-primary: linear-gradient(135deg, #FF512F 0%, #DD2476 100%);
--gradient-secondary: linear-gradient(135deg, #F09819 0%, #EDDE5D 100%);

// Forest Theme
--gradient-primary: linear-gradient(135deg, #134E5E 0%, #71B280 100%);
--gradient-secondary: linear-gradient(135deg, #56AB2F 0%, #A8E063 100%);

// Neon Theme
--gradient-primary: linear-gradient(135deg, #FF00FF 0%, #00FFFF 100%);
--gradient-secondary: linear-gradient(135deg, #FF0080 0%, #FF8C00 100%);
\`\`\`

### Font Size Adjustments

Make text larger or smaller:

\`\`\`scss
// In app/globals.scss
html {
  font-size: 18px; // Default is 16px
}

// Or for specific elements
.markdown {
  font-size: 1.125rem; // 18px
  line-height: 1.8;
}
\`\`\`

### Sidebar Width

Make sidebar wider or narrower:

\`\`\`scss
// In components/Sidebar.module.scss
.sidebar {
  width: 320px; // Default is 280px
}
\`\`\`

### Content Width

Adjust max content width:

\`\`\`scss
// In components/ContentViewer.module.scss
.contentInner {
  max-width: 1200px; // Default is 900px
}
\`\`\`

## 🚀 Performance Tips

### Faster Development

1. **Use Fast Refresh**: Edit files and see changes instantly
2. **Keep DevTools Open**: Monitor performance
3. **Use React DevTools**: Debug component state

### Optimize Images

If you add images:

\`\`\`tsx
import Image from 'next/image'

<Image 
  src="/your-image.jpg" 
  alt="Description"
  width={800}
  height={600}
  priority // For above-fold images
/>
\`\`\`

### Lazy Load Components

For heavy components:

\`\`\`tsx
import dynamic from 'next/dynamic'

const HeavyChart = dynamic(() => import('./HeavyChart'), {
  loading: () => <p>Loading chart...</p>,
  ssr: false // Disable server-side rendering
})
\`\`\`

## 📱 Mobile Tips

### Testing on Mobile

1. **Chrome DevTools**: Toggle device toolbar (Cmd/Ctrl + Shift + M)
2. **Responsive Mode**: Test different screen sizes
3. **Network Throttling**: Test on slow connections
4. **Touch Events**: Use device mode to simulate touch

### Mobile-Specific Styles

\`\`\`scss
// Target mobile only
@media (max-width: 767px) {
  .component {
    // Mobile-only styles
  }
}

// Target touch devices
@media (hover: none) {
  .button {
    // Touch-friendly styles
  }
}
\`\`\`

## 🎯 Content Tips

### Markdown Best Practices

1. **Use Headings**: Create clear hierarchy
2. **Add Lists**: Break up long paragraphs
3. **Use Tables**: For structured data
4. **Add Code Blocks**: For technical content
5. **Include Links**: Reference external resources

### File Naming

For proper ordering:

\`\`\`
✅ Good:
01-overview.md
02-analysis.md
03-predictions.md

❌ Bad:
overview.md
analysis.md
predictions.md
\`\`\`

### Frontmatter (Optional)

Add metadata to markdown files:

\`\`\`markdown
---
title: Custom Title
date: 2024-01-01
author: Your Name
---

# Content starts here
\`\`\`

## 🐛 Debugging Tips

### Check Console

Open browser console (F12) and look for:
- Red errors
- Yellow warnings
- Network requests
- Component renders

### React DevTools

Install React DevTools extension:
- Inspect component tree
- View props and state
- Profile performance
- Track re-renders

### Common Issues

**Sidebar not showing files?**
\`\`\`bash
# Check file path
ls ../marriage/

# Should show .md files
\`\`\`

**Styles not applying?**
\`\`\`bash
# Clear Next.js cache
rm -rf .next
npm run dev
\`\`\`

**Chart not rendering?**
\`\`\`javascript
// Check browser console for D3 errors
// Ensure SVG ref is attached
\`\`\`

## 🎨 Design Tips

### Consistent Spacing

Use the spacing scale:

\`\`\`scss
// Good
padding: var(--spacing-md);
margin-bottom: var(--spacing-lg);

// Avoid
padding: 15px;
margin-bottom: 23px;
\`\`\`

### Color Usage

\`\`\`scss
// Use semantic colors
color: var(--color-text-primary);
background: var(--color-surface);

// Use gradients for accents
background: var(--gradient-primary);
\`\`\`

### Responsive Design

\`\`\`scss
// Mobile first
.card {
  padding: var(--spacing-md);
  
  @media (min-width: 768px) {
    padding: var(--spacing-xl);
  }
}
\`\`\`

## 📊 Data Visualization Tips

### D3.js Best Practices

1. **Clean up**: Remove old elements before redrawing
2. **Animate**: Use transitions for smooth updates
3. **Responsive**: Update on window resize
4. **Accessible**: Add ARIA labels

### Custom Charts

Create new chart components:

\`\`\`tsx
// components/CustomChart.tsx
'use client'

import { useEffect, useRef } from 'react'
import * as d3 from 'd3'

export function CustomChart({ data }) {
  const svgRef = useRef<SVGSVGElement>(null)
  
  useEffect(() => {
    if (!svgRef.current) return
    
    // Your D3 code here
    const svg = d3.select(svgRef.current)
    // ...
  }, [data])
  
  return <svg ref={svgRef} />
}
\`\`\`

## 🔧 Development Workflow

### Recommended Flow

1. **Start dev server**: \`npm run dev\`
2. **Open browser**: http://localhost:3000
3. **Open editor**: VS Code or your favorite
4. **Edit files**: Changes auto-reload
5. **Check browser**: See updates instantly
6. **Test mobile**: Use DevTools device mode
7. **Build**: \`npm run build\` before deploying

### Git Workflow

\`\`\`bash
# Create feature branch
git checkout -b feature/new-chart

# Make changes
# ...

# Commit
git add .
git commit -m "Add new chart component"

# Push
git push origin feature/new-chart

# Merge to main
git checkout main
git merge feature/new-chart
\`\`\`

## 🎯 Production Tips

### Before Deploying

1. **Test build**: \`npm run build\`
2. **Check errors**: Fix all TypeScript errors
3. **Test production**: \`npm start\`
4. **Test mobile**: On real devices
5. **Check performance**: Use Lighthouse
6. **Optimize images**: Compress before adding

### Environment Variables

Create \`.env.local\`:

\`\`\`bash
NEXT_PUBLIC_SITE_URL=https://yourdomain.com
NEXT_PUBLIC_GA_ID=your-google-analytics-id
\`\`\`

Use in code:

\`\`\`tsx
const siteUrl = process.env.NEXT_PUBLIC_SITE_URL
\`\`\`

### Performance Monitoring

Add analytics:

\`\`\`tsx
// app/layout.tsx
import { Analytics } from '@vercel/analytics/react'

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        {children}
        <Analytics />
      </body>
    </html>
  )
}
\`\`\`

## 💡 Pro Tips

### Speed Up Development

1. **Use snippets**: Create code snippets in your editor
2. **Hot keys**: Learn keyboard shortcuts
3. **Multiple terminals**: One for dev, one for commands
4. **Browser extensions**: React DevTools, Redux DevTools

### Code Organization

\`\`\`
components/
├── layout/          # Layout components
│   ├── Header.tsx
│   └── Sidebar.tsx
├── content/         # Content components
│   └── ContentViewer.tsx
├── charts/          # Chart components
│   └── TimelineChart.tsx
└── ui/              # Reusable UI components
    └── StatsCard.tsx
\`\`\`

### Component Patterns

\`\`\`tsx
// Reusable component with TypeScript
interface CardProps {
  title: string
  children: React.ReactNode
  variant?: 'default' | 'elevated'
}

export function Card({ title, children, variant = 'default' }: CardProps) {
  return (
    <div className={\`card card-\${variant}\`}>
      <h3>{title}</h3>
      {children}
    </div>
  )
}
\`\`\`

### Style Patterns

\`\`\`scss
// Reusable mixins
@mixin card-base {
  padding: var(--spacing-lg);
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border);
  background: var(--color-surface);
}

.statsCard {
  @include card-base;
  // Additional styles
}
\`\`\`

## 🎓 Learning Resources

### Next.js
- [Next.js Docs](https://nextjs.org/docs)
- [Next.js Learn](https://nextjs.org/learn)
- [Next.js Examples](https://github.com/vercel/next.js/tree/canary/examples)

### React
- [React Docs](https://react.dev)
- [React Patterns](https://reactpatterns.com)
- [React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app)

### D3.js
- [D3 Gallery](https://observablehq.com/@d3/gallery)
- [D3 Graph Gallery](https://d3-graph-gallery.com)
- [D3 in Depth](https://www.d3indepth.com)

### SCSS
- [Sass Docs](https://sass-lang.com/documentation)
- [Sass Guidelines](https://sass-guidelin.es)

### TypeScript
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [TypeScript Deep Dive](https://basarat.gitbook.io/typescript)

## 🎉 Fun Experiments

### Easter Eggs

Add fun interactions:

\`\`\`tsx
// Konami code easter egg
useEffect(() => {
  const konamiCode = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown']
  let konamiIndex = 0
  
  const handleKeyDown = (e: KeyboardEvent) => {
    if (e.key === konamiCode[konamiIndex]) {
      konamiIndex++
      if (konamiIndex === konamiCode.length) {
        // Activate easter egg!
        console.log('🎉 You found the secret!')
        konamiIndex = 0
      }
    } else {
      konamiIndex = 0
    }
  }
  
  window.addEventListener('keydown', handleKeyDown)
  return () => window.removeEventListener('keydown', handleKeyDown)
}, [])
\`\`\`

### Particle Effects

Add background particles:

\`\`\`tsx
// Use react-particles or create custom canvas animation
\`\`\`

### Theme Switcher

Add light/dark mode toggle:

\`\`\`tsx
const [theme, setTheme] = useState('dark')

const toggleTheme = () => {
  setTheme(theme === 'dark' ? 'light' : 'dark')
  document.body.className = theme
}
\`\`\`

---

**Experiment, have fun, and make it your own!** ✨

Remember: The best way to learn is by doing. Try things, break things, fix things!
