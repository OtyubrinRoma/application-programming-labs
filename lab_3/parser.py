import argparse

def create_parse() -> argparse.Namespace:
    """
    Read arguments from terminal
    :return: arguments
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("dir_img",type=str, help="path to image")
        parser.add_argument("dir_res", type=str, help="path to save result")
        return parser.parse_args()
    except:
        raise SyntaxError("Command line arguments must not be empty")