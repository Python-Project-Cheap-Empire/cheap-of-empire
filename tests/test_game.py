from COE.logic import Game
from COE.camera import Camera


def test_setter():
    game = Game([], None, None, 3.4, Camera(1, 1), "new")
    assert game.speed == 3.4
    game.set_speed(1.0)
    assert game.speed == 1.0
