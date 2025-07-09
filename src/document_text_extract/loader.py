# document_text_extract/loader.py

import fitz  # PyMuPDF
import docx
import os
from pathlib import Path
from typing import Union


def load_pdf_text(pdf_path: Union[str, Path]) -> str:
    """Extract text from a PDF file using PyMuPDF."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def load_docx_text(docx_path: Union[str, Path]) -> str:
    """Extract text from a DOCX file using python-docx."""
    doc = docx.Document(docx_path)
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)


def load_text(file_path: Union[str, Path]) -> str:
    """
    Auto-detect file type and extract text accordingly.
    Supports: .pdf, .docx
    """
    ext = Path(file_path).suffix.lower()

    if ext == ".pdf":
        return load_pdf_text(file_path)
    elif ext == ".docx":
        return load_docx_text(file_path)
    elif ext == ".doc":
        raise ValueError(
            "Unsupported file format: .doc (binary). Please convert to .docx."
        )
    else:
        raise ValueError(f"Unsupported file extension: {ext}")
