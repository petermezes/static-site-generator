import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_init_all_null(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode(None, None, None, None)")

    def test_init_with_values(self):
        node = HTMLNode(tag='div', value='Hello', children=[],
                        props={'class': 'container'})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'Hello')
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {'class': 'container'})

    def test_repr(self):
        node = HTMLNode(tag='span', value='World', children=None, props=None)
        self.assertEqual(repr(node), "HTMLNode('span', 'World', None, None)")

    def test_props_to_html(self):
        node = HTMLNode(props={'id': 'main', 'class': 'highlight'})
        self.assertEqual(node.props_to_html(), ' id="main" class="highlight"')

    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')


if __name__ == "__main__":
    unittest.main()
