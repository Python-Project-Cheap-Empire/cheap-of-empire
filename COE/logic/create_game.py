from logic.Player import Player
from map.map import Map
from camera.camera import Camera
from COE.logic.Game import Game

from COE.contents.static.static import Static
from UI.interfaces.interface_menu_newgame import MenuNewGame
from logic.GameSaveLoad import GameSaveLoad
from COE.map.enum.map_sizes import MapSizes
from COE.map.enum.map_types import MapTypes
from COE.map.enum.resources_rarity import ResourcesRarity
from COE.logic.game_logic import GameLogic
from COE.logic.time import Time_
import datetime


class CreateGame:  # pragma: no cover
    def __init__(self, data=None, type_load=-1, window=None):
        self.saver = GameSaveLoad()
        self.type = type_load
        self.data = data
        self.game = None
        self.window = window

    def gen_game(self):
        if self.type == 0:
            return self.game_with_newGame()
        if self.type == 1:
            return self.game_with_save()

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
                is_human=True,
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
                    is_human=False,
                )
            )

        static = Static()
        gen_map = Map(
            players, MapSizes.TINY, MapTypes.CONTINENTAL, ResourcesRarity.HIGH
        )
        gen_map.blit_world()
        self.game = Game(
            players=players,
            map=gen_map,
            speed=1,
            camera=Camera(self.window.height, self.window.width),
            name=name,
            timer=Time_(),
        )
        game_logic = GameLogic(self.window.display, self.game, static)
        return game_logic

    def game_with_save(self):
        name = self.data.get_name_game_select()
        self.game = self.saver.load_game(name)
        self.game.map.blit_world()
        static = Static()
        game_logic = GameLogic(self.window.display, self.game, static)
        return game_logic

    def get_game(self):
        return self.game

    def save_game(self):
        self.game.map.grass_tiles = None
        tmp_name = self.game.name
        game_name = tmp_name + str(datetime.datetime.today()).replace(" ", "_")
        self.game.name = game_name
        self.saver.save_game(current_game=self.game, save_name=self.game.name)
        self.game.name = tmp_name
        self.game.map.blit_world()
