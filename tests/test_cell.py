from COE.map.cell import Cell
from COE.map.enum.cell_types import CellTypes
from COE.UI.window_ui import Window
from COE.contents.entity import Entity


def test_init():
    e = Entity("Tree", 10, (10, -10), 1, 1, 10, "")
    c = Cell(CellTypes.GRASS, [[e]])
    assert c.cell_type == CellTypes.GRASS
    assert c.entities == [[e]]


def test_get_pixel_cells_size():
    w = Window(800, 600)
    assert Cell.get_pixel_cells_size() == 28
    assert Cell.get_pixel_cells_size(25, 800, 600) == 28
