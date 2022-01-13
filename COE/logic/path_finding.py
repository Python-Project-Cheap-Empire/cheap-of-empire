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


# def reverse_coordinate(list_of_tuple):
#     # if list_of_tuple != []:
#     #     del list_of_tuple[0]
#     return [tup[::-1] for tup in list_of_tuple]


def find_move(transformed_map, A, B):
    grid = Grid(matrix=transformed_map)
    start = grid.node(A[0], A[1])
    end = grid.node(B[0], B[1])
    distance = max(abs(A[1] - B[1]), abs(A[0] - B[0]))
    finder = AStarFinder()
    print(end.weight)
    if end.weight == 1:
        print("12")
        path, runs = finder.find_path(start, end, grid)
        grid.cleanup()
        if path :
            print("7")
            print(path)
            return path[1::]
    p = 1
    
    while distance > 1:
        print("9")
        # if A[0] == B[0] and A[1] == B[1] : # VERT
        #     pass
        if A[0] == B[0] and A[1] < B[1] :# BORDEAUX
            print("10")
            # Above aimed cell
            d = grid.node(B[0], end.y-p)
            print(d.weight)
            if d.weight == 1 :
                print("11")
                path, _ = finder.find_path(start, d, grid)
                if path :
                    print("12")
                    print(path)
                    return path[1::]
                grid.cleanup()
            # First row except above aimed cell
            for j in range(1, p):
                d = grid.node(B[0]-j, end.y-p)
                if d.weight == 1 :
                    path, _ = finder.find_path(start, d, grid)
                    if path :
                        return path[1::]
                    grid.cleanup()
                d = grid.node(B[0]+j, end.y-p)
                if d.weight == 1 :
                    path, _ = finder.find_path(start, d, grid)
                    if path :
                        return path[1::]
                    grid.cleanup()
            # Middle rows
            for l in range(1, (1 + (p-1)*2)+1):
                if d.weight == 1 :
                    d = grid.node(B[0]-p, end.y+p-l)
                    path, _ = finder.find_path(start, d, grid)
                    if path :
                        return path[1::]
                    grid.cleanup()
                d = grid.node(B[0]+p, end.y+p-l)
                if d.weight == 1 :
                    path, _ = finder.find_path(start, d, grid)
                    if path :
                        return path[1::]
                    grid.cleanup()
            # Last row
            for i in range(1, p):
                d = grid.node(B[0]-i, end.y+p)
                if d.weight == 1 :
                    path, _ = finder.find_path(start, d, grid)
                    if path :
                        return path[1::]
                    grid.cleanup()
                d = grid.node(B[0]+i, end.y+p)
                if d.weight == 1 :
                    path, _ = finder.find_path(start, d, grid)
                    if path :
                        return path[1::]
                    grid.cleanup()
            

        # if A[0] == B[0] and A[1] > B[1] :# JAUNE VOMIT
        #     end = grid.node(end.x+1, B[1])
        #     path, _ = finder.find_path(start, end, grid)
        #     distance -= 1
        # if A[0] < B[0] and A[1] < B[1] :# ROUGE
        #     end = grid.node(B[0], end.y-1)
        #     path, _ = finder.find_path(start, end, grid)
        #     distance -= 1
        # if A[0] < B[0] and A[1] > B[1] :# ROSE
        #     pass
        # if A[0] < B[0] and A[1] == B[1] :# VIOLET
        #     pass
        # if A[0] > B[0] and A[1] > B[1] :# BLEU
        #     pass
        # if A[0] > B[0] and A[1] < B[1] :# GRIS
        #     pass
        # if A[0] > B[0] and A[1] == B[1] :# VERT PALE
        #     pass

        distance -= 1
        p += 1
    print("8")
    return []


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
