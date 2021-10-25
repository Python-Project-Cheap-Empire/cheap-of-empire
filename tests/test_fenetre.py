from COE.UI.UI_Fenetre import Fenetre


def test_fenetre():
    F = Fenetre()
    assert F.loop
    assert F.display() is None
    assert F.get_loop()
    assert F.quitter() is None
    assert F.menu.loop
