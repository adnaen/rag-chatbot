import chromadb
from sentence_transformers import SentenceTransformer
from src.config.paths import DB_DIR


def get_collection(collection_name: str) -> chromadb.Collection:
    chroma_client = chromadb.PersistentClient(path=str(DB_DIR))
    return chroma_client.get_or_create_collection(name=collection_name)


def get_model() -> SentenceTransformer:
    return SentenceTransformer("all-MiniLM-L6-v2")
