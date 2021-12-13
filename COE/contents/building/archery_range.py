from COE.contents.entity import Entity
from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding

# Require Barrack to be built
required_barrack = False


class ArcheryRange(MilitaryBuilding, TechnologyBuilding):
    def __init__(self, position: tuple):
        super().__init__(
            name="Archery Range",
            hp=350,
            positions=position,
            height=1,
            width=1,
            line_of_sight=6,
            unit_type="archer",
            pending_units=[],
            required=set(["Barrack"]),
        )

    # def upgrade_technology(self, tech_name):
    #     archery_range_tech[tech_name] = True

    def train_bowman(self):
        self.pending_units.append("BowMan")
