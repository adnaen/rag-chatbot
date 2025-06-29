import re


def _preprocess_text(text: str) -> str:
    """Apply all cleaning steps."""
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"[^a-zA-Z0-9.,!?'\s]", "", text)
    return text.lower()
