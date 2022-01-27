from typing import List
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

    def __init__(self, players: list, map, speed, camera, name: str, timer):
        """
        Constructs all the necessary attributes for the Game object.

        :param players: list
        :param map_game: Map
        :param speed: float
        :param name: str
        """
        self.players: list[Player] = players
        self.map: Map = map
        self.speed = speed
        self.camera = camera
        self.name = name
        self.mouse_down = False
        self.selection_rectangle = None
        self.timer = timer
        self.currently_selected: List[Entity] = []
        self.x_, self.y_, self.x, self.y = -1, -1, -1, -1

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
                    # if len(unit.current_path) == 1:
                    #     unit.current_path = None
                    # else:
                    unit.current_path = find_move(
                        self.map.dict_binary_cells.get(unit.unit_type),
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
            """
            attack an enemy if is_attack and check_in_range
            """
            if unit.attacked_entity is None or unit.attacked_entity.die():
                unit.attacked_entity = None
                unit.is_attacking = False
            elif unit.is_attacking and unit.check_in_range(unit.attacked_entity):
                # unit.attack()
                unit.update_attack()
                print("mode attack is on")
        for unit in self.players[1].units:
            unit.current_path = unit.current_path
            if unit.current_path:
                next_cell_in_path = self.map.cells[unit.current_path[0][0]][
                    unit.current_path[0][1]
                ]
                if next_cell_in_path.entity:
                    unit.current_path = find_move(
                        self.map.dict_binary_cells.get(unit.unit_type),
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
            if unit.die():
                self.map.empty_cell(unit.positions[0], unit.positions[1])
                self.players[1].units.remove(unit)

    def event(self, static, event):  # pragma: no cover
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x, y = self.map.screen_to_map(
                mouse_pos,
                self.camera.x_offset,
                self.camera.y_offset,
                static.half_width_cells_size,
                static.half_height_cells_size,
            )
            x, y = int(x), int(y)

            if event.button == 1:
                if not self.mouse_down:
                    self.mouse_down = True
                    self.x, self.y = x, y
                    self.currently_selected = []
                if (
                    x >= 0
                    and x < self.map.size.value
                    and y >= 0
                    and y < self.map.size.value
                ):
                    if self.map.cells[x][y].entity:
                        self.currently_selected = [self.map.cells[x][y].entity]
                    else:
                        self.currently_selected = []

            elif event.button == 3:
                if (
                    x >= 0
                    and x < self.map.size.value
                    and y >= 0
                    and y < self.map.size.value
                ):
                    for selected_unit in self.currently_selected:
                        if selected_unit in self.players[0].units:
                            if (
                                self.map.cells[x][y].entity in self.players[1].units
                                or self.map.cells[x][y].entity
                                in self.players[1].buildings
                            ):
                                if selected_unit.check_in_range(
                                    self.map.cells[x][y].entity
                                ):
                                    # selected_unit.attack(selected_unit.attacked_entity)
                                    selected_unit.update_attack()
                                    print(
                                        "attack unit at pos{}".format(
                                            self.map.cells[x][y]
                                        )
                                    )
                                else:
                                    selected_unit.current_path = find_move(
                                        self.map.dict_binary_cells.get(
                                            selected_unit.unit_type
                                        ),
                                        selected_unit.positions,
                                        (x, y),
                                    )
                                selected_unit.attacked_entity = self.map.cells[x][
                                    y
                                ].entity
                                selected_unit.is_attacking = True
                            else:
                                selected_unit.current_path = find_move(
                                    self.map.dict_binary_cells.get(
                                        selected_unit.unit_type
                                    ),
                                    selected_unit.positions,
                                    (x, y),
                                )
                                if selected_unit.is_attacking:
                                    selected_unit.is_attacking = False
                                    selected_unit.attacked_entity = None
                                    print("Turnoff attack")

        elif event.type == pygame.MOUSEMOTION and self.mouse_down:
            x, y = pygame.mouse.get_pos()
            self.x_, self.y_ = self.map.screen_to_map(
                (x, y),
                self.camera.x_offset,
                self.camera.y_offset,
                static.half_width_cells_size,
                static.half_height_cells_size,
            )

            x_, y_ = self.map.map_to_screen(
                (self.x, self.y),
                self.camera.x_offset,
                self.camera.y_offset,
                static.half_width_cells_size,
                static.half_height_cells_size,
            )
            self.selection_rectangle = pygame.Rect(x_, y_, x - x_, y - y_)

        elif event.type == pygame.MOUSEBUTTONUP:
            if self.x != -1 and self.y != -1:
                for x in range(int(self.x), int(self.x_ + 1)):
                    for y in range(int(self.y), int(self.y_ + 1)):
                        if x < self.map.size.value and y < self.map.size.value:
                            print(f"mouse x, y : {x}, {y}")
                            s = self.map.cells[x][y].entity
                            if s:
                                self.currently_selected.append(s)
            self.mouse_down = False
            self.selection_rectangle = None
