import unittest
from src.file_handlers.pdf_handler import extract_text_from_pdf
from src.file_handlers.text_handler import extract_text_from_txt
from src.file_handlers.docx_handler import extract_text_from_docx

class TestFileHandlers(unittest.TestCase):

    def test_extract_text_from_pdf(self):
        # Add a sample PDF file path for testing
        sample_pdf_path = 'path/to/sample.pdf'
        text = extract_text_from_pdf(sample_pdf_path)
        self.assertIsInstance(text, str)

    def test_extract_text_from_txt(self):
        # Add a sample TXT file path for testing
        sample_txt_path = 'path/to/sample.txt'
        text = extract_text_from_txt(sample_txt_path)
        self.assertIsInstance(text, str)

    def test_extract_text_from_docx(self):
        # Add a sample DOCX file path for testing
        sample_docx_path = 'path/to/sample.docx'
        text = extract_text_from_docx(sample_docx_path)
        self.assertIsInstance(text, str)

if __name__ == '__main__':
    unittest.main()