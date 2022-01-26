from .storage_building import StorageBuilding
from .market import Market


class Farm(StorageBuilding):
    def __init__(self, resource, position: tuple):
        super().__init__(
            name="Farm",
            hp=480,
            positions=position,
            height=1,
            width=1,
            line_of_sight=1,
            resources=resource,
            max_held=250,
            required_building={Market.__class__.__name__},
            required_age=2,
            required_researches={},
            wood_required=75,
            stone_required=0,
            construction_time=24,
        )

    def re_seeding_farm(self):
        return "ReSeeding Farm"
