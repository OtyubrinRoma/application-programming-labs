from icrawler.builtin import GoogleImageCrawler
import argparse
import os

def img_download(keyword, num, path) -> None:

    google_crawler = GoogleImageCrawler(storage={'root_dir': path})
    google_crawler.crawl(keyword=keyword, max_num=num)

def create_parse() -> argparse.Namespace:
    """
    Read arguments from terminal
    :return: arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="key word to search images", default="stalker")
    parser.add_argument("num_img", type=int, help="number of images for downloading", default=100)
    parser.add_argument("dir_path", type="str", help="path to save images", default="./images")
    parser.add_argument("dir_annotation", type="str", help = "path to save annotation file", default="annotation.csv")
    return parser.parse_args()

def main() -> None:
    try:
        args = create_parse()
        img_download(args.keyword, args.num_img, args.dir_path)
    except:
        print("Error")

if __name__ == "__main__":
    main()