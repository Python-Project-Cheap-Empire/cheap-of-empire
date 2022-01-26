from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding
from .town_center import TownCenter


class Barrack(MilitaryBuilding, TechnologyBuilding):
    def __init__(self, position: tuple):
        super().__init__(
            name="Barrack",
            hp=1200,
            positions=position,
            height=1,
            width=1,
            line_of_sight=6,
            required_building={TownCenter.__class__.__name__},
            required_age=1,
            required_researches={},
            researches={},
            wood_required=130,
            stone_required=0,
            construction_time=40,
        )

    def upgrade_technology(self):
        return "Upgrading..."

    def train_clubman(self):
        self.pending_units.append("ClubMan")

    def train_axeman(self):
        self.pending_units.append("AxeMan")

    def train_slinger(self):
        self.pending_units.append("Slinger")
