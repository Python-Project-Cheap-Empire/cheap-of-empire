from COE.contents.entity import Entity
from .building import Building


# Required Granary to build


class SmallWall(Building):
    def __init__(self, position: tuple):
        super().__init__(
            name="Small Wall",
            hp=100,
            positions=position,
            width=1,
            height=1,
            line_of_sight=1,
        )
