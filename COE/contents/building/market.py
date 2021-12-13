from COE.contents.entity import Entity
from .storage_building import StorageBuilding
from .technology_building import TechnologyBuilding


class Market(StorageBuilding, TechnologyBuilding):
    """
    Static Variable for enable_tribute
    Once market has been built, its tribute feature will last forever
    """

    def __init__(self, position: tuple, enable_tribute: bool = False):
        self.enabled_tribute = enable_tribute
        super().__init__(
            name="Market",
            hp=350,
            positions=position,
            width=1,
            height=1,
            line_of_sight=6,
            resources=None,
            max_held=0,
            required={"Stable", "Granary"},
        )

    def enable_tribute(self):
        self.enabled_tribute = True

    def research_economic_technology(self):
        return "Research Economic Technologies"
