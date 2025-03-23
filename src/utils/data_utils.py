import re


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
