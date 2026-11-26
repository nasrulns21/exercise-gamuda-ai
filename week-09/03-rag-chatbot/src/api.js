export async function askDocument(question, fetcher = fetch) {
  const url = `http://localhost:8000/ask?question=${encodeURIComponent(question)}`
  const response = await fetcher(url)
  if (!response.ok) throw new Error('Unable to get an answer')
  return response.json()
}
