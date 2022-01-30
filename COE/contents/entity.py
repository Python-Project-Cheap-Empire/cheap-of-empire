# coding: utf-8


"""
    Contains the Class Entity, from which all content class inherit.
"""


from COE.contents.entity_types import EntityTypes


class Entity:
    def __init__(
        self,
        name: str,
        hp: int,
        positions: tuple,
        height: int,
        width: int,
        line_of_sight: int,
        entity_type: EntityTypes,
        sub_entities,
        is_master: bool = True,
        master=None,
        **kwargs,
    ):  # pragma: no cover
        self.name = name
        self.hp = hp
        self.positions = positions
        self.height = height
        self.width = width
        self.line_of_sight = line_of_sight
        self.entity_type = entity_type
        self.is_master = is_master
        self.master = master
        self.sub_entities = sub_entities
