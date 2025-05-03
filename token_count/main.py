# main.py
import argparse
import logging
import sys

from token_count import TokenCount
from .model_types import MODEL_LIST


def main():
    parser = argparse.ArgumentParser(
        description=("Count the number of tokens in a text string or file, "
                     "similar to the Unix 'wc' utility."))
    parser.add_argument(
        "-m",
        "--model_name",
        type=str,
        help="model name",
        default="gpt-3.5-turbo",
        choices=MODEL_LIST)
    parser.add_argument('file', nargs='*', help='file to count tokens in')

    args = parser.parse_args()

    token_count = TokenCount(args.model_name)

    if args.file:
        total = 0
        print_width = 4
        results = []
        for file in args.file:
            tokens = token_count.num_tokens_from_file(file)
            results.append((tokens, file))
            total += tokens
            print_width = max(print_width, len(str(total)))
        for tokens, file in results:
            print('{} {}'.format(str(tokens).rjust(print_width), file))
        if len(args.file) > 1:
            print('{} total'.format(str(total).rjust(print_width)))
    else:
        tokens = token_count.num_tokens_from_string(sys.stdin.read())
        print(tokens)


if __name__ == "__main__":
    main()
