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
    ):
        self.name = name
        self.positions = positions
        self.height = height
        self.width = width
        self.line_of_sight = line_of_sight
        self.img = img
