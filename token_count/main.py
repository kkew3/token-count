# main.py
import argparse
import sys

from token_count import TokenCount
from .model_types import MODEL_LIST


def main():
    parser = argparse.ArgumentParser(
        description=("Count the number of tokens in a text string or file, "
                     "similar to the Unix 'wc' utility."))
    default_model = 'gpt-3.5-turbo'
    parser.add_argument(
        "-m",
        "--model_name",
        type=str,
        help=f"model name [default: {default_model}]",
        default=default_model,
        choices=MODEL_LIST)
    parser.add_argument(
        '-T',
        '--files-from',
        metavar='FILENAME',
        help=('the list of files to count tokens will be read from FILENAME, '
              'or stdin if `-` is given; '
              'this option takes precedence over FILE if both are provided'))
    parser.add_argument(
        '--null',
        action='store_true',
        help=('used with --files-from, such that null character '
              'rather than newline will be used as FILE separator'))
    parser.add_argument(
        'file', metavar='FILE', nargs='*', help='file to count tokens in')

    args = parser.parse_args()

    token_count = TokenCount(args.model_name)

    if args.files_from is not None:
        sep = '\0' if args.null else '\n'
        if args.files_from == '-':
            file_list = sys.stdin.read().rstrip(sep).split(sep)
        else:
            with open(args.files_from, encoding='utf-8') as infile:
                file_list = infile.read().rstrip(sep).split(sep)
    elif args.file:
        file_list = args.file
    else:
        file_list = None
    if file_list:
        total = 0
        print_width = 4
        results = []
        for file in file_list:
            tokens = token_count.num_tokens_from_file(file)
            results.append((tokens, file))
            total += tokens
            print_width = max(print_width, len(str(total)))
        for tokens, file in results:
            print('{} {}'.format(str(tokens).rjust(print_width), file))
        if len(file_list) > 1:
            print('{} total'.format(str(total).rjust(print_width)))
    else:
        tokens = token_count.num_tokens_from_string(sys.stdin.read())
        print(tokens)
