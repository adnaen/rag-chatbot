import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM

load_dotenv()


HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")


class LLMInference:
    # TODO:
    def __init__(self, model_name: str = "") -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name, use_auth_token=HUGGING_FACE_TOKEN
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name, use_auth_token=HUGGING_FACE_TOKEN
        )

    def generate_response(self, prompt: str, max_length: int = 100) -> str:

        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs["input_ids"], max_length=max_length)
        response = self.tokenizer.decode(outputs[0], skip_spacial_tokens=True)
        return response
