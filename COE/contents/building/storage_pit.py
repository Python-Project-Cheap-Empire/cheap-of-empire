# from COE.contents.entity import Entity
from .storage_building import StorageBuilding
from .technology_building import TechnologyBuilding


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
            required={},
        )

    def upgrade_technology(self):
        return "Upgrading..."
