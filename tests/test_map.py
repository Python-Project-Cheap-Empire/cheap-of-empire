from COE.map.map import Map
from COE.map.enum.map_types import MapTypes
from COE.map.enum.resources_rarity import ResourcesRarity
from COE.map.exceptions.not_standardized_metric_exception import (
    NotStandardizedMetricException,
)
from COE.map.enum.map_sizes import MapSizes
from COE.map.exceptions.map_arguments_exception import MapArgumentsException
from COE.map.exceptions.zero_map_size_exception import ZeroMapSizeException
import pytest


def test_is_type_known():
    assert Map.is_type_known(MapTypes.CONTINENTAL)
    with pytest.raises(NotStandardizedMetricException):
        Map.is_type_known(1)


def test_is_resources_rarity_known():
    assert Map.is_resources_rarity_known(ResourcesRarity.HIGH)
    with pytest.raises(NotStandardizedMetricException):
        Map.is_resources_rarity_known(1)


def test_is_map_size_known():
    assert Map.is_map_size_known(MapSizes.TINY)
    with pytest.raises(ZeroMapSizeException):
        Map.is_map_size_known(0)
    with pytest.raises(NotStandardizedMetricException):
        Map.is_map_size_known(1)


def test_are_args_enough():
    assert Map.are_args_enough([1, 2, 3])
    with pytest.raises(MapArgumentsException):
        Map.are_args_enough([2])


def test_get_size():
    assert Map.get_size([1, 2, 3]) == 1


def test_get_type():
    assert Map.get_type([1, 2, 3]) == 2


def test_get_resources_rarity():
    assert Map.get_resources_rarity([1, 2, 3]) == 3


def test_are_args_fine():
    assert Map.are_args_fine(
        [MapSizes.TINY, MapTypes.CONTINENTAL, ResourcesRarity.HIGH]
    )
    with pytest.raises(NotStandardizedMetricException):
        assert Map.are_args_fine([1, 2, 3])


def test_init():
    m = Map(MapSizes.TINY, MapTypes.CONTINENTAL, ResourcesRarity.HIGH)
    assert m.size == MapSizes.TINY
    assert m.type == MapTypes.CONTINENTAL
    assert m.resources_rarity == ResourcesRarity.HIGH
