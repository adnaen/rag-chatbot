from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models.llamacpp import ChatLlamaCpp
from src.core import settings


class LLMInferenceManager:
    def __init__(self) -> None:
        self.llm = ChatLlamaCpp(
            model_path=str(settings.MODEL_DIR / f"{settings.LLM}.gguf"),
            verbose=False,
            top_p=settings.LLM_TOP_P,
            top_k=settings.LLM_TOP_K,
            temperature=settings.LLM_TEMPERATURE,
            n_threads=settings.N_THREADS,
            n_ctx=settings.N_CTX,
            max_tokens=settings.MAX_TOKENS,
        )

    def ask(self, query: str, context: str) -> str:
        prompt = self._set_prompt()
        chain = prompt | self.llm
        output = chain.invoke({"context": context, "query": query})
        return output.content

    def _set_prompt(self) -> ChatPromptTemplate:
        template = ChatPromptTemplate.from_messages(
            messages=[
                (
                    "system",
                    "Your an AI Assistant for  Empire College Of Science. Answer only using the provided context. If the answer is not in the context or unclear, replay with 'I Dont know about this, Please contact college.' Keep the response brief and simple.",
                ),
                (
                    "user",
                    "Context:\n{context}\n\nUser Query: {query}\nResponse strictly based on the context only.",
                ),
            ]
        )
        return template
