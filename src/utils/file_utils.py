from typing import Any
from pathlib import Path
import json


def _dump_json(content: Any, path: str | Path) -> str | Path:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(content, path, indent=4)
    return path


def _load_json(path: str | Path) -> Any:
    with open(path, "r", encoding="utf-8") as file:
        content = json.load(file)
    return content


def _save_file(content: Any, path: str | Path) -> str | Path:
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
    return path


def _load_file(path: str | Path) -> Any:
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        return content
