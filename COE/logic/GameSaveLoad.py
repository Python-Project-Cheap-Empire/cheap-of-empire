from . import Game


class GameSaveLoad:
    """
    Singleton class that is used to save/load game to/from file
    """

    def __new__(cls):  # cls refers to the class itself and not the instance like self
        """
        Initialize a instance of GameSaveLoad if not created.
        Else return the instance.
        """
        cls._sl_path = "/save"
        if not hasattr(cls, "instance"):
            cls.instance = super(GameSaveLoad, cls).__new__(cls)
        return cls.instance

    def save_game(self, current_game: Game, save_name: str):
        """
        Save a game to 'sl_path' class's attribute
        :param current_game: Game
        :param save_name : str
        :return: Nothing
        """
        pass

    def load_game(self, save_name: str) -> Game:
        """
        Create a game object from a file in 'sl_path' class's attribute
        :param save_name : str
        :return: Game object
        """
        pass

    @property
    def path(self) -> str:
        """
        Get the path of the save folder
        :return: str
        """
        return self._sl_path
