import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))

from UI.window_ui import Window
from logic import Game
from UI.interfaces.game_render import GameRender
from UI.interfaces.interface_play_menu import MenuPlay


# pour generer une map
from logic.Player import Player
from map.map import Map
from camera.camera import Camera


def main():
    window = Window()
    running = True
    playing = False
    while running:
        window.show()
        (running, playing) = window.get_loop()
        if window.playing:
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
                ),
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
                ),
            ]
            gen_map = Map()
            gen_map.blit_world()
            game = Game(
                players=players,
                map_game=gen_map,
                timer=None,
                speed=1,
                camera=Camera(window),
            )
            game_render = GameRender(window.display, game)
            playing = True
            while game_render.playing:
                game_render.run()
            window.playing = False
            window.menu = MenuPlay(window.display)


if __name__ == "__main__":
    main()
