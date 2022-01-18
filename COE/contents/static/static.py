from pygame import image
import glob
from COE.map.cell import Cell


class Static:  # pragma: no cover
    def __init__(self) -> None:
        self.entities_pos_dict = {"tree": (11, -55), "villager": (25, -50)}
        self.cells_size = Cell.get_pixel_cells_size()
        self.scaled_blocks = Cell.get_scaled_blocks()
        self.images = glob.glob("**/*.png", recursive=True)
        self.image_cache = {
            key[11:-4].lower(): image.load(key).convert_alpha() for key in self.images
        }
        self.image_cache.update(self.scaled_blocks)
        self.width_cells_size = self.cells_size[0]
        self.height_cells_size = self.cells_size[1]
        self.half_width_cells_size = self.width_cells_size / 2
        self.half_height_cells_size = self.height_cells_size / 2
