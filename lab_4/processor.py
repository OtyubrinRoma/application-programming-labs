import cv2
import os
import pandas as pd

def create_dataframe(annotation_path : str) -> pd.DataFrame:
    """
    Creates a DataFrame with 2 columns
    :param annotation_path: Path to annotation file.
    :return: DataFrame with two columns
    """
    if os.path.isfile(annotation_path):
        df = pd.read_csv(annotation_path)
        return df
    else:
        raise FileNotFoundError


def add_image_shape(df : pd.DataFrame) -> pd.DataFrame:
    """
    Adds image size information to a DataFrame.
    :param df: DataFrame with two columns
    :return: DataFrame with image paths and shapes
    """
    height, width, depth = [],[],[]
    for absolute in df["absolute path"]:
        img = cv2.imread(absolute)
        if os.path.isfile(absolute) and img is not None:
            hwd = img.shape
            height.append(hwd[0])
            width.append(hwd[1])
            depth.append(hwd[2])
        else:
            raise FileNotFoundError

    return df.assign(height = height, width = width, depth = depth)


def compute_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the area of images and adds it to the column
    :param df: DataFrame with image paths and shapes
    :return: DataFrame with image paths, shapes and areas
    """
    return df.assign(area = df['height'] * df['width'])


def get_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates statistics for columns containing image size information.
    :param df: DataFrame with image paths and shapes
    :return: DataFrame statistics with image size information.
    """
    return df[['height', 'width', 'depth']].describe()


def filter_images(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Filters a DataFrame by the specified parameters
    :param df: DataFrame with image paths and shapes
    :param max_width: Maximum filter width
    :param max_height: Maximum filter height.
    :return: Filters the DataFrame by the specified parameters.
    """
    return df[(df['height'] <= max_height) & (df['width'] <= max_width)]