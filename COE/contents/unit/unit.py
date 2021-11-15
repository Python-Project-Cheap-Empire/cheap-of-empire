from COE.contents.entity import Entity


class Unit(Entity):
    def __init__(
        self,
        attack_damage: int,
        range: int,
        speed: float,
        rate_of_fire: float,
        melee_armor: int,
        pierce_armor: int,
        line_of_sight: int,
    ):
        super().__init__()
        self.attack_damage = attack_damage
        self.range = range
        self.speed = speed
        self.rate_of_fire = rate_of_fire
        self.melee_armor = melee_armor
        self.pierce_armor = pierce_armor
        self.line_of_sight = line_of_sight

    def set_attack(self, damage):
        self.attack_damage = damage

    def attack(self, entity: Entity):
        entity.take_damage(self.attack_damage)

    def move():
        pass
