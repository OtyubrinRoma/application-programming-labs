import cv2
import matplotlib.pyplot as plt
import numpy as np

def create_color_histogram(streams, i):
    return cv2.calcHist([streams], [i], None, [256], [0, 256])

def show_color_histogram(streams: tuple, colors: list) -> None:
    """
    Build a histogram of the intensity and frequency of the three primary colors
    :param streams:
    Three streams into which the image was divided
    :param colors:
    An array of primary colors
    """
    colors = ('g', 'b', 'r')

    for i, color in enumerate(colors):
        hist = create_color_histogram(streams, i)
        plt.plot(hist, color=color)

    plt.title('Comparative histogram of colors')
    plt.xlabel('Intensity')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()