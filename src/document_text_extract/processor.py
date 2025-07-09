# document_text_extract/processor.py

from document_text_extract.loader import load_text
from document_text_extract.sanitizer import sanitize_text


def extract_and_sanitize(file_path: str) -> str:
    """
    Load text from a document and sanitize it for safe LLM use.
    """
    raw_text = load_text(file_path)
    clean_text = sanitize_text(raw_text)
    return clean_text
