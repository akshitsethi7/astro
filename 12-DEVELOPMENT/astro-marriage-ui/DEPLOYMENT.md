# Deployment Guide

## Deploy to Vercel (Recommended)

Vercel is the easiest way to deploy Next.js apps.

### Steps:

1. **Push to GitHub:**
   \`\`\`bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   \`\`\`

2. **Connect to Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Click "Import Project"
   - Select your GitHub repository
   - Vercel will auto-detect Next.js settings

3. **Configure:**
   - Root Directory: \`astro-marriage-ui\`
   - Build Command: \`npm run build\`
   - Output Directory: \`.next\`

4. **Deploy:**
   - Click "Deploy"
   - Your app will be live in ~2 minutes!

## Deploy to Netlify

1. **Build the app:**
   \`\`\`bash
   npm run build
   \`\`\`

2. **Install Netlify CLI:**
   \`\`\`bash
   npm install -g netlify-cli
   \`\`\`

3. **Deploy:**
   \`\`\`bash
   netlify deploy --prod
   \`\`\`

## Deploy to Your Own Server

1. **Build:**
   \`\`\`bash
   npm run build
   \`\`\`

2. **Start:**
   \`\`\`bash
   npm start
   \`\`\`

3. **Use PM2 for production:**
   \`\`\`bash
   npm install -g pm2
   pm2 start npm --name "astro-ui" -- start
   pm2 save
   pm2 startup
   \`\`\`

## Environment Variables

If you need environment variables, create \`.env.local\`:

\`\`\`
NEXT_PUBLIC_API_URL=your_api_url
\`\`\`

## Performance Tips

- Enable image optimization
- Use Next.js built-in caching
- Enable compression
- Use CDN for static assets

## Custom Domain

### Vercel:
1. Go to Project Settings > Domains
2. Add your custom domain
3. Update DNS records as instructed

### Netlify:
1. Go to Domain Settings
2. Add custom domain
3. Configure DNS

## SSL Certificate

Both Vercel and Netlify provide free SSL certificates automatically.

## Monitoring

- Use Vercel Analytics for performance monitoring
- Set up error tracking with Sentry
- Monitor with Google Analytics

Enjoy your deployed app! 🚀
