from icrawler.builtin import GoogleImageCrawler
from iterator import Iterator
import argparse
import os
import csv

def create_parse() -> argparse.Namespace:
    """
    Read arguments from terminal
    :return: arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="key word to search images")
    parser.add_argument("num_img", type=int, help="number of images for downloading")
    parser.add_argument("dir_img", type=str, help="path to save images")
    parser.add_argument("dir_annotation", type=str, help = "path to save annotation file")
    return parser.parse_args()

def img_download(keyword: str, num: int, img_path: str) -> None:
    """
    Downloads images according to specified parameters
    :param keyword: key word to search images
    :param num: number of images for downloading
    :param img_path: path to save images
    :return:
    """
    if not os.path.isdir(img_path):
        os.mkdir(img_path)
    google_crawler = GoogleImageCrawler(storage={'root_dir': img_path})
    google_crawler.crawl(keyword=keyword, max_num=num)

def create_annotation(dir_img: str, dir_annotation: str):
    with open(dir_annotation, 'w', newline='', encoding='utf-8') as annotation:
        writer = csv.writer(annotation)
        writer.writerow(["relative path", "absolute path"])
        for file in os.listdir(dir_img):
            rel_path = os.path.relpath(os.path.join(dir_img, file), start='./')
            abs_path = os.path.abspath(os.path.join(dir_img, file))
            writer.writerow([rel_path, abs_path])

def main() -> None:
    args = create_parse()
    img_download(args.keyword, args.num_img, args.dir_img)
    create_annotation(args.dir_img, args.dir_annotation)
    img_iterator = Iterator(args.dir_annotation)
    for path in img_iterator:
        print(path)

if __name__ == "__main__":
    main()