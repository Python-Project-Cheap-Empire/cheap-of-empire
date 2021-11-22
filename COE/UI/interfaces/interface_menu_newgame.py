import pygame
from pygame.locals import *
import pygame_gui

import os

script_dir = os.path.dirname(os.path.abspath(__file__))


class MenuNewGame:
    def __init__(self, display__):
        self.display_ = display__
        self.screen_size = pygame.display.get_surface().get_size()
        self.manager = pygame_gui.UIManager(self.screen_size)
        self.ESM = (self.screen_size[0] / 2 - 450, self.screen_size[0] / 2 - 400)
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
                text="START GAME",
                manager=self.manager,
            ),
        ]
        self.img = [
            pygame.image.load(script_dir + "/images/background_menu.png").convert()
        ]

        # recuperation des informations pour la gereration de map
        from COE.map.enum.map_sizes import MapSizes
        from COE.map.enum.map_types import MapTypes
        from COE.map.enum.resources_rarity import ResourcesRarity

        self.enumeration_size = []
        self.enumeration_type = []
        self.enumeration_ressources = []
        for mapsize in MapSizes:
            self.enumeration_size.append(mapsize)
        for maptype in MapTypes:
            self.enumeration_type.append(str(maptype))
        for ressource in ResourcesRarity:
            self.enumeration_ressources.append(str(ressource))
        self.DropDownMenus = [
            pygame_gui.elements.UIDropDownMenu(
                options_list=[str(x)[9:] for x in self.enumeration_size],
                starting_option=str(self.enumeration_size[0])[9:],
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 100, self.ESM[1] + 180), (250, 50)
                ),
                manager=self.manager,
            ),
            pygame_gui.elements.UIDropDownMenu(
                options_list=[str(x)[9:] for x in self.enumeration_type],
                starting_option=str(self.enumeration_type[0])[9:],
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 100, self.ESM[1] + 60), (250, 50)
                ),
                manager=self.manager,
            ),
            pygame_gui.elements.UIDropDownMenu(
                options_list=[str(x)[16:] for x in self.enumeration_ressources],
                starting_option=str(self.enumeration_ressources[0])[16:],
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 100, self.ESM[1] + 120), (250, 50)
                ),
                manager=self.manager,
            ),
        ]

        # text input
        self.text_input = [
            pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 120, self.ESM[1] + 7), (250, 50)
                ),
                manager=self.manager,
            )
        ]

        self.font = pygame.font.Font(None, 25)
        self.texts = [
            self.font.render("game name", True, (255, 255, 255)),
            self.font.render("map size", True, (255, 255, 255)),
        ]

        self.img[0] = pygame.transform.scale(self.img[0], (300, 199))
        self.clock = pygame.time.Clock()

    def display(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.display_.fill(0x000)
        pygame.draw.rect(
            self.display_, (99, 104, 107), (self.ESM[0], self.ESM[1], 600, 500)
        )
        pygame.draw.rect(
            self.display_, (99, 104, 107), (self.ESM[0] + 650, self.ESM[1], 250, 75)
        )
        self.display_.blit(self.img[0], (self.screen_size[0] - 275, 0))

        self.display_.blit(self.texts[0], (self.ESM[0] + 10, self.ESM[1] + 10))
        self.display_.blit(self.texts[0], (self.ESM[0] + 10, self.ESM[1] + 50))

        self.manager.update(time_delta)
        self.manager.draw_ui(self.display_)

    def event(self, isTest=False):
        for event in pygame.event.get():
            if event.type == QUIT:  # stopper le programme si on click sur la crois
                self.loop = False
            if isTest or event.type == pygame.USEREVENT:
                if isTest or event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if isTest or event.ui_element == self.buttons[0]:
                        from COE.UI.interfaces.interface_play_menu import (
                            MenuPlay,
                        )

                        return MenuPlay(self.display_)
                    elif isTest or event.ui_element == self.buttons[1]:
                        pass

            self.manager.process_events(event)
        return self
