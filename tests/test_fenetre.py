from COE.UI.window_ui import Window
from COE.map.map import Map


def test_fenetre():
    map = Map()
    F = Window()
    assert F.loop
    assert F.show(map) is None
    assert F.get_loop()
    assert F.quit() is None
    assert F.menu.loop
