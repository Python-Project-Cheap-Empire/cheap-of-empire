from COE.contents.unit.unit import Unit
from COE.logic.Player import Player
from COE.contents.entity_types import EntityTypes
from COE.contents.building.town_center import TownCenter
from COE.contents.resources.gold import Gold
from COE.contents.resources.stone import Stone
from COE.contents.resources.food import Food
from COE.contents.resources.wood import Wood
from COE.contents.resources.gold_ore import GoldOre
from COE.contents.resources.stone_ore import StoneOre
from COE.contents.resources.tree import Tree
from COE.contents.resources.cuttable_animal import CuttableAnimal
from COE.contents.resources.resource import Resource
import time


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
            pierce_attack=0,
            range_=0,
            speed=1.1,
            rate_of_fire=1.5,
            melee_armor=0,
            pierce_armor=0,
            player=player,
            entity_type=EntityTypes.GROUND,
        )

        self.held_ressource = None
        self.amount_holding = 0
        # self.gathering_target = None
        self.MAX_AMOUNT_HOLDING = 15
        self.building = None
        self.is_gathering = False
        self.gathering_time = 100
        self.last_gather_time = time.time()
        self.held_ressource_x, self.held_ressource_y = -1, -1

    # def build():
    #     pass

    # def repair():
    #     pass

    # def seedingFarm():
    #     pass

    def update_gathering(self, game_speed):
        # s = None
        if self.is_gathering and self.check_in_range(self.held_ressource):
            now = time.time()
            if (
                now - self.last_gather_time
            ) * 60 * game_speed * self.gathering_time >= 20:
                # s = self.gather_resource()
                self.gather_resource()
                self.last_gather_time = now
        # return s

    """
    Check   if amount >= MAX_AMOUNT_HOLDING => return to towncenter to release
            if not => move to resource and gather

    """

    def check_ressource_and_amount_holding(self, u, x, y):  # pragma: no cover
        if (
            self.held_ressource is None
            or (isinstance(self.held_ressource, Gold) and isinstance(u, Gold))
            or (isinstance(self.held_ressource, Stone) and isinstance(u, Stone))
            or (isinstance(self.held_ressource, Wood) and isinstance(u, Wood))
            or (isinstance(self.held_ressource, Food) and isinstance(u, Food))
        ):
            print("GO HERE")
            self.held_ressource = u
            self.is_gathering = True
            print(self.held_ressource, "==== ")
            return True
        else:
            return False

    def gather_resource(self):
        if self.held_ressource is not None and self.held_ressource.amount > 0:
            if self.held_ressource.amount > 5:
                self.amount_holding += 5
                self.held_ressource.decrease_amount(5)
            else:
                self.amount_holding += self.held_ressource.amount
                self.held_ressource.decrease_amount(self.held_ressource.amount)

        # return self.held_ressource.amount

    def release_resource(self):
        if isinstance(self.held_ressource, Gold):
            self.player._gold += self.amount_holding
        if isinstance(self.held_ressource, Wood):
            self.player._wood += self.amount_holding
        if isinstance(self.held_ressource, Stone):
            self.player._stone += self.amount_holding
        if isinstance(self.held_ressource, Food):
            self.player._food += self.amount_holding
        self.amount_holding = 0
