from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        super().__init__(tag, value=None, children=children, props=None)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")

        return f"<{self.tag}>{self._render_children()}</{self.tag}>"

    def _render_children(self):
        return "".join(child.to_html() for child in self.children)
