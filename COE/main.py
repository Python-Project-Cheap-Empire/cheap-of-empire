import os
import sys
from COE.contents.unit.enum.unit_types import UnitTypes

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
            gen_map = Map()
            gen_map.cells = Map.generate_map(players, gen_map.size, gen_map.type, gen_map.resources_rarity)
            gen_map.dict_binary_cells = {UnitTypes.GROUND:Map.transform_for_unit(gen_map, UnitTypes.GROUND), 
            UnitTypes.NAVY:Map.transform_for_unit(gen_map, UnitTypes.NAVY)}
            gen_map.blit_world()
            game = Game(
                players=players,
                map=gen_map,
                timer=None,
                speed=1,
                camera=Camera(window),
            )
            game_logic = GameLogic(window.display, game, static)
            playing = True
            while game_logic.playing:
                game_logic.run()
            window.playing = False
            window.menu = MenuPlay(window.display)


if __name__ == "__main__":
    main()
