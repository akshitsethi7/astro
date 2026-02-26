'use client';

import { useState } from 'react';
import Link from 'next/link';
import { TrendingUp, ArrowLeft, Calendar, AlertCircle, Zap } from 'lucide-react';
import { sampleChartData } from '@/lib/data/sampleChartData';
import styles from './page.module.scss';

export default function TransitsPage() {
  const [selectedDate, setSelectedDate] = useState(new Date());

  // Use actual transit data from sampleChartData
  const transitData = {
    currentTransits: sampleChartData.currentTransits,
    natalMoonSign: sampleChartData.planets.find(p => p.planet === 'Moon')?.sign || 'Virgo',
    majorTransits: [
      {
        planet: 'Jupiter',
        event: 'Transiting Gemini',
        date: new Date('2024-05-14'),
        significance: 'Jupiter in 11th house brings gains, friendships, and fulfillment of desires',
        impact: 'positive',
      },
      {
        planet: 'Saturn',
        event: 'Transiting Pisces',
        date: new Date('2023-01-17'),
        significance: 'Saturn in 8th house brings transformation and deep learning',
        impact: 'mixed',
      },
      {
        planet: 'Rahu',
        event: 'Transiting Pisces',
        date: new Date('2025-05-18'),
        significance: 'Rahu in 8th house intensifies research and occult interests',
        impact: 'mixed',
      },
    ],
  };

  return (
    <div className={styles.transitsPage}>
      {/* Header */}
      <header className={styles.header}>
        <Link href="/" className={styles.backBtn}>
          <ArrowLeft size={20} />
          Back to Home
        </Link>
        
        <div className={styles.headerContent}>
          <div className={styles.titleSection}>
            <h1 className={styles.title}>
              <TrendingUp size={36} />
              Planetary Transits
            </h1>
            <p className={styles.subtitle}>
              Current planetary movements and their impact on your natal chart
            </p>
          </div>
          
          <div className={styles.dateSelector}>
            <Calendar size={20} />
            <input 
              type="date" 
              value={selectedDate.toISOString().split('T')[0]}
              onChange={(e) => setSelectedDate(new Date(e.target.value))}
              className={styles.dateInput}
            />
          </div>
        </div>
      </header>

      {/* Sade Sati Information */}
      <section className={styles.sadeSatiSection}>
        <div className={styles.infoCard}>
          <div className={styles.infoHeader}>
            <AlertCircle size={24} />
            <h2>Sade Sati Information</h2>
          </div>
          <p className={styles.infoText}>
            Natal Moon in {transitData.natalMoonSign}. Saturn is currently transiting {transitData.currentTransits.find(t => t.planet === 'Saturn')?.sign}.
            Sade Sati occurs when Saturn transits the 12th, 1st, or 2nd house from natal Moon.
          </p>
        </div>
      </section>

      {/* Current Transits Table */}
      <section className={styles.tableSection}>
        <div className={styles.sectionHeader}>
          <h2 className={styles.sectionTitle}>Current Planetary Positions</h2>
          <p className={styles.sectionSubtitle}>As of {selectedDate.toLocaleDateString('en-US', { month: 'long', year: 'numeric' })}</p>
        </div>
        
        <div className={styles.transitsTable}>
          <div className={styles.tableHeader}>
            <div>Planet</div>
            <div>Sign</div>
            <div>Degree</div>
            <div>House</div>
            <div>Speed</div>
            <div>Status</div>
          </div>
          {transitData.currentTransits.map((transit, index) => (
            <div key={index} className={styles.tableRow}>
              <div className={styles.planetName}>{transit.planet}</div>
              <div>{transit.sign}</div>
              <div>{transit.degree.toFixed(2)}°</div>
              <div>{transit.house}th</div>
              <div>{transit.speed.toFixed(2)}°/day</div>
              <div>
                <span className={`${styles.status} ${transit.retrograde ? styles.retrograde : styles.direct}`}>
                  {transit.retrograde ? 'Retrograde' : 'Direct'}
                </span>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Major Transits */}
      <section className={styles.majorTransitsSection}>
        <div className={styles.sectionHeader}>
          <h2 className={styles.sectionTitle}>
            <AlertCircle size={24} />
            Current Major Transits
          </h2>
        </div>
        
        <div className={styles.majorTransitsGrid}>
          {transitData.majorTransits.map((transit, index) => (
            <div key={index} className={styles.majorTransitCard}>
              <div className={styles.transitHeader}>
                <span className={styles.transitPlanet}>{transit.planet}</span>
                <span className={`${styles.transitImpact} ${styles[transit.impact]}`}>
                  {transit.impact}
                </span>
              </div>
              <h3 className={styles.transitEvent}>{transit.event}</h3>
              <p className={styles.transitSignificance}>{transit.significance}</p>
              <div className={styles.transitDate}>
                <Calendar size={16} />
                {transit.date.toLocaleDateString('en-US', { 
                  year: 'numeric', 
                  month: 'long', 
                  day: 'numeric' 
                })}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Transit Impact Summary */}
      <section className={styles.aspectsSection}>
        <div className={styles.sectionHeader}>
          <h2 className={styles.sectionTitle}>Transit Impact on Natal Chart</h2>
        </div>
        
        <div className={styles.aspectsGrid}>
          <div className={styles.aspectCard}>
            <h3 className={styles.aspectTitle}>Jupiter Transit</h3>
            <p className={styles.aspectDescription}>
              Jupiter in 11th house (Gemini) brings opportunities for gains, networking, and fulfillment of long-term goals.
            </p>
          </div>
          
          <div className={styles.aspectCard}>
            <h3 className={styles.aspectTitle}>Saturn Transit</h3>
            <p className={styles.aspectDescription}>
              Saturn in 8th house (Pisces) brings transformation, deep research, and lessons in shared resources.
            </p>
          </div>
          
          <div className={styles.aspectCard}>
            <h3 className={styles.aspectTitle}>Rahu-Ketu Axis</h3>
            <p className={styles.aspectDescription}>
              Rahu in 8th and Ketu in 2nd creates focus on transformation and detachment from material possessions.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
