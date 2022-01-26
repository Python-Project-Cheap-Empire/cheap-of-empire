from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding
from .town_center import TownCenter


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
            required_building={TownCenter.__class__.__name__},
            required_age=1,
            required_researches={},
            researches={},
            wood_required=100,
            stone_required=0,
            construction_time=40,
        )

    def upgrade_technology(self):
        return "Upgrading..."

    def train_fishing_boat(self):
        self.pending_units.append("FishingBoat")

    def train_trade_boat(self):
        self.pending_units.append("TradeBoat")

    def train_light_transport(self):
        self.pending_units.append("LightTransport")

    def train_scout_ship(self):
        self.pending_units.append("ScoutShip")
