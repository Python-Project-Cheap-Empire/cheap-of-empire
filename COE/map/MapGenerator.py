from perlin_noise import PerlinNoise
import numpy as np

from .cell import Cell
from .enum.cell_types import CellTypes
from .map import Map
from .enum.map_sizes import MapSizes
from .enum.map_types import MapTypes
from .enum.resources_rarity import ResourcesRarity


class MapGenerator:
    def __init__(
        self,
        players,
        map_size=MapSizes.TINY,
        map_type=MapTypes.CONTINENTAL,
        resources_rarity=ResourcesRarity.HIGH,
    ):
        self.size = map_size
        self.type = map_type
        self.resources_rarity = resources_rarity
        self.players = players

    def generate(self):
        cells = self._perlin_noise()
        cells = cells
        return Map(cells, self.players, self.size, self.type, self.resources_rarity)

    def _biome(self, value):
        if value < 0.43:
            return Cell(CellTypes.WATER, None)
        else:
            return Cell(CellTypes.GRASS, None)

    def _perlin_noise(self):
        noise = PerlinNoise(octaves=5)
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
        for x in range(self.size.value):
            for y in range(self.size.value):
                map_noise[x][y] = self._biome(map_noise[x][y])

        return map_noise
