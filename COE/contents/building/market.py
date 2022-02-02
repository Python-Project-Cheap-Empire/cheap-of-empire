from COE.contents.entity_types import EntityTypes
from COE.logic.Player import Player
from .technology_building import TechnologyBuilding
from .granary import Granary


class Market(TechnologyBuilding):
    """
    Static Variable for enable_tribute
    Once market has been built, its tribute feature will last forever
    """

    def __init__(self, position: tuple, player: Player):
        super().__init__(
            name="Market",
            hp=350,
            positions=position,
            width=3,
            height=3,
            line_of_sight=6,
            required_building={Granary.__class__.__name__},
            required_age=1,
            required_researches={},
            researches={},
            wood_required=150,
            stone_required=0,
            construction_time=40,
            melee_armor=0,
            pierce_armor=0,
            entity_type=EntityTypes.GROUND,
            player=player,
        )

    def enable_tribute(self):
        self.enabled_tribute = True

    def research_economic_technology(self):
        return "Research Economic Technologies"
