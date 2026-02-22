import pdfplumber
from docx import Document
from pathlib import Path

def extract_text_from_pdf(path):
    text=[]
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text=page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)

def extract_text_from_docx(path):
    doc=Document(path)
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

def load_document(path):
    path=Path(path)
    suffix=path.suffix.lower()

    if suffix==".pdf":
        return extract_text_from_pdf(path)
    elif suffix== ".docx":
        return extract_text_from_docx(path)
    elif suffix==".txt":
        return path.read_text(encoding="utf-8")
    else:
        raise ValueError("Unsupported file format.")