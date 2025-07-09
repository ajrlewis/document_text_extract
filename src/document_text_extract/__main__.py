# document_text_extract/__main__.py

import sys

from loguru import logger

from document_text_extract.processor import extract_and_sanitize

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logger.error("Usage: python -m document_text_extract <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        result = extract_and_sanitize(file_path)
        logger.info(result)
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)
