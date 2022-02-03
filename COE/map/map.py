import copy
from COE.contents.building.building import Building
from COE.contents.entity import Entity
from COE.contents.unit.unit import Unit
from COE.logic.Player import Player
from COE.map.cell import Cell
from COE.map.exceptions.zero_map_size_exception import ZeroMapSizeException
from COE.map.exceptions.not_standardized_metric_exception import (
    NotStandardizedMetricException,
)
from COE.map.exceptions.map_arguments_exception import MapArgumentsException
from COE.map.enum.map_sizes import MapSizes
from COE.map.enum.map_types import MapTypes
from COE.map.enum.resources_rarity import ResourcesRarity
from COE.map.enum.cell_types import CellTypes
import pygame
from COE.contents.entity_types import EntityTypes
from COE.contents.unit.villager import Villager
from pygame.locals import *


class Map:
    def __init__(self, cells, players, size, type_map, resources_rarity):
        self.grass_tiles = None
        self.cells = cells
        self.size = size
        self.type = type_map
        self.resources_rarity = resources_rarity
        self.dict_binary_cells = {
            EntityTypes.GROUND: self.transform_for_unit(EntityTypes.GROUND),
            EntityTypes.NAVY: self.transform_for_unit(EntityTypes.NAVY),
        }
        self.players = players

    @staticmethod
    def map_to_screen(
        map_coordinates,
        x_camera_offset,
        y_camera_offset,
        half_width_cells_size,
        half_height_cells_size,
    ):  # pragma: no cover
        x = (
            (map_coordinates[0] - map_coordinates[1]) * half_width_cells_size
            + x_camera_offset
            - half_width_cells_size
        )
        y = (
            map_coordinates[0] + map_coordinates[1]
        ) * half_height_cells_size + y_camera_offset
        return x, y

    @staticmethod
    def screen_to_map(
        screen_pixels,
        x_camera_offset,
        y_camera_offset,
        half_width_cells_size,
        half_height_cells_size,
    ):  # pragma: no cover
        screen_x, screen_y = screen_pixels[0], screen_pixels[1]
        x_without_offset, y_without_offset = (
            screen_x - x_camera_offset,
            screen_y - y_camera_offset,
        )
        x = (
            x_without_offset / half_width_cells_size
            + y_without_offset / half_height_cells_size
        ) / 2
        y = (
            y_without_offset / half_height_cells_size
            - x_without_offset / half_width_cells_size
        ) / 2
        return x, y

    def draw_rect_around(
        self,
        window,
        selected_entity,
        camera,
        half_width_cells_size,
        half_height_cells_size,
    ):  # pragma: no cover
        _x, _y = self.map_to_screen(
            (selected_entity.master.positions[0], selected_entity.master.positions[1]),
            camera.x_offset,
            camera.y_offset,
            half_width_cells_size,
            half_height_cells_size,
        )
        width_cells_size = 2 * half_width_cells_size
        height_cells_size = 2 * half_height_cells_size
        pygame.draw.polygon(
            window,
            (255, 255, 255),
            [
                (_x + half_width_cells_size, _y),
                (
                    _x
                    + width_cells_size
                    + (half_width_cells_size * (selected_entity.width - 1)),
                    _y + (half_height_cells_size * (selected_entity.height)),
                ),
                (
                    _x + half_width_cells_size,
                    _y + (height_cells_size * (selected_entity.height)),
                ),
                (
                    _x - (half_width_cells_size * (selected_entity.width - 1)),
                    _y + (half_height_cells_size * selected_entity.height),
                ),
            ],
            1,
        )

    def draw_construction_bar(
        self,
        window,
        x,
        y,
        camera,
        half_width_cells_size,
        half_height_cells_size,
        construct_percent,
    ):
        _x, _y = self.map_to_screen(
            (x, y),
            camera.x_offset,
            camera.y_offset,
            half_width_cells_size,
            half_height_cells_size,
        )
        height_cells_size = 2 * half_height_cells_size
        bar = [_x + 10, _y - 1.5 * height_cells_size, construct_percent, 5]
        bar_color = (0, 0, 255)
        bar2 = [_x + 10, _y - 1.5 * height_cells_size, 100, 5]
        bar_color2 = (255, 0, 0)
        pygame.draw.rect(window, bar_color2, bar2)
        pygame.draw.rect(window, bar_color, bar)

    def draw_health_bar(
        self,
        window,
        x,
        y,
        camera,
        half_width_cells_size,
        half_height_cells_size,
        hp,
        max_hp,
    ):  # pragma: no cover
        if hp < 0:
            return
        _x, _y = self.map_to_screen(
            (x, y),
            camera.x_offset,
            camera.y_offset,
            half_width_cells_size,
            half_height_cells_size,
        )
        ratio = hp / max_hp
        height_cells_size = 2 * half_height_cells_size
        bar_position1 = [_x + 10, _y - 1.5 * height_cells_size, 50 * ratio, 5]
        bar_color1 = (50, 205, 50)
        bar_position2 = [_x + 10, _y - 1.5 * height_cells_size, 50, 5]
        bar_color2 = (255, 0, 0)
        pygame.draw.rect(window, bar_color2, bar_position2)
        pygame.draw.rect(window, bar_color1, bar_position1)

    def update_cell(self, x, y):
        cell_type = self.cells[x][y].cell_type
        if cell_type == CellTypes.GRASS:
            if self.cells[x][y].entity:
                self.dict_binary_cells.get(EntityTypes.GROUND)[y][x] = 0
            else:
                self.dict_binary_cells.get(EntityTypes.GROUND)[y][x] = 1
            self.dict_binary_cells.get(EntityTypes.NAVY)[y][x] = 0

        elif cell_type == CellTypes.WATER:
            if self.cells[x][y].entity:
                self.dict_binary_cells.get(EntityTypes.NAVY)[y][x] = 0
            else:
                self.dict_binary_cells.get(EntityTypes.NAVY)[y][x] = 1
            self.dict_binary_cells.get(EntityTypes.GROUND)[y][x] = 0

    def change_cell(self, x, y, cell_type):
        self.cells[x][y] = Cell(cell_type, None)
        self.update_cell(x, y)

    def populate_cell(self, x, y, entity: Entity):
        if entity:
            self.cells[x][y].entity = entity
            for k in self.dict_binary_cells:
                self.dict_binary_cells.get(k)[y][x] = 0

    def empty_cell(self, x, y):
        entity_on_cell = self.cells[x][y].entity
        if entity_on_cell is not None:
            self.dict_binary_cells.get(entity_on_cell.entity_type)[y][x] = 1
            self.cells[x][y].entity = None

    def place_building(self, x, y, player, building: Building):
        for x_ in range(building.width):
            for y_ in range(building.height):
                s = self.cells[x + x_][y + y_]
                if s.entity or s.cell_type.value != building.entity_type.value:
                    return
        if (
            player._wood >= building.wood_required
            and player._stone >= building.stone_required
        ):

            self.populate_cell(x, y, building)
            player.buildings.append(building)
            for x_ in range(building.width):
                for y_ in range(building.height):
                    if x_ != 0 or y_ != 0:
                        building_ = copy.copy(building)
                        building_.is_master = False
                        building_.positions = (x + x_, y + y_)
                        building_.master = building
                        self.populate_cell(x + x_, y + y_, building_)
                        building.sub_entities.append(building_)
                        player.buildings.append(building_)
            player._wood -= building.wood_required
            player._stone -= building.stone_required

    def transform_for_unit(self, entity_type):
        trans_list = [
            [0 for _ in range(self.size.value)] for _ in range(self.size.value)
        ]
        for x in range(self.size.value):
            for y in range(self.size.value):
                if self.cells[x][y].entity:
                    trans_list[y][x] = 0
                elif self.cells[x][y].cell_type.name == CellTypes.WATER.name:
                    if entity_type == EntityTypes.NAVY:
                        trans_list[y][x] = 1
                    else:
                        trans_list[y][x] = 0
                elif self.cells[x][y].cell_type.name == CellTypes.GRASS.name:
                    if entity_type == EntityTypes.GROUND:
                        trans_list[y][x] = 1
                    else:
                        trans_list[y][x] = 0
        return trans_list

    def draw_map(self, window, camera):  # pragma: no cover
        """Draw a map on the screen using the cells"""
        window.blit(
            self.grass_tiles,
            (
                camera.x_offset - self.grass_tiles.get_width() / 2 + 0,
                camera.y_offset,
            ),
        )

    def draw_entities(
        self,
        window,
        camera,
        entities_images,
        entities_pos_dict,
        width_cells_size,
        height_cells_size,
        half_width_cells_size,
        half_height_cells_size,
        x_limit,
        y_limit,
    ):  # pragma: no cover
        for x, row in enumerate(self.cells):
            for y, column in enumerate(row):
                if column.entity:
                    if column.entity.is_master:
                        entity_x, entity_y = entities_pos_dict[
                            column.entity.name.lower()
                        ]
                        _x, _y = Map.map_to_screen(
                            (x, y),
                            camera.x_offset + entity_x,
                            camera.y_offset + entity_y,
                            half_width_cells_size,
                            half_height_cells_size,
                        )
                        if (
                            _x <= x_limit
                            and _x >= -width_cells_size
                            and _y >= -height_cells_size
                            and _y <= y_limit
                        ):
                            window.blit(
                                entities_images[column.entity.name.lower()], (_x, _y)
                            )

    def blit_world(self):  # pragma: no cover
        scaled_blocks = Cell.get_scaled_blocks()
        width_cells_size, height_cells_size = Cell.get_pixel_cells_size()
        half_width_cells_size = width_cells_size / 2
        half_height_cells_size = height_cells_size / 2
        width_map_pixel_size = self.size.value * width_cells_size
        height_map_pixel_size = self.size.value * height_cells_size
        blit_world = pygame.Surface(
            (width_map_pixel_size, height_map_pixel_size)
        ).convert_alpha()
        for x, row in enumerate(self.cells):
            for y, column in enumerate(row):
                _x, _y = Map.map_to_screen(
                    (x, y),
                    width_map_pixel_size / 2,
                    0,
                    half_width_cells_size,
                    half_height_cells_size,
                )
                blit_world.blit(scaled_blocks[column.cell_type.name], (_x, _y))
        self.grass_tiles = blit_world
