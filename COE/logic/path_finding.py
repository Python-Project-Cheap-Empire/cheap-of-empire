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

# (x,y) in x-axis and y-axis to coordinate for matrix


def reverse_coordinate(list_of_tuple):
    if list_of_tuple != []:
        del list_of_tuple[0]
    return [tup[::-1] for tup in list_of_tuple]


def find_move(transformed_map, A, B):
    grid = Grid(matrix=transformed_map)
    start = grid.node(A[1], A[0])
    end = grid.node(B[1], B[0])

    finder = AStarFinder()
    path, runs = finder.find_path(start, end, grid)

    return reverse_coordinate(path)


# class AStar:
#     def __init__(self, map_, A, B, unit_type):
#         # generate_map
#         """
#         Create a new instance of our finder, we allow diagonal movement

#         find_path return 2 things:
#         path --- from start to end
#         number of times --- the algorithm needed to be called until a way was found
#         """
#         self.unit_type = unit_type
#         self.start = A
#         self.end = B
#         self.map = map_
#         self.matrix = self.map.transform_for_unit(self.unit_type)

#     def set_grid(self):
#         self.grid = Grid(matrix=self.matrix)
#         self.start_ = self.grid.node(self.start[1], self.start[0])
#         self.end_ = self.grid.node(self.end[1], self.end[0])

#     def set_matrix(self, pos, value):  # for testing only
#         self.matrix[pos[0]][pos[1]] = value

#     def find_move(self):
#         self.set_grid()
#
#         finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
#         path, runs = finder.find_path(self.start_, self.end_, self.grid)

#         self.pathfinding = reverse_coordinate(path)
#         self.runs = runs
