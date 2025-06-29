import os
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
from src.config import paths
from src.utils.file_utils import _load_file
from src.utils.state_utils import mark_completed


class ChromaVectorStore:
    def __init__(self, encoder_name: str = "all-MiniLM-L6-v2") -> None:
        self.embedder = SentenceTransformer(model_name=encoder_name)
        self.client = PersistentClient(path=str(paths.DB_DIR))
        self.collection = self.client.get_or_create_collection(
            name="chatbot_embeddings"
        )

    def generate_embeddings(self) -> bool:
        chunk_folder = paths.DATA_DIR / "preprocessed"

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
        mark_completed("generate_embeddings")
        return True

    def query_embeddings(self, query: str, top_k: int = 1) -> list:
        embedings = self.encoder.encode(query).tolist()
        results = self.collection.query(query_embeddings=embedings, n_results=top_k)
        return results["documents"]
