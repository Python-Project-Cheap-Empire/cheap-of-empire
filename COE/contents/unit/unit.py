from COE.contents.entity import Entity
from COE.contents.unit.enum.unit_types import UnitTypes
from COE.logic.Player import Player


class Unit(Entity):
    def __init__(
        self,
        name: str,
        hp: int,
        positions: tuple,
        height: int,
        width: int,
        line_of_sight: int,
        attack_damage: int,
        range: int,
        speed: float,
        rate_of_fire: float,
        melee_armor: int,
        pierce_armor: int,
        player: Player,
        unit_type: UnitTypes,
    ):  # pragma: no cover
        super().__init__(name, hp, positions, height, width, line_of_sight)
        self.attack_damage = attack_damage
        self.range = range
        self.speed = speed
        self.rate_of_fire = rate_of_fire
        self.melee_armor = melee_armor
        self.pierce_armor = pierce_armor
        self.player = player
        self.unit_type = unit_type
        self.current_path: list = []

    # def set_attack(self, damage): self.attack_damage = damage

    # def attack(self, entity: Entity): entity.take_damage(self.attack_damage)
