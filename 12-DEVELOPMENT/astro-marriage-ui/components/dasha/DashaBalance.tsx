'use client';

import { useEffect, useState } from 'react';
import styles from './DashaBalance.module.scss';

interface DashaBalanceProps {
  startDate: Date;
  endDate: Date;
  currentDate: Date;
}

export default function DashaBalance({ startDate, endDate, currentDate }: DashaBalanceProps) {
  const [progress, setProgress] = useState(0);
  const [remaining, setRemaining] = useState({ years: 0, months: 0, days: 0 });

  useEffect(() => {
    const total = endDate.getTime() - startDate.getTime();
    const elapsed = currentDate.getTime() - startDate.getTime();
    const percent = Math.max(0, Math.min(100, (elapsed / total) * 100));
    setProgress(percent);

    // Calculate remaining time
    const remainingMs = endDate.getTime() - currentDate.getTime();
    const remainingDays = Math.max(0, Math.ceil(remainingMs / (1000 * 60 * 60 * 24)));
    
    const years = Math.floor(remainingDays / 365);
    const months = Math.floor((remainingDays % 365) / 30);
    const days = remainingDays % 30;
    
    setRemaining({ years, months, days });
  }, [startDate, endDate, currentDate]);

  return (
    <div className={styles.dashaBalance}>
      <div className={styles.progressBar}>
        <div 
          className={styles.progressFill} 
          style={{ width: `${progress}%` }}
        />
      </div>
      
      <div className={styles.stats}>
        <div className={styles.statItem}>
          <span className={styles.statValue}>{progress.toFixed(1)}%</span>
          <span className={styles.statLabel}>Complete</span>
        </div>
        
        <div className={styles.remaining}>
          {remaining.years > 0 && (
            <span className={styles.timeUnit}>
              {remaining.years}y
            </span>
          )}
          {remaining.months > 0 && (
            <span className={styles.timeUnit}>
              {remaining.months}m
            </span>
          )}
          <span className={styles.timeUnit}>
            {remaining.days}d
          </span>
          <span className={styles.remainingLabel}>remaining</span>
        </div>
      </div>
    </div>
  );
}
