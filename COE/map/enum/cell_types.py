from enum import Enum
import pygame
import os


class CellTypes(Enum):
    GRASS = pygame.image.load(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "assets", "grass.png")
        )
    )
    WATER = pygame.image.load(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "assets", "water.jpg")
        )
    )
    DESERT = 3
    ICE = 4
