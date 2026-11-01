import React from 'react'
import { createRoot } from 'react-dom/client'
import PersonalInfo from './components/PersonalInfo.jsx'
import FixedJsxExample from './components/FixedJsxExample.jsx'
import './styles.css'

createRoot(document.getElementById('root')).render(<main><PersonalInfo/><FixedJsxExample/></main>)
