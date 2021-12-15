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

import os

script_dir = os.path.dirname(os.path.abspath(__file__))


class GameRender:
    def __init__(self, display_, game):
        self.display_ = display_
        self.clock = pygame.time.Clock(60)
        self.game = game
        self.pause = False
        self.manager = pygame_gui.UIManager(self.screen_size)
        self.menu = GameMenu(self.display_, self.manager)

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        self.playing = self.menu.event(self.pause)
        self.pause = self.menu.pause

    def update(self):
        if not self.pause:
            self.camera.update()
            for e in self.entities:
                e.update()
            # self.hud.update()
            self.map.update(self.camera)
        time_delta = self.clock.tick(60) / 1000.0
        self.manager.update(time_delta)

    def draw(self):
        self.display_.fill((0, 0, 0))
        self.map.draw_map(self.display_, self.camera)
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
