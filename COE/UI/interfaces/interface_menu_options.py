import pygame
from pygame.locals import *
import pygame_gui

import os

script_dir = os.path.dirname(os.path.abspath(__file__))


class MenuOptions:
    def __init__(self, display__):
        self.display_ = display__
        self.screen_size = pygame.display.get_surface().get_size()
        self.width = self.screen_size[0]
        self.height = self.screen_size[1]

        self.mul_width = (self.width * 1 / 2) / self.width
        self.mul_height = (self.height * 1 / 2) / self.height
        # a modifier pour les taille d'ecrans
        self.ESM = (
            self.screen_size[0] / 2 - (self.width * self.mul_width / 2),
            self.screen_size[1] / 2 - (self.height * self.mul_height / 2),
        )

        self.manager = pygame_gui.UIManager(self.screen_size)
        self.bouttons = [
            pygame_gui.elements.ui_button.UIButton(
                relative_rect=pygame.Rect(
                    (50, 50),
                    (100, 50),
                ),
                text="BACK",
                manager=self.manager,
            ),
        ]
        self.img = [
            pygame.image.load(script_dir + "/images/background_menu.png").convert()
        ]
        self.img[0] = pygame.transform.scale(self.img[0], (300, 199))
        self.clock = pygame.time.Clock()
        self.currante_key = ""
        self.font = pygame.font.Font(None, 25)
        self.text = [
            self.font.render(
                "NINJALUI : give 10,000 for all ressources", True, (255, 255, 255)
            ),
            self.font.render("COINAGE : give 1,000 golds", True, (255, 255, 255)),
            self.font.render(
                "PEPPERONI PIZZA : give 1,000 of foods", True, (255, 255, 255)
            ),
            self.font.render("QUARRY : give 1,000 of stones", True, (255, 255, 255)),
            self.font.render("WOODSTOCK : give 1,000 of woods", True, (255, 255, 255)),
        ]

    def display(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.display_.fill(0x000)
        self.display_.blit(self.img[0], (self.width - 275, 0))
        self.manager.update(time_delta)
        self.manager.draw_ui(self.display_)
        pygame.draw.rect(
            self.display_,
            (99, 104, 107),
            (
                self.ESM[0],
                self.ESM[1],
                self.width * self.mul_width,
                self.height * self.mul_height,
            ),
        )
        for i in range(len(self.text)):
            self.display_.blit(
                self.text[i], (self.ESM[0] + 50, self.ESM[1] + (i + 1) * 50)
            )

    def event(self, isTest=False):
        for event in pygame.event.get():
            # stopper le programme si on click sur la crois
            if event.type == QUIT:
                self.loop = False

            # evennement des bouttons
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    # si le boutton selectionner et back
                    if event.ui_element == self.bouttons[0]:
                        from COE.UI.interfaces.main_menu import (
                            MainMenu,
                        )

                        # on retourne sur le menu principale
                        return MainMenu(self.display_)

            self.manager.process_events(event)
        return self

    def get_playing(self):
        return False
