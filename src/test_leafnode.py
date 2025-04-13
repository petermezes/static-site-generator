import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Main Title")
        self.assertEqual(node.to_html(), "<h1>Main Title</h1>")

    def test_leaf_to_html_h2(self):
        node = LeafNode("h2", "Subtitle")
        self.assertEqual(node.to_html(), "<h2>Subtitle</h2>")

    def test_leaf_to_html_code(self):
        node = LeafNode("code", "print('hello')")
        self.assertEqual(node.to_html(), "<code>print('hello')</code>")

    def test_leaf_to_html_empty_content(self):
        node = LeafNode("p", "")
        self.assertRaises(ValueError)

    def test_leaf_to_html_strong(self):
        node = LeafNode("strong", "Bold text")
        self.assertEqual(node.to_html(), "<strong>Bold text</strong>")

    def test_leaf_to_html_em(self):
        node = LeafNode("em", "Emphasized text")
        self.assertEqual(node.to_html(), "<em>Emphasized text</em>")


if __name__ == '__main__':
    unittest.main()
