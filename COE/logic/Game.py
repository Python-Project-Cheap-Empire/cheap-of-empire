from select import select
from typing import List
from COE.contents.building.barrack import Barrack
from COE.contents.building.building import Building
from COE.contents.building.house import House
from COE.contents.building.town_center import TownCenter
from COE.contents.entity import Entity
from COE.contents.unit.unit import Unit
from COE.contents.unit.villager import Villager
from COE.logic.Player import Player
from COE.logic.path_finding import find_move
from COE.map.map import Map
from COE.camera.camera import Camera
from COE.contents.entity_types import EntityTypes
from COE.contents.unit.axeman import Axeman
from COE.contents.building.town_center import TownCenter
from COE.contents.resources.resource import Resource
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
        self.prev_time = time.time()
        self.ia_defenders = []
        self.is_victory = None
        self.training_time = 12

    def set_speed(self, new_speed):
        assert (
            isinstance(new_speed, float) and new_speed > 0
        ), "new_speed is a float and new_speed > 0"
        self.speed = new_speed

    def set_attack(self, unit, unit_atk_by):  # pragma: no cover
        unit.is_attacking = True
        unit.attacked_entity = unit_atk_by.is_attacked_by.pop(0)
        if not unit.check_in_range(unit.attacked_entity):
            x, y = unit.positions
            j, k = unit.attacked_entity.positions
            unit.current_path = find_move(
                self.map.dict_binary_cells.get(unit.entity_type),
                (x, y),
                (j, k),
            )

    def check_win_def_for_player(self, player):  # pragma: no cover
        is_tc = False
        for batiment in player.buildings:
            if isinstance(batiment, TownCenter):
                is_tc = True
        if not is_tc:
            if player._is_human:
                self.is_victory = False
            else:
                self.is_victory = True

    def update(self):  # pragma: no cover

        for player in self.players:
            self.check_win_def_for_player(player)

        # Spawning IA units
        ia_list = self.players[1:]
        now = time.time()

        spawn_rate = 2000
        if (now - self.prev_time) * 60 * self.speed > spawn_rate:
            ia_list = self.players[1:]
            for ia in ia_list:
                if len(ia.buildings) > 0:
                    spw_x, spw_y = ia.buildings[0].positions
                    paths = find_move(
                        self.map.dict_binary_cells.get(EntityTypes.GROUND),
                        (spw_x, spw_y),
                        (spw_x - 4, spw_y + 4),
                    )
                    if paths:
                        # Getting free cell
                        x_pos, y_pos = paths[-1]
                        axe = Axeman((x_pos, y_pos), ia)
                        ia.units.append(axe)
                        self.map.populate_cell(x_pos, y_pos, axe)

                        if len(self.ia_defenders) == 3:
                            for batiment in self.players[0].buildings:
                                if isinstance(batiment, TownCenter):
                                    axe.attacked_entity = batiment
                                    axe.is_attacking = True

                                    axe.current_path = find_move(
                                        self.map.dict_binary_cells.get(axe.entity_type),
                                        axe.positions,
                                        batiment.positions,
                                    )
                        else:
                            self.ia_defenders.append(axe)
                            print(f"Number of defenders : {len(self.ia_defenders)}")

            spawn_rate -= 15
            if spawn_rate < 60:
                spawn_rate = 60
            self.prev_time = now
        for building in self.players[0].buildings:
            nb_house = 0
            for building_ in self.players[0].buildings:
                if isinstance(building_, House):
                    if building_.is_master:
                        if building_.construction_percent == 100:
                            nb_house += 1
            if len(building.player.units) < 5 + (5 * nb_house):
                if isinstance(building, Barrack):
                    if building.update_training(self.speed):
                        x, y = building.pop_unit(self.map)
                        if list((x, y)) != [-1, -1]:
                            u = Axeman((x, y), building.player)
                            building.player.units.append(u)
                            self.map.populate_cell(x, y, u)
                elif isinstance(building, TownCenter):
                    if building.update_training(self.speed):
                        x, y = building.pop_unit(self.map)
                        if list((x, y)) != [-1, -1]:
                            u = Villager((x, y), building.player)
                            building.player.units.append(u)
                            self.map.populate_cell(x, y, u)

        # defenders check if an enemy is in range
        for ia_unit in self.players[1].units:
            if len(ia_unit.is_attacked_by) > 0:
                self.set_attack(ia_unit, ia_unit)

        for defender in self.ia_defenders:
            if len(self.players[1].buildings) > 0:
                if len(self.players[1].buildings[0].is_attacked_by) > 0:
                    tc = self.players[1].buildings[0]
                    self.set_attack(defender, tc)
                if defender.is_attacking:
                    if not defender.check_in_range(defender.attacked_entity):
                        x, y = defender.positions
                        j, k = defender.attacked_entity.positions
                        defender.current_path = find_move(
                            self.map.dict_binary_cells.get(defender.entity_type),
                            (x, y),
                            (j, k),
                        )

        # For each unit of the human player
        all_units = self.players[0].units + self.players[1].units
        for unit in all_units:
            self.unit_action(unit)

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
            ally_villager_in_selected_units = False
            if event.button == 1:
                for entity in self.currently_selected:
                    if isinstance(entity, Villager) and entity.player._is_human:
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
                            for building, img in static.scaled_UI_imgs[
                                "buildings"
                            ].items():
                                if (
                                    img[0]
                                    .get_rect(topleft=img[1])
                                    .collidepoint(mouse_pos)
                                ):
                                    self.selected_building = building
                        else:
                            if (
                                x >= 0
                                and x < self.map.size.value
                                and y >= 0
                                and y < self.map.size.value
                            ):
                                if self.selected_building:
                                    building = None
                                    if self.selected_building == "house":
                                        building = House((x, y), self.players[0])
                                    elif self.selected_building == "barrack":
                                        building = Barrack((x, y), self.players[0])
                                    if building:
                                        self.map.place_building(
                                            x, y, self.players[0], building
                                        )
                                        self.selected_building = None
                                        for entity in self.currently_selected:
                                            if isinstance(entity, Villager):
                                                entity.is_building = True
                                                entity.building = building
                                                entity.current_path = find_move(
                                                    self.map.dict_binary_cells.get(
                                                        entity.entity_type
                                                    ),
                                                    entity.positions,
                                                    building.positions,
                                                )
                                    return

                            if not self.mouse_down:
                                self.mouse_down = True
                                self.x, self.y = x, y
                                if self.map.cells[x][y].entity:
                                    self.currently_selected = [
                                        self.map.cells[x][y].entity
                                    ]
                                else:
                                    self.currently_selected = []
                        ally_villager_in_selected_units = True
                        break
                    if isinstance(entity, Barrack) and entity.player._is_human:
                        img, pos = (
                            static.scaled_UI_imgs["clubman"][0],
                            static.scaled_UI_imgs["clubman"][1],
                        )
                        if img.get_rect(topleft=pos).collidepoint(mouse_pos):
                            entity.train_axeman(x, y, self.training_time)
                    if isinstance(entity, TownCenter) and entity.player._is_human:
                        img, pos = (
                            static.scaled_UI_imgs["villager_production"][0],
                            static.scaled_UI_imgs["villager_production"][1],
                        )
                        if img.get_rect(topleft=pos).collidepoint(mouse_pos):
                            entity.train_villager(x, y, self.training_time)
                if not ally_villager_in_selected_units:
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
                                building = House((x, y), self.players[0])
                                self.map.place_building(x, y, self.players[0], building)
                            elif self.selected_building == "barrack":
                                building = Barrack((x, y), self.players[0])
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
                                        self.map.cells[x][
                                            y
                                        ].entity.is_attacked_by.append(selected_unit)

                                    elif (
                                        self.map.cells[x][y].entity
                                        in self.players[0].buildings
                                    ):

                                        selected_unit.building = self.map.cells[x][
                                            y
                                        ].entity.master
                                        if isinstance(
                                            self.map.cells[x][y].entity, TownCenter
                                        ) and isinstance(selected_unit, Villager):
                                            selected_unit.is_returning = True
                                            selected_unit.current_path = find_move(
                                                self.map.dict_binary_cells.get(
                                                    selected_unit.entity_type
                                                ),
                                                selected_unit.positions,
                                                self.map.cells[x][
                                                    y
                                                ].entity.master.positions,
                                            )
                                        else:
                                            selected_unit.current_path = find_move(
                                                self.map.dict_binary_cells.get(
                                                    selected_unit.entity_type
                                                ),
                                                selected_unit.positions,
                                                (x, y),
                                            )

                                    else:
                                        if isinstance(
                                            selected_unit, Villager
                                        ) and isinstance(
                                            self.map.cells[x][y].entity, Resource
                                        ):
                                            selected_unit.current_path = find_move(
                                                self.map.dict_binary_cells.get(
                                                    selected_unit.entity_type
                                                ),
                                                selected_unit.positions,
                                                (x, y),
                                            )
                                            clicked_resource = self.map.cells[x][
                                                y
                                            ].entity
                                            if selected_unit.check_ressource(
                                                clicked_resource
                                            ):
                                                selected_unit.gathered_resource = (
                                                    clicked_resource
                                                )
                                                selected_unit.gathered_resource_type = (
                                                    clicked_resource.type
                                                )
                                        else:
                                            selected_unit.current_path = find_move(
                                                self.map.dict_binary_cells.get(
                                                    selected_unit.entity_type
                                                ),
                                                selected_unit.positions,
                                                (x, y),
                                            )
                                        selected_unit.building = None
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
                                elif selected_unit.is_attacking:
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
            self.training_time = self.training_time - 2
            if self.training_time <= 0:
                self.training_time = 15

    def unit_action(self, unit):  # pragma: no cover
        now = time.time()
        if isinstance(unit, Villager):
            if unit.building:
                if unit.building.construction_percent < 100:
                    if any(
                        abs(unit.positions[0] - sub_entity.positions[0]) == 1
                        and abs(unit.positions[1] - sub_entity.positions[1]) == 1
                        for sub_entity in unit.building.master.sub_entities
                    ):
                        if (
                            (now - unit.prev_construct_time)
                            * 60
                            * self.speed
                            * unit.speed
                            > unit.building.construction_time
                        ):
                            unit.building.master.construction_percent += 1
                            unit.prev_construct_time = now

            if unit.is_returning:
                for building in unit.player.buildings:
                    if isinstance(building, TownCenter):
                        if unit.check_in_range(building):
                            unit.transfer_resource_to_player()
                            unit.is_returning = False
                        break
            elif (
                unit.gathered_resource
                is not None
                # and unit.check_in_range(unit.gathered_resource)
            ):
                if unit.gathered_resource.amount <= 0:
                    self.map.empty_cell(
                        unit.gathered_resource.positions[0],
                        unit.gathered_resource.positions[1],
                    )
                    for unit_ in unit.player.units:
                        if isinstance(unit_, Villager):
                            if unit_.gathered_resource == unit.gathered_resource:
                                unit_.gathered_resource = None
                    unit.gathered_resource = None
                if unit.amount_holding >= unit.MAX_AMOUNT_HOLDING:
                    for building in unit.player.buildings:
                        if isinstance(building, TownCenter):
                            unit.current_path = find_move(
                                self.map.dict_binary_cells.get(unit.entity_type),
                                unit.positions,
                                (building.positions[0], building.positions[1]),
                            )
                            unit.is_returning = True
                            break
                elif unit.check_in_range(unit.gathered_resource):
                    unit.update_gathering(self.speed)

                elif unit.gathered_resource is not None:
                    unit.current_path = unit.current_path = find_move(
                        self.map.dict_binary_cells.get(unit.entity_type),
                        unit.positions,
                        (
                            unit.gathered_resource.positions[0],
                            unit.gathered_resource.positions[1],
                        ),
                    )
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
            attacked_player = unit.attacked_entity.player
            if unit.attacked_entity.hp <= 0:
                unit.attacked_entity = None
                unit.is_attacking = False
                if not unit.player.is_human and unit not in self.ia_defenders:
                    unit.is_attacking = True
                    for batiment in self.players[0].buildings:
                        if isinstance(batiment, TownCenter):
                            unit.attacked_entity = batiment
            else:
                remaining_hp = unit.update_attack(self.speed)
                if remaining_hp is not None and remaining_hp <= 0:
                    # if unit.attacked_entity.is_master:
                    for entity in unit.attacked_entity.master.sub_entities[::-1]:
                        if isinstance(entity, Building):
                            attacked_player.buildings.remove(entity)
                        elif isinstance(entity, Unit):
                            attacked_player.units.remove(entity)
                            if entity in self.ia_defenders:
                                self.ia_defenders.remove(entity)
                        self.map.empty_cell(entity.positions[0], entity.positions[1])

                    unit.attacked_entity = None
                    unit.is_attacking = False
