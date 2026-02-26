'use client'

import { Sparkles } from 'lucide-react'
import styles from './Header.module.scss'

export function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.content}>
        <div className={styles.logo}>
          <div className={styles.iconWrapper}>
            <Sparkles size={24} />
          </div>
          <h1 className={styles.title}>Astro Marriage Analysis</h1>
        </div>
        <div className={styles.badge}>
          <span className={styles.badgeText}>Vedic Astrology</span>
        </div>
      </div>
    </header>
  )
}
