import unittest
from utils.token_counter import count_tokens

class TestTokenCounter(unittest.TestCase):

    def test_count_tokens_basic(self):
        text = "Hello world!"
        self.assertEqual(count_tokens(text), 2)

    def test_count_tokens_empty(self):
        text = ""
        self.assertEqual(count_tokens(text), 0)

    def test_count_tokens_with_punctuation(self):
        text = "Hello, world! This is a test."
        self.assertEqual(count_tokens(text), 7)

    def test_count_tokens_with_newlines(self):
        text = "Hello\nworld!"
        self.assertEqual(count_tokens(text), 2)

if __name__ == '__main__':
    unittest.main()