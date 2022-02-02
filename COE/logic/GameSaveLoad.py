from . import Game
import os
from pathlib import Path
import pickle


class GameSaveLoad:
    """
    Singleton class that is used to save/load game to/from file
    """

    def __new__(cls):  # cls refers to the class itself and not the instance like self
        """
        Initialize a instance of GameSaveLoad if not created.
        Else return the instance.
        """
        cls._sl_path = os.path.join(Path(__file__).parent.parent.parent, "save")
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
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        with open(os.path.join(self.path, save_name), "wb") as file:
            pickle.dump(current_game, file)

    def load_game(self, save_name: str) -> Game:
        """
        Create a game object from a file in 'sl_path' class's attribute
        :param save_name : str
        :return: Game object
        """
        with open(os.path.join(self.path, save_name), "rb") as file:
            loaded_game = pickle.load(file)
        return loaded_game

    @property
    def path(self) -> str:
        """
        Get the path of the save folder
        :return: str
        """
        return self._sl_path
