'use client';

import { Star, TrendingUp, Calendar, AlertCircle } from 'lucide-react';
import styles from './DashaPeriodCard.module.scss';

interface DashaPeriodCardProps {
  period: {
    planet: string;
    startDate: Date;
    endDate: Date;
    strength?: number;
    favorability?: string;
    predictions?: string[];
  };
}

export default function DashaPeriodCard({ period }: DashaPeriodCardProps) {
  const strength = period.strength || 50;
  const favorability = period.favorability || 'neutral';
  
  const getFavorabilityColor = (fav: string) => {
    switch (fav) {
      case 'excellent': return '#22c55e';
      case 'good': return '#10b981';
      case 'neutral': return '#8b5cf6';
      case 'challenging': return '#f59e0b';
      case 'difficult': return '#ef4444';
      default: return '#8b5cf6';
    }
  };

  return (
    <div className={styles.periodCard}>
      <div className={styles.header}>
        <div className={styles.planetInfo}>
          <h3 className={styles.planet}>{period.planet}</h3>
          <div className={styles.dates}>
            <Calendar size={14} />
            {period.startDate.toLocaleDateString()} - {period.endDate.toLocaleDateString()}
          </div>
        </div>
        
        <div className={styles.strengthBadge} style={{ borderColor: getFavorabilityColor(favorability) }}>
          <Star size={16} fill={getFavorabilityColor(favorability)} color={getFavorabilityColor(favorability)} />
          <span>{strength}/100</span>
        </div>
      </div>

      <div className={styles.favorability}>
        <div className={styles.favorabilityLabel}>Favorability</div>
        <div 
          className={styles.favorabilityValue}
          style={{ color: getFavorabilityColor(favorability) }}
        >
          {favorability.charAt(0).toUpperCase() + favorability.slice(1)}
        </div>
      </div>

      <div className={styles.strengthBar}>
        <div className={styles.strengthLabel}>
          <TrendingUp size={14} />
          Planetary Strength
        </div>
        <div className={styles.bar}>
          <div 
            className={styles.barFill}
            style={{ 
              width: `${strength}%`,
              background: `linear-gradient(90deg, ${getFavorabilityColor(favorability)}, ${getFavorabilityColor(favorability)}dd)`
            }}
          />
        </div>
      </div>

      {period.predictions && period.predictions.length > 0 && (
        <div className={styles.predictions}>
          <div className={styles.predictionsHeader}>
            <AlertCircle size={16} />
            Key Predictions
          </div>
          <ul className={styles.predictionsList}>
            {period.predictions.map((prediction, index) => (
              <li key={index} className={styles.predictionItem}>
                {prediction}
              </li>
            ))}
          </ul>
        </div>
      )}

      <div className={styles.actions}>
        <button className={styles.actionBtn}>View Details</button>
        <button className={styles.actionBtn}>Export Report</button>
      </div>
    </div>
  );
}
