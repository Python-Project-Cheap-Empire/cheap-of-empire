from COE.contents.entity import Entity
from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding


class Barrack(MilitaryBuilding, TechnologyBuilding):
    def __init__(self):
        MilitaryBuilding.__init__(self, "", [])
        TechnologyBuilding.__init__(self, {})
        Entity.__init__(self, "Barrack", 1200, (0, 0), 1, 1, 6)

    def upgrade_technology(self):
        return "Upgrading..."

    def train_clubman(self):
        self.pending_units += ["ClubMan"]

    def train_axeman(self):
        self.pending_units += ["AxeMan"]

    def train_slinger(self):
        self.pending_units += ["Slinger"]
