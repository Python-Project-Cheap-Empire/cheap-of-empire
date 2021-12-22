# coding: utf-8
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
        img,
        **kwargs
    ):  # pragma: no cover

        self.name = name
        self.hp = hp
        self.positions = positions
        self.height = height
        self.width = width
        self.line_of_sight = line_of_sight
        self.img = img
