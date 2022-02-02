import random

import numpy as np
from perlin_noise import PerlinNoise

from COE.contents.building.town_center import TownCenter
from COE.contents.resources import *
from COE.contents.unit.villager import Villager
from .cell import Cell
from .enum.cell_types import CellTypes
from .enum.map_sizes import MapSizes
from .enum.map_types import MapTypes
from .enum.resources_rarity import ResourcesRarity
from .map import Map
from COE.contents.entity_types import EntityTypes
from COE.logic.path_finding import find_move


class MapGenerator:
    def __init__(
        self,
        players,
        map_size=MapSizes.TINY,
        map_type=MapTypes.CONTINENTAL,
        resources_rarity=ResourcesRarity.HIGH,
        seed=None,
    ):
        self.size = map_size
        self.type = map_type
        self.resources_rarity = resources_rarity
        self.players = players

        if seed is None:
            self.seed = random.randint(0, 1000)
        else:
            self.seed = seed

        if players is not None:
            self.spawn_points = self.setup_spawns(len(players))
        else:
            self.spawn_points = []

        random.seed(self.seed)

    def generate(self, empty=False):
        if empty:
            cells = self.place_biomes()
        else:
            cells = self.place_biomes()
            cells = self.place_water(cells)
            cells = self.place_forest(cells, 0.3)
            cells = self.place_resources(cells)

        # Used for testing
        if self.players:
            vlg = Villager((1, 1), self.players[0])
            cells[1][1].entity = vlg
            self.players[0].units.append(vlg)
            if len(self.players) > 1:
                vlg = Villager((4, 4), self.players[1])
                cells[4][4].entity = vlg
                self.players[1].units.append(vlg)

        world_map = Map(
            cells, self.players, self.size, self.type, self.resources_rarity
        )

        if self.players:
            for i, p in enumerate(self.players):
                x, y = self.spawn_points[i]
                world_map.place_building(x, y, p, TownCenter((x, y), True))
                for v in range(3):
                    x_pos, y_pos = find_move(
                        world_map.dict_binary_cells.get(EntityTypes.GROUND),
                        (x, y),
                        (x + 4, y + 4),
                    )[-1]
                    villager = Villager((x_pos, y_pos), p)
                    p.units.append(villager)
                    world_map.populate_cell(x_pos, y_pos, villager)

        return world_map

    def _biome(self, value):
        return Cell(CellTypes.GRASS, None)

    def place_biomes(self):
        cells = self._perlin_noise(self.size.value)
        for x in range(self.size.value):
            for y in range(self.size.value):
                cells[x][y] = self._biome(cells[x][y])
        return cells

    def place_water(self, cells):
        """
        Place water in center
        @param cells:
        @return:
        """
        center = int(self.size.value / 2)

        # First we do a square
        quarter = int(self.size.value / 4)
        for x in range(int(-quarter / 2), int(quarter / 2)):
            for y in range(int(-quarter / 2), int(quarter / 2)):
                cells[center + x][center + y] = Cell(CellTypes.WATER, None)

        return cells

    def place_forest(self, cells, threshold):
        """
        Places forest and trees
        @param cells: cells to populate
        @param threshold: threshold for the forest
        @return: cells
        """
        map_tree = self._perlin_noise(self.size.value, octaves=6, seed=self.seed)

        # place forest
        for x in range(self.size.value):
            for y in range(self.size.value):
                if (
                    cells[x][y].cell_type == CellTypes.GRASS
                    and map_tree[x][y] < threshold
                    and not self.is_near_spawn((x, y))
                ):
                    cells[x][y].entity = Tree((x, y))

        for x in range(self.size.value):
            for y in range(self.size.value):
                rand = random.random()
                if rand < 0.01 and not self.is_near_spawn((x, y)):
                    if (
                        cells[x][y].cell_type == CellTypes.GRASS
                        and not cells[x][y].entity
                    ):
                        cells[x][y].entity = Tree((x, y))

        return cells

    def place_resources(self, cells):
        """
        Places resources inside the map
        @param cells: the cells to populate
        @return: cells
        """
        resource_list = [GoldOre, StoneOre, Berry]

        for x in range(self.size.value):
            for y in range(self.size.value):
                placement = random.random()
                if placement < self.resources_rarity.value and not self.is_near_spawn(
                    (x, y)
                ):
                    patch = self._perlin_noise(
                        3, octaves=8, seed=random.randint(0, 500)
                    )
                    rand_r = random.randint(0, 2)

                    try:
                        for j in range(3):
                            for k in range(3):
                                if (
                                    patch[j][k] < random.random()
                                    and cells[x + j][y + k].cell_type == CellTypes.GRASS
                                    and not cells[x + j][y + k].entity
                                    and not self.is_near_spawn((x + j, y + k))
                                ):
                                    cells[x + j][y + k].entity = resource_list[rand_r](
                                        position=(x + j, y + k)
                                    )
                    except IndexError:
                        continue

        return cells

    def is_near_spawn(self, coordinate: tuple, proximity=5):
        """
        Checke if cell is near spawn
        @param coordinate: coordinate of the cell to check
        @param proximity: distance to spawn point
        @return: True if near spawn; if not else
        """
        x, y = coordinate
        is_near = False

        for s in range(len(self.spawn_points)):
            if (
                self.spawn_points[s][0] - proximity
                <= x
                <= self.spawn_points[s][0] + proximity
                and self.spawn_points[s][1] - proximity
                <= y
                <= self.spawn_points[s][1] + proximity
            ):
                is_near = True
                break

        return is_near

    def _perlin_noise(self, size, octaves=5, seed=None):
        if seed is None:
            noise = PerlinNoise(octaves=5, seed=self.seed)
        else:
            noise = PerlinNoise(octaves=5, seed=seed)

        map_noise = np.asarray(
            [[noise([i / size, j / size]) for j in range(size)] for i in range(size)]
        )
        map_noise = np.interp(map_noise, (map_noise.min(), map_noise.max()), (0, +1))

        map_noise = map_noise.tolist()

        return map_noise

    def setup_spawns(self, nb_players):
        spawns = []
        if nb_players == 1:
            spawns.append((10, 10))
        if nb_players == 2:
            spawns.append((10, 10))
            spawns.append((self.size.value - 10, self.size.value - 10))
        if nb_players == 3:
            spawns.append((10, 10))
            spawns.append((self.size.value - 10, self.size.value - 10))
            spawns.append((10, self.size.value - 10))
        if nb_players >= 4:
            spawns.append((10, 10))
            spawns.append((self.size.value - 10, self.size.value - 10))
            spawns.append((10, self.size.value - 10))
            spawns.append((self.size.value - 10, 10))

        return spawns
