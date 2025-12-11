from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="codeanalyzer",
    version="0.1.0",
    author="CodeAnalyzer Team",
    description="A simple code analysis utility library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mcpmark-test-xjtu/CodeAnalyzer",
    packages=find_packages(),
    python_requires=">=3.7",
)

