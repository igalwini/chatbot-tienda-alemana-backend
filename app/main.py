from fastapi import FastAPI
from app.models import QuestionRequest, AnswerResponse
from app.rag_pipeline import RAGPipeline
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
rag = RAGPipeline()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask", response_model=AnswerResponse)
def ask_question(req: QuestionRequest) -> AnswerResponse:
    try:
        answer = rag.ask(req.question)
        return AnswerResponse(answer=answer)
    except Exception as exc:
        return AnswerResponse(answer=f"Error: {exc}")
