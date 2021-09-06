# bookmarkdown

Parse your browser's exported HTML bookmark file to Markdown.

Supported browsers: Brave.

## Installation

```bash
pip install bookmarkdown
```

## Usage

### CLI

```bash
# Convert "bookmarks.html" to markdown and output to STDOUT
btm bookmarks.html

# Convert "bookmarks.html" to markdown and write to "bookmarks.md"
btm --output=bookmarks.md bookmarks.html

# Alternatively
btm bookmarks.html > bookmarks.md
```

### Python

The `BookmarkHTMLParser` is an instance of the Python standard library's
[`HTMLParser`](https://docs.python.org/3/library/html.parser.html) and thus supports all its
methods.

```python
from bookmarkdown import btm

parser = btm.BookmarkHTMLParser()
parser.feed(html_content)

# Access the data
parser.data
```

## FAQ

### Concerns

* Minimal dependencies. `bookmarkdown` is likely to be installed on the system level Python to make
  use of the `btm` script.
* Correctness. No one likes to lose a bookmark nor a different ordering.

### Future ideas

> The current application solves my needs pretty well, but there are additional applications I can
> think of. Such as merging multiple bookmark files.

Add functionality to the CLI and Python codebase to support the following:

```bash
# Merge bookmark html-file into existing markdown file.
btm --merge=[md-file] [html-file]

btm [html-file]  # already implemented

# Read the `-r` as "reverse", i.e. instead of bookmark to markdown it
# becomes markdown to bookmark.
btm -r [md-file]

btm -r --merge=[md-file] [html-file]
```
