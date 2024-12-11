from histogram import create_histogram
from processor import add_image_shape, compute_area, create_dataframe, get_statistics, filter_images
from parser import create_parse

def main():
    try:
        args = create_parse()
        annotation_file = args.annotation_path
        df = create_dataframe(annotation_file)
        df_with_shapes = add_image_shape(df)
        print("Statistics:\n", get_statistics(df_with_shapes), "\n")
        print("DataFrame:\n", df_with_shapes)
        max_height, max_width = 1000, 1000
        filtered_df = filter_images(df_with_shapes, max_width, max_height)
        print("Filtered DataFrame:\n", filtered_df, "\n")
        df_sorted = compute_area(filtered_df).sort_values(by='area')
        print("Filtered DataFrame by area:\n", df_sorted, "\n")
        create_histogram(df_sorted)
    except Exception as exc:
        print("Error:", exc)

if __name__ == "__main__":
    main()