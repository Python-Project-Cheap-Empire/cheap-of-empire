from COE.contents.entity import Entity
from .building import Building


class House(Building):
    def __init__(self):
        Building.__init__(self)
        Entity.__init__(self, "House", 0, (0, 0), 1, 1, 1, "None")

    def increase_max_population(self, amount=5) -> str:
        return "Max pop +5"

    def decrease_max_population(self, amount=-5) -> str:
        return "Max pop -5"

    def __del__(self):
        self.decrease_max_population()
        del self
