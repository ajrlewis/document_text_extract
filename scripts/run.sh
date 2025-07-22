#!/bin/bash

# Ensure you're in the repo root when calling this script
# Run with: ./scripts/run.sh <FILENAME>

source .venv/bin/activate
PYTHONPATH=src python3 -m document_text_extract $1
