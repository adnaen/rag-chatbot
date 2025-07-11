from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from src.rag.indexing import ChromaStoreManager
from src.rag.generation import LLMInferenceManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.store = ChromaStoreManager()
    app.state.llm = LLMInferenceManager()

    yield
    print("App closed.")


app = FastAPI(lifespan=lifespan)


@app.get("/ask")
def ask_llm(prompt: str, request: Request):
    context = request.app.state.store.retriever(query=prompt)
    llm_response = request.app.state.llm.ask(query=prompt, context=context)
    return {"assistant": llm_response}
