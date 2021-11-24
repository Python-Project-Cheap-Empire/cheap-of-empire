from COE.contents.entity import Entity
from .storage_building import StorageBuilding
from .technology_building import TechnologyBuilding


class Market(StorageBuilding, TechnologyBuilding):
    """
    Static Variable for enable_tribute
    Once market has been built, its tribute feature will last forever
    """

    def __init__(self, enable_tribute: bool = False):
        StorageBuilding.__init__(self, 0, 0)
        TechnologyBuilding.__init__(self)
        Entity.__init__(self, "Market", 1800, (0, 0), 1, 1, 6, "none")
        self.enabled_tribute = enable_tribute

    def enable_tribute(self):
        self.enabled_tribute = True

    def research_economic_technology(self):
        return "Research Economic Technologies"
