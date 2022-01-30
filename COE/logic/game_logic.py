from COE.contents.resources.tree import Tree
from COE.contents.unit.unit import Unit
from COE.UI.cheat_code import CheatCode
import pygame
from pygame.locals import *
import pygame_gui
from COE.UI.interfaces.interface_in_game import GameMenu
from COE.UI.item import Item
from COE.UI.time_counting import time_counting
from COE.logic.Game import Game
from map.cell import Cell
from COE.logic.path_finding import find_move
from COE.contents.static.static import Static


class GameLogic:
    def __init__(self, display_, game: Game, static: Static):
        self.display_ = display_
        self.clock = pygame.time.Clock()
        self.game: Game = game
        self.static: Static = static
        self.screen_size = pygame.display.get_surface().get_size()
        self.manager = pygame_gui.UIManager(self.screen_size)
        self.width = self.screen_size[0]
        self.height = self.screen_size[1]
        self.scaled_cell = Cell.get_scaled_blocks()
        self.playing = True
        self.item = Item(self.width, self.height)
        self.timer = time_counting(self.game.timer)
        self.x_limit = self.display_.get_width() + self.static.width_cells_size
        self.y_limit = self.display_.get_height() + self.static.height_cells_size
        self.cheatcode = CheatCode(self.display_, self.game)
        self.menu = GameMenu(self.display_, self.manager, self.cheatcode, self.timer)

    def run(self):
        self.events()
        self.update()
        self.draw()

    def events(self):
        for event in pygame.event.get():
            self.playing = self.menu.event(event)
            if not self.playing:
                break
            self.game.event(self.static, event)

    def update(self):
        dt = self.clock.tick(60) / 1000.0
        if not self.menu.pause:
            self.game.update()
            self.game.camera.update()
            # self.game.map.update(self.game.camera)
            self.item.update()
            self.timer.update(self.game.speed)
        self.manager.update(dt)

    def draw(self):
        self.display_.fill((0, 0, 0))
        self.game.map.draw_map(self.display_, self.game.camera)
        self.game.map.draw_entities(
            self.display_,
            self.game.camera,
            self.static.image_cache,
            self.static.entities_pos_dict,
            self.static.width_cells_size,
            self.static.height_cells_size,
            self.static.half_width_cells_size,
            self.static.half_height_cells_size,
            self.x_limit,
            self.y_limit,
        )
        for selected_unit in self.game.currently_selected:
            self.game.map.draw_rect_around(
                self.display_,
                selected_unit.positions[0],
                selected_unit.positions[1],
                self.game.camera,
                self.static.half_width_cells_size,
                self.static.half_height_cells_size,
            )
            self.game.map.draw_health_bar(
                self.display_,
                selected_unit.positions[0],
                selected_unit.positions[1],
                self.game.camera,
                self.static.half_width_cells_size,
                self.static.half_height_cells_size,
                # self.hp
            )
        self.item.draw_item(self.display_)
        self.timer.draw_time(self.display_)
        self.menu.draw_ressources(self.game)
        self.menu.draw_fps(self.clock.get_fps())
        self.menu.draw_pos(self.game, self.static)
        self.menu.draw_selection_rectangle(self.game.selection_rectangle)
        self.menu.draw_shortcuts(self.game.speed)
        if self.menu.pause:
            self.menu.draw()
            self.cheatcode.draw()
        self.manager.draw_ui(self.display_)
        pygame.display.update()
