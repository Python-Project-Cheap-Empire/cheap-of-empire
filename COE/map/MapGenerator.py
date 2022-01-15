from .enum.map_sizes import MapSizes
from .enum.map_types import MapTypes
from .enum.resources_rarity import ResourcesRarity
from cell import Cell
from map import Map


class MapGenerator:
    def __init__(self, map_size=MapSizes.TINY, map_type=MapTypes.CONTINENTAL, resources_rarity=ResourcesRarity.HIGH):
        self.size = map_size
        self.type = map_type
        self.resources_rarity = resources_rarity

    def generate(self):
        return Map()

    def _perlin_noise(self):
        pass