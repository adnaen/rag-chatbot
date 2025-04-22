from src.llm.infer import LLMInference


class RAGGenerator:
    def __init__(self) -> None:
        self.llm = LLMInference()

    def generate(self, retrived_content: list[str] | str, query: str) -> str:
        PROMPT_TEMPLATE = """
        CONTEXT:
        {context}

        QUESTION:
        {question}

        ANSWER:
        """
        prompt = PROMPT_TEMPLATE.format(context=retrived_content, question=query)
        self.llm.generate_response(prompt)
