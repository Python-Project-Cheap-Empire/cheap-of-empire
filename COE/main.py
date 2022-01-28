import os
import sys

# from COE.contents.unit.enum.unit_types import UnitTypes

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))

from UI.window_ui import Window
from COE.logic.Game import Game
from UI.interfaces.interface_play_menu import MenuPlay
from map.MapGenerator import MapGenerator

# pour generer une map
from logic.Player import Player
from map.map import Map
from camera.camera import Camera

from logic.create_game import CreateGame


def main():
    window = Window()
    running = True
    while running:
        window.show()
        running, _ = window.get_loop()
        if window.playing:
            players = [
                Player(
                    username="personnage",
                    is_human=True,
                    units=[],
                    buildings=[],
                    age=None,
                    civilization=None,
                    gold_amount=500,
                    wood_amount=500,
                    stone_amount=300,
                    food_amount=300,
                ),
                Player(
                    username="AI",
                    is_human=False,
                    units=[],
                    buildings=[],
                    age=None,
                    civilization=None,
                    gold_amount=500,
                    wood_amount=500,
                    stone_amount=300,
                    food_amount=300,
                ),
            ]
            static = Static()
            generator = MapGenerator(players=players)
            gen_map = generator.generate()
            gen_map.blit_world()
            game = Game(
                players=players,
                map=gen_map,
                timer=None,
                speed=1,
                camera=Camera(window),
            )
            game_logic = GameLogic(window.display, game, static)

            while game_logic.playing:
                game_logic.run()
            window.playing = False
            gen_game.save_game()
            window.menu = MenuPlay(window.display)


if __name__ == "__main__":
    main()
