import { render, screen, within } from '@testing-library/react'
import { expect, it } from 'vitest'
import UserDashboard from './UserDashboard.jsx'

it('composes labelled header, navigation, profile, statistics, and activity regions', () => {
  render(<UserDashboard />)
  expect(screen.getByRole('banner')).toBeInTheDocument()
  expect(screen.getByRole('navigation', {name:'Dashboard navigation'})).toBeInTheDocument()
  expect(screen.getByRole('region', {name:'Profile summary'})).toBeInTheDocument()
  const stats = screen.getByRole('region', {name:'Statistics'})
  expect(within(stats).getAllByRole('listitem')).toHaveLength(3)
  expect(screen.getByRole('region', {name:'Recent activity'})).toBeInTheDocument()
})
