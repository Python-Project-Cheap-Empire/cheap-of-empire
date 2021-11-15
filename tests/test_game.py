from COE.logic import Game


def test_setter():
    game = Game([], None, None, None, 3.4)
    assert game.speed == 3.4
    game.set_speed(1.0)
    assert game.speed == 1.0
