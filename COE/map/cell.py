from COE.contents.entity import Entity
from COE.map.enum.cell_types import CellTypes
import pygame
import os


class Cell:
    def __init__(self, cell_type: CellTypes, entity: Entity):
        self.cell_type = cell_type
        self.entity = entity

    @staticmethod
    def get_pixel_cells_size():
        return 80, 40

    @staticmethod
    def get_assets_img():  # pragma: no cover
        return {
            CellTypes.GRASS.name: pygame.image.load(
                os.path.abspath(
                    os.path.join(os.path.dirname(__file__), "..", "assets", "grass.png")
                )
            ).convert_alpha(),
            CellTypes.WATER.name: pygame.image.load(
                os.path.abspath(
                    os.path.join(os.path.dirname(__file__), "..", "assets", "water.png")
                )
            ).convert_alpha(),
        }

    @staticmethod
    def get_scaled_grass(
        width_pixel_size=None, height_pixel_size=None
    ):  # pragma: no cover
        if width_pixel_size is None or height_pixel_size is None:
            width_pixel_size, height_pixel_size = Cell.get_pixel_cells_size()
        return pygame.transform.scale(
            Cell.get_assets_img().get(CellTypes.GRASS.name),
            (width_pixel_size, height_pixel_size),
        )

    @staticmethod
    def get_scaled_water(
        width_pixel_size=None, height_pixel_size=None
    ):  # pragma: no cover
        if width_pixel_size is None or height_pixel_size is None:
            width_pixel_size, height_pixel_size = Cell.get_pixel_cells_size()
        return pygame.transform.scale(
            Cell.get_assets_img().get(CellTypes.WATER.name),
            (width_pixel_size, height_pixel_size),
        ).convert_alpha()

    @staticmethod
    def get_scaled_blocks(
        width_pixel_size=None, height_pixel_size=None
    ):  # pragma: no cover
        if width_pixel_size is None or height_pixel_size is None:
            width_pixel_size, height_pixel_size = Cell.get_pixel_cells_size()
        return {
            "GRASS": Cell.get_scaled_grass(width_pixel_size, height_pixel_size),
            "WATER": Cell.get_scaled_water(width_pixel_size, height_pixel_size),
        }
