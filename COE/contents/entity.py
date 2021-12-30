# coding: utf-8
import os.path
from pathlib import Path
import pygame.surface
from pygame.sprite import Sprite

"""
    Contains the Class Entity, from which all content class inherit.
"""


class Entity:
    def __init__(
        self,
        name: str,
        hp: int,
        positions: tuple,
        height: int,
        width: int,
        line_of_sight: int,
        **kwargs
    ):  # pragma: no cover
        self.name = name
        self.hp = hp
        self.positions = positions
        self.height = height
        self.width = width
        self.line_of_sight = line_of_sight
        self.img_path = os.path.join(Path(__file__).parent.parent, "assets/default.png")
        self.image = self.img_path
