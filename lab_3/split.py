import cv2
import numpy as np

def rgb_split(img: np.ndarray) -> tuple:
    """
    Splits the image into red, blue and green parts
    :param img:
    Variable that stores the image
    :return:
    three colors
    """
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    r, g, b = cv2.split(rgb_img)
    return r, g, b