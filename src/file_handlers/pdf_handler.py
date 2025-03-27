import PyPDF2

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file."""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text