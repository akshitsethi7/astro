'use client'

import { useState } from 'react'
import { FileText, ChevronRight, Menu, X } from 'lucide-react'
import styles from './Sidebar.module.scss'

interface MarriageFile {
  slug: string
  title: string
  order: number
}

interface SidebarProps {
  files: MarriageFile[]
}

export function Sidebar({ files }: SidebarProps) {
  const [activeFile, setActiveFile] = useState(files[0]?.slug || '')
  const [isOpen, setIsOpen] = useState(false)

  const handleFileClick = (slug: string) => {
    setActiveFile(slug)
    setIsOpen(false)
    
    // Scroll to section
    const element = document.getElementById(slug)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }

  return (
    <>
      <button 
        className={styles.mobileToggle}
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Toggle menu"
      >
        {isOpen ? <X size={24} /> : <Menu size={24} />}
      </button>
      
      <aside className={`${styles.sidebar} ${isOpen ? styles.open : ''}`}>
        <div className={styles.sidebarContent}>
          <div className={styles.sidebarHeader}>
            <h2 className={styles.sidebarTitle}>Contents</h2>
            <span className={styles.fileCount}>{files.length} files</span>
          </div>
          
          <nav className={styles.nav}>
            {files.map((file) => (
              <button
                key={file.slug}
                className={`${styles.navItem} ${activeFile === file.slug ? styles.active : ''}`}
                onClick={() => handleFileClick(file.slug)}
              >
                <FileText size={16} className={styles.icon} />
                <span className={styles.navText}>{file.title}</span>
                <ChevronRight size={16} className={styles.chevron} />
              </button>
            ))}
          </nav>
        </div>
      </aside>
      
      {isOpen && (
        <div 
          className={styles.overlay}
          onClick={() => setIsOpen(false)}
        />
      )}
    </>
  )
}
