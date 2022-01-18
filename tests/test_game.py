from COE.logic.Game import Game
from COE.camera.camera import Camera
from COE.logic.time import Time_


def test_setter():
    game = Game([], None, 3.4, Camera(1, 1), "new", Time_())
    assert game.speed == 3.4
    game.set_speed(1.0)
    assert game.speed == 1.0
