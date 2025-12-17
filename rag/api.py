from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag.answer import answer_question


app = FastAPI(
    title="Physical AI RAG API",
    description="RAG backend for AI-native textbook",
    version="1.0.0"
)

# 🔹 CORS (THIS FIXES YOUR ERROR)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for demo; restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    citations: list[str]

@app.post("/query", response_model=QueryResponse)
def query_rag(req: QueryRequest):
    return answer_question(req.question)

