'use client'

import { useState, useEffect } from 'react'
import { Calendar, Sun, Moon, Clock, Star } from 'lucide-react'
import styles from './page.module.scss'

interface PanchangData {
  date: Date
  tithi: string
  nakshatra: string
  yoga: string
  karana: string
  sunrise: string
  sunset: string
  moonrise: string
  moonset: string
  rahukaal: string
  yamaganda: string
  gulika: string
  abhijit: string
  durmuhurtam: string[]
  shubhaMuhurta: string[]
}

export default function PanchangPage() {
  const [selectedDate, setSelectedDate] = useState(new Date())
  const [location, setLocation] = useState({ lat: 28.6139, lon: 77.2090, name: 'New Delhi' })
  const [panchangData, setPanchangData] = useState<PanchangData | null>(null)

  useEffect(() => {
    calculatePanchang()
  }, [selectedDate, location])

  const calculatePanchang = () => {
    // Mock data - replace with actual calculations
    const data: PanchangData = {
      date: selectedDate,
      tithi: 'Shukla Paksha Saptami (7th day)',
      nakshatra: 'Rohini',
      yoga: 'Siddha',
      karana: 'Bava',
      sunrise: '06:45 AM',
      sunset: '06:30 PM',
      moonrise: '08:15 AM',
      moonset: '09:45 PM',
      rahukaal: '03:00 PM - 04:30 PM',
      yamaganda: '09:00 AM - 10:30 AM',
      gulika: '12:00 PM - 01:30 PM',
      abhijit: '12:00 PM - 12:48 PM',
      durmuhurtam: ['06:45 AM - 07:33 AM', '03:00 PM - 03:48 PM'],
      shubhaMuhurta: ['08:00 AM - 09:30 AM', '10:30 AM - 12:00 PM', '02:00 PM - 03:30 PM'],
    }
    
    setPanchangData(data)
  }

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1>Panchang</h1>
        <p>Daily Vedic calendar and auspicious timings</p>
      </div>

      <div className={styles.controls}>
        <div className={styles.dateSelector}>
          <Calendar size={20} />
          <input
            type="date"
            value={selectedDate.toISOString().split('T')[0]}
            onChange={(e) => setSelectedDate(new Date(e.target.value))}
            className={styles.dateInput}
          />
        </div>
        
        <div className={styles.locationSelector}>
          <input
            type="text"
            value={location.name}
            onChange={(e) => setLocation({ ...location, name: e.target.value })}
            className={styles.locationInput}
            placeholder="Enter location"
          />
        </div>
      </div>

      {panchangData && (
        <>
          <div className={styles.mainGrid}>
            <div className={styles.card}>
              <div className={styles.cardHeader}>
                <Star size={20} />
                <h3>Panchang Elements</h3>
              </div>
              <div className={styles.elementsList}>
                <div className={styles.element}>
                  <span className={styles.label}>Tithi</span>
                  <span className={styles.value}>{panchangData.tithi}</span>
                </div>
                <div className={styles.element}>
                  <span className={styles.label}>Nakshatra</span>
                  <span className={styles.value}>{panchangData.nakshatra}</span>
                </div>
                <div className={styles.element}>
                  <span className={styles.label}>Yoga</span>
                  <span className={styles.value}>{panchangData.yoga}</span>
                </div>
                <div className={styles.element}>
                  <span className={styles.label}>Karana</span>
                  <span className={styles.value}>{panchangData.karana}</span>
                </div>
              </div>
            </div>

            <div className={styles.card}>
              <div className={styles.cardHeader}>
                <Sun size={20} />
                <h3>Sun & Moon</h3>
              </div>
              <div className={styles.elementsList}>
                <div className={styles.element}>
                  <span className={styles.label}>Sunrise</span>
                  <span className={styles.value}>{panchangData.sunrise}</span>
                </div>
                <div className={styles.element}>
                  <span className={styles.label}>Sunset</span>
                  <span className={styles.value}>{panchangData.sunset}</span>
                </div>
                <div className={styles.element}>
                  <span className={styles.label}>Moonrise</span>
                  <span className={styles.value}>{panchangData.moonrise}</span>
                </div>
                <div className={styles.element}>
                  <span className={styles.label}>Moonset</span>
                  <span className={styles.value}>{panchangData.moonset}</span>
                </div>
              </div>
            </div>
          </div>

          <div className={styles.timingsGrid}>
            <div className={styles.card}>
              <div className={styles.cardHeader}>
                <Clock size={20} />
                <h3>Inauspicious Timings</h3>
              </div>
              <div className={styles.timingsList}>
                <div className={styles.timing}>
                  <span className={styles.timingLabel}>Rahu Kaal</span>
                  <span className={styles.timingValue}>{panchangData.rahukaal}</span>
                </div>
                <div className={styles.timing}>
                  <span className={styles.timingLabel}>Yamaganda</span>
                  <span className={styles.timingValue}>{panchangData.yamaganda}</span>
                </div>
                <div className={styles.timing}>
                  <span className={styles.timingLabel}>Gulika</span>
                  <span className={styles.timingValue}>{panchangData.gulika}</span>
                </div>
                <div className={styles.timing}>
                  <span className={styles.timingLabel}>Durmuhurtam</span>
                  <div className={styles.multipleTimings}>
                    {panchangData.durmuhurtam.map((time, i) => (
                      <span key={i} className={styles.timingValue}>{time}</span>
                    ))}
                  </div>
                </div>
              </div>
            </div>

            <div className={styles.card}>
              <div className={styles.cardHeader}>
                <Star size={20} />
                <h3>Auspicious Timings</h3>
              </div>
              <div className={styles.timingsList}>
                <div className={styles.timing}>
                  <span className={styles.timingLabel}>Abhijit Muhurta</span>
                  <span className={styles.timingValue}>{panchangData.abhijit}</span>
                </div>
                <div className={styles.timing}>
                  <span className={styles.timingLabel}>Shubha Muhurta</span>
                  <div className={styles.multipleTimings}>
                    {panchangData.shubhaMuhurta.map((time, i) => (
                      <span key={i} className={styles.timingValue}>{time}</span>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </>
      )}
    </div>
  )
}
