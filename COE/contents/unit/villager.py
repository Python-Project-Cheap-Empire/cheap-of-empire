from COE.contents.resources.resource_type import ResourceType
from COE.contents.unit.unit import Unit
from COE.logic.Player import Player
from COE.contents.entity_types import EntityTypes
from COE.contents.resources.gold import Gold
from COE.contents.resources.stone import Stone
from COE.contents.resources.food import Food
from COE.contents.resources.wood import Wood
import time


class Villager(Unit):  # pragma: no cover
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
            pierce_attack=0,
            range_=0,
            speed=1.1,
            rate_of_fire=1.5,
            melee_armor=0,
            pierce_armor=0,
            player=player,
            entity_type=EntityTypes.GROUND,
        )

        self.gathered_resource = None
        self.gathered_resource_type: ResourceType = None
        self.amount_holding = 0
        self.MAX_AMOUNT_HOLDING = 15
        self.building = None
        self.is_returning = False
        self.gathering_time = 100
        self.last_gather_time = time.time()
        self.cost = {
            "GOLD": 0,
            "STONE": 0,
            "WOOD": 0,
            "FOOD": 50,
        }

    def update_gathering(self, game_speed):
        if self.gathered_resource is not None and self.check_in_range(
            self.gathered_resource
        ):
            now = time.time()
            if (
                now - self.last_gather_time
            ) * 60 * game_speed * self.gathering_time >= 20:
                self.gather_resource()
                self.last_gather_time = now

    """
    Check   if amount >= MAX_AMOUNT_HOLDING => return to towncenter to release
            if not => move to resource and gather

    """

    def check_ressource(self, clicked_resource):
        if self.amount_holding <= 0 and (
            self.gathered_resource is None
            or (
                self.gathered_resource_type == ResourceType.GOLD
                and isinstance(clicked_resource, Gold)
            )
            or (
                self.gathered_resource_type == ResourceType.STONE
                and isinstance(clicked_resource, Stone)
            )
            or (
                self.gathered_resource_type == ResourceType.WOOD
                and isinstance(clicked_resource, Wood)
            )
            or (
                self.gathered_resource_type == ResourceType.FOOD
                and isinstance(clicked_resource, Food)
            )
        ):
            return True
        else:
            return False

    def gather_resource(self):
        if self.gathered_resource.amount > 0:
            if self.gathered_resource.amount > 5:
                self.amount_holding += 5
                self.gathered_resource.decrease_amount(5)
            else:
                self.amount_holding += self.gathered_resource.amount
                self.gathered_resource.decrease_amount(self.gathered_resource.amount)

        # return self.gathered_resource.amount

    def transfer_resource_to_player(self):
        if self.gathered_resource_type == ResourceType.GOLD:
            self.player._gold += self.amount_holding
        if self.gathered_resource_type == ResourceType.WOOD:
            self.player._wood += self.amount_holding
        if self.gathered_resource_type == ResourceType.STONE:
            self.player._stone += self.amount_holding
        if self.gathered_resource_type == ResourceType.FOOD:
            self.player._food += self.amount_holding
        self.amount_holding = 0
