from COE.contents.entity import Entity
from COE.map.enum.cell_types import CellTypes
from typing import List
from math import sqrt
import pygame


class Cell:
    diagonal_nb_cells = 25

    def __init__(self, cell_type: CellTypes, entities: List[List[Entity]]):
        self.cell_type = cell_type
        self.entities = entities

    @staticmethod
    def get_pixel_cells_size(diagonal_nb_cells, display_width, display_height):
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
    def get_scaled_grass(pixel_cells_size):  # pragma: no cover
        return pygame.transform.scale(
            CellTypes.GRASS.value, (pixel_cells_size, pixel_cells_size)
        )

    @staticmethod
    def get_scaled_water(pixel_cells_size):  # pragma: no cover
        return pygame.transform.scale(
            CellTypes.WATER.value, (pixel_cells_size, pixel_cells_size)
        )

    @staticmethod
    def get_scaled_blocks(pixel_cells_size):  # pragma: no cover
        return {
            "GRASS": Cell.get_scaled_grass(pixel_cells_size),
            "WATER": Cell.get_scaled_water(pixel_cells_size),
        }
