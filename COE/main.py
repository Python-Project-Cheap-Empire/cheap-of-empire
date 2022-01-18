import os
import sys
from COE.contents.unit.enum.unit_types import UnitTypes

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))

from UI.window_ui import Window
from COE.logic.Game import Game
from UI.interfaces.interface_play_menu import MenuPlay

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
            gen_game = CreateGame(
                data=window.menu,
                type_load=window.menu.get_type_create_map(),
                window=window,
            )
            game_logic = gen_game.gen_game()

            while game_logic.playing:
                game_logic.run()
            window.playing = False
            gen_game.save_game()
            window.menu = MenuPlay(window.display)


if __name__ == "__main__":
    main()
