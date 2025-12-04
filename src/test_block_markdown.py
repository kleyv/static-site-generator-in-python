import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
    markdown_to_html_node
)

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_with_special_text(self):
        md = """
Blockquotes

Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.
![This is an alt text.](/image/sample.webp "This is a sample image.").

Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.
You may be using [Markdown Live Preview](https://markdownlivepreview.com/).

1. Item 1
2. Item 2
3. Item 3
    1. Item 3a
    2. Item 3b
"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [
                "Blockquotes",
                'Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.\n![This is an alt text.](/image/sample.webp "This is a sample image.").',
                "Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.\nYou may be using [Markdown Live Preview](https://markdownlivepreview.com/).",
                "1. Item 1\n2. Item 2\n3. Item 3\n    1. Item 3a\n    2. Item 3b"
            ],
        )

    def test_block_to_block_type_code(self):
        block_of_text = """
```
let message = 'Hello world';
alert(message);
```
"""
        block_type = block_to_block_type(block_of_text)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_paragraph(self):
        block_of_text = """
mo
> Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.  
## Second section
>> Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.message);
```
"""
        block_type = block_to_block_type(block_of_text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

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
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
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

    def test_italic_in_list_item(self):
        md = """
- Disney _didn't ruin it_ (okay, but Amazon might have)
- It created an entirely new genre of fantasy
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Disney <i>didn't ruin it</i> (okay, but Amazon might have)</li><li>It created an entirely new genre of fantasy</li></ul></div>",
        )

    def test_bold_in_list_item(self):
        md = """
1. Disney **didn't ruin it** (okay, but Amazon might have)
2. It created an entirely new genre of fantasy
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Disney <b>didn't ruin it</b> (okay, but Amazon might have)</li><li>It created an entirely new genre of fantasy</li></ol></div>",
        )

if __name__ == "__main__":
    unittest.main()