from COE.contents.entity_types import EntityTypes
from COE.logic.Player import Player
from .building import Building
from .town_center import TownCenter


class House(Building):
    def __init__(self, position: tuple, player: Player):
        super().__init__(
            name="House",
            hp=75,
            positions=position,
            height=2,
            width=2,
            line_of_sight=4,
            required_building={TownCenter.__class__.__name__},
            required_age=1,
            required_researches={},
            wood_required=30,
            stone_required=0,
            construction_time=15,
            entity_type=EntityTypes.GROUND,
            melee_armor=-2,
            pierce_armor=7,
            player=player,
        )

    def increase_max_population(self, amount=5) -> str:
        return "Max pop +5"

    def decrease_max_population(self, amount=-5) -> str:
        return "Max pop -5"

    def __del__(self):
        self.decrease_max_population()
        del self
