'use client'

import { useState } from 'react'
import { Calendar, Heart, Star, TrendingUp, User, BookOpen } from 'lucide-react'
import styles from './Dashboard.module.scss'

interface Tab {
  id: string
  label: string
  icon: React.ReactNode
}

const tabs: Tab[] = [
  { id: 'overview', label: 'Overview', icon: <Star size={18} /> },
  { id: 'chart', label: 'Birth Chart', icon: <TrendingUp size={18} /> },
  { id: 'marriage', label: 'Marriage', icon: <Heart size={18} /> },
  { id: 'timing', label: 'Timing', icon: <Calendar size={18} /> },
  { id: 'spouse', label: 'Spouse', icon: <User size={18} /> },
  { id: 'analysis', label: 'Analysis', icon: <BookOpen size={18} /> },
]

interface DashboardProps {
  children: React.ReactNode
}

export function Dashboard({ children }: DashboardProps) {
  const [activeTab, setActiveTab] = useState('overview')

  return (
    <div className={styles.dashboard}>
      <div className={styles.tabs}>
        <div className={styles.tabsInner}>
          {tabs.map((tab) => (
            <button
              key={tab.id}
              className={`${styles.tab} ${activeTab === tab.id ? styles.active : ''}`}
              onClick={() => setActiveTab(tab.id)}
            >
              <span className={styles.tabIcon}>{tab.icon}</span>
              <span className={styles.tabLabel}>{tab.label}</span>
            </button>
          ))}
        </div>
      </div>
      
      <div className={styles.content}>
        {children}
      </div>
    </div>
  )
}
