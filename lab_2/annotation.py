import os
import csv

def create_annotation(dir_img: str, dir_annotation: str):
    """
    Generate an annotation as a csv file containing the absolute and relative path to each image
    :param dir_img: path to images
    :param dir_annotation: path to the annotation file
    :return:
    """
    try:
        path, file_name = os.path.split(dir_annotation)
        if not os.path.isdir(path):
            raise NotADirectoryError("Path missing")
        with open(dir_annotation, "w", newline="", encoding="utf-8") as annotation:
            writer = csv.writer(annotation)
            writer.writerow(["relative path", "absolute path"])
            for file in os.listdir(dir_img):
                rel_path = os.path.relpath(os.path.join(dir_img, file), start="./")
                abs_path = os.path.abspath(os.path.join(dir_img, file))
                writer.writerow([rel_path, abs_path])
    except:
        raise SystemError("Failure to create file")