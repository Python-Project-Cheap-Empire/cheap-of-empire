from COE.contents.unit.unit import Unit
from COE.logic.Player import Player
from COE.contents.entity_types import EntityTypes


class Villager(Unit):
    def __init__(
        self,
        positions: tuple,
        player: Player,
    ):  # pragma: no cover
        super().__init__(
            name="Villager",
            hp=50,
            positions=positions,
            height=1,
            width=1,
            line_of_sight=4,
            attack_damage=3,
            pierce_attack=0,
            range_=0,
            speed=1.1,
            rate_of_fire=1.5,
            melee_armor=0,
            pierce_armor=0,
            player=player,
            entity_type=EntityTypes.GROUND,
            sub_entities=[],
        )
        self.held_ressource = None
        self.building = None
