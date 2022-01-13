from COE.contents.unit.villager import Villager
from COE.logic.Player import Player
from COE.logic.path_finding import find_move
from COE.map.map import Map
from COE.camera.camera import Camera


class Game:
    """
    A class to represent a unique game
    """

    def __init__(self, players: list, map: Map, timer, speed, camera: Camera):
        """
        Constructs all the necessary attributes for the Game object.

        :param players: list
        :param map_game: Map
        :param timer: Time
        :param speed: float
        """
        self.players: list[Player] = players
        self.map = map
        self.timer = timer
        self.speed = speed
        self.camera = camera

    def set_speed(self, new_speed):
        assert (
            isinstance(new_speed, float) and new_speed > 0
        ), "new_speed is a float and new_speed > 0"
        self.speed = new_speed

    def update(self):  # pragma: no cover
        # For each unit of the human player
        for unit in self.players[0].units:
            # If the unit is in travel between two points
            if unit.current_path:
                next_cell_in_path = self.map.cells[unit.current_path[0][0]][
                    unit.current_path[0][1]
                ]
                # If the next cell where the unit is supposed to go to has
                # already an entity
                if next_cell_in_path.entity:
                    print("1")
                    if len(unit.current_path) == 1:
                        print("2")
                        unit.current_path = None
                    else:
                        print("3")
                        unit.current_path = find_move(
                            self.map.dict_binary_cells.get(unit.unit_type),
                            unit.positions,
                            unit.current_path[-1],
                        )
                else:
                    print("4")
                    self.map.empty_cell(unit.positions[0], unit.positions[1])
                    self.map.populate_cell(
                        unit.current_path[0][0], unit.current_path[0][1], unit
                    )
                    unit.positions = unit.current_path[0][0], unit.current_path[0][1]
                    unit.current_path.pop(0)

        for unit in self.players[1].units:
            unit.current_path = unit.current_path
            if unit.current_path:
                next_cell_in_path = self.map.cells[unit.current_path[0][0]][
                    unit.current_path[0][1]
                ]
                if next_cell_in_path.entity:
                    unit.current_path = find_move(
                        self.game.map.dict_binary_cells.get(unit.unit_type),
                        unit.positions,
                        unit.current_path[-1],
                    )
                else:
                    self.map.empty_cell(unit.positions[0], unit.positions[1])
                    self.map.populate_cell(
                        unit.current_path[0][0], unit.current_path[0][1], unit
                    )
                    unit.positions = unit.current_path[0][0], unit.current_path[0][1]
                    unit.current_path.pop(0)
