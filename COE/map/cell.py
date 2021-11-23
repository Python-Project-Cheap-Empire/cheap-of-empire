from COE.contents.entity import Entity
from COE.map.enum.cell_types import CellTypes
from typing import List
import pygame


class Cell:
    def __init__(self, cell_type: CellTypes, entities: List[List[Entity]]):
        self.cell_type = cell_type
        self.entities = entities

    @staticmethod
    def get_pixel_cells_size():
        return 64, 32

    @staticmethod
    def get_scaled_grass(
        width_pixel_size=None, height_pixel_size=None
    ):  # pragma: no cover
        if width_pixel_size is None or height_pixel_size is None:
            width_pixel_size, height_pixel_size = Cell.get_pixel_cells_size()
        return pygame.transform.scale(
            CellTypes.GRASS.value, (width_pixel_size, height_pixel_size)
        )

    @staticmethod
    def get_scaled_water(
        width_pixel_size=None, height_pixel_size=None
    ):  # pragma: no cover
        if width_pixel_size is None or height_pixel_size is None:
            width_pixel_size, height_pixel_size = Cell.get_pixel_cells_size()
        return pygame.transform.scale(
            CellTypes.WATER.value, (width_pixel_size, height_pixel_size)
        )

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
