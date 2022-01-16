from .storage_building import StorageBuilding
from .military_building import MilitaryBuilding


class TownCenter(StorageBuilding, MilitaryBuilding):
    def __init__(self, position: tuple, is_drop_point: bool):
        self.is_drop_point = is_drop_point
        super().__init__(
            name="TownCenter",
            hp=600,
            positions=position,
            height=3,
            width=3,
            line_of_sight=7,
            resources=None,
            max_held=9999,
            required_building={},
            required_age=1,
            required_researches={},
            researches={},
        )

    def train_villager(self):
        self.pending_units.append("Villager")

    def advance_age(self):
        return "Advancing Age..."
