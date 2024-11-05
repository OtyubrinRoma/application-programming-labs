import os

from icrawler.builtin import GoogleImageCrawler

def img_download(keyword: str, num: int, img_path: str) -> None:
    """
    Downloads images according to specified parameters
    :param keyword: key word to search images
    :param num: number of images for downloading
    :param img_path: path to save images
    :return:
    """
    if not os.path.isdir(img_path):
        os.makedirs(img_path)
    google_crawler = GoogleImageCrawler(storage={"root_dir": img_path})
    google_crawler.crawl(keyword=keyword, max_num=num)