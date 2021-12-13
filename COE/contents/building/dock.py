from COE.contents.entity import Entity
from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding


class Dock(MilitaryBuilding, TechnologyBuilding):
    def __init__(self, position: tuple):
        super().__init__(
            name="Dock",
            hp=1800,
            positions=position,
            height=1,
            width=1,
            line_of_sight=6,
            pending_units=[],
            required=set([""]),
        )

    def upgrade_technology(self):
        return "Upgrading..."

    def train_fishing_boat(self):
        self.pending_units += ["FishingBoat"]

    def train_trade_boat(self):
        self.pending_units += ["TradeBoat"]

    def train_light_transport(self):
        self.pending_units += ["LightTransport"]

    def train_scout_ship(self):
        self.pending_units += ["ScoutShip"]
