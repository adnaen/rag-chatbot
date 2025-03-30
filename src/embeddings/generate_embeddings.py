import os
from src.config import paths
from src.utils.file_utils import _load_file
from src.utils.state_utils import mark_completed
from .utils import get_collection, get_model


model = get_model()
collection = get_collection("chatbot_embeddings")


def generate_embeddings():
    chunk_folder = paths.DATA_DIR / "preprocessed"

    for sections in os.listdir(chunk_folder):
        for file_name in os.listdir(chunk_folder / sections):
            print("filename", file_name)
            absolute_path = str(chunk_folder / sections / file_name)
            content = _load_file(path=absolute_path)

            embedding = model.encode(sentences=content).tolist()

            collection.add(
                ids=[absolute_path.replace(".txt", "")],
                embeddings=[embedding],
                metadatas=[{"source": absolute_path}],
            )
    mark_completed("generate_embeddings")
