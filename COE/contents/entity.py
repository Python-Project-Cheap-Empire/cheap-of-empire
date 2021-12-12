# coding: utf-8
import os.path
from pathlib import Path
import pygame.surface
from pygame.sprite import Sprite

"""
    Contains the Class Entity, from which all content class inherit.
"""


class Entity(Sprite):
    def __init__(
        self,
        name: str,
        hp: int,
        positions: tuple,
        height: int,
        width: int,
        line_of_sight: int,
    ):  # pragma: no cover
        Sprite.__init__(self)
        self.name = name
        self.hp = hp
        self.positions = positions
        self.height = height
        self.width = width
        self.line_of_sight = line_of_sight
        self.img_path = os.path.join(Path(__file__).parent.parent, "assets/default.png")
        self.image = pygame.image.load(self.img_path)
        self.rect = self.image.get_rect()

    def __getstate__(self):
        # Copy the object's state from self.__dict__ which contains
        # all our instance attributes. Always use the dict.copy()
        # method to avoid modifying the original state.
        state = self.__dict__.copy()
        # Remove the unpicklable entries.
        del state["image"]
        del state["rect"]
        return state

    def __setstate__(self, state):
        # Restore instance attributes.
        self.__dict__.update(state)

        self.image = pygame.image.load(self.img_path)
        self.rect = self.image.get_rect()
