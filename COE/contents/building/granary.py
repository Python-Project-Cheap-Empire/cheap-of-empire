from .storage_building import StorageBuilding
from .technology_building import TechnologyBuilding
from .town_center import TownCenter

"""
    Tool Age:
        Small Wall
        Watch Tower
    Bronze Age:
        Medium Wall
        Sentry Tower
"""


class Granary(StorageBuilding, TechnologyBuilding):
    def __init__(self, position: tuple):
        super().__init__(
            name="Granary",
            hp=500,
            positions=position,
            height=1,
            width=1,
            line_of_sight=6,
            resources=0,
            max_held=9999,
            required_building={TownCenter.__class__.__name__},
            required_age=1,
            required_researches={},
            researches={},
        )

    def upgrade_technology(self):
        return "Upgrading..."
