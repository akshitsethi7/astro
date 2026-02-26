'use client'

import { LucideIcon } from 'lucide-react'
import styles from './InfoCard.module.scss'

interface InfoCardProps {
  title: string
  value: string | number
  subtitle?: string
  icon?: LucideIcon
  gradient?: string
  trend?: 'up' | 'down' | 'neutral'
  trendValue?: string
}

export function InfoCard({ 
  title, 
  value, 
  subtitle, 
  icon: Icon, 
  gradient = 'var(--gradient-primary)',
  trend,
  trendValue 
}: InfoCardProps) {
  return (
    <div className={styles.card}>
      <div 
        className={styles.gradient}
        style={{ background: gradient }}
      />
      
      <div className={styles.content}>
        <div className={styles.header}>
          <span className={styles.title}>{title}</span>
          {Icon && (
            <div className={styles.iconWrapper}>
              <Icon size={20} />
            </div>
          )}
        </div>
        
        <div className={styles.value}>{value}</div>
        
        {subtitle && (
          <div className={styles.subtitle}>{subtitle}</div>
        )}
        
        {trend && trendValue && (
          <div className={`${styles.trend} ${styles[trend]}`}>
            <span className={styles.trendIndicator}>
              {trend === 'up' ? '↑' : trend === 'down' ? '↓' : '→'}
            </span>
            <span className={styles.trendValue}>{trendValue}</span>
          </div>
        )}
      </div>
    </div>
  )
}
