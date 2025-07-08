from dotenv import load_dotenv
from typing import List
from rich import print as pprint
import logging

load_dotenv()

def setup_logger(name:str, level=logging.INFO) -> logging.Logger:
    """
    Configure and return a Logger with the specified name and logging Level.

    Args:
        name (str): The name of the Logger.
        Level (int): The Logging Level (default is Logging.INFO)

    Returns:
        logging.Logger: Configured Logger instance.
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger

if __name__ == "__main__":

    logger = setup_logger(__name__, logging.INFO)
    logger.info("Starting Azure Search Practice")