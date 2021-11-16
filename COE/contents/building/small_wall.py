from COE.contents.entity import Entity
from .building import Building


# Required Granary to build


class SmallWall(Building):
    def __init__(self):
        Building.__init__(self)
        Entity.__init__(self, "Small Wall", 240, (0, 0), 1, 1, 1, "None")
