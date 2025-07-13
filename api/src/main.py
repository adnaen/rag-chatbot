from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.core.db import Base, engine
from src.rag.indexing import ChromaStoreManager
from src.rag.generation import LLMInferenceManager
from src.routes.llm_routes import router as llm_router
from src.routes.chat_routes import router as chat_router


Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.store = ChromaStoreManager()
    app.state.llm = LLMInferenceManager()

    yield

    print("App closed.")


app = FastAPI(lifespan=lifespan)
app.include_router(chat_router)
app.include_router(llm_router)
