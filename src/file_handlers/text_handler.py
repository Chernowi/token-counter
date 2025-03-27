def extract_text_from_txt(uploaded_file):
    """Extract text from a plain text file."""
    text = uploaded_file.read().decode("utf-8")
    return text