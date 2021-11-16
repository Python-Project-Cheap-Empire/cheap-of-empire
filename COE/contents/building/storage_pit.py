# from COE.contents.entity import Entity
from .storage_building import StorageBuilding
from .technology_building import TechnologyBuilding


class StoragePit(StorageBuilding, TechnologyBuilding):
    def __init__(self, is_drop_point: bool = True):
        StorageBuilding.__init__(self, 0, 0)
        TechnologyBuilding.__init__(self)

        self.is_drop_point = is_drop_point

    def upgrade_technology(self):
        return "Upgrading..."
