from image_iterator import Iterator
from parser import create_parse
from image_downloader import img_download
from annotation import create_annotation
import os

def main() -> None:
    try:
        args = create_parse()
        img_download(args.keyword, args.num_img, args.dir_img)
        create_annotation(args.dir_img, args.dir_annotation)
        img_iterator = Iterator(args.dir_annotation)
        for path in img_iterator:
            print(path)
    except Exception as exc:
        print("Error:", exc)

if __name__ == "__main__":
    main()