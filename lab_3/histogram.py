import cv2
import matplotlib.pyplot as plt
import numpy as np

def create_color_histogram(streams: tuple, colors: list) -> None:
    """
    Build a histogram of the intensity and frequency of the three primary colors
    :param streams:
    Three streams into which the image was divided
    :param colors:
    An array of primary colors
    """
    x = np.arange(256)
    bar_width = 0.5
    plt.figure(figsize = (10, 6))
    for i, (streams, colors) in enumerate(zip(streams, colors)):
        hist = cv2.calcHist([streams], [0], None, [256], [0, 256]).flatten()
        plt.bar(x + i * bar_width, hist, width = bar_width, label = colors, alpha = 0.2)

    plt.title('Comparative histogram of colors')
    plt.xlabel('Intensity')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()