from COE.contents.entity import Entity
from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding


class Dock(MilitaryBuilding, TechnologyBuilding):
    def __init__(self):
        MilitaryBuilding.__init__(self, "", pending_units=[])
        TechnologyBuilding.__init__(self, required=set([""]))
        Entity.__init__(self, "Dock", 1800, (0, 0), 1, 1, 6, "none")

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
