from Mosaic.mosaic.run import Mosaic

import argparse
from pathlib import Path


def run(path_photos: Path, output_path: Path):
    mo = Mosaic(tile_size=(20, 20), path_photos=path_photos)
    mo.find_closest_colors()
    mo.draw_outputs(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path_photos",
                        type=str,
                        default="D:\project_artistic\Mosaic\data\img.PNG",
                        help="path to folder of main photo and tile photos")

    parser.add_argument("--output_path",
                        type=str,
                        default="D:\project_artistic\Mosaic\data\output.png",
                        help="path of output")
    args = parser.parse_args()
    run(path_photos=Path(args.path_photos), output_path=Path(args.output_path))
