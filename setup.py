from pathlib import Path
from setuptools import setup

# The long_description field is used by PyPI when you publish a package,
# to build its project page.
long_description = Path("README.md").read_text(encoding="utf-8")

setup(
    name="bookmarkdown",
    description="Parse your browser's exported HTML bookmark file to Markdown.",
    long_description=long_description,
    version="0.1.0",
    author="Yannick Perrenet",
    license="MIT",
    url="https://github.com/yannickperrenet/bookmarkdown",
    keywords="bookmarks markdown parser",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
    ],
    # Add the CLI script to PATH on installation.
    # scripts=["bin/btm"],
)
