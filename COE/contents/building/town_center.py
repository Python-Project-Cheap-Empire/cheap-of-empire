from COE.contents.entity import Entity
from .storage_building import StorageBuilding
from .military_building import MilitaryBuilding


class TownCenter(StorageBuilding, MilitaryBuilding):
    def __init__(self, is_drop_point: bool, max_population: int):
        StorageBuilding.__init__(self, 200, 200)
        MilitaryBuilding.__init__(self, "", [])
        Entity.__init__(self, "TownCenter", 2400, (0, 0), 1, 1, 6, "none")
        self.is_drop_point = is_drop_point
        self.max_population = max_population

    def train_villager(self):
        self.pending_units.append("Villager")

    def advance_age(self):
        return "Advancing Age..."
