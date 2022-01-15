from COE.contents.entity import Entity
from COE.contents.unit.unit import Unit
from COE.contents.unit.villager import Villager
from COE.logic.Player import Player
from COE.logic.path_finding import find_move
from COE.map.map import Map
from COE.camera.camera import Camera
import pygame


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
        self.currently_selected: Entity = None
        self.set_initial_ressources()

    def set_speed(self, new_speed):
        assert (
            isinstance(new_speed, float) and new_speed > 0
        ), "new_speed is a float and new_speed > 0"
        self.speed = new_speed

    def set_initial_ressources(self):
        if self.players:
            for i in range(3):
                v0 = Villager((2 + i, 2 + i), self.players[0])
                self.players[0].units.append(v0)
                self.map.cells[2 + i][2 + i].entity = v0
                if len(self.players) > 1:
                    v1 = Villager((10 + i, 10 + i), self.players[1])
                    self.players[1].units.append(v1)
                    self.map.cells[10 + i][10 + i].entity = v1

    def update(self):
        for unit in self.players[0].units:
            unit_current_path = unit.current_path
            if unit_current_path:
                next_cell_in_path = self.map.cells[unit_current_path[0][0]][
                    unit_current_path[0][1]
                ]
                if not next_cell_in_path.entity:
                    self.map.cells[unit.positions[0]][unit.positions[1]].entity = None
                    next_cell_in_path.entity = unit
                    unit.positions = unit_current_path[0][0], unit_current_path[0][1]
                    unit_current_path.pop(0)

        for unit in self.players[1].units:
            unit_current_path = unit.current_path
            if unit_current_path:
                next_cell_in_path = self.map.cells[unit_current_path[0][0]][
                    unit_current_path[0][1]
                ]
                if not next_cell_in_path.entity:
                    self.map.cells[unit.positions[0]][unit.positions[1]].entity = None
                    next_cell_in_path.entity = unit
                    unit.positions = unit_current_path[0][0], unit_current_path[0][1]
                    unit_current_path.pop(0)

    def event(self, static):
        if pygame.mouse.get_pressed()[0]:
            x, y = self.map.screen_to_map(
                pygame.mouse.get_pos(),
                self.camera.x_offset,
                self.camera.y_offset,
                static.half_width_cells_size,
                static.half_height_cells_size,
            )
            x, y = int(x), int(y)
            if self.map.cells[x][y].entity:
                self.currently_selected = self.map.cells[x][y].entity
            else:
                self.currently_selected = None

        elif pygame.mouse.get_pressed()[2]:
            if (
                self.currently_selected
                and self.currently_selected in self.players[0].units
            ):
                x, y = self.map.screen_to_map(
                    pygame.mouse.get_pos(),
                    self.camera.x_offset,
                    self.camera.y_offset,
                    static.half_width_cells_size,
                    static.half_height_cells_size,
                )
                x, y = int(x), int(y)
                if (
                    x >= 0
                    and x < self.map.size.value
                    and y >= 0
                    and y < self.map.size.value
                ):
                    if isinstance(self.currently_selected, Unit):
                        self.currently_selected.current_path = find_move(
                            self.map.transform_for_unit(
                                self.currently_selected.unit_type
                            ),
                            self.currently_selected.positions,
                            (x, y),
                        )
