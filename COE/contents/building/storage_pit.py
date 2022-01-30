from COE.contents.entity_types import EntityTypes
from .storage_building import StorageBuilding
from .technology_building import TechnologyBuilding
from .town_center import TownCenter


class StoragePit(StorageBuilding, TechnologyBuilding):
    def __init__(self, position: tuple, is_drop_point: bool = True):
        self.is_drop_point = is_drop_point
        super().__init__(
            name="Storage Pit",
            hp=350,
            positions=position,
            height=3,
            width=3,
            line_of_sight=4,
            resources=None,
            max_held=9999,
            required_building={TownCenter.__class__.__name__},
            required_age=1,
            required_researches={},
            researches={},  # Tool working, leather armor (ca, in, ar)
            wood_required=120,
            stone_required=0,
            construction_time=30,
            melee_armor=0,
            pierce_armor=0,
            entity_type=EntityTypes.GROUND,
            sub_entities=[],
        )

    def upgrade_technology(self):
        return "Upgrading..."
