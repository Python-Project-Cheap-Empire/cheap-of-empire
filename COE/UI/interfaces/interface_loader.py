import pygame
from pygame.locals import *
import pygame_gui
import random

import os

script_dir = os.path.dirname(os.path.abspath(__file__))


class Loader:
    def __init__(self, display__):
        self.display_ = display__
        self.screen_size = pygame.display.get_surface().get_size()
        self.width = self.screen_size[0]
        self.height = self.screen_size[1]
        self.manager = pygame_gui.UIManager(self.screen_size)
        self.buttons = [
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (50, 50),
                    (100, 50),
                ),
                text="BACK",
                manager=self.manager,
            )
        ]
        self.img = [
            pygame.image.load(script_dir + "/images/background_menu.png").convert()
        ]

        self.img[0] = pygame.transform.scale(self.img[0], (500, 331))
        self.clock = pygame.time.Clock()
        self.faked = 0
        self.loaded = 0
        self.size_loader = self.width - 110
        self.courant_loader_x = self.loaded * self.size_loader / 100

    def display(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.display_.fill(0x000)
        self.display_.blit(self.img[0], (self.width / 2 - 275, self.height / 2 - 160))

        pygame.draw.rect(
            self.display_, (99, 104, 107), (50, self.height - 100, self.width - 100, 50)
        )

        pygame.draw.rect(
            self.display_,
            (104, 126, 187),
            (55, self.height - 95, self.courant_loader_x, 40),
        )

        self.faked += 1
        if self.faked >= 50:
            self.faked = 0
            self.loaded += random.randint(1, 10)
            if self.loaded > 100:
                self.loaded = 100
            self.courant_loader_x = self.loaded * self.size_loader / 100

        self.manager.update(time_delta)
        self.manager.draw_ui(self.display_)

    def event(self, isTest=False):
        for event in pygame.event.get():
            if event.type == QUIT:  # stopper le programme si on click sur la crois
                self.loop = False
            if isTest or event.type == pygame.USEREVENT:
                if isTest or event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if isTest or event.ui_element == self.buttons[0]:
                        from COE.UI.interfaces.interface_menu_newgame import (
                            MenuNewGame,
                        )

                        return MenuNewGame(self.display_)

            self.manager.process_events(event)
        return self
