import os
from colorama import Fore
from src.core import settings, logger
from src.rag.indexing import ChromaStoreManager
from src.rag.preprocessing import genarate_chunks, load_documents

store = ChromaStoreManager()


paths = (
    settings.ABOUT_DATA_DIR,
    settings.PROGRAM_TYPE_DATA_DIR,
    settings.PROGRAM_DATA_DIR,
    settings.BLOGS_DATA_DIR,
)


for path in paths:
    logger.info(
        f"{Fore.GREEN}Indexing started for {str(path).split('/')[-1]}.{Fore.RESET}"
    )
    for file in os.listdir(path):
        docs = load_documents(str(path / file))
        chunks = genarate_chunks(docs)
        store.add_document(chunks)

        logger.info(f"{Fore.GREEN}INDXED `{str(path / file)}`{Fore.RESET}")

    logger.info(
        f"{Fore.GREEN}ALL '{str(path).split('/')[-1]}' FILES SUCCESSFULLY INDEXED.{Fore.RESET}"
    )
    print(50 * f"{Fore.GREEN}*" + f"{Fore.RESET}")
