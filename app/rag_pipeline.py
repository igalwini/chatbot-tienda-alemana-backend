from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain.chains import RetrievalQA

from app import config

class RAGPipeline:
    def __init__(self) -> None:
        embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDINGS_MODEL)
        faiss = FAISS.load_local(
            config.VECTOR_STORE_PATH,
            embeddings,
            allow_dangerous_deserialization=True,
        )
        retriever = faiss.as_retriever(search_type="similarity", search_kwargs={"k": 4})
        llm = ChatOllama(model=config.OLLAMA_MODEL)
        self.qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    def ask(self, question: str) -> str:
        result = self.qa_chain.invoke(question)
        return result["result"]
