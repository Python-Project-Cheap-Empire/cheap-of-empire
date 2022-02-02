from COE.contents.entity_types import EntityTypes
from COE.logic.Player import Player
from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding
from .town_center import TownCenter


class Barrack(MilitaryBuilding, TechnologyBuilding):
    def __init__(self, position: tuple, player: Player):
        super().__init__(
            name="Barrack",
            hp=1200,
            positions=position,
            height=3,
            width=3,
            line_of_sight=6,
            required_building={TownCenter.__class__.__name__},
            required_age=1,
            required_researches={},
            researches={},
            wood_required=130,
            stone_required=0,
            construction_time=40,
            melee_armor=0,
            pierce_armor=0,
            entity_type=EntityTypes.GROUND,
            player=player,
        )

    def upgrade_technology(self):
        return "Upgrading..."

    def train_clubman(self):
        self.pending_units.append("ClubMan")

    def train_axeman(self):
        self.pending_units.append("AxeMan")

    def train_slinger(self):
        self.pending_units.append("Slinger")
