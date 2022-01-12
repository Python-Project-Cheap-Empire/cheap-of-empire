from COE.contents.unit.unit import Unit
import pygame
from pygame.locals import *
import pygame_gui
from COE.map.map import Map
from COE.UI.interfaces.interface_in_game import GameMenu
from COE.UI.interfaces.interface_play_menu import MenuPlay
from COE.UI.item import Item
from COE.UI.time_counting import time_counting
from COE.contents.entity import Entity
from COE.logic.Game import Game
from map.cell import Cell
from COE.logic.path_finding import find_move
from COE.contents.static.static import Static

import os
import json

script_dir = os.path.dirname(os.path.abspath(__file__))


class GameLogic:  # pragma: no cover
    def __init__(self, display_, game: Game, static: Static):
        self.display_ = display_
        self.clock = pygame.time.Clock()
        self.game: Game = game
        self.pause = False
        self.static: Static = static
        self.currently_selected: Entity = None
        self.screen_size = pygame.display.get_surface().get_size()
        self.manager = pygame_gui.UIManager(self.screen_size)
        self.menu = GameMenu(self.display_, self.manager)
        self.width = self.screen_size[0]
        self.height = self.screen_size[1]
        self.scaled_cell = Cell.get_scaled_blocks()
        self.playing = True
        self.item = Item(self.width, self.height)
        self.timeur = time_counting(self.display)
        self.x_limit = self.display_.get_width() + self.static.width_cells_size
        self.y_limit = self.display_.get_height() + self.static.height_cells_size

    def run(self):
        self.events()
        self.update()
        self.draw()

    def events(self):
        self.playing = self.menu.event(self.pause)
        self.pause = self.menu.pause
        self.event()

    def update(self):
        if not self.pause:
            self.game.update()
            self.game.camera.update()
            # self.game.map.update(self.game.camera)
            self.item.update()
        time_delta = self.clock.tick(60) / 1000.0
        self.manager.update(time_delta)

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
        if self.currently_selected:
            self.game.map.draw_rect_around(
                self.display_,
                self.currently_selected.positions[0],
                self.currently_selected.positions[1],
                self.game.camera,
                self.static.half_width_cells_size,
                self.static.half_height_cells_size,
            )
        self.draw_text(
            f"fps={round(self.clock.get_fps())}",
            25,
            (255, 0, 0),
            (self.width - 100, 100),
        )
        self.item.draw_item(self.display_)
        self.timeur.draw_time(self.display_)

        x, y = Map.screen_to_map(
            pygame.mouse.get_pos(),
            self.game.camera.x_offset,
            self.game.camera.y_offset,
            self.static.half_width_cells_size,
            self.static.half_height_cells_size,
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
        if pygame.mouse.get_pressed()[0]:
            x, y = self.game.map.screen_to_map(
                pygame.mouse.get_pos(),
                self.game.camera.x_offset,
                self.game.camera.y_offset,
                self.static.half_width_cells_size,
                self.static.half_height_cells_size,
            )
            x, y = int(x), int(y)
            if self.game.map.cells[x][y].entity:
                self.currently_selected = self.game.map.cells[x][y].entity
            else:
                self.currently_selected = None

        elif pygame.mouse.get_pressed()[2]:
            if (
                self.currently_selected
                and self.currently_selected in self.game.players[0].units
            ):
                x, y = self.game.map.screen_to_map(
                    pygame.mouse.get_pos(),
                    self.game.camera.x_offset,
                    self.game.camera.y_offset,
                    self.static.half_width_cells_size,
                    self.static.half_height_cells_size,
                )
                x, y = int(x), int(y)
                if (
                    x >= 0
                    and x < self.game.map.size.value
                    and y >= 0
                    and y < self.game.map.size.value
                ):
                    if isinstance(self.currently_selected, Unit):
                        self.currently_selected.current_path = find_move(
                            self.game.map.transform_for_unit(
                                self.currently_selected.unit_type
                            ),
                            self.currently_selected.positions,
                            (x, y),
                        )
