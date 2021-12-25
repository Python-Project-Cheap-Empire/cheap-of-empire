from COE.contents.unit.unit import Unit
from COE.logic.Player import Player


class Axeman(Unit):
    def __init__(
        self,
        positions: tuple,
        player: Player,
    ):  # pragma: no cover
        super().__init__(
            name="Axeman",
            hp=50,
            positions=positions,
            height=1,
            width=1,
            line_of_sight=4,
            attack_damage=5,
            range=0,
            speed=1.2,
            rate_of_fire=1.5,
            melee_armor=0,
            pierce_armor=0,
            player=player,
            unit_type="LightInfantry",
        )
