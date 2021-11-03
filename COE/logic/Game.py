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
        self._players = players
        self._map_game = map_game
        self._camera = camera
        self._timer = timer
        self._speed = speed

    ###########
    # Getters #
    ###########
    @property
    def players(self):
        return self._players

    @property
    def map_game(self):
        return self._map_game

    @property
    def camera(self):
        return self._camera

    @property
    def timer(self):
        return self._timer

    @property
    def speed(self):
        return self._speed

    ###########
    # Setters #
    ###########

    @speed.setter
    def speed(self, new_speed):
        assert (
            isinstance(new_speed, float) and new_speed > 0
        ), "new_speed is a float and new_speed > 0"
        self._speed = new_speed
