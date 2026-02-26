import type { Metadata } from 'next'
import { IBM_Plex_Sans, IBM_Plex_Mono } from 'next/font/google'
import { ChartProvider } from '@/lib/context/ChartContext'
import { Navigation } from '@/components/Navigation'
import './globals.scss'

const ibmPlexSans = IBM_Plex_Sans({
  weight: ['400', '500', '600', '700'],
  subsets: ['latin'],
  variable: '--font-ibm-plex-sans',
})

const ibmPlexMono = IBM_Plex_Mono({
  weight: ['400', '500', '600'],
  subsets: ['latin'],
  variable: '--font-ibm-plex-mono',
})

export const metadata: Metadata = {
  title: 'Vedic Astrology Platform',
  description: 'Complete Vedic astrology analysis with Dasha, transits, and birth chart',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={`${ibmPlexSans.variable} ${ibmPlexMono.variable}`}>
        <ChartProvider>
          <div className="gradient-bg" />
          <Navigation />
          {children}
        </ChartProvider>
      </body>
    </html>
  )
}
