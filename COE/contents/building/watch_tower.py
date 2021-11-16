from COE.contents.entity import Entity
from .building import Building


class WatchTower(Building):
    def __init__(self):
        Building.__init__(self)
        Entity.__init__(self, "Watch Tower", 1020, (0, 0), 1, 1, 6, "None")

    def attack(
        self,
        e: Entity(
            name="Enemy",  # noqa
            hp=0,
            positions=(0, 0),
            height=1,
            width=1,
            line_of_sight=1,
            img="None",
        ),
    ) -> str:
        return "Attacking..."
