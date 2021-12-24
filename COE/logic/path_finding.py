from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

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
        self.start = A
        self.end = B
        self.map = map_
        self.matrix = self.map.transform_for_unit()

    def set_grid(self):
        self.grid = Grid(matrix=self.matrix)
        self.start_ = self.grid.node(self.start[0], self.start[1])
        self.end_ = self.grid.node(self.end[0], self.end[1])

    def set_matrix(self, pos, value):
        self.matrix[pos[0]][pos[1]] = value

    def find_move(self):
        self.set_grid()
        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        path, runs = finder.find_path(self.start_, self.end_, self.grid)
        # print('operation:', runs, 'path length:', len(path))
        # print(self.grid.grid_str(path=path, start=self.start, end=self.end))
        self.pathfinding = path
        self.runs = runs
