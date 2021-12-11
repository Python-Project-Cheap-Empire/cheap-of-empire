import pygame
from pygame.locals import QUIT
import pygame_gui
from COE.UI.interfaces.interface_menu_options import MenuOptions
from COE.UI.interfaces.interface_play_menu import MenuPlay
from COE.map.map import Map
from COE.camera.camera import Camera
from COE.UI.interfaces.interface_in_game import GameMenu

import os

script_dir = os.path.dirname(os.path.abspath(__file__))


class GameRender:
    def __init__(self, display_):
        self.display_ = display_
        self.clock = pygame.time.Clock()
        self.loop = True
        self.screen_size = pygame.display.get_surface().get_size()
        self.width = self.screen_size[0]
        self.height = self.screen_size[1]
        self.camera = Camera([self.width, self.height])
        self.map = Map()
        self.pause = False
        self.manager = pygame_gui.UIManager(self.screen_size)
        self.menu = GameMenu(self.display_, self.manager)

    def display(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.display_.fill(0x000)
        self.map.draw_map(self.display_, self.camera)
        self.manager.update(time_delta)
        self.menu.display()
        self.loop = self.menu.event()

    def event(self, isTest=False):
        if self.loop is False:
            from COE.UI.interfaces.interface_play_menu import MenuPlay

            return MenuPlay(self.display_)
        if not self.menu.pause:
            self.camera.update()
        return self
