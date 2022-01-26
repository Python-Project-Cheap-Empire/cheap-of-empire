from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding
from .barrack import Barrack


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
            required_building={Barrack.__class__.__name__},
            required_age=2,
            required_researches={},
            researches={},
            wood_required=150,
            time_construction=40,
        )

    # def upgrade_technology(self, tech_name):
    #     archery_range_tech[tech_name] = True

    def train_bowman(self):
        self.pending_units.append("BowMan")
