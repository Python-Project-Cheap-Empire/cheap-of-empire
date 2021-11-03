from COE.contents.entity import Entity
from COE.map.enum.cell_types import CellTypes
from typing import List
from math import sqrt
import pygame
from COE.UI.window_ui import Window


class Cell:
    diagonal_nb_cells = 25

    def __init__(self, cell_type: CellTypes, entities: List[List[Entity]]):
        self.cell_type = cell_type
        self.entities = entities

    @staticmethod
    def get_pixel_cells_size(
        diagonal_nb_cells=None, display_width=None, display_height=None
    ):
        if diagonal_nb_cells is None:
            diagonal_nb_cells = Cell.diagonal_nb_cells
        if display_width is None:
            display_width = Window.width
        if display_height is None:
            display_height = Window.height
        return int(
            sqrt(
                pow(
                    sqrt(pow(display_width, 2) + pow(display_height, 2))
                    / diagonal_nb_cells,
                    2,
                )
                / 2
            )
        )

    @staticmethod
    def get_scaled_grass(pixel_cells_size=None):  # pragma: no cover
        if pixel_cells_size is None:
            pixel_cells_size = Cell.get_pixel_cells_size()
        return pygame.transform.scale(
            CellTypes.GRASS.value, (pixel_cells_size, pixel_cells_size)
        )

    @staticmethod
    def get_scaled_water(pixel_cells_size=None):  # pragma: no cover
        if pixel_cells_size is None:
            pixel_cells_size = Cell.get_pixel_cells_size()
        return pygame.transform.scale(
            CellTypes.WATER.value, (pixel_cells_size, pixel_cells_size)
        )

    @staticmethod
    def get_scaled_blocks(pixel_cells_size=None):  # pragma: no cover
        if pixel_cells_size is None:
            pixel_cells_size = Cell.get_pixel_cells_size()
        return {
            "GRASS": Cell.get_scaled_grass(pixel_cells_size),
            "WATER": Cell.get_scaled_water(pixel_cells_size),
        }
