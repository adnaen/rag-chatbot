from uuid import uuid1
from typing import List, Tuple
from chromadb import PersistentClient
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from src.core import settings


class ChromaStoreManager:
    def __init__(self) -> None:
        self.embedder = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)
        self.client = PersistentClient(path=str(settings.CHROMA_DIR))
        self.collection = self.client.get_or_create_collection(
            name=settings.CHROMA_COLLECTION
        )

        self.chroma = Chroma(
            client=self.client,
            collection_name=settings.CHROMA_COLLECTION,
            persist_directory=str(settings.CHROMA_DIR),
            embedding_function=self.embedder,
        )

    def add_document(self, docs: List[Document]) -> Tuple[bool, str]:
        try:
            ids = [str(uuid1()) for _ in docs]
            self.chroma.add_documents(documents=docs, ids=ids)
            return True, "document added to store."
        except Exception as e:
            return False, str(e)

    def retriever(self, query: str) -> str:
        docs = self.chroma.similarity_search(query=query, k=4)
        merged_docs = ".".join([each.page_content for each in docs])
        return merged_docs
