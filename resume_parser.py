from pypdf import PdfReader
from docx import Document


def extract_text_from_pdf(file):
    """Extract text from a PDF resume."""
    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_text_from_docx(file):
    """Extract text from a DOCX resume."""
    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_resume_text(file):
    """Extract text based on the uploaded file type."""
    file_name = file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(file)

    elif file_name.endswith(".docx"):
        return extract_text_from_docx(file)

    else:
        raise ValueError("Only PDF and DOCX files are supported.")