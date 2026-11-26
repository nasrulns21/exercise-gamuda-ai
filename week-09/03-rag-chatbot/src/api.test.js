import { describe, expect, it, vi } from 'vitest'
import { askDocument } from './api'

describe('RAG API client', () => {
  it('encodes the question and returns the answer', async () => {
    const fetcher = vi.fn().mockResolvedValue({ ok: true, json: async () => ({ answer: 'From the PDF', sources: [2] }) })
    await expect(askDocument('What is diabetes?', fetcher)).resolves.toMatchObject({ sources: [2] })
    expect(fetcher.mock.calls[0][0]).toContain('What%20is%20diabetes%3F')
  })

  it('shows a useful error for failed requests', async () => {
    await expect(askDocument('Question', async () => ({ ok: false }))).rejects.toThrow('Unable to get an answer')
  })
})
