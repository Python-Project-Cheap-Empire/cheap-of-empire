import pygame
from pygame.locals import QUIT
import pygame_gui
from COE.UI.interfaces.interface_menu_options import MenuOptions
from COE.UI.interfaces.interface_play_menu import MenuPlay

import os

script_dir = os.path.dirname(os.path.abspath(__file__))


class MainMenu:
    def __init__(self, display_):
        self.display_ = display_
        self.menu_passed = False
        self.screen_size = pygame.display.get_surface().get_size()
        self.width = self.screen_size[0]
        self.height = self.screen_size[1]
        self.manager = pygame_gui.UIManager(self.screen_size)
        self.buttons = [
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.width / 2 - 200, self.height / 2 + 200),
                    (400, 100),
                ),
                text="QUIT",
                manager=self.manager,
            ),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.width / 2 - 200, self.height / 2 + 50),
                    (400, 100),
                ),
                text="OPTIONS",
                manager=self.manager,
            ),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.width / 2 - 200, self.height / 2 - 100),
                    (400, 100),
                ),
                text="PLAY",
                manager=self.manager,
            ),
        ]
        self.img = [
            pygame.image.load(script_dir + "/images/background_menu.png").convert()
        ]
        self.img[0] = pygame.transform.scale(self.img[0], (500, 331))
        self.clock = pygame.time.Clock()
        self.loop = True

    def display(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.display_.fill(0x000)
        self.display_.blit(self.img[0], (self.width / 2 - 250, 0))
        self.manager.update(time_delta)
        self.manager.draw_ui(self.display_)

    def event(self):
        for event in pygame.event.get():
            if (
                event.type == pygame.MOUSEBUTTONUP
            ):  # or MOUSEBUTTONDOWN depending on what you want.
                print(event.pos)
            if event.type == QUIT:  # Stop the game if the QUIT button is clicked on
                self.loop = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.buttons[0]:
                        self.loop = False
                    if event.ui_element == self.buttons[1]:
                        return MenuOptions(self.display_)
                    if event.ui_element == self.buttons[2]:
                        return MenuPlay(self.display_)

            self.manager.process_events(event)
        if not self.loop:
            return None
        return self

    def get_playing(self):
        return False
