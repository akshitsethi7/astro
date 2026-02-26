'use client'

import styles from './StatsCard.module.scss'

interface StatsCardProps {
  label: string
  value: string
  gradient: string
}

export function StatsCard({ label, value, gradient }: StatsCardProps) {
  return (
    <div className={styles.card}>
      <div 
        className={styles.gradient}
        style={{ background: gradient }}
      />
      <div className={styles.content}>
        <div className={styles.label}>{label}</div>
        <div className={styles.value}>{value}</div>
      </div>
    </div>
  )
}
