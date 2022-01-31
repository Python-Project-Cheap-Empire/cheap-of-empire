from typing import List
from COE.contents.building.barrack import Barrack
from COE.contents.building.building import Building
from COE.contents.building.house import House
from COE.contents.entity import Entity
from COE.contents.unit.unit import Unit
from COE.contents.unit.villager import Villager
from COE.logic.Player import Player
from COE.logic.path_finding import find_move
from COE.map.map import Map
from COE.camera.camera import Camera
import pygame
import time


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
        self.selected_building = None

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
                        self.map.dict_binary_cells.get(unit.entity_type),
                        unit.positions,
                        unit.current_path[-1],
                    )
                else:
                    now = time.time()
                    if (now - unit.prev_move_time) * 60 * self.speed * unit.speed > 20:
                        self.map.empty_cell(unit.positions[0], unit.positions[1])
                        self.map.populate_cell(
                            unit.current_path[0][0], unit.current_path[0][1], unit
                        )
                        unit.positions = (
                            unit.current_path[0][0],
                            unit.current_path[0][1],
                        )
                        unit.current_path.pop(0)
                        unit.prev_move_time = now
            """
            attack an enemy if is_attack and check_in_range
            """
            if (
                unit.is_attacking
                and unit.attacked_entity
                and unit.check_in_range(unit.attacked_entity)
            ):
                if unit.attacked_entity.hp <= 0:
                    unit.attacked_entity = None
                    unit.is_attacking = False
                else:
                    remaining_hp = unit.update_attack(self.speed)
                    if remaining_hp is not None and remaining_hp <= 0:
                        if unit.attacked_entity.is_master:
                            for entity in unit.attacked_entity.sub_entities:
                                if isinstance(entity, Building):
                                    self.players[1].buildings.remove(entity)
                                elif isinstance(entity, Unit):
                                    self.players[1].units.remove(entity)
                                self.map.empty_cell(
                                    entity.positions[0], entity.positions[1]
                                )
                            if isinstance(unit.attacked_entity, Building):
                                self.players[1].buildings.remove(unit.attacked_entity)
                            elif isinstance(unit.attacked_entity, Unit):
                                self.players[1].units.remove(unit.attacked_entity)
                            self.map.empty_cell(
                                unit.attacked_entity.positions[0],
                                unit.attacked_entity.positions[1],
                            )

                        else:
                            for entity in unit.attacked_entity.master.sub_entities:
                                if isinstance(entity, Building):
                                    self.players[1].buildings.remove(entity)
                                elif isinstance(entity, Unit):
                                    self.players[1].units.remove(entity)
                                self.map.empty_cell(
                                    entity.positions[0], entity.positions[1]
                                )

                            if isinstance(unit.attacked_entity.master, Building):
                                self.players[1].buildings.remove(
                                    unit.attacked_entity.master
                                )
                            elif isinstance(unit.attacked_entity.master, Unit):
                                self.players[1].units.remove(
                                    unit.attacked_entity.master
                                )
                            self.map.empty_cell(
                                unit.attacked_entity.master.positions[0],
                                unit.attacked_entity.master.positions[1],
                            )
                        unit.attacked_entity = None
                        unit.is_attacking = False

                # print("mode attack is on")
        for unit in self.players[1].units:
            unit.current_path = unit.current_path
            if unit.current_path:
                next_cell_in_path = self.map.cells[unit.current_path[0][0]][
                    unit.current_path[0][1]
                ]
                if next_cell_in_path.entity:
                    unit.current_path = find_move(
                        self.map.dict_binary_cells.get(unit.entity_type),
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
                if any(
                    isinstance(entity, Villager) for entity in self.currently_selected
                ):  # Bottom left action panel is displayed
                    if (
                        static.scaled_UI_imgs["menu_panel"][0]
                        .get_rect(topleft=static.scaled_UI_imgs["menu_panel"][1])
                        .collidepoint(mouse_pos)
                    ):
                        pass
                    elif (
                        static.scaled_UI_imgs["action_panel"][0]
                        .get_rect(topleft=static.scaled_UI_imgs["action_panel"][1])
                        .collidepoint(mouse_pos)
                    ):
                        for building, img in static.scaled_UI_imgs["buildings"].items():
                            if img[0].get_rect(topleft=img[1]).collidepoint(mouse_pos):
                                self.selected_building = building
                    else:
                        if (
                            x >= 0
                            and x < self.map.size.value
                            and y >= 0
                            and y < self.map.size.value
                        ):
                            if self.selected_building:
                                if self.selected_building == "house":
                                    building = House((x, y))
                                    self.map.place_building(
                                        x, y, self.players[0], building
                                    )
                                    self.selected_building = None
                                elif self.selected_building == "barrack":
                                    building = Barrack((x, y))
                                    self.map.place_building(
                                        x, y, self.players[0], building
                                    )
                                    self.selected_building = None
                                return

                        if not self.mouse_down:
                            self.mouse_down = True
                            self.x, self.y = x, y
                            if self.map.cells[x][y].entity:
                                self.currently_selected = [self.map.cells[x][y].entity]
                            else:
                                self.currently_selected = []

                else:
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

                        if self.selected_building:
                            if self.selected_building == "house":
                                building = House((x, y))
                                self.map.place_building(x, y, self.players[0], building)
                            elif self.selected_building == "barrack":
                                building = Barrack((x, y))
                                self.map.place_building(x, y, self.players[0], building)

                    if not self.mouse_down:
                        self.mouse_down = True
                        self.x, self.y = x, y
                        if self.map.cells[x][y].entity:
                            self.currently_selected = [self.map.cells[x][y].entity]
                        else:
                            self.currently_selected = []

            elif event.button == 3:
                self.selected_building = None
                if self.currently_selected:  # Bottom left action panel is displayed
                    if not static.scaled_UI_imgs["action_panel"][0].get_rect(
                        topleft=static.scaled_UI_imgs["action_panel"][1]
                    ).collidepoint(mouse_pos) and not static.scaled_UI_imgs[
                        "menu_panel"
                    ][
                        0
                    ].get_rect(
                        topleft=static.scaled_UI_imgs["menu_panel"][1]
                    ).collidepoint(
                        mouse_pos
                    ):
                        if (
                            x >= 0
                            and x < self.map.size.value
                            and y >= 0
                            and y < self.map.size.value
                        ):
                            for selected_unit in self.currently_selected:
                                if selected_unit in self.players[0].units:
                                    if (
                                        self.map.cells[x][y].entity
                                        in self.players[1].units
                                        or self.map.cells[x][y].entity
                                        in self.players[1].buildings
                                    ):
                                        selected_unit.current_path = find_move(
                                            self.map.dict_binary_cells.get(
                                                selected_unit.entity_type
                                            ),
                                            selected_unit.positions,
                                            (x, y),
                                        )
                                        selected_unit.attacked_entity = self.map.cells[
                                            x
                                        ][y].entity
                                        selected_unit.is_attacking = True
                                    else:
                                        selected_unit.current_path = find_move(
                                            self.map.dict_binary_cells.get(
                                                selected_unit.entity_type
                                            ),
                                            selected_unit.positions,
                                            (x, y),
                                        )
                                        if selected_unit.is_attacking:
                                            selected_unit.is_attacking = False
                                            selected_unit.attacked_entity = None
                                            # print("Turnoff attack")
                else:
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
                                    selected_unit.current_path = find_move(
                                        self.map.dict_binary_cells.get(
                                            selected_unit.entity_type
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
                                            selected_unit.entity_type
                                        ),
                                        selected_unit.positions,
                                        (x, y),
                                    )
                                    if selected_unit.is_attacking:
                                        selected_unit.is_attacking = False
                                        selected_unit.attacked_entity = None
                                        # print("Turnoff attack")

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
                            s = self.map.cells[x][y].entity
                            if s:
                                self.currently_selected.append(s)
            self.mouse_down = False
            self.selection_rectangle = None

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F4:
            self.speed = (self.speed + 2) % 12

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F5:
            self.map.place_building(15, 15, self.players[1], House((15, 15)))
