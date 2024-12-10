import matplotlib.pyplot as plt
import pandas as pd

def create_histogram(df: pd.DataFrame) -> None:
    """
    Plots a histogram of the distribution of an image region
    :param df: DataFrame with paths, shapes, and image areas
    """
    df['area'].hist(bins=30)
    plt.title('Image area distribution')
    plt.xlabel('Area')
    plt.ylabel('Freq')
    plt.savefig("test.png")