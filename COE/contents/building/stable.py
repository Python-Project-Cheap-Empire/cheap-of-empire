from COE.contents.entity import Entity
from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding


# Require Barrack to be built
class Stable(MilitaryBuilding, TechnologyBuilding):
    def __init__(self, position: tuple):
        super().__init__(
            name="Stable",
            hp=350,
            positions=position,
            height=1,
            width=1,
            line_of_sight=4,
            required=set([""]),
        )

    def upgrade_technology(self):
        return "Upgrading..."

    def train_scout(self):
        self.pending_units.append("Scout")
