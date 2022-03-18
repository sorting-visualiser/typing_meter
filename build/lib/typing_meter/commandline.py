"""
Start of app.

Parses command line arguments and decides and fills text accordingly.
"""

import argparse
import os
import random
import sys

import typing_meter
import typing_meter.database
from typing_meter.history import show_history


def resolve_commandline_arguments():
    """Parse CLI arguments and return practice text details.

    Returns:
        (str, Union[str, int]): Tuple of text content and text ID.
    """
    opt = parse_arguments()
    if opt.version:
        display_version()
        sys.exit(0)

    elif opt.history is not None:
        show_history(opt.history)
        sys.exit(0)

    elif opt.file:
        text, text_id = load_text_from_file(opt.file)

    elif opt.id:
        text, text_id = load_from_database(opt.id)

    elif opt.difficulty:
        text, text_id = load_based_on_difficulty(opt.difficulty)

    else:
        text, text_id = load_based_on_difficulty()

    return text, text_id


def parse_arguments():
    """Parse command line arguments.

    Returns:
        str: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Process typing_meter command line arguments",
    )

    parser.add_argument(
        "-V",
        "--version",
        default=False,
        action="store_true",
        help="Show typing_meter version",
    )

    parser.add_argument(
        "-f",
        "--file",
        metavar="FILENAME",
        default=None,
        type=str,
        help="File to use text from as sample text",
    )

    parser.add_argument(
        "-i",
        "--id",
        metavar="id",
        default=None,
        type=int,
        help="ID to retrieve text from database",
    )

    parser.add_argument(
        "-d",
        "--difficulty",
        metavar="N",
        default=2,
        type=int,
        help="Choose difficulty within range 1-5",
    )

    parser.add_argument(
        "-H",
        "--history",
        nargs="?",
        default=None,
        const=-1,
        type=int,
        help="Show typing_meter score history",
    )

    return parser.parse_args()


def display_version():
    """Display version."""
    print(f"typing_meter version {typing_meter.__version__}")


def load_text_from_file(file_path):
    """Load file contents.

    Args:
        file_path (str): Full path to text to load.

    Returns:
        (str, str): Tuple of text content followed by file path.
    """
    if os.path.isfile(file_path):
        with open(file_path, encoding="utf-8") as file:
            text = file.read()
            filename = os.path.basename(file_path)
        return text, filename

    print("Cannot open file -", file_path)
    sys.exit(0)


def load_from_database(text_id):
    """Load given text from database with given id.

    Args:
        text_id (int): Row identifier of database text to load.

    Returns:
        (str, int): Tuple of text content followed by DB row identifier.
    """
    row_count = 6000
    if 1 <= text_id <= row_count:
        text = typing_meter.database.fetch_text_from_id(text_id)
        return text, text_id

    print("ID must be in range [1,6000]")
    sys.exit(1)


def load_based_on_difficulty(difficulty_level=random.randrange(1, 6)):
    """
    Load text of given difficulty from database if parameter is passed.

    Defaults to random difficulty level when none is provided.

    Args:
        difficulty_level (int): difficulty level in a range of 1 - 5

    Returns:
        (str, int): Tuple of text content followed by DB row identifier.
    """
    max_level = 5

    if 1 <= difficulty_level <= max_level:
        # Each difficulty section has 6000/5 = 1200 texts each
        upper_limit = difficulty_level * 1200
        lower_limit = upper_limit - 1200 + 1

        text_id = random.randrange(lower_limit, upper_limit + 1)
        text = typing_meter.database.fetch_text_from_id(text_id)

        return text, text_id

    print("Select a difficulty level in range [1,5]")
    sys.exit(1)
