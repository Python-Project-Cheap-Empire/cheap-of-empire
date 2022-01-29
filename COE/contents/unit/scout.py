from COE.contents.unit.unit import Unit
from COE.logic.Player import Player
from COE.contents.entity_types import EntityTypes


class Scout(Unit):
    def __init__(
        self,
        positions: tuple,
        player: Player,
    ):  # pragma: no cover
        super().__init__(
            name="Scout",
            hp=60,
            positions=positions,
            height=1,
            width=1,
            line_of_sight=7,
            attack_damage=3,
            pierce_attack=0,
            range_=0,
            speed=2,
            rate_of_fire=1.5,
            melee_armor=0,
            pierce_armor=0,
            player=player,
            entity_type=EntityTypes.GROUND,
            sub_entities=[],
        )
