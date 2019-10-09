from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="loggable-decorator",
    packages=["loggable"],
    version="1.1.1",
    description="Add a logger attribute to class decorated",
    author="Luis Fernando Gomes",
    author_email="luiscoms@ateliedocodigo.com.br",
    url="https://github.com/ateliedocodigo/python-loggable-decorator",
    download_url="https://github.com/ateliedocodigo/python-loggable-decorator/tarball/1.1.1",  # noqa: E501
    keywords=["logging"],
    classifiers=[],
    long_description=long_description,
    long_description_content_type="text/markdown"
)
