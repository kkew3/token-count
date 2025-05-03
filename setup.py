from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="token-count",
    version="0.2.3",
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        "tiktoken>=0.9",
    ],
    entry_points={
        "console_scripts": [
            "token-count = token_count:main",
        ],
    },
    scripts=[
        'scripts/update_available_models.py',
    ],
    author="Felvin",
    author_email="team@felvin.com",
    description=("Count the number of tokens in a text string or file, "
                 "similar to the Unix 'wc' utility."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/felvin-search/token-count",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
