from COE.contents.unit.unit import Unit
from .cuttable_animal import CuttableAnimal
from COE.contents.entity_types import EntityTypes


class Deer(Unit):
    def __init__(self, position):
        super().__init__(
            name="Deer",
            hp=25,
            positions=position,
            height=1,
            width=1,
            line_of_sight=0,
            attack_damage=0,
            pierce_attack=0,
            range_=1,
            speed=1.5,
            rate_of_fire=0,
            melee_armor=2,
            pierce_armor=0,
            player=None,
            entity_type=EntityTypes.GROUND,
            sub_entities=[],
        )
        self.state = None  # State change when animal is dead

    def death(self):
        if not self.state:
            self.state = CuttableAnimal(
                amount=55,
                name="Dead deer",
                position=self.positions,
            )

    def decrease_amount(self, amount):
        assert self.state is not None
        self.state.decrease_amount(amount)
