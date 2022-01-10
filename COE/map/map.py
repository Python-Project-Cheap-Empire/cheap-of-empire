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
from COE.contents.unit.enum.unit_types import UnitTypes
from COE.contents.resources.tree import Tree
from COE.contents.unit.villager import Villager
from pygame.locals import *


class Map:
    def __init__(self, *args):
        try:
            if Map.are_args_fine(args):
                self.size = Map.get_size(args)
                self.type = Map.get_type(args)
                self.resources_rarity = Map.get_resources_rarity(args)
                self.cells = Map.generate_map(
                    self.size, self.type, self.resources_rarity
                )
                self.grass_tiles = None
        except Exception as e:
            print(f"Exception handled : {e}")
            self.size = MapSizes.TINY
            self.type = MapTypes.CONTINENTAL
            self.resources_rarity = ResourcesRarity.HIGH
            self.cells = Map.generate_map(self.size, self.type, self.resources_rarity)
            self.grass_tiles = None
            print("Map was generated using default value : ")
            print("Tiny size, continental and high resources rarity")

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

    def change_cell(self, A, B, cell_type):
        self.cells[A][B] = Cell(cell_type, [])

    def draw_rect_around(
        self, window, x, y, camera, half_width_cells_size, half_height_cells_size
    ):
        _x, _y = self.map_to_screen(
            (x, y),
            camera.x_offset,
            camera.y_offset,
            half_width_cells_size,
            half_height_cells_size,
        )
        pygame.draw.polygon(
            window,
            (255, 255, 255),
            [(_x + 40, _y), (_x + 80, _y + 20), (_x + 40, _y + 40), (_x, _y + 20)],
            1,
        )

    def transform_for_unit(self, unit_type):
        trans_list = []
        for cell_list in self.cells:
            trans_list.append([])
            for cell in cell_list:
                # if cell.entity:
                #     trans_list[-1].append(0)
                if cell.cell_type.name == CellTypes.WATER.name:
                    if unit_type == UnitTypes.NAVY:
                        trans_list[-1].append(1)
                    else:
                        trans_list[-1].append(0)
                elif cell.cell_type.name == CellTypes.GRASS.name:
                    if unit_type == UnitTypes.GROUND:
                        trans_list[-1].append(1)
                    else:
                        trans_list[-1].append(0)
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
                    entity_x, entity_y = entities_pos_dict[column.entity.name.lower()]
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

    def update(self, camera):
        pass

    @staticmethod
    def generate_map(
        map_size: MapSizes = MapSizes.TINY,
        map_type: MapTypes = MapTypes.CONTINENTAL,
        resources_rarity: ResourcesRarity = ResourcesRarity.HIGH,
    ):  # pragma: no cover
        res = [
            [Cell(CellTypes.GRASS, None) for i in range(map_size.value)]
            for j in range(map_size.value)
        ]
        # res[0][0].entity = Villager((0, 0), Player("", [], [], 0, 0, 0))
        # res[2][4].entity = Tree((2, 4))
        for j in range(0, map_size.value, 2):
            for i in range(0, map_size.value, 2):
                res[i][j].entity = Tree((i, j))

        return res

    @staticmethod
    def is_type_known(map_type: MapTypes):
        if map_type in [mt for mt in MapTypes]:
            return True
        raise NotStandardizedMetricException("the map type is unknown")

    @staticmethod
    def is_resources_rarity_known(resources_rarity: ResourcesRarity):
        if resources_rarity in [rr for rr in ResourcesRarity]:
            return True
        raise NotStandardizedMetricException("the resources rarity is unknown")

    @staticmethod
    def is_map_size_known(map_size: MapSizes):
        if map_size == 0:
            raise ZeroMapSizeException("the map can't be of size 0")
        if map_size in [size for size in MapSizes]:
            return True
        raise NotStandardizedMetricException("the map size is unknown")

    @staticmethod
    def are_args_enough(args):
        if len(args) >= 3:
            return True
        raise MapArgumentsException("You need at least 3 arguments to create a map")

    @staticmethod
    def get_size(args):
        return args[0]

    @staticmethod
    def get_type(args):
        return args[1]

    @staticmethod
    def get_resources_rarity(args):
        return args[2]

    @staticmethod
    def are_args_fine(args):
        if Map.are_args_enough(args):
            map_size = Map.get_size(args)
            map_type = Map.get_type(args)
            resources_rarity = Map.get_resources_rarity(args)
            return (
                Map.is_map_size_known(map_size)
                and Map.is_type_known(map_type)
                and Map.is_resources_rarity_known(resources_rarity)
            )
        return False
