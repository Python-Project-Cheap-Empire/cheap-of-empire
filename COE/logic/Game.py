class Game:
    """
    A class to represent a unique game
    """

    def __init__(self, players: list, map_game, timer, speed, camera, name: str):
        """
        Constructs all the necessary attributes for the Game object.

        :param players: list
        :param map_game: Map
        :param timer: Time
        :param speed: float
        :param name: str
        """
        self.players = players
        self.map_game = map_game
        self.timer = timer
        self.speed = speed
        self.camera = camera
        self.name = name

    def set_speed(self, new_speed):
        assert (
            isinstance(new_speed, float) and new_speed > 0
        ), "new_speed is a float and new_speed > 0"
        self.speed = new_speed
