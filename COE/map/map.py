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
from COE.contents.unit.enum.unit_types import ground_units
from COE.contents.unit.enum.unit_types import navy_units


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
        except Exception as e:
            print(f"Exception handled : {e}")
            self.size = MapSizes.TINY
            self.type = MapTypes.CONTINENTAL
            self.resources_rarity = ResourcesRarity.HIGH
            self.cells = Map.generate_map()
            print("Map was generated using default value : ")
            print("Tiny size, continental and high resources rarity")

    @staticmethod
    def map_to_screen(
        map_coordinates, x_camera_offset, y_camera_offset
    ):  # pragma: no cover
        width_pixel_size, height_pixel_size = Cell.get_pixel_cells_size()
        half_width_pixel_size, half_height_pixel_size = (
            width_pixel_size / 2,
            height_pixel_size / 2,
        )
        x = (
            (map_coordinates[0] - map_coordinates[1]) * half_width_pixel_size
            + x_camera_offset
            - half_width_pixel_size
        )
        y = (
            map_coordinates[0] + map_coordinates[1]
        ) * half_height_pixel_size + y_camera_offset
        return x, y

    @staticmethod
    def screen_to_map(
        screen_pixels, x_camera_offset, y_camera_offset
    ):  # pragma: no cover
        width_pixel_size, height_pixel_size = Cell.get_pixel_cells_size()
        half_width_pixel_size, half_height_pixel_size = (
            width_pixel_size / 2,
            height_pixel_size / 2,
        )
        screen_x, screen_y = screen_pixels[0], screen_pixels[1]
        x_without_offset, y_without_offset = (
            screen_x - x_camera_offset,
            screen_y - y_camera_offset,
        )
        x = (
            x_without_offset / half_width_pixel_size
            + y_without_offset / half_height_pixel_size
        ) / 2
        y = (
            y_without_offset / half_height_pixel_size
            - x_without_offset / half_width_pixel_size
        ) / 2
        return x, y

    def transform_for_unit(self, unit_type=None):
        trans_list = []
        for cell_list in self.cells:
            trans_list.append([])
            for cell in cell_list:
                if cell.cell_type.name == "WATER":
                    if unit_type in ground_units:
                        trans_list[-1].append(0)
                    else:
                        trans_list[-1].append(1)
                elif cell.cell_type.name == "GRASS":
                    if unit_type in navy_units:
                        trans_list[-1].append(0)
                    else:
                        trans_list[-1].append(1)
        return trans_list

    def draw_map(self, window, camera, scaled_blocks):  # pragma: no cover
        """Draw a map on the screen using the cells"""
        window.display.fill((0, 0, 0))
        for x, row in enumerate(self.cells):
            for y, column in enumerate(row):
                _x, _y = Map.map_to_screen((x, y), camera.x_offset, camera.y_offset)
                window.display.blit(scaled_blocks[column.cell_type.name], (_x, _y))

    @staticmethod
    def generate_map(
        map_size: MapSizes = MapSizes.TINY,
        map_type: MapTypes = MapTypes.CONTINENTAL,
        resources_rarity: ResourcesRarity = ResourcesRarity.HIGH,
    ):  # pragma: no cover
        return [
            [Cell(CellTypes.GRASS, []) for i in range(map_size.value)]
            for j in range(map_size.value)
        ]

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
