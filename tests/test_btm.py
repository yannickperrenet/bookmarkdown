from bookmarkdown import btm
import os

import pytest


@pytest.fixture(
    params=[
        ("bookmarks-1.html", "bookmarks-1.md"),
    ],
    ids=["nested-structure"],
)
def test_case(request) -> tuple[str, str]:
    test_file = os.path.join("tests/files", request.param[0])
    answer_file = os.path.join("tests/files", request.param[1])

    with open(test_file, "r") as f:
        html_content = f.read()

    with open(answer_file, "r") as f:
        md_content = f.read()

    return html_content, md_content


def test_html_to_markdown(test_case: tuple[str, str]):
    html_content, md_content = test_case
    parser = btm.BookmarkHTMLParser()
    parser.feed(html_content)

    ans = "".join(parser.data)
    assert ans == md_content
