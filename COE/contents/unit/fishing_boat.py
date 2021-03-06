from COE.contents.unit.unit import Unit
from COE.logic.Player import Player
from COE.contents.entity_types import EntityTypes


class FishingBoat(Unit):
    def __init__(
        self,
        positions: tuple,
        player: Player,
    ):  # pragma: no cover
        super().__init__(
            name="Fishing boat",
            hp=45,
            positions=positions,
            height=1,
            width=1,
            line_of_sight=6,
            attack_damage=0,
            pierce_attack=0,
            range_=0,
            speed=1.4,
            rate_of_fire=0,
            melee_armor=0,
            pierce_armor=0,
            player=player,
            entity_type=EntityTypes.NAVY,
        )
