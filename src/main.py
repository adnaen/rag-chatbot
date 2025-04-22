# FIXME:

# from src.embedding import vectorstore
# from src.scraping import run_scraper
# from src.scraping.process_data import process_data
#
# from src.embedding.vectorstore import ChromaVectorStore
# from src.rag.generator import RAGGenerator
#
# from src.config import logger
# from src.utils.state_utils import is_completed
#
#
# def main():
#     (
#         logger.info("Data Ingestion are Already completed.")
#         if is_completed("data_ingestion")
#         else run_scraper()
#     )
#
#     (
#         logger.info("Data Preprocessing are Already completed.")
#         if is_completed("data_preprocessing")
#         else process_data()
#     )
#
#     if is_completed("generate_embeddings"):
#         logger.info("Embeddings are Already generated.")
#     else:
#         vector_store = ChromaVectorStore()
#         rag_generator = RAGGenerator()
#         # vector_store.generate_embeddings()
#         while True:
#             query = input("Enter yoour query : ")
#             result = vector_store.query_embeddings(query)
#             llm_output = rag_generator.generate(retrived_content=result, query=query)
#             print(llm_output)
#
#
# quite: bool = False
# while not quite:
#     is_have_to_run = input(
#         "Do you have to re-run the stages ? (press Enter to no) (yes/no) : "
#     )
#     match is_have_to_run:
#         case "yes":
#             run_scraper()
#             process_data()
#         case "no":
#             quite = True
#             return
#         case "":
#             quite = True
#             return
#         case _:
#             print("Please choose either 'yes' or 'no' !")
#
#
# if __name__ == "__main__":
#     main()
