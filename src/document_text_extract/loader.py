# document_text_extract/loader.py

import io
import os
from pathlib import Path
from typing import Union

from bs4 import BeautifulSoup
import fitz  # PyMuPDF
from loguru import logger
import docx


def load_pdf_text_from_bytes(pdf_bytes: bytes) -> str:
    """Extract text from a PDF file in memory (binary data)."""
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    return "".join(page.get_text() for page in doc)


def load_pdf_text(pdf_path: Union[str, Path]) -> str:
    """Extract text from a PDF file using PyMuPDF."""
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()
    return load_pdf_text_from_bytes(pdf_bytes)


def load_docx_text_from_bytes(docx_bytes: bytes) -> str:
    """Extract text from a DOCX file in memory (binary data)."""
    doc = docx.Document(io.BytesIO(docx_bytes))
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)


def load_docx_text(docx_path: Union[str, Path]) -> str:
    """Extract text from a DOCX file using python-docx."""
    with open(docx_path, "rb") as f:
        docx_bytes = f.read()
    return load_docx_text_from_bytes(docx_bytes)


def load_html_text_from_bytes(html_bytes: bytes) -> str:
    """Extract visible text from an HTML file in memory (binary data)."""
    soup = BeautifulSoup(html_bytes, "html.parser")

    for element in soup(["script", "style"]):
        element.decompose()

    return soup.get_text(separator="\n", strip=True)


def load_html_text(html_path: Union[str, Path]) -> str:
    with open(html_path, "rb") as f:
        html_bytes = f.read()
    return load_html_text_from_bytes(html_bytes)


def load_text(file: Union[str, Path, bytes], filename: str = "") -> str:
    """
    Detect file type by extension and extract text accordingly.

    Args:
        file: A file path (str or Path) or binary content (bytes).
        filename: Required if `file` is bytes, to determine extension.

    Returns:
        Extracted plain text.

    Raises:
        ValueError if file type is unsupported.
    """
    if isinstance(file, (str, Path)):
        ext = Path(file).suffix.lower()
        with open(file, "rb") as f:
            file_bytes = f.read()
    elif isinstance(file, bytes):
        if not filename:
            raise ValueError(
                "Filename is required when passing binary data to determine file type."
            )
        ext = Path(filename).suffix.lower()
        file_bytes = file
    else:
        raise TypeError("file must be a str, Path, or bytes")

    logger.debug(f"{ext = } {filename = } {type(file_bytes)}")

    if ext == ".pdf":
        return load_pdf_text_from_bytes(file_bytes)
    elif ext == ".docx":
        return load_docx_text_from_bytes(file_bytes)
    elif ext in (".html", ".htm"):
        return load_html_text_from_bytes(file_bytes)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
