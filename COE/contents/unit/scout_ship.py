from COE.contents.unit.unit import Unit
from COE.logic.Player import Player


class ScoutShip(Unit):
    def __init__(
        self,
        positions: tuple,
        player: Player,
    ):  # pragma: no cover
        super().__init__(
            name="Scout ship",
            hp=120,
            positions=positions,
            height=1,
            wight=1,
            line_of_sight=7,
            attack_damage=5,
            range=5,
            speed=1.75,
            rate_of_fire=1.5,
            melee_armor=0,
            pierce_armor=0,
            player=player,
        )
