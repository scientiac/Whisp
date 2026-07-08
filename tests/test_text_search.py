import sys
import os
import unittest

# Ensure the 'src' directory is in the Python path so the IDE can find 'whisp'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from whisp.text_search import body_match_offsets

class TestTextSearch(unittest.TestCase):
    def test_search_skips_title_line(self):
        text = "This is the title\nThis is the body"
        # Search for 'this'
        offsets = body_match_offsets(text, "this")
        # Should only find the 'this' in the body, which is at index 18
        self.assertEqual(offsets, [18])

    def test_search_case_insensitive(self):
        text = "Title\nHere is some TEXT"
        offsets = body_match_offsets(text, "text")
        self.assertEqual(offsets, [19])

    def test_search_multiple_matches(self):
        text = "Title\nword word word"
        offsets = body_match_offsets(text, "word")
        self.assertEqual(offsets, [6, 11, 16])

    def test_search_no_body(self):
        text = "Title only"
        offsets = body_match_offsets(text, "title")
        self.assertEqual(offsets, [])

    def test_search_empty_term(self):
        text = "Title\nBody text"
        offsets = body_match_offsets(text, "")
        self.assertEqual(offsets, [])

if __name__ == '__main__':
    unittest.main()
