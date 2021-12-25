from COE.contents.unit.unit import Unit
from COE.logic.Player import Player
from COE.contents.unit.enum.unit_types import UnitTypes


class Bowman(Unit):
    def __init__(
        self,
        positions: tuple,
        player: Player,
    ):  # pragma: no cover
        super().__init__(
            name="Bowman",
            hp=35,
            positions=positions,
            height=1,
            width=1,
            line_of_sight=7,
            attack_damage=3,
            range=5,
            speed=1.2,
            rate_of_fire=1.4,
            melee_armor=0,
            pierce_armor=0,
            player=player,
            unit_type=UnitTypes.GROUND,
        )

    # def move():
    #     pass

    # def shoot(self):
    #     pass
