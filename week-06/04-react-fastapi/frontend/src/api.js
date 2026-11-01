export async function loadBooks(fetcher = fetch) {
  const response = await fetcher('http://localhost:8000/books')
  if (!response.ok) throw new Error('Unable to load books')
  return response.json()
}
