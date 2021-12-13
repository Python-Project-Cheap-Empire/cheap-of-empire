import pygame
from pygame.locals import *
import pygame_gui

import os

script_dir = os.path.dirname(os.path.abspath(__file__))


class MenuMulti:
    def __init__(self, display__):
        self.display_ = display__
        self.screen_size = pygame.display.get_surface().get_size()
        self.width = self.screen_size[0]
        self.height = self.screen_size[1]
        self.manager = pygame_gui.UIManager(self.screen_size)
        self.ESM = (self.width / 2 - 450, self.width / 2 - 400)
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
        self.img[0] = pygame.transform.scale(self.img[0], (300, 199))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 50)
        self.text = self.font.render("not available", True, (255, 0, 0))
        self.text_menu = self.font.render("Multiplayers", True, (255, 255, 255))

    def display(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.display_.fill(0x000)
        pygame.draw.rect(
            self.display_, (99, 104, 107), (self.ESM[0], self.ESM[1], 900, 500)
        )

        self.display_.blit(self.img[0], (self.width - 275, 0))
        self.manager.update(time_delta)
        self.manager.draw_ui(self.display_)
        self.display_.blit(self.text, (self.ESM[0] + 50, self.ESM[1] + 50))
        self.display_.blit(self.text_menu, (self.ESM[0], 150))

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:  # stopper le programme si on click sur la crois
                self.loop = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.buttons[0]:
                        from COE.UI.interfaces.interface_play_menu import (
                            MenuPlay,
                        )

                        return MenuPlay(self.display_)

            self.manager.process_events(event)
        return self
