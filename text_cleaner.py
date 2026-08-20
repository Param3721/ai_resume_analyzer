import re


def clean_text(text):
    """Clean and normalize resume text."""

    # Convert text to lowercase
    text = text.lower()

    # Keep useful characters and remove unnecessary symbols
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)

    # Replace multiple spaces with a single space
    text = re.sub(r"\s+", " ", text)

    return text.strip()