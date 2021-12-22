from .building import Building
from .town_center import TownCenter


class House(Building):
    def __init__(self, position: tuple):
        super().__init__(
            name="House",
            hp=75,
            positions=position,
            height=1,
            width=1,
            line_of_sight=4,
            required_building={TownCenter.__class__.__name__},
            required_age=2,
            required_researches={},
        )

    def increase_max_population(self, amount=5) -> str:
        return "Max pop +5"

    def decrease_max_population(self, amount=-5) -> str:
        return "Max pop -5"

    def __del__(self):
        self.decrease_max_population()
        del self
