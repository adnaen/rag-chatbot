from llama_cpp import Llama
from src.config import paths


class LLMInference:
    def __init__(self) -> None:
        self.llm = Llama(model_path=str(paths.MODEL_DIR / "model.gguf"), verbose=False)

    def generate_response(self, prompt: str, max_length: int = 100) -> str:
        output = self.llm(prompt=prompt, max_tokens=600, temperature=0.7, top_p=0.9)
        return output["choices"][0]["text"]
