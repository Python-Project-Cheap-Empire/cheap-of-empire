from COE.contents.unit.unit import Unit
from COE.logic.Player import Player
from COE.contents.unit.enum.unit_types import UnitTypes


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
            range=0,
            speed=1.1,
            rate_of_fire=1.5,
            melee_armor=0,
            pierce_armor=0,
            player=player,
            unit_type=UnitTypes.GROUND,
        )
        self.held_ressource = None

    # def build():
    #     pass

    # def repair():
    #     pass

    # def seedingFarm():
    #     pass

    # def gather_resource():
    #     pass

    # def release_resource():
    #     pass
