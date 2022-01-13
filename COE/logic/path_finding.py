from typing import List
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import operator

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


# def reverse_coordinate(list_of_tuple):
#     # if list_of_tuple != []:
#     #     del list_of_tuple[0]
#     return [tup[::-1] for tup in list_of_tuple]


def fsp(grid, x, y, finder, start):
    end = grid.node(x, y)
    if end.weight == 1:
        path, _ = finder.find_path(start, end, grid)
        grid.cleanup()
        if path:
            return path[1::], grid
    return [], grid


def search_available_path(unit_direction, p, grid, end, finder, start):
    if unit_direction == "N" or unit_direction == "NW":
        close_neighbors = [[0, -p], [-p, 0], [p, 0], [0, p]]
        vertex = [[-p, -p], [p, -p], [-p, p], [p, p]]
        ops = [operator.sub, operator.add]
        ops3, ops4 = [operator.sub, operator.add], [operator.sub, operator.add]
    elif unit_direction == "S" or unit_direction == "SE":
        close_neighbors = [[0, p], [p, 0], [-p, 0], [0, -p]]
        vertex = [[p, p], [-p, p], [p, -p], [-p, -p]]
        ops = [operator.add, operator.sub]
        ops3, ops4 = [operator.add, operator.sub], [operator.add, operator.sub]
    elif unit_direction == "W" or unit_direction == "SW":
        close_neighbors = [[-p, 0], [0, p], [0, -p], [p, 0]]
        vertex = [[-p, p], [-p, -p], [p, p], [p, -p]]
        ops = [operator.add, operator.sub]
        ops3, ops4 = [operator.sub, operator.add], [operator.add, operator.sub]
    elif unit_direction == "E" or unit_direction == "NE":
        close_neighbors = [[p, 0], [0, -p], [0, p], [-p, 0]]
        vertex = [[p, -p], [p, p], [-p, -p], [-p, p]]
        ops = [operator.sub, operator.add]
        ops3, ops4 = [operator.add, operator.sub], [operator.sub, operator.add]
    else:
        return []

    # Closest neighbors of the current square searched
    for t in close_neighbors:
        path, grid = fsp(grid, end.x + t[0], end.y + t[1], finder, start)
        if path:
            return path

    for i in range(1, p):
        # First row/column cells of the current square searched
        for op in ops:
            if unit_direction == "N" or unit_direction == "NW":
                x, y = op(end.x, i), end.y - p
            elif unit_direction == "W" or unit_direction == "SW":
                x, y = end.x - p, op(end.y, i)
            elif unit_direction == "S" or unit_direction == "SE":
                x, y = op(end.x, i), end.y + p
            elif unit_direction == "E" or unit_direction == "NE":
                x, y = end.x + p, op(end.y, i)
            path, grid = fsp(grid, x, y, finder, start)
            if path:
                return path

        # Middle cells of the current square searched
        for op1 in ops3:
            for op2 in ops4:
                if (
                    unit_direction == "N"
                    or unit_direction == "NW"
                    or unit_direction == "S"
                    or unit_direction == "SE"
                ):
                    x, y = op2(end.x, p), op1(end.y, i)
                elif (
                    unit_direction == "W"
                    or unit_direction == "SW"
                    or unit_direction == "E"
                    or unit_direction == "NE"
                ):
                    x, y = op1(end.x, i), op2(end.y, p)

                path, grid = fsp(grid, x, y, finder, start)
                if path:
                    return path

        # Last row/column cells of the current square searched
        for op in ops:
            if unit_direction == "N" or unit_direction == "NW":
                x, y = op(end.x, i), end.y + p
            elif unit_direction == "W" or unit_direction == "SW":
                x, y = end.x + p, op(end.y, i)
            elif unit_direction == "S" or unit_direction == "SE":
                x, y = op(end.x, i), end.y - p
            elif unit_direction == "E" or unit_direction == "NE":
                x, y = end.x - p, op(end.y, i)
            path, grid = fsp(grid, x, y, finder, start)
            if path:
                return path

    # Vertex cells of the current square searched
    for t in vertex:
        path, grid = fsp(grid, end.x + t[0], end.y + t[1], finder, start)
        if path:
            return path

    return []


def find_move(transformed_map, A, B):
    grid = Grid(matrix=transformed_map)
    start = grid.node(A[0], A[1])
    end = grid.node(B[0], B[1])
    distance = max(abs(A[1] - B[1]), abs(A[0] - B[0]))
    finder = AStarFinder()
    if end.weight == 1:
        path, _ = finder.find_path(start, end, grid)
        if path:
            return path[1::]
        grid.cleanup()
    p = 1
    while distance > 0:
        if A[0] == B[0] and A[1] < B[1]:  # BORDEAUX
            path = search_available_path("N", p, grid, end, finder, start)

        elif A[0] == B[0] and A[1] > B[1]:  # JAUNE VOMIT
            path = search_available_path("S", p, grid, end, finder, start)
            # if path:
            # return path

        elif A[0] < B[0] and A[1] == B[1]:  # VIOLET
            path = search_available_path("W", p, grid, end, finder, start)
            # if path:
            # return path

        elif A[0] > B[0] and A[1] == B[1]:  # VERT PALE
            path = search_available_path("E", p, grid, end, finder, start)
            # if path:
            # return path

        elif A[0] < B[0] and A[1] < B[1]:  # ROUGE
            path = search_available_path("NW", p, grid, end, finder, start)
            # if path:
            # return path

        elif A[0] < B[0] and A[1] > B[1]:  # ROSE
            path = search_available_path("SW", p, grid, end, finder, start)
            # if path:
            # return path

        elif A[0] > B[0] and A[1] > B[1]:  # BLEU
            path = search_available_path("SE", p, grid, end, finder, start)
            # if path:
            # return path

        elif A[0] > B[0] and A[1] < B[1]:  # GRIS
            path = search_available_path("NE", p, grid, end, finder, start)
            # if path:
            # return path
        if path:
            return path
        distance -= 1
        p += 1

    return []
