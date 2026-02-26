'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { Home, Calendar, Users, Clock, Moon, Activity, BookOpen } from 'lucide-react'
import styles from './Navigation.module.scss'

const navItems = [
  { href: '/', label: 'Dashboard', icon: Home },
  { href: '/chart', label: 'Birth Chart', icon: BookOpen },
  { href: '/dasha', label: 'Dasha', icon: Clock },
  { href: '/transits', label: 'Transits', icon: Activity },
  { href: '/shadows', label: 'Shadows', icon: Moon },
  { href: '/panchang', label: 'Panchang', icon: Calendar },
  { href: '/muhurata', label: 'Muhurata', icon: Clock },
  { href: '/compatibility', label: 'Compatibility', icon: Users },
]

export function Navigation() {
  const pathname = usePathname()

  return (
    <nav className={styles.navigation}>
      <div className={styles.navContainer}>
        <div className={styles.logo}>
          <span className={styles.logoIcon}>🪐</span>
          <span className={styles.logoText}>Lagna360</span>
        </div>
        
        <div className={styles.navLinks}>
          {navItems.map((item) => {
            const Icon = item.icon
            const isActive = pathname === item.href
            
            return (
              <Link
                key={item.href}
                href={item.href}
                className={`${styles.navLink} ${isActive ? styles.active : ''}`}
              >
                <Icon size={18} />
                <span>{item.label}</span>
              </Link>
            )
          })}
        </div>
      </div>
    </nav>
  )
}
