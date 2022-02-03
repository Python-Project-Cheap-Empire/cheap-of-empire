from COE.contents.entity_types import EntityTypes
from COE.logic.Player import Player
from COE.contents.unit.axeman import Axeman
from COE.map.map import Map
from COE.logic.path_finding import find_move
from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding
from .town_center import TownCenter

import time


class Barrack(MilitaryBuilding, TechnologyBuilding):
    def __init__(self, position: tuple, player: Player):
        super().__init__(
            name="Barrack",
            hp=1200,
            positions=position,
            height=3,
            width=3,
            line_of_sight=6,
            required_building={TownCenter.__class__.__name__},
            required_age=1,
            required_researches={},
            researches={},
            wood_required=130,
            stone_required=0,
            construction_time=40,
            melee_armor=0,
            pierce_armor=0,
            entity_type=EntityTypes.GROUND,
            player=player,
        )
        self.time_flag = []

    def upgrade_technology(self):
        return "Upgrading..."

    # (now - self.time_flag[0]) * 60 * game_speed > self.pending_units[0].training_time
    def update_training(self, game_speed):
        if (self.is_training()):
            now = time.time()
            if (
                (now - self.time_flag[0])
            ):
                u = self.pending_units.pop(0)
                t = self.time_flag.pop(0)
                return True
        # print('self is not training')
        return False

    def is_training(self):
        return self.pending_units != None and self.time_flag != []
# (now - self.prev_time) * 60 * self.speed > spawn_rate:

    def train_axeman(self, x, y, training_time):
        if (len(self.pending_units) < 7
                    and self.player._food >= Axeman((-1, -1), self.player).cost['FOOD']
                ):
            u = Axeman((x, y), self.player)
            if len(self.pending_units) == 0:
                self.pending_units.append(u)
                self.time_flag.append(time.time() + training_time)
                self.player._food -= 50
            else:
                self.pending_units.append(u)
                self.time_flag.append(self.time_flag[-1] + training_time)
                self.player._food -= 50

    def train_slinger(self):
        self.pending_units.append("Slinger")

    def train_clubman(self):
        self.pending_units.append("ClubMan")

    def pop_unit(self, map: Map):
        for i in range(self.positions[0]+1, self.positions[0] + 4):
            for j in range(self.positions[1]+1, self.positions[1] + 4):
                available = find_move(
                    map.dict_binary_cells.get(self.entity_type),
                    self.positions,
                    (i, j)
                )
                if available != [] and map.cells[i][j].entity == None:
                    return i, j
        return -1, -1
