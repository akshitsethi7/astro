import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'

const marriageDirectory = path.join(process.cwd(), '..', 'marriage')

export interface MarriageFile {
  slug: string
  title: string
  content: string
  order: number
}

export async function getMarriageFiles(): Promise<MarriageFile[]> {
  try {
    const fileNames = fs.readdirSync(marriageDirectory)
    const markdownFiles = fileNames.filter(name => name.endsWith('.md'))

    const files = markdownFiles.map(fileName => {
      const slug = fileName.replace(/\.md$/, '')
      const fullPath = path.join(marriageDirectory, fileName)
      const fileContents = fs.readFileSync(fullPath, 'utf8')
      const { data, content } = matter(fileContents)

      // Extract title from first heading or use filename
      const titleMatch = content.match(/^#\s+(.+)$/m)
      const title = titleMatch ? titleMatch[1] : formatTitle(slug)

      // Determine order based on filename prefix
      const orderMatch = slug.match(/^(\d+)/)
      const order = orderMatch ? parseInt(orderMatch[1]) : 999

      return {
        slug,
        title,
        content,
        order,
      }
    })

    // Sort by order
    return files.sort((a, b) => a.order - b.order)
  } catch (error) {
    console.error('Error reading marriage files:', error)
    return []
  }
}

function formatTitle(slug: string): string {
  return slug
    .replace(/^\d+-/, '') // Remove number prefix
    .split('-')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ')
}
