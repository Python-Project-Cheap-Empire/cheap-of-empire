import pygame
from pygame.locals import *
import pygame_gui

import os

script_dir = os.path.dirname(os.path.abspath(__file__))


class MenuPlay:
    def __init__(self, display__):
        self.playing = False
        self.selected_save = ""
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
            ),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 650, self.ESM[1]),
                    (250, 75),
                ),
                text="NEW GAME",
                manager=self.manager,
            ),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 650, self.ESM[1] + 76),
                    (250, 75),
                ),
                text="MULTIPLAYERS",
                manager=self.manager,
            ),
        ]
        self.img = [
            pygame.image.load(script_dir + "/images/background_menu.png").convert()
        ]
        self.img[0] = pygame.transform.scale(self.img[0], (300, 199))
        self.clock = pygame.time.Clock()

        # recuperation des dossier de sauvegarde
        self.save_url = script_dir + "/../../../save/"
        self.saves = os.listdir(self.save_url)
        self.nb_saves = 0
        self.load_save_bp = []
        for save in self.saves:
            self.load_save_bp.append(
                pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(
                        (self.ESM[0], self.ESM[1] + self.nb_saves * 75),
                        (570, 75),
                    ),
                    text=save,
                    manager=self.manager,
                )
            )
            self.nb_saves += 1
        self.scroll_pourcent = (
            1 if self.nb_saves * 75 <= 500 else (500 / (self.nb_saves * 75))
        )
        self.scroll_max = -4.5424 * (self.scroll_pourcent * 100) + 454.53
        # initialisation de la scrollBar
        self.scrole = pygame_gui.elements.ui_vertical_scroll_bar.UIVerticalScrollBar(
            relative_rect=pygame.Rect(
                (self.ESM[0] + 575, self.ESM[1]),
                (25, 500),
            ),
            manager=self.manager,
            visible_percentage=self.scroll_pourcent,
        )

    def display(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.display_.fill(0x000)
        pygame.draw.rect(
            self.display_, (99, 104, 107), (self.ESM[0], self.ESM[1], 600, 500)
        )
        pygame.draw.rect(
            self.display_, (99, 104, 107), (self.ESM[0] + 650, self.ESM[1], 250, 151)
        )

        if self.scrole.check_has_moved_recently():
            offset = (
                self.scrole.scroll_position
                * (self.nb_saves * 75 - 500)
                / self.scroll_max
            )
            temp = 0
            for button in self.load_save_bp:
                button.hide()
            self.load_save_bp = []
            for save in self.saves:
                self.load_save_bp.append(
                    pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(
                            (self.ESM[0], self.ESM[1] + temp * 75 - offset),
                            (570, 75),
                        ),
                        text=save,
                        manager=self.manager,
                    )
                )
                temp += 1

        self.manager.draw_ui(self.display_)
        pygame.draw.rect(
            self.display_, (0, 0, 0), (self.ESM[0], self.ESM[1] + 500, 600, 250)
        )
        pygame.draw.rect(
            self.display_, (0, 0, 0), (self.ESM[0], self.ESM[1] - 500, 600, 500)
        )
        self.display_.blit(self.img[0], (self.width - 275, 0))
        self.manager.update(time_delta)

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:  # stopper le programme si on click sur la crois
                self.loop = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.buttons[0]:
                        from COE.UI.interfaces.main_menu import (
                            MainMenu,
                        )

                        return MainMenu(self.display_)

                    if event.ui_element == self.buttons[1]:
                        from COE.UI.interfaces.interface_menu_newgame import (
                            MenuNewGame,
                        )

                        return MenuNewGame(self.display_)

                    if event.ui_element == self.buttons[2]:
                        from COE.UI.interfaces.interface_menu_multiplayers import (
                            MenuMulti,
                        )

                        return MenuMulti(self.display_)

                    for bp in self.load_save_bp:
                        if event.ui_element == bp:
                            self.selected_save = bp.text
                            self.playing = True

            self.manager.process_events(event)
        return self

    def get_playing(self):
        return self.playing

    def get_type_create_map(self):
        return 1

    def get_name_game_select(self):
        return self.selected_save
