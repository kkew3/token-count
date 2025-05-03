import logging

import tiktoken

# Create a logger
logger = logging.getLogger()


class TokenCount:
    def __init__(self, model_name="gpt-3.5-turbo"):
        '''Creating the encoding based on model name'''
        try:
            self.encoding = tiktoken.encoding_for_model(model_name)
        except Exception as e:
            logger.error("Error occurred: {}".format(e))

    def num_tokens_from_string(self, string: str) -> int:
        """Returns the number of tokens in a text string."""
        try:
            num_tokens = len(self.encoding.encode(string))
            return num_tokens
        except Exception as e:
            logger.error("Error occurred: {}".format(e))

    def num_tokens_from_file(self, file_path: str) -> int:
        """Returns the number of tokens in a text file."""
        try:
            with open(file_path, "r") as f:
                text = f.read()
            num_tokens = len(self.encoding.encode(text))
            return num_tokens
        except Exception as e:
            logger.error("Error occurred: {}".format(e))
