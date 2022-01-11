from COE.map.cell import Cell
from COE.map.enum.cell_types import CellTypes
from COE.contents.resources.tree import Tree


def test_init():
    t = Tree((10, -10))
    c = Cell(CellTypes.GRASS, t)
    assert c.cell_type == CellTypes.GRASS
    assert c.entity == t


def test_get_pixel_cells_size():
    assert Cell.get_pixel_cells_size() == (80, 40)
