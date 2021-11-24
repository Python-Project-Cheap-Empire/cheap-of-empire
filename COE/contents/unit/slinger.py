from COE.contents.unit.unit import Unit
from COE.logic.Player import Player


class Slinger(Unit):
    def __init__(
        self,
        positions: tuple,
        player: Player,
    ):  # pragma: no cover
        super().__init__(
            name="Slinger",
            hp=25,
            positions=positions,
            height=1,
            width=1,
            line_of_sight=6,
            attack_damage=2,
            range=4,
            speed=1.2,
            rate_of_fire=1.5,
            melee_armor=0,
            pierce_armor=2,
            player=player,
        )
