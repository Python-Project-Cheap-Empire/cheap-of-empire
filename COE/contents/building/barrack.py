from COE.contents.entity import Entity
from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding


class Barrack(MilitaryBuilding, TechnologyBuilding):
    def __init__(self, position: tuple):
        super().__init__(
            name="Barrack",
            hp=1200,
            positions=position,
            height=1,
            width=1,
            line_of_sight=6,
            required={},
        )

    def upgrade_technology(self):
        return "Upgrading..."

    def train_clubman(self):
        self.pending_units += ["ClubMan"]

    def train_axeman(self):
        self.pending_units += ["AxeMan"]

    def train_slinger(self):
        self.pending_units += ["Slinger"]
