from llama_cpp import Llama
from langchain.prompts import ChatPromptTemplate
from src.config import paths


class LLMManager:
    def __init__(self, model_path: str) -> None:
        self.llm = Llama(
            model_path=str(paths.MODEL_DIR / "model.gguf"),
            verbose=False,
        )

    def set_prompt(self, **kwargs) -> str:
        template = ChatPromptTemplate.from_messages(
            messages=[
                ("system", "you're an helpfull ai assistant."),
                ("user", "hello from user"),
            ]
        )

        return template.format(**kwargs)

    def generate_response(self, prompt: str, max_length: int = 100) -> str:
        output = self.llm(prompt=prompt, max_tokens=500, temperature=0.7, top_p=0.9)
        return output["choices"][0]["text"]
