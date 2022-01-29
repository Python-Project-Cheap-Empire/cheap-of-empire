from COE.contents.entity_types import EntityTypes
from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding
from .barrack import Barrack


class ArcheryRange(MilitaryBuilding, TechnologyBuilding):
    def __init__(self, position: tuple):
        super().__init__(
            name="Archery Range",
            hp=350,
            positions=position,
            height=3,
            width=3,
            line_of_sight=6,
            unit_type="archer",
            pending_units=[],
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
            sub_entities=[],
        )

    # def upgrade_technology(self, tech_name):
    #     archery_range_tech[tech_name] = True

    def train_bowman(self):
        self.pending_units.append("BowMan")
