from COE.contents.entity import Entity
from COE.contents.unit.enum.unit_types import UnitTypes
from COE.logic.Player import Player
from COE.contents.building.building import Building
from COE.logic.path_finding import find_move
import math


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
        pierce_attack: int,
        range_: int,
        speed: float,
        rate_of_fire: float,
        melee_armor: int,
        pierce_armor: int,
        player: Player,
        unit_type: UnitTypes,
    ):  # pragma: no cover
        super().__init__(name, hp, positions, height, width, line_of_sight)
        self.attack_damage = attack_damage
        self.range = range_
        self.speed = speed
        self.rate_of_fire = rate_of_fire
        self.melee_armor = melee_armor
        self.pierce_armor = pierce_armor
        self.player = player
        self.unit_type = unit_type
        self.is_attacking = False
        self.attacked_entity = None
        self.current_path: list = []
        self.pierce_attack = pierce_attack

    def attack(self):
        if self.is_attacking:
            if isinstance(self.attacked_entity, Unit):
                damage = max(
                    1,
                    (
                        max(0, self.attack_damage - self.attacked_entity.melee_armor)
                        + max(0, self.pierce_attack - self.attacked_entity.pierce_armor)
                    ),
                )
                if self.attacked_entity.hp > 0 and not self.die():
                    self.attacked_entity.hp -= damage
                    print("u.health {}".format(self.attacked_entity.hp))
            elif isinstance(self.attacked_entity, Building) and not self.die():
                damage = max(
                    1 / 10,
                    (
                        max(0, self.attack_damage - self.attacked_entity.melee_armor)
                        + max(0, self.pierce_attack - self.attacked_entity.pierce_armor)
                    ),
                )
                if self.attacked_entity.hp > 0 and not self.die():
                    self.attacked_entity.hp -= damage

    def check_in_range(self, u):
        if u is not None:
            distance = math.sqrt(
                (self.positions[0] - u.positions[0]) ** 2
                + (self.positions[1] - u.positions[1]) ** 2
            )
            # print(self.positions[0], self.positions[1], end=" ")
            # print(distance)
            return distance <= self.range + math.sqrt(2)
        else:
            return False

    def die(self):
        return self.hp <= 0

    def delete(self):
        del self
