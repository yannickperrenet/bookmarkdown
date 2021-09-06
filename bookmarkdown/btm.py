#!/usr/bin/env python3

from __future__ import annotations

from html.parser import HTMLParser
from typing import Optional
import argparse


class BookmarkHTMLParser(HTMLParser):
    """Parse an HTML bookmarks file to Markdown.

    Browsers allow you to export its defined bookmarks in HTML format.
    This class parses such a file's content to Markdown.

    Note:
        The exported HTML is auto-generated and thus new browser
        versions could break compatibility.

    Attributes:
        data: A list of strings where each element in the list
            represents a parsed Markdown line. This includes newline
            characters. For example::

                ["\n#Bookmarks\n\n", "* [text](link)\n"]

    Examples:
        Parse the content of an exported bookmarks HTML file to a
        markdown string and reset the parser afterwards for successive
        use.

        >>> html_content = ""  # string content of HTML file
        >>> parser = BookmarkHTMLParser()
        >>> parser.feed(html_content)
        >>> markdown = "".join(parser.data)  # could write to file
        >>> parser.reset()
        >>> parser.data == []
        ... True

    """

    def __init__(self):
        super().__init__(convert_charrefs=True)

        self.data: list[str] = []
        self._level = 1
        self._latest_tag: Optional[str] = None
        self._latest_tag_attrs: Optional[list[tuple[str, str]]] = None

    def handle_starttag(self, tag: str, attrs: Optional[list[tuple[str, str]]]) -> None:
        self._latest_tag = tag
        self._latest_tag_attrs = attrs

        if tag == "dl":
            self._level += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "dl":
            self._level -= 1

    def handle_data(self, data: str) -> None:
        tag = self._latest_tag
        attrs = self._latest_tag_attrs

        if tag is None:
            tmp = None
        elif tag in ["h1", "h3"]:
            tmp = "\n" if self.data else ""
            tmp += self._level * "#" + f" {data}\n\n"
        elif tag == "a":
            # We know for certain that the `<a>` tag contains a `href`
            # because we are parsing an auto-generated bookmarks file.
            href = ""
            for attr in attrs:
                if attr[0] == "href":
                    href = attr[1]

            tmp = f"* [{data}]({href})\n"
        else:
            tmp = None

        if tmp is not None:
            self.data.append(tmp)

        # Dereference attributes after their data has been handled,
        # because `HTMLParser.handle_data` is called again with string
        # like e.g. `"\n   "` due to formatting of the fed (through
        # `HTMLParser.feed`) HTML file.
        # NOTE: Because super() was initialized with
        # `convert_charrefs=True` we know that `data` is not split in
        # chunks. Thus it is safe to dereference the following
        # attributes.
        self._latest_tag = None
        self._latest_tag_attrs = None

    def reset(self):
        super().reset()

        self.data = []
        self._level = 1
        self._latest_tag = None
        self._latest_tag_attrs = None


def _parse_args():
    parser = argparse.ArgumentParser(
        description=("Parse your browser's exported HTML bookmark file to Markdown.")
    )
    parser.add_argument("file", help="The HTML file containing the exported bookmarks")
    parser.add_argument(
        "--output",
        help="File to output Markdown to (defaults to STDOUT)",
        default="stdout",
    )
    args = parser.parse_args()

    return args


def main():
    args = _parse_args()

    with open(args.file, "r") as f:
        html_content = f.read()

    parser = BookmarkHTMLParser()
    parser.feed(html_content)
    ans = "".join(parser.data)

    if args.output.lower() == "stdout":
        print(ans)
    else:
        with open(args.output, "w") as f:
            f.write(ans)


if __name__ == "__main__":
    main()
