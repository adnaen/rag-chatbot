from typing import List
from langchain_core.documents import Document


def load_documents(path: str) -> List[Document]:
    from langchain_community.document_loaders import TextLoader

    loader = TextLoader(file_path=path)
    return loader.load()


def genarate_chunks(docs: List[Document]) -> List[Document]:
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " ", ""],
        chunk_size=1500,
        chunk_overlap=200,
    )

    return splitter.split_documents(docs)
