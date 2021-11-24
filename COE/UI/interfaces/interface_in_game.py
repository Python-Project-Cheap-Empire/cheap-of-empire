import pygame
from pygame.locals import QUIT
import pygame_gui
from COE.UI.interfaces.interface_menu_options import MenuOptions
from COE.UI.interfaces.interface_play_menu import MenuPlay
from COE.map.map import Map
from COE.camera.camera import Camera

import os

script_dir = os.path.dirname(os.path.abspath(__file__))


class GameMenu:
    def __init__(self, display_):
        self.display_ = display_
        self.menu_passed = False
        self.screen_size = pygame.display.get_surface().get_size()
        self.width = self.screen_size[0]
        self.height = self.screen_size[1]
        self.manager = pygame_gui.UIManager(self.screen_size)
        self.buttons = []
        self.clock = pygame.time.Clock()
        self.loop = True
        self.camera = Camera([self.width, self.height])
        self.map = Map()

    def display(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.display_.fill(0x000)
        self.map.draw_map(self.display_, self.camera)
        self.manager.update(time_delta)
        self.manager.draw_ui(self.display_)

    def event(self, isTest=False):
        for event in pygame.event.get():
            if event.type == QUIT:  # Stop the game if the QUIT button is clicked on
                self.loop = False
                if event.type == pygame.MOUSEBUTTONUP:
                    res = Map.screen_to_map(
                        (event.pos[0], event.pos[1]),
                        self.camera.x_offset,
                        self.camera.y_offset,
                    )
            self.camera.update()

            self.manager.process_events(event)
        if not self.loop:
            return None
        return self
