# document_text_extract/sanitizer.py

import re
import html
import unicodedata


def normalize_unicode(text):
    """
    Convert Unicode characters to closest ASCII equivalent.
    """
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


def remove_sql_injection_risks(text):
    """
    Remove patterns commonly used in SQL injection attacks.
    """
    patterns = [
        r"(?i)(\b(SELECT|INSERT|DELETE|UPDATE|DROP|UNION|OR|AND)\b\s+.+)",  # SQL keywords
        r"(--|#|/\*|\*/|;)",  # SQL comment and statement terminators
        r"(?i)(\bWHERE\b\s+.+)",
    ]
    for pattern in patterns:
        text = re.sub(pattern, "", text)
    return text


PROMPT_INJECTION_PATTERNS = [
    r"(?i)(ignore.*(previous|above|prior).*(instruction|content|text))",
    r"(?i)(disregard.*(rules|guidelines|prior))",
    r"(?i)(you are an? .* language model)",
    r"(?i)(repeat after me:.*)",
    r"(?i)(act as an? .* expert)",
    r"(?i)(override.*instruction)",
    r"(?i)(hallucinate|make up|pretend).*experience",
]


def detect_prompt_injection(text):
    for pattern in PROMPT_INJECTION_PATTERNS:
        if re.search(pattern, text):
            return True
    return False


def is_text_safe(text):
    return not detect_prompt_injection(text)


def neutralize_prompt_injection(text):
    """
    Strip out prompt injection phrases like "Ignore previous instructions" etc.
    """
    for pattern in PROMPT_INJECTION_PATTERNS:
        text = re.sub(pattern, "[REDACTED]", text)
    return text


def sanitize_text(text):
    """
    Run all sanitization steps on the input text.
    """
    text = normalize_unicode(text)
    text = html.escape(text)  # HTML safety (optional)
    text = remove_sql_injection_risks(text)  # Just in case
    text = neutralize_prompt_injection(text)
    return text
