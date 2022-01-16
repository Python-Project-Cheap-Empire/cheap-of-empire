from COE.logic.path_finding import find_move
from COE.map.map import Map
from COE.contents.resources.tree import Tree
from COE.map.enum.map_sizes import MapSizes
from COE.map.enum.map_types import MapTypes
from COE.map.enum.resources_rarity import ResourcesRarity
from COE.map.enum.cell_types import CellTypes
from COE.contents.unit.enum.unit_types import UnitTypes
from COE.map.MapGenerator import MapGenerator


def test_path_finding():


    generator = MapGenerator()
    map_1 = generator.generate()

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

    assert find_move(map_1.dict_binary_cells.get(UnitTypes.GROUND), (0, 0), (4, 2)) == [
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (4, 1),
        (4, 2),
    ]
    assert find_move(map_1.dict_binary_cells.get(UnitTypes.GROUND), (0, 0), (0, 4)) == [
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (4, 1),
        (4, 2),
        (4, 3),
        (4, 4),
        (3, 4),
        (2, 4),
        (1, 4),
        (0, 4),
    ]
    assert find_move(map_1.dict_binary_cells.get(UnitTypes.GROUND), (0, 4), (0, 2)) == [
        (1, 4),
        (2, 4),
        (3, 4),
        (4, 4),
        (4, 3),
        (4, 2),
        (4, 1),
        (4, 0),
        (3, 0),
        (2, 0),
        (1, 0),
        (0, 0),
        (0, 1),
        (0, 2),
    ]
    assert find_move(map_1.dict_binary_cells.get(UnitTypes.NAVY), (1, 1), (3, 3)) == [
        (2, 1),
        (3, 1),
        (3, 2),
        (3, 3),
    ]

    map_1.change_cell(0, 3, CellTypes.GRASS)
    map_1.change_cell(1, 1, CellTypes.GRASS)
    map_1.change_cell(1, 2, CellTypes.GRASS)
    map_1.change_cell(1, 3, CellTypes.GRASS)
    map_1.change_cell(2, 1, CellTypes.GRASS)
    map_1.change_cell(2, 2, CellTypes.GRASS)
    map_1.change_cell(2, 3, CellTypes.GRASS)
    map_1.change_cell(3, 1, CellTypes.GRASS)
    map_1.change_cell(3, 2, CellTypes.GRASS)
    map_1.change_cell(3, 3, CellTypes.GRASS)
    map_1.change_cell(4, 1, CellTypes.GRASS)
    map_1.change_cell(4, 2, CellTypes.GRASS)
    map_1.change_cell(4, 3, CellTypes.GRASS)

    map_1.populate_cell(2, 1, Tree((2, 1)))
    map_1.populate_cell(2, 2, Tree((2, 2)))
    map_1.populate_cell(2, 3, Tree((2, 3)))
    map_1.populate_cell(3, 1, Tree((3, 1)))
    map_1.populate_cell(3, 2, Tree((3, 2)))
    map_1.populate_cell(3, 3, Tree((3, 3)))
    map_1.populate_cell(4, 1, Tree((4, 1)))
    map_1.populate_cell(4, 2, Tree((4, 2)))
    map_1.populate_cell(4, 3, Tree((4, 3)))

    assert find_move(map_1.dict_binary_cells.get(UnitTypes.GROUND), (0, 0), (3, 2)) == [
        (1, 0),
        (2, 0),
        (3, 0),
    ]
