import unittest
from main import markdown_to_html_node
class TestMarkdownToBlocks(unittest.TestCase):
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_blockquote(self):
        md = """
> For 60 years, WWF has worked to help people and nature thrive.
> As the world's leading conservation organization, WWF works in nearly 100 countries.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p>For 60 years, WWF has worked to help people and nature thrive.</p><p>As the world's leading conservation organization, WWF works in nearly 100 countries.</p></blockquote></div>"
        )

    def test_unordered_list(self):
        md = """
- Item 1
- Item 2
- Item 2a
- Item 2b
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 2a</li><li>Item 2b</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. Item 1
2. Item 2
3. Item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol></div>"
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_headings(self):
        md = """
# This is a Heading h1

###### This is a Heading h6

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a Heading h1</h1><h6>This is a Heading h6</h6></div>",
        )

if __name__ == "__main__":
    unittest.main()