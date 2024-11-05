import argparse

def create_parse() -> argparse.Namespace:
    """
    Read arguments from terminal
    :return: arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="key word to search images")
    parser.add_argument("num_img", type=int, help="number of images for downloading")
    parser.add_argument("dir_img", type=str, help="path to save images")
    parser.add_argument("dir_annotation", type=str, help = "path and name to save annotation file")
    return parser.parse_args()