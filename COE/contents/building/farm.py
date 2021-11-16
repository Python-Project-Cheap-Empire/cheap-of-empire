from COE.contents.entity import Entity
from .storage_building import StorageBuilding
from .technology_building import TechnologyBuilding

required_market = False


class Farm(StorageBuilding, TechnologyBuilding):
    def __init__(self, ressource):
        StorageBuilding.__init__(self, ressource, max_held=250)
        TechnologyBuilding.__init__(self, required={"Market"})
        Entity.__init__(self, "Farm", 480, (0, 0), 0, 0, 1, "none")
        self.ressource = ressource

    def re_seeding_farm(self):
        return "ReSeeding Farm"
