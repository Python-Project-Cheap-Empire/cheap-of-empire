import pygame
from pygame.locals import QUIT
import pygame_gui
from COE.UI.interfaces.interface_menu_options import MenuOptions
from COE.UI.interfaces.interface_play_menu import MenuPlay
from COE.map.map import Map
from COE.camera.camera import Camera
from COE.UI.interfaces.interface_in_game import GameMenu
from COE.UI.interfaces.interface_play_menu import MenuPlay
from COE.UI.item import Item
from COE.UI.time_counting import time_counting

from COE.logic.Game import Game
from map.cell import Cell

import os

script_dir = os.path.dirname(os.path.abspath(__file__))


class GameRender:
    def __init__(self, display_, game):
        self.display_ = display_
        self.clock = pygame.time.Clock()
        self.game = game
        self.pause = False
        self.screen_size = pygame.display.get_surface().get_size()
        self.manager = pygame_gui.UIManager(self.screen_size)
        self.menu = GameMenu(self.display_, self.manager)
        self.width = self.screen_size[0]
        self.height = self.screen_size[1]
        self.scaled_cell = Cell.get_scaled_blocks()
        self.playing = True
        self.item = Item(self.width, self.height)
        self.timeur = time_counting(self.display)

    def run(self):
        self.events()
        self.update()
        self.draw()

    def events(self):
        self.playing = self.menu.event(self.pause)
        self.pause = self.menu.pause

    def update(self):
        if not self.pause:
            self.game.camera.update()
            self.game.map_game.update(self.game.camera)
            self.item.update()
        time_delta = self.clock.tick(60) / 1000.0
        self.manager.update(time_delta)

    def draw(self):
        self.display_.fill((0, 0, 0))
        self.game.map_game.draw_map(self.display_, self.game.camera)
        self.game.map_game.draw_entities(
            self.display_, self.game.camera, self.scaled_cell
        )
        self.draw_text(
            f"fps={round(self.clock.get_fps())}",
            25,
            (255, 0, 0),
            (self.width - 100, 10),
        )
        self.item.draw_item(self.display_)
        self.timeur.draw_time(self.display_)
        x, y = Map.screen_to_map(
            pygame.mouse.get_pos(), self.game.camera.x_offset, self.game.camera.y_offset
        )
        x, y = int(x), int(y)
        pos = f"{x}, {y}"
        mpos = pygame.mouse.get_pos()
        self.draw_text(
            pos,
            25,
            (255, 0, 0),
            (mpos[0] + 20, mpos[1]),
        )

        # self.display_.blit(pos, (mpos[0]+20, mpos[1]))
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
