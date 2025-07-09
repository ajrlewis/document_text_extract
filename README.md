# 📝 Document Text Extract

A lightweight Python library to extract and sanitize text in **PDF** and **DOCX** format.

---

## 🚀 Features

- ✅ Extracts text from `.pdf` and `.docx` files
- 🛡️ Sanitizes for SQL injections and LLM prompt injections
- ⚡ Simple CLI and modular structure for reuse in APIs or batch jobs

---

## 📦 Installation

```bash
git clone https://github.com/ajrlewis/document-text-extract.git
cd document-text-extract
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🧪 Usage

### 🖥 CLI

`python -m src.document_text_extract path/to/document.pdf`

Supports .pdf and .docx files.

### 📦 In Python

```python
from document_text_extract.processor import extract_and_sanitize

clean_text = extract_and_sanitize("path/to/cv.docx")
```

## 🧼 Sanitization

Text is processed to:

- Normalize Unicode characters

- Remove or neutralize common SQL injection patterns

- Strip basic prompt injection triggers (e.g. ignore previous instructions)

You can customize sanitization in "sanitizer.py".

## 📂 Project Structure

```
src/
├── document_text_extract/
│   ├── __init__.py
│   ├── __main__.py        # CLI entrypoint
│   ├── loader.py          # File text extraction
│   ├── processor.py       # Orchestration logic
│   └── sanitizer.py       # Text cleaning & flagging
tests/
├── __init__.py
assets/
├── bitcoin.pdf            # Sample test asset
scripts/
├── run.sh                 # Sample script
```

## 📄 License

MIT License — see LICENSE for details.