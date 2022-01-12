import pygame
from pygame.locals import QUIT
import pygame_gui
from COE.UI.interfaces.interface_menu_options import MenuOptions
from COE.UI.interfaces.interface_play_menu import MenuPlay
from COE.map.map import Map
from COE.camera.camera import Camera
from COE.UI.cheat_code import CheatCode
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

ressource = ""


class GameMenu:
    def __init__(self, display_, manager):
        self.display_ = display_
        self.menu_passed = False
        self.screen_size = pygame.display.get_surface().get_size()
        self.width = self.screen_size[0]
        self.height = self.screen_size[1]
        self.manager = manager
        self.manager_menu = pygame_gui.UIManager(self.screen_size)
        self.ESM = (self.screen_size[0] / 2 - 300, self.screen_size[0] / 2 - 500)
        self.buttons = [
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((0, 20), (100, 50)),
                text="Menu",
                manager=self.manager,
            ),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 250, self.ESM[1] + 400), (100, 50)
                ),
                text="Exit",
                manager=self.manager,
                visible=0,
            ),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 250, self.ESM[1] + 50), (100, 50)
                ),
                text="Resume",
                manager=self.manager,
                visible=0,
            ),
        ]
        self.cheat_code = CheatCode(self.display_, self.width, self.height)
        self.pause = False
        self.clock = pygame.time.Clock()

    def display(self, pause):
        if pause:
            s = pygame.Surface((self.width, self.height))
            s.set_alpha(128)
            s.fill((0, 0, 0))
            pygame.draw.rect(
                self.display_, (99, 104, 107), (self.ESM[0], self.ESM[1], 600, 500)
            )
            self.display_.blit(s, (0, 0))
            self.cheat_code.draw()

    def event(self, pause):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if pause and event.ui_element == self.buttons[1]:
                        return False
                    if pause and event.ui_element == self.buttons[2]:
                        self.pause = False
                        self.visibility_default_bp()
                    if event.ui_element == self.buttons[0]:
                        self.pause = True
                        self.visibility_pause_bp()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pause = True
                    self.visibility_pause_bp()
            self.cheat_code.process_event(event)
            self.manager.process_events(event)
        return True

    def visibility_pause_bp(self):
        self.buttons[0].visible = 0
        self.buttons[1].visible = 1
        self.buttons[2].visible = 1

    def visibility_default_bp(self):
        self.buttons[0].visible = 1
        self.buttons[1].visible = 0
        self.buttons[2].visible = 0
