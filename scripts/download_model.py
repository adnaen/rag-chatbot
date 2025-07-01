import os
import shutil
import requests
from colorama import Fore
from src.core import settings, logger


full_path = settings.MODEL_DIR / f"{settings.LLM}.gguf"
want_to_continue: bool = True

if os.path.exists(full_path):
    status = input("Do you want to re-download the LLM file? (yes/no)")
    want_to_continue = True if status.lower() == "yes" else False

if want_to_continue:

    model_file_downloadable_url: str = (
        "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q8_0.gguf?download=true"
    )

    logger.info(f"{Fore.GREEN}LLM MODEL FILE DOWNLOAD STARTED.{Fore.RESET}")
    with requests.get(url=model_file_downloadable_url, stream=True) as obj:
        os.makedirs(full_path.parent)
        with open(full_path, "wb") as file:
            shutil.copyfileobj(obj.raw, file)

    logger.info(f"{Fore.GREEN}LLM MODEL FILE DOWNLOADED SUCCESSFULLY.{Fore.RESET}")
    print(50 * f"{Fore.GREEN}*" + f"{Fore.RESET}")
