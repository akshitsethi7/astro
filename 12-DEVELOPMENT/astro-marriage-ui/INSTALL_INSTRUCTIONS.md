# Installation Instructions

## Prerequisites Check

Before starting, make sure you have:

### 1. Node.js (Required)
Check if installed:
\`\`\`bash
node --version
\`\`\`

Should show v18.0.0 or higher.

**Don't have Node.js?**
- Download from: https://nodejs.org/
- Choose LTS version (recommended)
- Install and restart terminal

### 2. npm (Comes with Node.js)
Check if installed:
\`\`\`bash
npm --version
\`\`\`

Should show v9.0.0 or higher.

## Step-by-Step Installation

### Step 1: Navigate to Project
\`\`\`bash
cd astro/astro-marriage-ui
\`\`\`

### Step 2: Install Dependencies
\`\`\`bash
npm install
\`\`\`

This will:
- Download all required packages
- Set up Next.js
- Install React, D3.js, and other dependencies
- Take 1-3 minutes depending on internet speed

**Expected output:**
\`\`\`
added 324 packages in 2m
\`\`\`

### Step 3: Verify Installation
Check that \`node_modules\` folder was created:
\`\`\`bash
ls -la
\`\`\`

You should see:
- \`node_modules/\` folder
- \`package-lock.json\` file

### Step 4: Run Development Server
\`\`\`bash
npm run dev
\`\`\`

**Expected output:**
\`\`\`
▲ Next.js 15.1.0
- Local:        http://localhost:3000
- Ready in 2.3s
\`\`\`

### Step 5: Open in Browser
Open your browser and go to:
\`\`\`
http://localhost:3000
\`\`\`

You should see the Astro Marriage Analysis UI!

## Common Installation Issues

### Issue 1: "command not found: npm"

**Problem**: Node.js not installed or not in PATH

**Solution**:
1. Install Node.js from https://nodejs.org/
2. Restart terminal
3. Try again

### Issue 2: "EACCES: permission denied"

**Problem**: Permission issues with npm

**Solution**:
\`\`\`bash
sudo npm install
\`\`\`

Or fix npm permissions:
\`\`\`bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
\`\`\`

### Issue 3: "Port 3000 already in use"

**Problem**: Another app is using port 3000

**Solution**: Use a different port
\`\`\`bash
npm run dev -- -p 3001
\`\`\`

Then visit: http://localhost:3001

### Issue 4: "Cannot find module"

**Problem**: Dependencies not installed properly

**Solution**: Clean install
\`\`\`bash
rm -rf node_modules package-lock.json
npm install
\`\`\`

### Issue 5: "Marriage files not found"

**Problem**: Marriage folder not in correct location

**Solution**: Ensure folder structure is:
\`\`\`
astro/
├── marriage/           ← Your markdown files here
│   ├── 01-overview.md
│   ├── 02-chart-data.md
│   └── ...
└── astro-marriage-ui/  ← Your Next.js app here
    ├── app/
    ├── components/
    └── ...
\`\`\`

### Issue 6: Slow installation

**Problem**: Slow internet or npm registry issues

**Solution**: Use a faster registry
\`\`\`bash
npm install --registry=https://registry.npmmirror.com
\`\`\`

Or use yarn instead:
\`\`\`bash
npm install -g yarn
yarn install
yarn dev
\`\`\`

## Verification Checklist

After installation, verify:

- [ ] \`node_modules/\` folder exists
- [ ] \`package-lock.json\` file exists
- [ ] \`npm run dev\` starts without errors
- [ ] Browser shows the UI at localhost:3000
- [ ] Sidebar shows list of markdown files
- [ ] Timeline chart is visible
- [ ] Stats cards are displayed
- [ ] Clicking sidebar items scrolls to sections

## Next Steps

Once installed successfully:

1. **Explore the UI**: Click around and see all features
2. **Read Documentation**: Check README.md for details
3. **Customize**: Modify colors, fonts, or content
4. **Deploy**: Follow DEPLOYMENT.md to go live

## Getting Help

If you're still stuck:

1. **Check logs**: Look at terminal output for error messages
2. **Browser console**: Open DevTools (F12) and check Console tab
3. **Clear cache**: Try clearing browser cache
4. **Restart**: Close terminal, restart, and try again
5. **Clean install**: Delete everything and start fresh

## Alternative: Using Yarn

If npm doesn't work, try yarn:

\`\`\`bash
# Install yarn
npm install -g yarn

# Install dependencies
yarn install

# Run dev server
yarn dev

# Build for production
yarn build
\`\`\`

## Alternative: Using pnpm

For faster installs:

\`\`\`bash
# Install pnpm
npm install -g pnpm

# Install dependencies
pnpm install

# Run dev server
pnpm dev

# Build for production
pnpm build
\`\`\`

## System Requirements

### Minimum
- Node.js 18+
- 2GB RAM
- 500MB disk space
- Modern browser

### Recommended
- Node.js 20+
- 4GB RAM
- 1GB disk space
- Chrome/Firefox/Safari latest

## Development Environment

### VS Code (Recommended)
Install these extensions:
- ESLint
- Prettier
- TypeScript and JavaScript Language Features
- SCSS IntelliSense

### Other Editors
- WebStorm: Works out of the box
- Sublime Text: Install TypeScript plugin
- Vim/Neovim: Install coc-tsserver

## Build for Production

When ready to deploy:

\`\`\`bash
# Build optimized version
npm run build

# Test production build locally
npm start

# Visit http://localhost:3000
\`\`\`

## Updating Dependencies

To update to latest versions:

\`\`\`bash
# Check for updates
npm outdated

# Update all dependencies
npm update

# Or update specific package
npm update next
\`\`\`

## Uninstalling

To remove the project:

\`\`\`bash
# Delete node_modules
rm -rf node_modules

# Delete lock file
rm package-lock.json

# Or delete entire project
cd ..
rm -rf astro-marriage-ui
\`\`\`

---

**Installation should take 2-5 minutes total.** 

If successful, you'll have a beautiful, working astrology UI! ✨
