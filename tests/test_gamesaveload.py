from COE.logic.GameSaveLoad import GameSaveLoad


def test_singleton():
    sl1 = GameSaveLoad()
    sl2 = GameSaveLoad()

    assert sl1 is sl2


def test_get_path():
    sl1 = GameSaveLoad()
    assert "/save" == sl1.path
