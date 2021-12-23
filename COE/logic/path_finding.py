from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from COE.map.map import Map

"""
flow:
 find_path
    init_find  # (re)set global values and open list
    check_neighbors  # for every node in open list
        next_node  # closest node to start in open list
        find_neighbors  # get neighbors
        process_node  # calculate new cost for neighboring node
"""


class AStar:
    def __init__(self, map_, A, B):
        # generate_map
        """
        Create a new instance of our finder, we allow diagonal movement

        find_path return 2 things:
            path --- from start to end
            number of times --- the algorithm needed to be called until a way was found
        """
        self.map = map_
        self.matrix = self.map.transform_for_unit()
        self.grid = Grid(matrix=self.matrix)
        self.start = self.grid.node(A[0], A[1])
        self.end = self.grid.node(B[0], B[1])

    def find_move(self):
        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        path, runs = finder.find_path(self.start, self.end, self.grid)
        # print('operation:', runs, 'path length:', len(path))
        # print(self.grid.grid_str(path=path, start=self.start, end=self.end))
        self.pathfinding = path
        self.runs = runs


# map_ = Map()
# my_map = AStar(map_, (0, 0), (2, 2))
# my_map.matrix[1][1] = 0
# print(my_map.matrix)
