import cv2
import numpy as np

def show_and_write(img: np.ndarray, path: str) -> None:
    """
    Saves and displays an image to the user
    :param img:
    The image to process
    :param path:
    The path to save the image
    """
    if not (cv2.imwrite(path, img)):
        raise SystemError("Unable to save image to directory")
    cv2.imshow(path, img)