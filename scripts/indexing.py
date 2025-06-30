from src.core import settings
from src.rag.indexing import ChromaStoreManager
from src.rag.preprocessing import genarate_chunks, load_documents

store = ChromaStoreManager()


def index_data(path: str):
    docs = load_documents(path)
    chunks = genarate_chunks(docs)
    store.add_documet(chunks)


paths = (
    settings.ABOUT_DATA_DIR,
    settings.PROGRAM_TYPE_DATA_DIR,
    settings.PROGRAM_DATA_DIR,
    settings.BLOGS_DATA_DIR,
)


for each in paths:
    index_data(str(each))
