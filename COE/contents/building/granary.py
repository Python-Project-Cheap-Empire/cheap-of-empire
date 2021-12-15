from COE.contents.entity import Entity
from .storage_building import StorageBuilding
from .technology_building import TechnologyBuilding


"""
    Tool Age:
        Small Wall
        Watch Tower
    Bronze Age:
        Medium Wall
        Sentry Tower
"""


class Granary(StorageBuilding, TechnologyBuilding):
    def __init__(self):
        StorageBuilding.__init__(self, 0, 9999)
        TechnologyBuilding.__init__(self)
        Entity.__init__(self, "Granary", 500, (0, 0), 1, 1, 6)

    def upgrade_technology(self):
        return "Upgrading..."
