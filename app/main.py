from fastapi import FastAPI
from app.models import QuestionRequest, AnswerResponse
from app.rag_pipeline import RAGPipeline

app = FastAPI()
rag = RAGPipeline()

@app.post("/ask", response_model=AnswerResponse)
def ask_question(req: QuestionRequest) -> AnswerResponse:
    try:
        answer = rag.ask(req.question)
        return AnswerResponse(answer=answer)
    except Exception as exc:
        return AnswerResponse(answer=f"Error: {exc}")
