'use client';

import Link from 'next/link';
import { ArrowLeft, Sparkles, Target, Calendar, Heart } from 'lucide-react';
import styles from './page.module.scss';

export default function JaiminiPage() {
  const jaiminiData = {
    darakaraka: {
      planet: 'Mars',
      sign: 'Leo',
      house: '1st',
      nakshatra: 'Magha',
      spouseTraits: [
        'Energetic, assertive, independent',
        'Direct communicator, strong willpower',
        'Leadership-oriented, creative',
        'Physically active, fitness-conscious',
      ],
    },
    upapada: {
      sign: 'Scorpio',
      house: '4th from Lagna',
      lord: 'Mars (in Lagna)',
      jupiterOnUL: true,
      rating: '9/10',
    },
    charaDasha: {
      current: 'Sagittarius',
      currentEnd: 'Dec 2026',
      marriageWindow: 'Capricorn (Dec 2026 - Dec 2028)',
      aquarius: 'Aquarius (Dec 2028 - Dec 2029)',
    },
    narayanaDasha: {
      current: 'Aquarius',
      currentEnd: '2031',
      marriagePeriod: '2025-12-24 – 2031-12-24',
    },
  };

  return (
    <div className={styles.jaiminiPage}>
      <header className={styles.header}>
        <Link href="/" className={styles.backBtn}>
          <ArrowLeft size={20} />
          Back to Home
        </Link>

        <div className={styles.headerContent}>
          <div className={styles.titleSection}>
            <h1 className={styles.title}>
              <Sparkles size={36} />
              Jaimini Marriage Analysis
            </h1>
            <p className={styles.subtitle}>
              Darakaraka, Upapada Lagna, Chara & Narayana Dasha
            </p>
          </div>
        </div>
      </header>

      <section className={styles.cardsSection}>
        <div className={styles.card}>
          <div className={styles.cardHeader}>
            <Target size={24} />
            <h2>Darakaraka (Spouse Significator)</h2>
          </div>
          <div className={styles.cardBody}>
            <div className={styles.highlight}>
              {jaiminiData.darakaraka.planet} in {jaiminiData.darakaraka.sign} ({jaiminiData.darakaraka.house})
            </div>
            <p className={styles.nakshatra}>{jaiminiData.darakaraka.nakshatra} Nakshatra</p>
            <ul>
              {jaiminiData.darakaraka.spouseTraits.map((trait, i) => (
                <li key={i}>{trait}</li>
              ))}
            </ul>
          </div>
        </div>

        <div className={styles.card}>
          <div className={styles.cardHeader}>
            <Heart size={24} />
            <h2>Upapada Lagna (Marriage Indicator)</h2>
          </div>
          <div className={styles.cardBody}>
            <div className={styles.highlight}>
              UL = {jaiminiData.upapada.sign} ({jaiminiData.upapada.house})
            </div>
            <p>UL Lord: {jaiminiData.upapada.lord}</p>
            {jaiminiData.upapada.jupiterOnUL && (
              <p className={styles.auspicious}>Jupiter on UL — extremely auspicious</p>
            )}
            <p className={styles.rating}>Marriage rating: {jaiminiData.upapada.rating}</p>
          </div>
        </div>

        <div className={styles.card}>
          <div className={styles.cardHeader}>
            <Calendar size={24} />
            <h2>Chara Dasha (Jaimini Timing)</h2>
          </div>
          <div className={styles.cardBody}>
            <p><strong>Current:</strong> {jaiminiData.charaDasha.current} until {jaiminiData.charaDasha.currentEnd}</p>
            <p className={styles.marriageWindow}>
              <strong>Marriage window:</strong> {jaiminiData.charaDasha.marriageWindow}
            </p>
            <p><strong>Aquarius:</strong> {jaiminiData.charaDasha.aquarius}</p>
          </div>
        </div>

        <div className={styles.card}>
          <div className={styles.cardHeader}>
            <Calendar size={24} />
            <h2>Narayana Dasha</h2>
          </div>
          <div className={styles.cardBody}>
            <p><strong>Current:</strong> {jaiminiData.narayanaDasha.current} until {jaiminiData.narayanaDasha.currentEnd}</p>
            <p className={styles.marriageWindow}>
              <strong>7th house (Aquarius):</strong> {jaiminiData.narayanaDasha.marriagePeriod}
            </p>
          </div>
        </div>
      </section>

      <section className={styles.footerSection}>
        <p>
          Full analysis: <code>02-MARRIAGE-ANALYSIS/JAIMINI_MARRIAGE_ANALYSIS.md</code>
        </p>
      </section>
    </div>
  );
}
