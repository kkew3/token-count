# Token Count

Token Count is a command-line utility that counts the number of tokens in a text string, file, or directory, similar to the Unix [`wc`](https://man7.org/linux/man-pages/man1/wc.1.html) utility. It uses the OpenAI [`tiktoken`](https://github.com/openai/tiktoken) library for tokenization and is compatible with GPT-3.5-turbo or any other OpenAI model token counts.

## Installation

To install Token Count, run the following command in your terminal:

```bash
pip install 'git+https://github.com/kkew3/token-count.git'
```

You may also install as an executable using [`pipx`](https://pipx.pypa.io/stable/) or [`uv`](https://docs.astral.sh/uv/):

```bash
uv tool install 'git+https://github.com/kkew3/token-count.git'
```

## Usage - Python Library

```python
from token_count import TokenCount
tc = TokenCount(model_name="gpt-3.5-turbo")
text = "Your text here"
tokens = tc.num_tokens_from_string(text)
print(f"Tokens in the string: {tokens}")

file_path = "path/to/your/file.txt"
tokens = tc.num_tokens_from_file(file_path)
print(f"Tokens in the file: {tokens}")
```

## Usage - Command Line

Token Count has three main options:

Count tokens in a text string:
```bash
echo -n "Your text here" | token-count
```

Count tokens in a file:

```bash
token-count path/to/your/file.txt
```

Additionally, you can provide any OpenAI model(gpt-4) to get token count according to the model. By default it uses "gpt-3.5-turbo".

```bash
echo -n "Your text here" | token-count --model_name "gpt-4"
```

## License

This project is licensed under the MIT License.
