from pathlib import Path
from PIL import Image
from scipy import spatial
import numpy as np
from typing import Tuple


class Mosaic(object):
    def __init__(self, tile_size: Tuple, path_photos: Path):
        self.tile_size = tile_size
        self.path_photos = path_photos

        self._preprocess_main_photos()
        self._preprocess_tile_photos()

    @property
    def tile_photos(self):
        return self.path_photos.parent / "tile_photos"

    def _preprocess_main_photos(self):
        main_photo = Image.open(str(self.path_photos))
        self.width = int(np.round(main_photo.size[0] / self.tile_size[0]))
        self.height = int(np.round(main_photo.size[1] / self.tile_size[1]))

        self.resized_photo = main_photo.resize((self.width, self.height))

        self.closest_tiles = np.zeros((self.width, self.height), dtype=np.uint32)
        self.output = Image.new("RGB", main_photo.size)

    def _preprocess_tile_photos(self):
        self.colors = []
        self.tiles = []
        for p in self.tile_photos.iterdir():
            tile = Image.open(str(p)).resize(self.tile_size)
            mean_color = np.array(tile).mean(axis=0).mean(axis=0)
            self.tiles.append(tile)
            self.colors.append(mean_color)

    def find_closest_colors(self):
        tree = spatial.KDTree(self.colors)
        for i in range(self.width):
            for j in range(self.height):
                pixel = self.resized_photo.getpixel((i, j))  # Get the pixel color at (i, j)
                closest = tree.query(pixel)  # return (distance, index)
                self.closest_tiles[i, j] = closest[1]  # get index of tile correspond

    def draw_outputs(self, output_name: Path):
        for i in range(self.width):
            for j in range(self.height):
                x, y = i * self.tile_size[0], j * self.tile_size[1]
                index = self.closest_tiles[i, j]
                self.output.paste(self.tiles[index], (x, y))
        self.output.save(output_name)