class Game:
    """
    A class to represent a unique game
    """

    def __init__(self, players: list, map_game, camera, timer, speed):
        """
        Constructs all the necessary attributes for the Game object.

        :param players: list
        :param map_game: Map
        :param camera: Camera
        :param timer: Time
        :param speed: float
        """
        self.players = players
        self.map_game = map_game
        self.camera = camera
        self.timer = timer
        self.speed = speed

    def set_speed(self, new_speed):
        assert (
            isinstance(new_speed, float) and new_speed > 0
        ), "new_speed is a float and new_speed > 0"
        self.speed = new_speed