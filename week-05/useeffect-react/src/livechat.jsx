import { useState, useEffect, useRef } from "react";
import "./livechat.css";

function LiveChat() {

  // Simpan semua mesej chat
  const [messages, setMessages] = useState([
    "Welcome to Live Chat!"
  ]);

  // Simpan status online / offline
  const [isOnline, setIsOnline] = useState(navigator.onLine);

  // Simpan status sedang menaip
  const [isTyping, setIsTyping] = useState(false);

  // Digunakan untuk scroll ke mesej paling bawah
  const bottomRef = useRef(null);


  // 1. AUTO-GENERATE MESSAGE
  useEffect(() => {

    const interval = setInterval(() => {

      setIsTyping(true);

      const typingTimer = setTimeout(() => {

        const newMessage =
          "New message at " + new Date().toLocaleTimeString();

        setMessages((prevMessages) => [
          ...prevMessages,
          newMessage
        ]);

        setIsTyping(false);

      }, 1000);

      return () => clearTimeout(typingTimer);

    }, 4000);


    // CLEANUP INTERVAL
    return () => {
      clearInterval(interval);
    };

  }, []);


  // 2. ONLINE / OFFLINE STATUS
  useEffect(() => {

    const handleOnline = () => {
      setIsOnline(true);
    };

    const handleOffline = () => {
      setIsOnline(false);
    };

    window.addEventListener("online", handleOnline);
    window.addEventListener("offline", handleOffline);


    // CLEANUP EVENT LISTENERS
    return () => {
      window.removeEventListener("online", handleOnline);
      window.removeEventListener("offline", handleOffline);
    };

  }, []);


  // 3. AUTO SCROLL TO BOTTOM
  useEffect(() => {

    bottomRef.current?.scrollIntoView({
      behavior: "smooth"
    });

  }, [messages]);


  return (

    <div className="chat-container">

      <h1>Live Chat Simulator</h1>

      <p className="status">
        Status: {isOnline ? "Online" : "Offline"}
      </p>


      <div className="chat-box">

        {messages.map((message, index) => (

          <div className="message" key={index}>
            {message}
          </div>

        ))}


        {isTyping && (
          <p className="typing">
            Someone is typing...
          </p>
        )}


        <div ref={bottomRef}></div>

      </div>

    </div>

  );
}

export default LiveChat;
