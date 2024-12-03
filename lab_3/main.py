import cv2

from histogram import show_color_histogram
from parser import create_parse
from split import rgb_split
from save import save_rgb

def main() -> None:
    try:
        args = create_parse()
        img = cv2.imread(args.dir_img)
        print("Image size: ", img.shape)
        cv2.imshow(args.dir_img, img)
        cv2.waitKey(0)
        colors = ["red", "green", "blue"]
        color_streams = rgb_split(img)
        show_color_histogram(img, colors)
        for i, j in enumerate(color_streams):
            save_rgb(j, args.dir_res + "\\" + colors[i] + ".jpg")
            cv2.waitKey(0)
    except Exception as exc:
        print("Error:", exc)


if __name__ == "__main__":
    main()
