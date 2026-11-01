import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { expect, it, vi } from 'vitest'
import ProductCard from './ProductCard.jsx'

it('shows every product field and submits the selected quantity', async () => {
  const onAddToCart = vi.fn()
  const product = {id:7,title:'Wireless Headphones',description:'Clear sound and long battery life.',category:'Electronics',rating:4.5,price:79.99,inStock:true,image:'/headphones.svg'}
  render(<ProductCard product={product} onAddToCart={onAddToCart} />)
  expect(screen.getByRole('img', {name:'Wireless Headphones'})).toBeInTheDocument()
  for (const text of ['Wireless Headphones','Clear sound and long battery life.','Electronics','$79.99','In stock']) expect(screen.getByText(text)).toBeInTheDocument()
  expect(screen.getByLabelText('Rated 4.5 out of 5')).toBeInTheDocument()
  await userEvent.click(screen.getByRole('button', {name:'Increase quantity'}))
  await userEvent.click(screen.getByRole('button', {name:'Add 2 Wireless Headphones to cart'}))
  expect(onAddToCart).toHaveBeenCalledWith(product, 2)
})
