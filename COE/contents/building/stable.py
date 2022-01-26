from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding
from .barrack import Barrack


class Stable(MilitaryBuilding, TechnologyBuilding):
    def __init__(self, position: tuple):
        super().__init__(
            name="Stable",
            hp=350,
            positions=position,
            height=1,
            width=1,
            line_of_sight=4,
            required_building={Barrack.__class__.__name__},
            required_age=2,
            required_researches={},
            researches={},
            wood_required=150,
            time_construction=40,
        )

    def upgrade_technology(self):
        return "Upgrading..."

    def train_scout(self):
        self.pending_units.append("Scout")
