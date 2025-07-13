from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.db import Base, engine
from src.rag.indexing import ChromaStoreManager
from src.rag.generation import LLMInferenceManager
from src.routes.chat_routes import router as chat_router


Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.store = ChromaStoreManager()
    app.state.llm = LLMInferenceManager()

    yield

    print("App closed.")


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.include_router(chat_router, prefix="/api")
