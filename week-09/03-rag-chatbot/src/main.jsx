import React, { useState } from 'react'
import { createRoot } from 'react-dom/client'
import { askDocument } from './api'
import './styles.css'

function App() {
  const [question, setQuestion] = useState('')
  const [messages, setMessages] = useState([])
  const [busy, setBusy] = useState(false)

  async function submit(event) {
    event.preventDefault()
    const text = question.trim()
    if (!text || busy) return
    setMessages(current => [...current, { role: 'user', text }])
    setQuestion('')
    setBusy(true)
    try {
      const result = await askDocument(text)
      const pages = result.sources.length ? `Pages: ${result.sources.join(', ')}` : 'No page reference'
      setMessages(current => [...current, { role: 'assistant', text: result.answer, pages }])
    } catch (error) {
      setMessages(current => [...current, { role: 'error', text: error.message }])
    } finally {
      setBusy(false)
    }
  }

  return <main>
    <header><p>Week 9 · RAG Exercise</p><h1>Diabetes PDF Assistant</h1><p>Ask a question and check the source pages.</p></header>
    <section className="messages" aria-live="polite">
      {messages.length === 0 && <p className="empty">No questions yet.</p>}
      {messages.map((message, index) => <article className={message.role} key={index}>
        <strong>{message.role === 'user' ? 'You' : message.role === 'error' ? 'Error' : 'Assistant'}</strong>
        <p>{message.text}</p>{message.pages && <small>{message.pages}</small>}
      </article>)}
      {busy && <p>Searching the document…</p>}
    </section>
    <form onSubmit={submit}><label htmlFor="question">Question</label><div><input id="question" value={question} onChange={event => setQuestion(event.target.value)} placeholder="What are the symptoms of diabetes?" required/><button disabled={busy}>Ask</button></div></form>
  </main>
}

createRoot(document.getElementById('root')).render(<App />)
