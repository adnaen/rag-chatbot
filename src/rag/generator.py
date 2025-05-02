from src.llm.infer import LLMInference


class RAGGenerator:
    def __init__(self) -> None:
        self.llm = LLMInference()

    def generate(self, retrived_content: list[str] | str, query: str) -> str:
        if isinstance(retrived_content, list):
            # Flatten the list if any item is also a list
            retrived_content = [
                str(item) if isinstance(item, str) else "\n".join(str(i) for i in item)
                for item in retrived_content
            ]
        elif not isinstance(retrived_content, str):
            retrived_content = str(retrived_content)

        PROMPT_TEMPLATE = """
        You are an intelligent and helpful **College Admission Assistant** for Empire College Of science.

        Your job is to help users with questions about admissions, courses, programs, fees, important dates, and college life based on the information given in CONTEXT.

        ---

        **Rules you must follow strictly:**

        - ONLY use the information provided in CONTEXT to answer.
        - If the answer is **not found in the CONTEXT** or you are **not confident**, say:
          "I'm sorry, I don't have the information you're looking for. Please contact our admissions office at admissions@college.edu for further help."
        - Be polite, short, and professional.

        ---

        CONTEXT:
        {context}

        QUESTION:
        {question}

        ANSWER:
        """
        prompt = PROMPT_TEMPLATE.format(
            context="\n\n".join(retrived_content), question=query
        )
        return self.llm.generate_response(prompt)
