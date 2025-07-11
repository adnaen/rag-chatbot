from typing import List
from langchain_core.documents import Document
from src.core import settings


def load_documents(path: str) -> List[Document]:
    from langchain_community.document_loaders import TextLoader

    loader = TextLoader(file_path=path)
    return loader.load()


def genarate_chunks(docs: List[Document]) -> List[Document]:
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " ", ""],
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
    )

    return splitter.split_documents(docs)
