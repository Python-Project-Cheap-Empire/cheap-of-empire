from logic.Player import Player
from map.map import Map
from camera.camera import Camera
from logic import Game

from UI.interfaces.interface_menu_newgame import MenuNewGame
from logic.GameSaveLoad import GameSaveLoad


class CreateGame:
    def __init__(self, data=None, type_load=-1, window=None):
        self.saver = GameSaveLoad()
        self.type = type_load
        self.data = data
        self.game = None
        self.window = window
        if data is None:
            self.type = -1

    def gen_game(self):
        if self.type == -1:
            return False
        if self.type == 0:
            self.game_with_newGame()
        if self.type == 1:
            self.game_with_save()
        return True

    def game_with_newGame(self):
        nb_player = self.data.get_select_nb_players()
        size_map = self.data.get_map_size_selected()
        type_map = self.data.get_map_type_selected()
        ressources = self.data.get_ressources_rarity_selected()
        name = self.data.get_map_name()

        players = [
            Player(
                username="personnage",
                units=[],
                buildings=[],
                age=None,
                civilization=None,
                gold_amount=500,
                wood_amount=500,
                stone_amount=300,
                food_amount=300,
                is_human=True
            )
        ]
        for i in range(nb_player):
            players.append(
                Player(
                    username="AI",
                    units=[],
                    buildings=[],
                    age=None,
                    civilization=None,
                    gold_amount=500,
                    wood_amount=500,
                    stone_amount=300,
                    food_amount=300,
                    is_human=False
                )
            )
        gen_map = Map(size_map, type_map, ressources)
        gen_map.blit_world()

        self.game = Game.Game(
            players=players,
            map_game=gen_map,
            timer=None,
            speed=1,
            camera=Camera(self.window.width, self.window.height),
            name=name
        )

    def game_with_save(self):
        name = self.data.get_name_game_select()
        self.game = self.saver.load_game(name)
        self.game.map_game.blit_world()

    def get_game(self):
        return self.game

    def save_game(self):
        self.saver.save_game(current_game=self.game, save_name=self.game.name)
