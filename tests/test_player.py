from COE.logic import Player


def test_init():
    player = Player("Toto", [], [], None, None)

    assert player.gold == 500
    assert player.username == "Toto"
