'use client'

import { marked } from 'marked'
import styles from './ContentViewer.module.scss'
import { OverviewDashboard } from './OverviewDashboard'

interface MarriageFile {
  slug: string
  title: string
  content: string
  order: number
}

interface ContentViewerProps {
  files: MarriageFile[]
}

export function ContentViewer({ files }: ContentViewerProps) {
  const renderContent = (content: string) => {
    const html = marked(content, { 
      breaks: true,
      gfm: true 
    })
    return { __html: html as string }
  }

  return (
    <main className={styles.content}>
      <div className={styles.contentInner}>
        {/* Overview Dashboard */}
        <OverviewDashboard />

        {/* Content Sections */}
        {files.map((file) => (
          <section 
            key={file.slug} 
            id={file.slug}
            className={styles.section}
          >
            <div className={styles.sectionHeader}>
              <h2 className={styles.sectionTitle}>{file.title}</h2>
              <span className={styles.sectionBadge}>{file.slug}</span>
            </div>
            <div 
              className={styles.markdown}
              dangerouslySetInnerHTML={renderContent(file.content)}
            />
          </section>
        ))}
      </div>
    </main>
  )
}
