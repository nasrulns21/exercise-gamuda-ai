import { describe, expect, it, vi } from 'vitest'
import { loadBooks } from './api'

describe('book API client', () => {
  it('returns books', async () => {
    const fetcher = vi.fn().mockResolvedValue({ ok: true, json: async () => [{ id: 1, category: 'technology' }] })
    await expect(loadBooks(fetcher)).resolves.toHaveLength(1)
  })
  it('reports API errors', async () => {
    await expect(loadBooks(async () => ({ ok: false }))).rejects.toThrow('Unable to load books')
  })
})
