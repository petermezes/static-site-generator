from typing import List, Dict


class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children: List['HTMLNode'] | None = None, props: Dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag!r}, {self.value!r}, {self.children!r}, {self.props!r})"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""
        props_list = []
        for key, value in self.props.items():
            props_list.append(f" {key}=\"{value}\"")
        return "".join(props_list)
