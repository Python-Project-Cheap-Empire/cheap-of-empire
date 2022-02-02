from COE.contents.entity_types import EntityTypes
from COE.logic.Player import Player
from .building import Building
from .granary import Granary


class SmallWall(Building):
    def __init__(self, position: tuple, player: Player):
        super().__init__(
            name="Small Wall",
            hp=100,
            positions=position,
            width=1,
            height=1,
            line_of_sight=1,
            required_building={Granary.__class__.__name__},
            required_age=2,
            required_researches={},  # Need research small wall
            researches={},
            wood_required=20,
            stone_required=0,
            construction_time=10,
            melee_armor=0,
            pierce_armor=0,
            entity_type=EntityTypes.GROUND,
            player=player,
        )
