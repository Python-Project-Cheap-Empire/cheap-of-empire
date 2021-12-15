from COE.contents.entity import Entity
from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding


# Require Barrack to be built
class Stable(MilitaryBuilding, TechnologyBuilding):
    def __init__(self):
        MilitaryBuilding.__init__(self, "", pending_units=[])
        TechnologyBuilding.__init__(self, required=set([""]))
        Entity.__init__(self, "Stable", 1500, (0, 0), 1, 1, 6)

    def upgrade_technology(self):
        return "Upgrading..."

    def train_scout(self):
        self.pending_units.append("Scout")
