from COE.logic.path_finding import AStar
from COE.map.map import Map
from COE.map.enum.map_sizes import MapSizes
from COE.map.enum.map_types import MapTypes
from COE.map.enum.resources_rarity import ResourcesRarity
from copy import deepcopy


def test_path_finding():

    map_ = Map(MapSizes.TINY, MapTypes.CONTINENTAL, ResourcesRarity.HIGH)
    # map_ = Map()
    my_map = AStar(map_, (0, 0), (2, 2), unit_type="Infantry")
    my_map.find_move()
    assert my_map.pathfinding == [(0, 0), (1, 1), (2, 2)]

    map_2 = Map(MapSizes.TINY, MapTypes.CONTINENTAL, ResourcesRarity.HIGH)
    my_map = AStar(map_2, (0, 0), (4, 2), unit_type="TradeVessel")
    my_map.set_matrix((0, 0), 1)
    my_map.set_matrix((0, 1), 1)
    my_map.set_matrix((0, 2), 1)
    my_map.set_matrix((1, 0), 1)
    my_map.set_matrix((1, 2), 1)
    my_map.set_matrix((1, 3), 1)
    my_map.set_matrix((2, 2), 1)
    my_map.set_matrix((2, 4), 1)
    print(my_map.matrix)
    my_map.find_move()
    assert my_map.pathfinding == [(0, 0), (1, 0), (2, 0), (3, 1), (4, 2)]

    map_3 = Map(MapSizes.TINY, MapTypes.CONTINENTAL, ResourcesRarity.HIGH)
    my_map = AStar(map_3, (0, 0), (0, 2), unit_type="Archer")
    my_map.set_matrix((1, 0), 0)
    my_map.set_matrix((1, 1), 0)
    my_map.set_matrix((1, 2), 0)
    my_map.find_move()
    assert my_map.pathfinding == [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),
        (2, 2),
        (1, 2),
        (0, 2),
    ]

    map_4 = Map(MapSizes.TINY, MapTypes.CONTINENTAL, ResourcesRarity.HIGH)
    my_map = AStar(map_4, (0, 0), (0, 2), unit_type="Cavalry")
    my_map.set_matrix((0, 1), 0)
    my_map.set_matrix((1, 0), 0)
    my_map.set_matrix((1, 1), 0)
    my_map.set_matrix((1, 2), 0)
    my_map.find_move()
    assert my_map.pathfinding == []
