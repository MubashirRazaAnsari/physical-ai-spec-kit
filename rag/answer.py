import os
from dotenv import load_dotenv
from google import genai

from rag.retriever import retrieve


load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-1.0-pro"


def is_section_query(question: str) -> bool:
    """
    Detects section-title style questions.
    """
    keywords = ["section", "opening", "background", "research question", "chapter"]
    q = question.lower()
    return any(k in q for k in keywords)


SYSTEM_PROMPT_GENERAL = """
You are an academic assistant answering questions strictly
from the provided context.

RULES:
- Use ONLY the context below.
- Do NOT add outside knowledge.
- If the answer is not present, say:
  "The answer is not found in the provided material."
- Cite section titles explicitly.
"""

SYSTEM_PROMPT_SECTION = """
You are an academic assistant summarizing a specific
section of a textbook.

RULES:
- Summarize ONLY the provided section content.
- Do NOT add outside knowledge.
- Write a concise, clear summary.
- Cite the section title explicitly.
"""


def answer_question(question: str, top_k: int = 5):
    results = retrieve(question, top_k=top_k)

    if not results:
        return {
            "answer": "The answer is not found in the provided material.",
            "citations": []
        }

    # -------------------------------
    # Rank by similarity score
    # -------------------------------
    results = sorted(results, key=lambda r: r.score, reverse=True)

    # -------------------------------
    # Build context (limit size)
    # -------------------------------
    context_blocks = []
    citations = []

    for r in results[:3]:  # top 3 only (cleaner)
        context_blocks.append(
            f"[{r.payload['section_title']}]\n{r.payload['text']}"
        )
        citations.append(r.payload["section_title"])

    citations = list(dict.fromkeys(citations))  # dedupe, preserve order

    # -------------------------------
    # Choose prompt style
    # -------------------------------
    system_prompt = (
        SYSTEM_PROMPT_SECTION
        if is_section_query(question)
        else SYSTEM_PROMPT_GENERAL
    )

    prompt = f"""
{system_prompt}

CONTEXT:
{chr(10).join(context_blocks)}

QUESTION:
{question}

ANSWER:
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return {
        "answer": response.text.strip(),
        "citations": citations
    }
