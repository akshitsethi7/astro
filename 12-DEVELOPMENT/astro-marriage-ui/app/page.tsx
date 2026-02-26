'use client';

import { useState } from 'react';
import Link from 'next/link';
import { Calendar, Moon, Star, TrendingUp, Sparkles, ArrowRight, Settings } from 'lucide-react';
import { useChart } from '@/lib/context/ChartContext';
import BirthChartForm from '@/components/BirthChartForm';
import styles from './page.module.scss';

export default function Home() {
  const { birthDetails, chartData, isLoading } = useChart();
  const [showForm, setShowForm] = useState(false);

  return (
    <div className={styles.homePage}>
      {/* Chart Info Banner */}
      {birthDetails && !showForm && (
        <div className={styles.chartBanner}>
          <div className={styles.bannerContent}>
            <div className={styles.bannerInfo}>
              <span className={styles.bannerLabel}>Current Chart:</span>
              <span className={styles.bannerValue}>
                {birthDetails.name || 'Birth Chart'} - {new Date(birthDetails.date).toLocaleDateString()}
              </span>
            </div>
            <button onClick={() => setShowForm(true)} className={styles.bannerBtn}>
              <Settings size={18} />
              Change Details
            </button>
          </div>
        </div>
      )}

      {/* Birth Chart Form Modal */}
      {showForm && (
        <div className={styles.modal}>
          <div className={styles.modalOverlay} onClick={() => setShowForm(false)} />
          <div className={styles.modalContent}>
            <BirthChartForm onClose={() => setShowForm(false)} />
          </div>
        </div>
      )}

      {/* Hero Section */}
      <section className={styles.hero}>
        <div className={styles.heroContent}>
          <div className={styles.badge}>
            <Sparkles size={16} />
            <span>Advanced Vedic Astrology Platform</span>
          </div>
          
          <h1 className={styles.heroTitle}>
            Unlock Your
            <span className={styles.gradient}> Cosmic Blueprint</span>
          </h1>
          
          <p className={styles.heroSubtitle}>
            Explore your birth chart, Dasha periods, planetary transits, and shadow planet influences
            with precision calculations and beautiful visualizations.
          </p>
          
          <div className={styles.heroActions}>
            {!birthDetails && (
              <button onClick={() => setShowForm(true)} className={styles.primaryBtn}>
                <Calendar size={20} />
                Enter Birth Details
                <ArrowRight size={20} />
              </button>
            )}
            
            {birthDetails && (
              <Link href="/dasha" className={styles.primaryBtn}>
                <Calendar size={20} />
                Explore Dasha Timeline
                <ArrowRight size={20} />
              </Link>
            )}
            
            <Link href="/chart" className={styles.secondaryBtn}>
              View Birth Chart
            </Link>
          </div>

          {isLoading && (
            <div className={styles.loadingIndicator}>
              <div className={styles.spinner} />
              <span>Calculating your chart...</span>
            </div>
          )}
        </div>
        
        <div className={styles.heroVisual}>
          <div className={styles.orb}>
            <div className={styles.orbInner} />
          </div>
        </div>
      </section>

      {/* Rest of the page remains the same */}
      <section className={styles.features}>
        <h2 className={styles.featuresTitle}>Comprehensive Astrological Analysis</h2>
        
        <div className={styles.featuresGrid}>
          <Link href="/dasha" className={styles.featureCard}>
            <div className={styles.featureIcon} style={{ background: 'linear-gradient(135deg, #8b5cf6 0%, #3b82f6 100%)' }}>
              <Calendar size={24} />
            </div>
            <h3 className={styles.featureTitle}>Vimshottari Dasha</h3>
            <p className={styles.featureDescription}>
              120-year planetary period system with Mahadasha, Antardasha, and Pratyantar calculations.
              Interactive timeline with strength evaluation.
            </p>
            <div className={styles.featureLink}>
              Explore Dasha <ArrowRight size={16} />
            </div>
          </Link>

          <Link href="/shadows" className={styles.featureCard}>
            <div className={styles.featureIcon} style={{ background: 'linear-gradient(135deg, #8338ec 0%, #fb5607 100%)' }}>
              <Moon size={24} />
            </div>
            <h3 className={styles.featureTitle}>Shadow Planets</h3>
            <p className={styles.featureDescription}>
              Deep analysis of Rahu and Ketu positions, aspects, yogas, and their impact on different life areas.
            </p>
            <div className={styles.featureLink}>
              Analyze Shadows <ArrowRight size={16} />
            </div>
          </Link>

          <Link href="/transits" className={styles.featureCard}>
            <div className={styles.featureIcon} style={{ background: 'linear-gradient(135deg, #22c55e 0%, #10b981 100%)' }}>
              <TrendingUp size={24} />
            </div>
            <h3 className={styles.featureTitle}>Planetary Transits</h3>
            <p className={styles.featureDescription}>
              Current and future planetary movements, Sade Sati detection, and transit-natal aspect analysis.
            </p>
            <div className={styles.featureLink}>
              Track Transits <ArrowRight size={16} />
            </div>
          </Link>

          <Link href="/chart" className={styles.featureCard}>
            <div className={styles.featureIcon} style={{ background: 'linear-gradient(135deg, #f59e0b 0%, #ef4444 100%)' }}>
              <Star size={24} />
            </div>
            <h3 className={styles.featureTitle}>Birth Chart</h3>
            <p className={styles.featureDescription}>
              Complete natal chart with planetary positions, houses, aspects, and dignity calculations.
            </p>
            <div className={styles.featureLink}>
              View Chart <ArrowRight size={16} />
            </div>
          </Link>
        </div>
      </section>

      {/* Stats Section */}
      <section className={styles.stats}>
        <div className={styles.statsGrid}>
          <div className={styles.statCard}>
            <div className={styles.statValue}>9</div>
            <div className={styles.statLabel}>Planets Analyzed</div>
          </div>
          
          <div className={styles.statCard}>
            <div className={styles.statValue}>27</div>
            <div className={styles.statLabel}>Nakshatras</div>
          </div>
          
          <div className={styles.statCard}>
            <div className={styles.statValue}>8</div>
            <div className={styles.statLabel}>Active Yogas</div>
          </div>
          
          <div className={styles.statCard}>
            <div className={styles.statValue}>120</div>
            <div className={styles.statLabel}>Years of Dasha</div>
          </div>
        </div>
      </section>

      {/* Quick Chart Summary */}
      {birthDetails && (
        <section className={styles.quickSummary}>
          <h2 className={styles.summaryTitle}>Your Chart at a Glance</h2>
          <div className={styles.summaryGrid}>
            <div className={styles.summaryCard}>
              <div className={styles.summaryLabel}>Ascendant</div>
              <div className={styles.summaryValue}>Leo 23°2'49"</div>
              <div className={styles.summaryDetail}>Purva Phalguni Nakshatra</div>
            </div>
            
            <div className={styles.summaryCard}>
              <div className={styles.summaryLabel}>Moon Sign</div>
              <div className={styles.summaryValue}>Virgo 22°44'</div>
              <div className={styles.summaryDetail}>Hasta Nakshatra</div>
            </div>
            
            <div className={styles.summaryCard}>
              <div className={styles.summaryLabel}>Current Dasha</div>
              <div className={styles.summaryValue}>Rahu/Jupiter</div>
              <div className={styles.summaryDetail}>2005-2007</div>
            </div>
            
            <div className={styles.summaryCard}>
              <div className={styles.summaryLabel}>Major Yogas</div>
              <div className={styles.summaryValue}>4 Present</div>
              <div className={styles.summaryDetail}>Malavya, Sasa, Raja, Musala</div>
            </div>
          </div>
        </section>
      )}

      {/* CTA Section */}
      <section className={styles.cta}>
        <h2 className={styles.ctaTitle}>Ready to explore your cosmic journey?</h2>
        <p className={styles.ctaSubtitle}>
          {birthDetails 
            ? 'Start with your Dasha timeline to understand the planetary periods shaping your life.'
            : 'Enter your birth details to unlock personalized astrological insights.'}
        </p>
        {birthDetails ? (
          <Link href="/dasha" className={styles.ctaBtn}>
            <Calendar size={20} />
            View Dasha Timeline
            <ArrowRight size={20} />
          </Link>
        ) : (
          <button onClick={() => setShowForm(true)} className={styles.ctaBtn}>
            <Calendar size={20} />
            Enter Birth Details
            <ArrowRight size={20} />
          </button>
        )}
      </section>
    </div>
  );
}
