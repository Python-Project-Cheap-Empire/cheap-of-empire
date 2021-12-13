from COE.contents.entity import Entity
from .building import Building


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
        )

    def attack(
        self,
        e: Entity(
            name="Enemy",  # noqa
            hp=0,
            positions=(0, 0),
            height=1,
            width=1,
            line_of_sight=1,
        ),
    ) -> str:
        return "Attacking..."
