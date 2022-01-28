import os.path
from pathlib import Path

from COE.logic.GameSaveLoad import GameSaveLoad
from COE.logic.Game import Game
from COE.map.map import Map
from COE.logic.Player import Player
from COE.contents.unit.villager import Villager
from COE.contents.building.storage_building import StorageBuilding
from COE.camera import Camera
from COE.contents.building.town_center import TownCenter
from COE.map.MapGenerator import MapGenerator


def test_singleton():
    sl1 = GameSaveLoad()
    sl2 = GameSaveLoad()

    assert sl1 is sl2


def test_get_path():
    sl1 = GameSaveLoad()
    root_dir = Path(__file__).parent.parent

    assert sl1.path == os.path.join(root_dir, "save/")


def remove_file_for_test():
    sl1 = GameSaveLoad()
    save_name = "pytest_save"
    if os.path.exists(os.path.join(sl1.path, save_name)):
        os.remove(os.path.join(sl1.path, save_name))


def test_save_and_load():
    sl1 = GameSaveLoad()
    save_name = "pytest_save"

    players = [
        Player("Toto", True, [], [], None, None),
        Player("P2", False, [], [], None, None),
    ]
    villager = Villager((0, 0), players[0])
    storage = TownCenter((54, 78), True)
    players[0].buildings.append(storage)
    players[0].units.append(villager)
    generator = MapGenerator(players=players)
    map = generator.generate()
    game_save = Game(players, map, 1.0, Camera(0, 0), "new", None)

    try:
        sl1.save_game(game_save, save_name)
    except FileExistsError:
        remove_file_for_test()
        sl1.save_game(game_save, save_name)

    game_load = sl1.load_game(save_name)

    assert game_save.speed == game_load.speed
    assert game_save.players[0].username == game_load.players[0].username

    save_cells = game_save.map.cells
    load_cells = game_load.map.cells
    assert all(
        save_cells[i][j].cell_type == load_cells[i][j].cell_type
        for i in range(len(save_cells))
        for j in range(len(save_cells[i]))
    )

    os.remove(os.path.join(sl1.path, save_name))
