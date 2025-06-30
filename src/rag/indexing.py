import os
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
from src.core import settings
from src.utils import mark_as_completed


class ChromaStoreManager:
    def __init__(self, encoder_name: str = "all-MiniLM-L6-v2") -> None:
        self.embedder = SentenceTransformer(model_name=encoder_name)
        self.client = PersistentClient(path=str(settings.DB_DIR))
        self.collection = self.client.get_or_create_collection(
            name="chatbot_embeddings"
        )

    def generate_embeddings(self) -> bool:
        chunk_folder = settings.DATA_DIR / "preprocessed"

        for sections in os.listdir(chunk_folder):
            for file_name in os.listdir(chunk_folder / sections):
                absolute_path = str(chunk_folder / sections / file_name)
                content = _load_file(path=absolute_path)

                embedding = self.encoder.encode(sentences=content).tolist()

                self.collection.add(
                    ids=[absolute_path.replace(".txt", "")],
                    documents=content,
                    embeddings=[embedding],
                    metadatas=[{"source": absolute_path}],
                )
        return True

    def retriever(self, query: str) -> list:
        embedings = self.encoder.encode(query).tolist()
        results = self.collection.query(query_embeddings=embedings, n_results=top_k)
        return results["documents"]
