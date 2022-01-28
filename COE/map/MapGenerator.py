import random

from perlin_noise import PerlinNoise
import numpy as np

from .cell import Cell
from .enum.cell_types import CellTypes
from .map import Map
from .enum.map_sizes import MapSizes
from .enum.map_types import MapTypes
from .enum.resources_rarity import ResourcesRarity
from COE.contents.resources import *


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
        self.spawn_point = (10, 10)

        random.seed(self.seed)

    def generate(self, empty=False):
        if empty:
            cells = self.place_biomes()
        else:
            cells = self.place_biomes()
            cells = self.place_water(cells)
            cells = self.place_forest(cells, 0.3)
            cells = self.place_resources(cells)
        return Map(cells, self.players, self.size, self.type, self.resources_rarity)

    def _biome(self, value):
        return Cell(CellTypes.GRASS, None)

    def place_biomes(self):
        cells = self._perlin_noise()
        for x in range(self.size.value):
            for y in range(self.size.value):
                cells[x][y] = self._biome(cells[x][y])
        return cells

    def place_water(self, cells):
        center = int(self.size.value / 2)

        # First we do a square
        quarter = int(self.size.value / 4)
        for x in range(quarter):
            for y in range(quarter):
                cells[center + x][center + y] = Cell(CellTypes.WATER, None)

        return cells

    def place_forest(self, cells, threshold):
        map_tree = self._perlin_noise(octaves=6, seed=self.seed)

        # place forest
        for x in range(self.size.value):
            for y in range(self.size.value):
                if (
                    cells[x][y].cell_type == CellTypes.GRASS
                    and map_tree[x][y] < threshold
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
        resource_list = [GoldOre, StoneOre, Berry]

        for x in range(self.size.value):
            for y in range(self.size.value):
                placement = random.random()
                if placement < 0.1 and not self.is_near_spawn((x, y)):
                    if (
                        cells[x][y].cell_type == CellTypes.GRASS
                        and not cells[x][y].entity
                    ):
                        rand_r = random.randint(0, 2)
                        cells[x][y].entity = resource_list[rand_r](position=(x, y))
        return cells

    def is_near_spawn(self, coordinate: tuple, proximity=5):
        x, y = coordinate
        return (
            self.spawn_point[0] - proximity <= x <= self.spawn_point[0] + proximity
            and self.spawn_point[1] - proximity <= y <= self.spawn_point[1] + proximity
        )

    def _perlin_noise(self, octaves=5, seed=None):
        if seed is None:
            noise = PerlinNoise(octaves=5, seed=self.seed)
        else:
            noise = PerlinNoise(octaves=5, seed=seed)

        map_noise = np.asarray(
            [
                [
                    noise([i / self.size.value, j / self.size.value])
                    for j in range(self.size.value)
                ]
                for i in range(self.size.value)
            ]
        )
        map_noise = np.interp(map_noise, (map_noise.min(), map_noise.max()), (0, +1))

        map_noise = map_noise.tolist()

        return map_noise
