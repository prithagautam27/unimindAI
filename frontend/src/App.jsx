import './App.css'
import axios from 'axios'
import { useState, useRef, useEffect } from 'react'
import { FaPaperPlane } from 'react-icons/fa'
import campusBg from './campus.jpg'

function App() {
  const [message, setMessage] = useState('')
  const [isTyping, setIsTyping] = useState(false)

  const [messages, setMessages] = useState([
    {
      text: 'Hello! Welcome to UniMind AI.',
      sender: 'bot'
    }
  ])

  const messagesEndRef = useRef(null)

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: 'smooth'
    })
  }, [messages])

  const sendMessage = async () => {
    if (!message.trim()) return

    const userMessage = {
      text: message,
      sender: 'user'
    }

    setMessages(prev => [...prev, userMessage])
    setMessage('')
    setIsTyping(true)

    try {
      await new Promise(resolve =>
        setTimeout(resolve, 1200)
      )

      const response = await axios.post(
       ' https://unimindai.onrender.com/api/chat,'
        {
          message: userMessage.text
        }
      )

      const botMessage = {
        text: response.data.response,
        sender: 'bot'
      }

      setMessages(prev => [...prev, botMessage])
    } catch (error) {
      setMessages(prev => [
        ...prev,
        {
          text: 'Backend connection failed.',
          sender: 'bot'
        }
      ])
    } finally {
      setIsTyping(false)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      sendMessage()
    }
  }

  return (
  <div
    className="app-container"
    style={{
      backgroundImage: `url(${campusBg})`,
      backgroundPosition: 'center',
      backgroundRepeat: 'no-repeat'
    }}
  >
      <div className="chat-container">

        <div className="chat-header">
          <div className="brand">
            🤖 <span>UniMind AI</span>
          </div>
        </div>

        <div className="chat-messages">

          {messages.map((msg, index) => (
            <div
              key={index}
              className={`message-row ${
                msg.sender === 'user'
                  ? 'user-row'
                  : 'bot-row'
              }`}
            >
              {msg.sender === 'bot' && (
                <div className="avatar bot-avatar">
                  🤖
                </div>
              )}

              <div
                className={`message ${
                  msg.sender === 'user'
                    ? 'user-message'
                    : 'bot-message'
                }`}
              >
                {msg.text}
              </div>

              {msg.sender === 'user' && (
                <div className="avatar user-avatar">
                  👤
                </div>
              )}
            </div>
          ))}

          {isTyping && (
            <div className="message-row bot-row">
              <div className="avatar bot-avatar">
                🤖
              </div>

              <div className="message bot-message">
                <div className="typing">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </div>
          )}

          <div ref={messagesEndRef}></div>

        </div>

        <div className="chat-input-container">
          <input
            type="text"
            className="chat-input"
            placeholder="Ask UniMind something..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleKeyPress}
          />

          <button
            className="send-button"
            onClick={sendMessage}
          >
            <FaPaperPlane />
          </button>
        </div>

      </div>
    </div>
  )
}

export default App