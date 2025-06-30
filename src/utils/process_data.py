import re


def clean_text(text: str) -> str:
    """removing whitespace, exclude all non-alphanumeric, punchuation chars"""
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"[^a-zA-Z0-9.,!?'\s]", "", text)
    return text.lower()
