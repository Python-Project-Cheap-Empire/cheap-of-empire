from COE.logic import Player


def test_init():
    player = Player("Toto", [], [], None, None)

    assert player.gold == 500
    assert player.username == "Toto"
    assert player.food == 300
    assert player.wood == 300
    assert player.stone == 300
    assert player.civilization is None
    assert player.age is None
    assert player.buildings == []
    assert player.units == []
