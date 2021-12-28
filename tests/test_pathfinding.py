from COE.logic.path_finding import find_move
from COE.map.map import Map
from COE.map.enum.map_sizes import MapSizes
from COE.map.enum.map_types import MapTypes
from COE.map.enum.resources_rarity import ResourcesRarity
from COE.map.enum.cell_types import CellTypes
from COE.contents.unit.enum.unit_types import UnitTypes


def test_path_finding():

    map_1 = Map(MapSizes.TINY, MapTypes.CONTINENTAL, ResourcesRarity.HIGH)

    # for testing only
    map_1.change_cell(0, 3, CellTypes.WATER)
    map_1.change_cell(1, 1, CellTypes.WATER)
    map_1.change_cell(1, 2, CellTypes.WATER)
    map_1.change_cell(1, 3, CellTypes.WATER)
    map_1.change_cell(2, 1, CellTypes.WATER)
    map_1.change_cell(2, 2, CellTypes.WATER)
    map_1.change_cell(2, 3, CellTypes.WATER)
    map_1.change_cell(3, 1, CellTypes.WATER)
    map_1.change_cell(3, 2, CellTypes.WATER)
    map_1.change_cell(3, 3, CellTypes.WATER)

    assert find_move(map_1, (0, 0), (2, 2), UnitTypes.GROUND) == []
    assert find_move(map_1, (0, 0), (4, 2), UnitTypes.GROUND) == [
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 1),
        (4, 2),
    ]
    assert find_move(map_1, (0, 0), (0, 4), UnitTypes.GROUND) == [
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 1),
        (4, 2),
        (4, 3),
        (3, 4),
        (2, 4),
        (1, 4),
        (0, 4),
    ]
    assert find_move(map_1, (0, 4), (0, 2), UnitTypes.GROUND) == [
        (1, 4),
        (2, 4),
        (3, 4),
        (4, 3),
        (4, 2),
        (4, 1),
        (3, 0),
        (2, 0),
        (1, 0),
        (0, 1),
        (0, 2),
    ]
