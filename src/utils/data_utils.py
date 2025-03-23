import os
import re
from pathlib import Path

from src.utils.file_utils import _load_file, _save_file
from src.config import settings, paths


def _normalize_whitespace(text):
    """Replace multiple spaces and newlines with a single space."""
    return re.sub(r"\s+", " ", text).strip()


def _remove_special_chars(text):
    """Remove special characters except basic punctuation."""
    return re.sub(r"[^a-zA-Z0-9.,!?'\s]", "", text)


def _preprocess_text(text):
    """Apply all cleaning steps."""
    text = _normalize_whitespace(text)
    text = _remove_special_chars(text)
    return text.lower()


def _generate_chunks(processed_path: str | Path, file_name: str, category: str):
    content = _load_file(path=processed_path)
    content = content.split(" ")
    word_count = len(content)
    total_file_need = word_count // settings.WORD_PER_FILE
    balance_words = word_count % settings.WORD_PER_FILE

    file_name = file_name.split(".")[0]

    absolute_path = paths.DATA_DIR / "preprocessed" / category
    os.makedirs(absolute_path, exist_ok=True)
    if word_count <= 500:
        content = " ".join(content)
        _save_file(
            content=content,
            path=absolute_path / f"{file_name}_chunk_{total_file_need}.txt",
        )

    else:
        for i in range(total_file_need):
            if len(content) % 500 != 0:
                final_content = " ".join(content[-balance_words:])
                _save_file(
                    content=final_content,
                    path=absolute_path / f"{file_name}_chunk_{total_file_need}.txt",
                )
                content = content[:-balance_words]

            if len(content) % 500 == 0:
                first_content = " ".join(content[:500])
                _save_file(
                    content=first_content,
                    path=absolute_path / f"{file_name}_chunk_{i}.txt",
                )
                content = content[500:]
