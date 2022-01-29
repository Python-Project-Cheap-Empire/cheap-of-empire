import time
from COE.contents.entity import Entity
from COE.contents.entity_types import EntityTypes
from COE.logic.Player import Player
from COE.contents.building.building import Building
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
        entity_type: EntityTypes,
        attack_damage: int,
        pierce_attack: int,
        range_: int,
        speed: float,
        rate_of_fire: float,
        melee_armor: int,
        pierce_armor: int,
        player: Player,
        sub_entities,
    ):  # pragma: no cover
        super().__init__(
            name, hp, positions, height, width, line_of_sight, entity_type, sub_entities
        )
        self.attack_damage = attack_damage
        self.range = range_
        self.speed = speed
        self.rate_of_fire = rate_of_fire
        self.melee_armor = melee_armor
        self.pierce_armor = pierce_armor
        self.player = player
        self.is_attacking = False
        self.attacked_entity = None
        self.current_path: list = []
        self.pierce_attack = pierce_attack
        self.last_update = time.time()

    """
    after rate_of_fire (s)
    unit will attack
    """

    def update_attack(self, game_speed):  # pragma: no cover
        s = None
        if self.is_attacking:
            now = time.time()
            if (now - self.last_update) * 60 * game_speed * self.rate_of_fire >= 20:
                s = self.attack()
                self.last_update = now
        return s

    def attack(self):
        if isinstance(self.attacked_entity, Unit):
            damage = max(
                1,
                (
                    max(0, self.attack_damage - self.attacked_entity.melee_armor)
                    + max(0, self.pierce_attack - self.attacked_entity.pierce_armor)
                ),
            )
        elif isinstance(self.attacked_entity, Building):
            damage = max(
                1 / 10,
                (
                    max(0, self.attack_damage - self.attacked_entity.melee_armor)
                    + max(0, self.pierce_attack - self.attacked_entity.pierce_armor)
                ),
            )
        else:
            damage = 0

        if self.attacked_entity.is_master:
            self.attacked_entity.hp -= damage
            for entity in self.attacked_entity.sub_entities:
                entity.hp -= damage
        else:
            self.attacked_entity.master.hp -= damage
            for entity in self.attacked_entity.master.sub_entities:
                entity.hp -= damage

        return self.attacked_entity.hp

        # print("u.health {}".format(self.attacked_entity.hp))

    def check_in_range(self, u):
        if u is not None:
            distance = math.sqrt(
                (self.positions[0] - u.positions[0]) ** 2
                + (self.positions[1] - u.positions[1]) ** 2
            )
            # print(distance)
            return distance <= self.range + math.sqrt(2)
