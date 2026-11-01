import { render, screen } from '@testing-library/react'
import { expect, it } from 'vitest'
import FixedJsxExample from './FixedJsxExample.jsx'

it('renders corrected JSX with a labelled learning list', () => {
  render(<FixedJsxExample />)
  expect(screen.getByRole('heading', { name: 'JSX Rules' })).toBeInTheDocument()
  expect(screen.getByRole('list', { name: 'Correct JSX examples' })).toBeInTheDocument()
})
