import { render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import PersonalInfo from './PersonalInfo.jsx'

describe('PersonalInfo', () => {
  it('renders accessible personal details, three hobbies, and current time', () => {
    render(<PersonalInfo now={new Date('2026-10-30T10:15:00+08:00')} />)
    expect(screen.getByRole('heading', { name: 'Nasrul Sharuddin' })).toBeInTheDocument()
    expect(screen.getByText('nasrul@example.com')).toBeInTheDocument()
    expect(screen.getByRole('img', { name: /Nasrul Sharuddin profile/i })).toBeInTheDocument()
    expect(screen.getAllByRole('listitem')).toHaveLength(3)
    expect(screen.getByText(/30 October 2026/)).toBeInTheDocument()
    expect(screen.getByText(/10:15/)).toBeInTheDocument()
  })
})
