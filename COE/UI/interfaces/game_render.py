import pygame
from pygame.locals import QUIT
import pygame_gui
from COE.UI.interfaces.interface_menu_options import MenuOptions
from COE.UI.interfaces.interface_play_menu import MenuPlay
from COE.map.map import Map
from COE.camera.camera import Camera
from COE.UI.interfaces.interface_in_game import GameMenu
from COE.UI.interfaces.interface_play_menu import MenuPlay

from COE.logic.Game import Game
<<<<<<< HEAD
from map.cell import Cell
=======
>>>>>>> 6576316167ef4f3da76c69b4893b11a066181ce3

import os

script_dir = os.path.dirname(os.path.abspath(__file__))


class GameRender:
    def __init__(self, display_, game):
        self.display_ = display_
<<<<<<< HEAD
        self.clock = pygame.time.Clock()
=======
        self.clock = pygame.time.Clock(60)
>>>>>>> 6576316167ef4f3da76c69b4893b11a066181ce3
        self.game = game
        self.pause = False
        self.screen_size = pygame.display.get_surface().get_size()
        self.manager = pygame_gui.UIManager(self.screen_size)
        self.menu = GameMenu(self.display_, self.manager)
<<<<<<< HEAD
        self.width = self.screen_size[0]
        self.height = self.screen_size[1]
        cell = Cell(None, None)
        self.scaled_cell = cell.get_scaled_blocks()
        self.playing = True

    def run(self):
        self.events()
        self.update()
        self.draw()
=======

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
>>>>>>> 6576316167ef4f3da76c69b4893b11a066181ce3

    def events(self):
        self.playing = self.menu.event(self.pause)
        self.pause = self.menu.pause

    def update(self):
        if not self.pause:
            self.game.camera.update()
            self.game.map_game.update(self.game.camera)
        time_delta = self.clock.tick(60) / 1000.0
        self.manager.update(time_delta)

    def draw(self):
        self.display_.fill((0, 0, 0))
        self.game.map_game.draw_map(self.display_, self.game.camera, self.scaled_cell)
        self.draw_text(
            f"fps={round(self.clock.get_fps())}",
            25,
            (255, 0, 0),
            (self.width - 100, 10),
        )
        self.menu.display(self.pause)
        self.manager.draw_ui(self.display_)
        pygame.display.update()

    def draw_text(self, format, size, color, positions):
        myfont = pygame.font.SysFont("Comic Sans MS", size)
        textsurface = myfont.render(format, False, color)
        self.display_.blit(textsurface, positions)

    def display(self):
        self.run()

    def event(self):
        return MenuPlay(self.display_)
