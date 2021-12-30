from COE.contents.entity import Entity
from .storage_building import StorageBuilding
from .technology_building import TechnologyBuilding
from .granary import Granary


class Market(TechnologyBuilding):
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
            required_building={Granary.__class__.__name__},
            required_age=1,
            required_researches={},
            researches={},
        )

    def enable_tribute(self):
        self.enabled_tribute = True

    def research_economic_technology(self):
        return "Research Economic Technologies"
