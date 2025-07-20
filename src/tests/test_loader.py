from loguru import logger
import pytest

from document_text_extract import loader


class TestLoader:
    def test_load_pdf_text(self) -> None:
        text = loader.load_pdf_text("assets/sample_document.pdf")
        logger.debug(f"PDF {text = }")
        assert (
            text
            == "Sample PDF Document\nThis is a test PDF file.\nIt contains a few lines of text for extraction testing.\n- Bullet point one\n- Bullet point two\nEnd of document.\n"
        )

    def test_load_docx_text(self) -> None:
        text = loader.load_pdf_text("assets/sample_document.docx")
        logger.debug(f"{text = }")
        assert (
            text
            == "Sample Document\nThis is a test DOCX file.\nIt contains a few lines of text for extraction testing.\n- Bullet point one\n- Bullet point two\nEnd of document.\n"
        )

    def test_load_html_text(self) -> None:
        pass

    def test_load_text(self) -> None:
        pass
