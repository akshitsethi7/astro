'use client'

import { useState } from 'react'
import { Calendar, Clock, Star, Heart, Briefcase, Home, Plane } from 'lucide-react'
import styles from './page.module.scss'

interface MuhurataResult {
  date: Date
  time: string
  score: number
  factors: {
    tithi: string
    nakshatra: string
    yoga: string
    karana: string
  }
  suitability: string
}

const eventTypes = [
  { id: 'marriage', label: 'Marriage', icon: Heart },
  { id: 'business', label: 'Business Start', icon: Briefcase },
  { id: 'housewarming', label: 'Housewarming', icon: Home },
  { id: 'travel', label: 'Travel', icon: Plane },
  { id: 'education', label: 'Education', icon: Star },
]

export default function MuhurataPage() {
  const [selectedEvent, setSelectedEvent] = useState('marriage')
  const [startDate, setStartDate] = useState(new Date())
  const [endDate, setEndDate] = useState(new Date(Date.now() + 30 * 24 * 60 * 60 * 1000))
  const [results, setResults] = useState<MuhurataResult[]>([])

  const calculateMuhurata = () => {
    // Mock data - replace with actual calculations
    const mockResults: MuhurataResult[] = [
      {
        date: new Date(2026, 2, 15),
        time: '10:30 AM - 12:00 PM',
        score: 95,
        factors: {
          tithi: 'Shukla Paksha Panchami',
          nakshatra: 'Rohini',
          yoga: 'Siddha',
          karana: 'Bava',
        },
        suitability: 'Excellent',
      },
      {
        date: new Date(2026, 2, 18),
        time: '09:00 AM - 10:30 AM',
        score: 88,
        factors: {
          tithi: 'Shukla Paksha Ashtami',
          nakshatra: 'Pushya',
          yoga: 'Amrita',
          karana: 'Balava',
        },
        suitability: 'Very Good',
      },
      {
        date: new Date(2026, 2, 22),
        time: '11:00 AM - 12:30 PM',
        score: 82,
        factors: {
          tithi: 'Shukla Paksha Dwadashi',
          nakshatra: 'Uttara Phalguni',
          yoga: 'Brahma',
          karana: 'Kaulava',
        },
        suitability: 'Good',
      },
    ]
    
    setResults(mockResults)
  }

  const getScoreColor = (score: number) => {
    if (score >= 90) return '#10b981'
    if (score >= 80) return '#3b82f6'
    if (score >= 70) return '#f59e0b'
    return '#ef4444'
  }

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1>Muhurata</h1>
        <p>Find auspicious timings for important events</p>
      </div>

      <div className={styles.selectionSection}>
        <div className={styles.card}>
          <h3>Select Event Type</h3>
          <div className={styles.eventGrid}>
            {eventTypes.map((event) => {
              const Icon = event.icon
              return (
                <button
                  key={event.id}
                  className={`${styles.eventButton} ${selectedEvent === event.id ? styles.active : ''}`}
                  onClick={() => setSelectedEvent(event.id)}
                >
                  <Icon size={24} />
                  <span>{event.label}</span>
                </button>
              )
            })}
          </div>
        </div>

        <div className={styles.card}>
          <h3>Date Range</h3>
          <div className={styles.dateRange}>
            <div className={styles.dateInput}>
              <label>Start Date</label>
              <input
                type="date"
                value={startDate.toISOString().split('T')[0]}
                onChange={(e) => setStartDate(new Date(e.target.value))}
              />
            </div>
            <div className={styles.dateInput}>
              <label>End Date</label>
              <input
                type="date"
                value={endDate.toISOString().split('T')[0]}
                onChange={(e) => setEndDate(new Date(e.target.value))}
              />
            </div>
          </div>
          <button className={styles.calculateButton} onClick={calculateMuhurata}>
            Find Auspicious Times
          </button>
        </div>
      </div>

      {results.length > 0 && (
        <div className={styles.resultsSection}>
          <h2>Recommended Muhurata</h2>
          <div className={styles.resultsList}>
            {results.map((result, index) => (
              <div key={index} className={styles.resultCard}>
                <div className={styles.resultHeader}>
                  <div className={styles.dateInfo}>
                    <Calendar size={20} />
                    <div>
                      <div className={styles.date}>
                        {result.date.toLocaleDateString('en-US', { 
                          weekday: 'long', 
                          year: 'numeric', 
                          month: 'long', 
                          day: 'numeric' 
                        })}
                      </div>
                      <div className={styles.time}>
                        <Clock size={16} />
                        {result.time}
                      </div>
                    </div>
                  </div>
                  <div className={styles.scoreSection}>
                    <div 
                      className={styles.score}
                      style={{ color: getScoreColor(result.score) }}
                    >
                      {result.score}
                    </div>
                    <div className={styles.suitability}>{result.suitability}</div>
                  </div>
                </div>

                <div className={styles.factors}>
                  <div className={styles.factor}>
                    <span className={styles.factorLabel}>Tithi</span>
                    <span className={styles.factorValue}>{result.factors.tithi}</span>
                  </div>
                  <div className={styles.factor}>
                    <span className={styles.factorLabel}>Nakshatra</span>
                    <span className={styles.factorValue}>{result.factors.nakshatra}</span>
                  </div>
                  <div className={styles.factor}>
                    <span className={styles.factorLabel}>Yoga</span>
                    <span className={styles.factorValue}>{result.factors.yoga}</span>
                  </div>
                  <div className={styles.factor}>
                    <span className={styles.factorLabel}>Karana</span>
                    <span className={styles.factorValue}>{result.factors.karana}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
