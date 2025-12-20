import React, { useState, useRef, useEffect } from "react";
import Layout from "@theme/Layout";

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    const userMessage = { type: "user", content: inputValue };
    const newMessages = [...messages, userMessage];
    setMessages(newMessages);
    setInputValue("");
    setIsLoading(true);

    try {
      // Use the production backend by default. 
      // If you want to run the backend locally, uncomment the localhost line.
      const API_URL = "https://physical-ai-spec-kit-production.up.railway.app/query";
      // const API_URL = "http://127.0.0.1:8000/query";

      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: inputValue }),
      });

      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }

      const data = await res.json();
      const botMessage = {
        type: "bot",
        content: data.answer,
        citations: data.citations || []
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error("Error:", error);
      const errorMessage = {
        type: "bot",
        content: `Sorry, I encountered an error: ${error.message}. Please check if the backend is running and reachable.`,
        citations: []
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const formatCitations = (citations) => {
    if (!citations || citations.length === 0) return null;

    return (
      <div className="citations-section">
        <h4>Sources:</h4>
        <ul>
          {citations.map((citation, index) => (
            <li key={index}>{citation}</li>
          ))}
        </ul>
      </div>
    );
  };

  return (
    <Layout title="Chat with Physical AI Knowledge Base">
      <div className="chat-container">
        <div className="chat-header">
          <h1>Physical AI Knowledge Assistant</h1>
          <p>Ask questions about Physical AI, embodied intelligence, and robotics systems</p>
        </div>

        <div className="chat-messages">
          {messages.length === 0 ? (
            <div className="welcome-message">
              <h3>Welcome to the Physical AI Knowledge Assistant!</h3>
              <p>Ask me anything about Physical AI, embodied intelligence, humanoid robotics, or related topics. I'm here to help you understand the concepts and specifications in the Physical AI domain.</p>

              <div className="suggested-questions">
                <h4>Suggested questions:</h4>
                <ul>
                  <li><button onClick={() => setInputValue("What is Physical AI?")}>What is Physical AI?</button></li>
                  <li><button onClick={() => setInputValue("How does Physical AI differ from traditional AI?")}>How does Physical AI differ from traditional AI?</button></li>
                  <li><button onClick={() => setInputValue("Explain embodied intelligence")}>Explain embodied intelligence</button></li>
                  <li><button onClick={() => setInputValue("What are the challenges in Physical AI?")}>What are the challenges in Physical AI?</button></li>
                </ul>
              </div>
            </div>
          ) : (
            messages.map((message, index) => (
              <div
                key={index}
                className={`message ${message.type === 'user' ? 'user-message' : 'bot-message'}`}
              >
                <div className="message-content">
                  <div className="message-text">
                    {message.content}
                  </div>
                  {message.citations && formatCitations(message.citations)}
                </div>
              </div>
            ))
          )}
          {isLoading && (
            <div className="message bot-message">
              <div className="message-content">
                <div className="typing-indicator">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <form onSubmit={handleSubmit} className="chat-input-form">
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Ask a question about Physical AI..."
            disabled={isLoading}
            className="chat-input"
          />
          <button type="submit" disabled={isLoading} className="chat-submit-btn">
            {isLoading ? "Sending..." : "Send"}
          </button>
        </form>
      </div>
    </Layout>
  );
}

