import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))

from UI.window_ui import Window
from COE.logic.Game import Game
from COE.logic.game_logic import GameLogic
from UI.interfaces.interface_play_menu import MenuPlay

# pour generer une map
from logic.Player import Player
from map.map import Map
from camera.camera import Camera
from COE.contents.static.static import Static

from logic.create_game import CreateGame


def main():
    window = Window()
    running = True
    playing = False
    while running:
        window.show()
        (running, playing) = window.get_loop()
        if window.playing:
            gen_game = CreateGame(
                data=window.menu,
                type_load=window.menu.get_type_create_map(),
                window=window,
            )
            gen_game.gen_game()
            game_render = GameRender(window.display, gen_game.get_game())
            playing = True
            while game_render.playing:
                game_render.run()
            gen_game.save_game()
            window.playing = False
            window.menu = MenuPlay(window.display)


if __name__ == "__main__":
    main()
