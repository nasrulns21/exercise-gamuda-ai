import { useEffect, useState } from 'react'
import { loadBooks } from './api'
import './styles.css'

export function BookCard({ book }) {
  return <article><h2>{book.title}</h2><p>{book.author}</p><span>{book.category}</span></article>
}

export default function App() {
  const [books, setBooks] = useState([])
  const [error, setError] = useState('')
  useEffect(() => { loadBooks().then(setBooks).catch(e => setError(e.message)) }, [])
  return <main><header><p>Week 6 full-stack exercise</p><h1>Book Manager</h1></header>{error && <p role="alert">{error}</p>}<section aria-label="Books">{books.map(book => <BookCard key={book.id} book={book} />)}</section></main>
}
