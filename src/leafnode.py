from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        self.tag = tag
        self.value = value
        self.props = props
        super().__init__(tag, value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("Value cannot be empty")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
