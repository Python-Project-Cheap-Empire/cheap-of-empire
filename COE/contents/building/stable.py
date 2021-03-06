from COE.contents.entity_types import EntityTypes
from COE.logic.Player import Player
from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding
from .barrack import Barrack


class Stable(MilitaryBuilding, TechnologyBuilding):
    def __init__(self, position: tuple, player: Player):
        super().__init__(
            name="Stable",
            hp=350,
            positions=position,
            height=3,
            width=3,
            line_of_sight=4,
            required_building={Barrack.__class__.__name__},
            required_age=2,
            required_researches={},
            researches={},
            wood_required=150,
            stone_required=0,
            construction_time=40,
            melee_armor=0,
            pierce_armor=0,
            entity_type=EntityTypes.GROUND,
            player=player,
        )

    def upgrade_technology(self):
        return "Upgrading..."

    def train_scout(self):
        self.pending_units.append("Scout")
