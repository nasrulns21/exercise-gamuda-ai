// // import { useState } from 'react'
// // import heroImg from './assets/hero.png'
// // import reactLogo from './assets/react.svg'
// // import viteLogo from './assets/vite.svg'
// // import './App.css'

// // function App() {
// //   const [count, setCount] = useState(0)

// //   return (
// //     <>
// //       <section id="center">
// //         <div className="hero">
// //           <img src={heroImg} className="base" width="170" height="179" alt="" />
// //           <img src={reactLogo} className="framework" alt="React logo" />
// //           <img src={viteLogo} className="vite" alt="Vite logo" />
// //         </div>
// //         <div>
// //           <h1>Get started</h1>
// //           <p>
// //             Edit <code>src/App.jsx</code> and save to test <code>HMR</code>
// //           </p>
// //         </div>
// //         <button
// //           type="button"
// //           className="counter"
// //           onClick={() => setCount((count) => count + 1)}
// //         >
// //           Count is {count}
// //         </button>
// //       </section>

// //       <div className="ticks"></div>

// //       <section id="next-steps">
// //         <div id="docs">
// //           <svg className="icon" role="presentation" aria-hidden="true">
// //             <use href="/icons.svg#documentation-icon"></use>
// //           </svg>
// //           <h2>Documentation</h2>
// //           <p>Your questions, answered</p>
// //           <ul>
// //             <li>
// //               <a href="https://vite.dev/" target="_blank">
// //                 <img className="logo" src={viteLogo} alt="" />
// //                 Explore Vite
// //               </a>
// //             </li>
// //             <li>
// //               <a href="https://react.dev/" target="_blank">
// //                 <img className="button-icon" src={reactLogo} alt="" />
// //                 Learn more
// //               </a>
// //             </li>
// //           </ul>
// //         </div>
// //         <div id="social">
// //           <svg className="icon" role="presentation" aria-hidden="true">
// //             <use href="/icons.svg#social-icon"></use>
// //           </svg>
// //           <h2>Connect with us</h2>
// //           <p>Join the Vite community</p>
// //           <ul>
// //             <li>
// //               <a href="https://github.com/vitejs/vite" target="_blank">
// //                 <svg
// //                   className="button-icon"
// //                   role="presentation"
// //                   aria-hidden="true"
// //                 >
// //                   <use href="/icons.svg#github-icon"></use>
// //                 </svg>
// //                 GitHub
// //               </a>
// //             </li>
// //             <li>
// //               <a href="https://chat.vite.dev/" target="_blank">
// //                 <svg
// //                   className="button-icon"
// //                   role="presentation"
// //                   aria-hidden="true"
// //                 >
// //                   <use href="/icons.svg#discord-icon"></use>
// //                 </svg>
// //                 Discord
// //               </a>
// //             </li>
// //             <li>
// //               <a href="https://x.com/vite_js" target="_blank">
// //                 <svg
// //                   className="button-icon"
// //                   role="presentation"
// //                   aria-hidden="true"
// //                 >
// //                   <use href="/icons.svg#x-icon"></use>
// //                 </svg>
// //                 X.com
// //               </a>
// //             </li>
// //             <li>
// //               <a href="https://bsky.app/profile/vite.dev" target="_blank">
// //                 <svg
// //                   className="button-icon"
// //                   role="presentation"
// //                   aria-hidden="true"
// //                 >
// //                   <use href="/icons.svg#bluesky-icon"></use>
// //                 </svg>
// //                 Bluesky
// //               </a>
// //             </li>
// //           </ul>
// //         </div>
// //       </section>

// //       <div className="ticks"></div>
// //       <section id="spacer"></section>
// //     </>
// //   )
// // }

// // export default App

// // import { useState, useEffect } from 'react';

// // function RealtimeClock() {

// //     const [time, setTime] = useState(new Date());
// //     const [isRunning, setIsRunning] = useState(true);
// //     const [format24Hour, setFormat24Hour] = useState(false);

// //     useEffect(() => {

// //         let interval;

// //         if (isRunning) {
// //             interval = setInterval(() => {
// //                 setTime(new Date());
// //             }, 1000);
// //         }

// //         // Cleanup function
// //         return () => {
// //             if (interval) {
// //                 clearInterval(interval);
// //             }
// //         };

// //     }, [isRunning]); // Re-run effect when isRunning changes


// //     // Update document title with current time
// //     useEffect(() => {

// //         document.title = `Clock - ${formatTime(time)}`;

// //         // Cleanup: Reset title when component unmounts
// //         return () => {
// //             document.title = 'React App';
// //         };

// //     }, [time, format24Hour]);


// //     const formatTime = (date) => {

// //         const options = {
// //             hour: '2-digit',
// //             minute: '2-digit',
// //             second: '2-digit',
// //             hour12: !format24Hour
// //         };

// //         return date.toLocaleTimeString('en-US', options);
// //     };


// //     const formatDate = (date) => {

// //         return date.toLocaleDateString('en-US', {
// //             weekday: 'long',
// //             year: 'numeric',
// //             month: 'long',
// //             day: 'numeric'
// //         });
// //     };


// //     return (
// //         <div className="clock-container">

// //             <div className="date">
// //                 {formatDate(time)}
// //             </div>

// //             <div className="time">
// //                 {formatTime(time)}
// //             </div>

// //             <div className="controls">

// //                 <button onClick={() => setIsRunning(!isRunning)}>
// //                     {isRunning ? 'Pause' : 'Resume'}
// //                 </button>

// //                 <label>
// //                     <input
// //                         type="checkbox"
// //                         checked={format24Hour}
// //                         onChange={(e) => setFormat24Hour(e.target.checked)}
// //                     />
// //                     24-hour format
// //                 </label>

// //             </div>

// //             <div className="status">
// //                 Clock is {isRunning ? 'running' : 'paused'}
// //             </div>

// //         </div>
// //     );
// // }

// // export default RealtimeClock;


// // import { useState, useEffect } from 'react';

// // function WindowTracker() {

// //     const [windowSize, setWindowSize] = useState({
// //         width: window.innerWidth,
// //         height: window.innerHeight
// //     });

// //     const [scrollPosition, setScrollPosition] = useState({
// //         x: window.scrollX,
// //         y: window.scrollY
// //     });

// //     const [isOnline, setIsOnline] = useState(navigator.onLine);


// //     // Window resize effect
// //     useEffect(() => {

// //         const handleResize = () => {
// //             setWindowSize({
// //                 width: window.innerWidth,
// //                 height: window.innerHeight
// //             });
// //         };

// //         window.addEventListener('resize', handleResize);

// //         return () => {
// //             window.removeEventListener('resize', handleResize);
// //         };

// //     }, []);


// //     // Scroll tracking effect
// //     useEffect(() => {

// //         const handleScroll = () => {
// //             setScrollPosition({
// //                 x: window.scrollX,
// //                 y: window.scrollY
// //             });
// //         };

// //         window.addEventListener('scroll', handleScroll);

// //         return () => {
// //             window.removeEventListener('scroll', handleScroll);
// //         };

// //     }, []);


// //     // Online/offline status effect
// //     useEffect(() => {

// //         const handleOnline = () => setIsOnline(true);
// //         const handleOffline = () => setIsOnline(false);

// //         window.addEventListener('online', handleOnline);
// //         window.addEventListener('offline', handleOffline);

// //         return () => {
// //             window.removeEventListener('online', handleOnline);
// //             window.removeEventListener('offline', handleOffline);
// //         };

// //     }, []);


// //     // Local storage effect
// //     useEffect(() => {

// //         const data = {
// //             windowSize,
// //             scrollPosition,
// //             timestamp: new Date().toISOString()
// //         };

// //         localStorage.setItem(
// //             'windowTracker',
// //             JSON.stringify(data)
// //         );

// //     }, [windowSize, scrollPosition]);


// //     // Page visibility effect
// //     useEffect(() => {

// //         const handleVisibilityChange = () => {

// //             if (document.hidden) {
// //                 console.log('Page is hidden');
// //             } else {
// //                 console.log('Page is visible');
// //             }

// //         };

// //         document.addEventListener(
// //             'visibilitychange',
// //             handleVisibilityChange
// //         );

// //         return () => {
// //             document.removeEventListener(
// //                 'visibilitychange',
// //                 handleVisibilityChange
// //             );
// //         };

// //     }, []);


// //     return (

// //         <div className="window-tracker">

// //             <h3>Window & Scroll Tracker</h3>


// //             <div className="info-grid">

// //                 <div className="info-card">

// //                     <h4>Window Size</h4>

// //                     <p>
// //                         Width: {windowSize.width}px
// //                     </p>

// //                     <p>
// //                         Height: {windowSize.height}px
// //                     </p>

// //                     <p>
// //                         Aspect Ratio:
// //                         {(windowSize.width / windowSize.height).toFixed(2)}
// //                     </p>

// //                 </div>


// //                 <div className="info-card">

// //                     <h4>Scroll Position</h4>

// //                     <p>
// //                         X: {scrollPosition.x}px
// //                     </p>

// //                     <p>
// //                         Y: {scrollPosition.y}px
// //                     </p>

// //                     <p>
// //                         Total Scrolled:
// //                         {Math.round(
// //                             Math.sqrt(
// //                                 scrollPosition.x ** 2 +
// //                                 scrollPosition.y ** 2
// //                             )
// //                         )}px
// //                     </p>

// //                 </div>


// //                 <div className="info-card">

// //                     <h4>Connection Status</h4>

// //                     <p className={isOnline ? 'online' : 'offline'}>
// //                         {isOnline ? '🟢 Online' : '🔴 Offline'}
// //                     </p>

// //                 </div>


// //                 <div className="info-card">

// //                     <h4>Viewport Classification</h4>

// //                     <p>
// //                         {
// //                             windowSize.width < 768
// //                                 ? 'Mobile'
// //                                 : windowSize.width < 1024
// //                                 ? 'Tablet'
// //                                 : 'Desktop'
// //                         }
// //                     </p>

// //                 </div>

// //             </div>


// //             {/* Add some content to enable scrolling */}

// //             <div
// //                 style={{
// //                     height: '200vh',
// //                     background: 'linear-gradient(to bottom, #f0f0f0, #e0e0e0)'
// //                 }}
// //             >

// //                 <p>
// //                     Scroll down to see the scroll position change...
// //                 </p>

// //             </div>

// //         </div>

// //     );
// // }

// // export default WindowTracker;

// import { useState, useEffect } from 'react';

// function UserProfile({ userId }) {

//     const [user, setUser] = useState(null);
//     const [posts, setPosts] = useState([]);

//     const [loading, setLoading] = useState({
//         user: false,
//         posts: false
//     });

//     const [error, setError] = useState({
//         user: null,
//         posts: null
//     });


//     // Fetch user data when userId changes
//     useEffect(() => {

//         if (!userId) {
//             setUser(null);
//             return;
//         }

//         const abortController = new AbortController();

//         const fetchUser = async () => {

//             setLoading(prev => ({
//                 ...prev,
//                 user: true
//             }));

//             setError(prev => ({
//                 ...prev,
//                 user: null
//             }));

//             try {

//                 // Simulate API delay
//                 await new Promise(resolve =>
//                     setTimeout(resolve, 1000)
//                 );

//                 const response = await fetch(
//                     `/api/users/${userId}`,
//                     {
//                         signal: abortController.signal
//                     }
//                 );

//                 if (!response.ok) {
//                     throw new Error(
//                         `HTTP error! status: ${response.status}`
//                     );
//                 }

//                 const userData = await response.json();

//                 setUser(userData);

//             } catch (err) {

//                 if (err.name !== 'AbortError') {
//                     setError(prev => ({
//                         ...prev,
//                         user: err.message
//                     }));
//                 }

//             } finally {

//                 setLoading(prev => ({
//                     ...prev,
//                     user: false
//                 }));

//             }

//         };

//         fetchUser();

//         return () => {
//             abortController.abort();
//         };

//     }, [userId]);


//     // Fetch user posts when user changes
//     useEffect(() => {

//         if (!user) {
//             setPosts([]);
//             return;
//         }

//         const abortController = new AbortController();

//         const fetchPosts = async () => {

//             setLoading(prev => ({
//                 ...prev,
//                 posts: true
//             }));

//             setError(prev => ({
//                 ...prev,
//                 posts: null
//             }));

//             try {

//                 await new Promise(resolve =>
//                     setTimeout(resolve, 800)
//                 );

//                 const response = await fetch(
//                     `/api/users/${user.id}/posts`,
//                     {
//                         signal: abortController.signal
//                     }
//                 );

//                 if (!response.ok) {
//                     throw new Error(
//                         `Failed to fetch posts: ${response.status}`
//                     );
//                 }

//                 const postsData = await response.json();

//                 setPosts(postsData);

//             } catch (err) {

//                 if (err.name !== 'AbortError') {
//                     setError(prev => ({
//                         ...prev,
//                         posts: err.message
//                     }));
//                 }

//             } finally {

//                 setLoading(prev => ({
//                     ...prev,
//                     posts: false
//                 }));

//             }

//         };

//         fetchPosts();

//         return () => {
//             abortController.abort();
//         };

//     }, [user]);
// }

// export default UserProfile;

// import UserProfile from './UserProfile';

// function App() {

//     return (
//         <div>
//             <UserProfile userId={1} />
//         </div>
//     );
// }

// export default App;

import LiveChat from "./livechat";

function App() {

  return (
    <LiveChat />
  );

}

export default App;
