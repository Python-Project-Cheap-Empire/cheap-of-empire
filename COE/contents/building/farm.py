from COE.contents.entity import Entity
from .storage_building import StorageBuilding
from .technology_building import TechnologyBuilding

required_market = False


class Farm(StorageBuilding, TechnologyBuilding):
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
            required={"Market"},
        )

    def re_seeding_farm(self):
        return "ReSeeding Farm"
