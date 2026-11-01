// import { useState } from 'react'
// import heroImg from './assets/hero.png'
// import reactLogo from './assets/react.svg'
// import viteLogo from './assets/vite.svg'
// import './App.css'

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <section id="center">
//         <div className="hero">
//           <img src={heroImg} className="base" width="170" height="179" alt="" />
//           <img src={reactLogo} className="framework" alt="React logo" />
//           <img src={viteLogo} className="vite" alt="Vite logo" />
//         </div>
//         <div>
//           <h1>Get started</h1>
//           <p>
//             Edit <code>src/App.jsx</code> and save to test <code>HMR</code>
//           </p>
//         </div>
//         <button
//           type="button"
//           className="counter"
//           onClick={() => setCount((count) => count + 1)}
//         >
//           Count is {count}
//         </button>
//       </section>

//       <div className="ticks"></div>

//       <section id="next-steps">
//         <div id="docs">
//           <svg className="icon" role="presentation" aria-hidden="true">
//             <use href="/icons.svg#documentation-icon"></use>
//           </svg>
//           <h2>Documentation</h2>
//           <p>Your questions, answered</p>
//           <ul>
//             <li>
//               <a href="https://vite.dev/" target="_blank">
//                 <img className="logo" src={viteLogo} alt="" />
//                 Explore Vite
//               </a>
//             </li>
//             <li>
//               <a href="https://react.dev/" target="_blank">
//                 <img className="button-icon" src={reactLogo} alt="" />
//                 Learn more
//               </a>
//             </li>
//           </ul>
//         </div>
//         <div id="social">
//           <svg className="icon" role="presentation" aria-hidden="true">
//             <use href="/icons.svg#social-icon"></use>
//           </svg>
//           <h2>Connect with us</h2>
//           <p>Join the Vite community</p>
//           <ul>
//             <li>
//               <a href="https://github.com/vitejs/vite" target="_blank">
//                 <svg
//                   className="button-icon"
//                   role="presentation"
//                   aria-hidden="true"
//                 >
//                   <use href="/icons.svg#github-icon"></use>
//                 </svg>
//                 GitHub
//               </a>
//             </li>
//             <li>
//               <a href="https://chat.vite.dev/" target="_blank">
//                 <svg
//                   className="button-icon"
//                   role="presentation"
//                   aria-hidden="true"
//                 >
//                   <use href="/icons.svg#discord-icon"></use>
//                 </svg>
//                 Discord
//               </a>
//             </li>
//             <li>
//               <a href="https://x.com/vite_js" target="_blank">
//                 <svg
//                   className="button-icon"
//                   role="presentation"
//                   aria-hidden="true"
//                 >
//                   <use href="/icons.svg#x-icon"></use>
//                 </svg>
//                 X.com
//               </a>
//             </li>
//             <li>
//               <a href="https://bsky.app/profile/vite.dev" target="_blank">
//                 <svg
//                   className="button-icon"
//                   role="presentation"
//                   aria-hidden="true"
//                 >
//                   <use href="/icons.svg#bluesky-icon"></use>
//                 </svg>
//                 Bluesky
//               </a>
//             </li>
//           </ul>
//         </div>
//       </section>

//       <div className="ticks"></div>
//       <section id="spacer"></section>
//     </>
//   )
// }

// export default App



import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [inputLanguage, setInputLanguage] = useState("English");
  const [outputLanguage, setOutputLanguage] = useState("German");
  const [textInput, setTextInput] = useState("");
  const [translatedText, setTranslatedText] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const languages = [
    "English",
    "Malay",
    "German",
    "French",
    "Spanish",
    "Chinese",
    "Japanese",
    "Korean",
    "Arabic",
    "Indonesian",
  ];

  const handleTranslate = async () => {
    if (!textInput.trim()) {
      setError("Please enter text to translate.");
      return;
    }

    setLoading(true);
    setError("");
    setTranslatedText("");

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/translate",
        {
          input_language: inputLanguage,
          output_language: outputLanguage,
          text_input: textInput,
        }
      );

      setTranslatedText(response.data.translated_text);
    } catch (err) {
      setError(
        err.response?.data?.detail ||
        "Translation failed. Please check the backend."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <div className="translator-card">
        <div className="header">
          <div className="logo">T</div>
          <h1>AI Text Translator</h1>
          <p>Translate smarter with Gemini AI</p>
        </div>

        <div className="language-row">
          <div className="field">
            <label>Input Language</label>
            <select
              value={inputLanguage}
              onChange={(e) => setInputLanguage(e.target.value)}
            >
              {languages.map((lang) => (
                <option key={lang}>{lang}</option>
              ))}
            </select>
          </div>

          <button
            className="swap-button"
            onClick={() => {
              setInputLanguage(outputLanguage);
              setOutputLanguage(inputLanguage);
              setTextInput(translatedText);
              setTranslatedText("");
              setError("");
            }}
            title="Swap languages"
          >
            ⇄
          </button>

          <div className="field">
            <label>Output Language</label>
            <select
              value={outputLanguage}
              onChange={(e) => setOutputLanguage(e.target.value)}
            >
              {languages.map((lang) => (
                <option key={lang}>{lang}</option>
              ))}
            </select>
          </div>
        </div>

        <div className="text-row">
          <div className="field">
            <label>Enter Text</label>
            <textarea
              placeholder="Type something to translate..."
              value={textInput}
              onChange={(e) => setTextInput(e.target.value)}
            />
          </div>

          <div className="field">
            <label>Translation</label>
            <textarea
              placeholder="Your translation will appear here..."
              value={translatedText}
              readOnly
            />
          </div>
        </div>

        {error && <p className="error">{error}</p>}

        <button
          className="translate-button"
          onClick={handleTranslate}
          disabled={loading}
        >
          {loading ? "Translating..." : "Translate Text"}
        </button>

        <p className="footer">
          Powered by FastAPI + Gemini AI
        </p>
      </div>
    </div>
  );
}

export default App;
