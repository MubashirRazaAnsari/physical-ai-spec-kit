import React, { useState } from "react";
import Layout from "@theme/Layout";

export default function Chat() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [citations, setCitations] = useState([]);
  const [loading, setLoading] = useState(false);

  async function askQuestion() {
    if (!question) return;
    setLoading(true);
    setAnswer("");
    setCitations([]);

    const res = await fetch("http://127.0.0.1:8000/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });

    const data = await res.json();
    setAnswer(data.answer);
    setCitations(data.citations || []);
    setLoading(false);
  }

  return (
    <Layout title="Chat with the Book">
      <div style={{ maxWidth: 800, margin: "40px auto" }}>
        <h1>Ask the Physical AI Book</h1>

        <textarea
          rows={4}
          style={{ width: "100%" }}
          placeholder="Ask a question about the book..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button onClick={askQuestion} style={{ marginTop: 10 }}>
          {loading ? "Thinking..." : "Ask"}
        </button>

        {answer && (
          <div style={{ marginTop: 30 }}>
            <h3>Answer</h3>
            <p>{answer}</p>

            {citations.length > 0 && (
              <>
                <h4>Sources</h4>
                <ul>
                  {citations.map((c, i) => (
                    <li key={i}>{c}</li>
                  ))}
                </ul>
              </>
            )}
          </div>
        )}
      </div>
    </Layout>
  );
}

