from COE.map.map import Map
from COE.map.enum.map_types import MapTypes
from COE.map.enum.resources_rarity import ResourcesRarity
from COE.map.enum.map_sizes import MapSizes
from COE.map.exceptions.map_arguments_exception import MapArgumentsException
from COE.map.exceptions.zero_map_size_exception import ZeroMapSizeException
from COE.map.MapGenerator import MapGenerator
import pytest


def test_map_generation_default():
    generator = MapGenerator(players=None)
    map_gen = generator.generate()
    assert map_gen.size == MapSizes.TINY
    assert map_gen.type == MapTypes.CONTINENTAL
    assert map_gen.resources_rarity == ResourcesRarity.HIGH
