from run import Mosaic
import argparse
from pathlib import Path
from typing import Tuple


def run(path_photos: Path, output_path: Path, tile_size: Tuple, path_tile_photos: Path):
    mo = Mosaic(tile_size=tile_size, path_photos=path_photos, path_tile_photos=path_tile_photos)
    mo.find_closest_colors()
    mo.draw_outputs(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path_photos",
                        type=str,
                        default="D:\project_artistic\Mosaic\data\inputs\input2.png",
                        help="path to folder of main photo")

    parser.add_argument("--path_tile_photos",
                        type=str,
                        default="D:\迅雷下载\ImageNet\data\ImageNet2013\ILSVRC2013_DET_val",
                        help="path to folder of tile photos folder")

    parser.add_argument("--output_path",
                        type=str,
                        default="D:\project_artistic\Mosaic\data\output.png",
                        help="path of output")
    parser.add_argument("--tile_size",
                        type=lambda s: [int(item) for item in s.split(',')],
                        default="20, 20",
                        help="resize real image to tile size")
    args = parser.parse_args()
    run(path_photos=Path(args.path_photos), output_path=Path(args.output_path),
        tile_size=args.tile_size, path_tile_photos=Path(args.path_tile_photos))
