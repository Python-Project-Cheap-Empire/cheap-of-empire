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

    def draw_map(self, fenetre, camera=None):  # pragma: no cover
        """Draw a map on the screen using the cells"""
        pixel_cells_size = Cell.get_pixel_cells_size()
        blocks_dict = Cell.get_scaled_blocks()
        map_size = self.size.value  # length == height because the map is square
        x = y = -pixel_cells_size  # x pos
        row_modulo = pixel_cells_size * map_size  #
        column_modulo = pixel_cells_size * map_size
        for row in self.cells:
            y = (y + pixel_cells_size) % row_modulo
            for column in row:
                x = (x + pixel_cells_size) % column_modulo
                fenetre.blit(blocks_dict[column.cell_type.name], (x, y))

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
