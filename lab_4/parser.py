import argparse
import os

def create_parse() -> argparse.Namespace:
    """
    Parses command-line arguments to retrieve the path to the annotation file.
    :return: Parsed arguments containing the annotation file path.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("annotation_path", type=str, help="Path to the annotation")

    args = parser.parse_args()

    if not os.path.exists(args.annotation_path):
        raise Exception("The annotation file was not found!")

    return args