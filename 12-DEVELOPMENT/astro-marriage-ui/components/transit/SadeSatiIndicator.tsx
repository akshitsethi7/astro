'use client';

import { AlertCircle } from 'lucide-react';
import styles from './SadeSatiIndicator.module.scss';

export default function SadeSatiIndicator({ sadeSati }: any) {
  const getPhaseColor = (phase: string) => {
    switch (phase) {
      case 'rising': return '#f59e0b';
      case 'peak': return '#ef4444';
      case 'setting': return '#eab308';
      default: return '#8b5cf6';
    }
  };

  return (
    <div className={styles.indicator}>
      <div className={styles.header}>
        <AlertCircle size={24} color={getPhaseColor(sadeSati.phase)} />
        <h3 className={styles.title}>Sade Sati Active</h3>
        <span 
          className={styles.phase}
          style={{ 
            background: `${getPhaseColor(sadeSati.phase)}20`,
            color: getPhaseColor(sadeSati.phase)
          }}
        >
          {sadeSati.phase} phase
        </span>
      </div>
      
      <div className={styles.content}>
        <p className={styles.description}>
          Saturn is transiting through or near your natal Moon sign ({sadeSati.natalMoonSign}), 
          creating a 7.5-year period of transformation and growth.
        </p>
        
        <div className={styles.dates}>
          <div className={styles.dateItem}>
            <span className={styles.label}>Started</span>
            <span className={styles.value}>
              {sadeSati.startDate.toLocaleDateString()}
            </span>
          </div>
          <div className={styles.dateItem}>
            <span className={styles.label}>Ends</span>
            <span className={styles.value}>
              {sadeSati.endDate.toLocaleDateString()}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
