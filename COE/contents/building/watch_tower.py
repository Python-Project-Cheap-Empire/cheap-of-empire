from COE.contents.entity import Entity
from .building import Building
from .granary import Granary


class WatchTower(Building):
    def __init__(self, position: tuple):
        self.damage = 3
        self.range = 5
        self.attack_speed = 1.5
        super().__init__(
            name="Watch Tower",
            hp=125,
            positions=position,
            height=1,
            width=1,
            line_of_sight=6,
            required_building={Granary.__class__.__name__},
            required_age=2,
            required_researches={},  # Watch tower
            researches={},
            stone_required=150,
            wood_required=0,
            time_construction=30,
        )

    def attack(
        self,
        target: Entity,
    ) -> str:
        return "Attacking..."
