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
                    (self.ESM[0] + 240, self.ESM[1] + 95), (250, 50)
                ),
                manager=self.manager,
            ),
            pygame_gui.elements.UIDropDownMenu(
                options_list=[str(x)[9:] for x in self.enumeration_type],
                starting_option=str(self.enumeration_type[0])[9:],
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 240, self.ESM[1] + 140), (250, 50)
                ),
                manager=self.manager,
            ),
            pygame_gui.elements.UIDropDownMenu(
                options_list=[str(x)[16:] for x in self.enumeration_ressources],
                starting_option=str(self.enumeration_ressources[0])[16:],
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 240, self.ESM[1] + 185), (250, 50)
                ),
                manager=self.manager,
            ),
            pygame_gui.elements.UIDropDownMenu(
                options_list=["1", "2", "3", "4", "5", "6", "7"],
                starting_option="1",
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 240, self.ESM[1] + 290), (250, 50)
                ),
                manager=self.manager,
            ),
            pygame_gui.elements.UIDropDownMenu(
                options_list=["None"],
                starting_option="None",
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 240, self.ESM[1] + 335), (250, 50)
                ),
                manager=self.manager,
            ),
        ]

        # text input
        self.text_input = [
            pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 190, self.ESM[1] + 7), (250, 50)
                ),
                manager=self.manager,
            )
        ]

        self.font = pygame.font.Font(None, 25)
        self.texts = [
            self.font.render("Game Name", True, (255, 255, 255)),
            self.font.render("Map Size", True, (255, 255, 255)),
            self.font.render("Map Type", True, (255, 255, 255)),
            self.font.render("Resources Ratity", True, (255, 255, 255)),
            self.font.render("Map Options", True, (255, 255, 255)),
            self.font.render("Game Options", True, (255, 255, 255)),
            self.font.render("AI Numbers", True, (255, 255, 255)),
            self.font.render("Civilisation", True, (255, 255, 255)),
        ]

        self.img[0] = pygame.transform.scale(self.img[0], (300, 199))
        self.clock = pygame.time.Clock()
        self.playing = False

    def display(self):
        if self.text_input[0].get_text() != "":
            self.texts[0] = self.font.render("Game Name", True, (255, 255, 255))
        time_delta = self.clock.tick(60) / 1000.0
        self.display_.fill(0x000)
        pygame.draw.rect(
            self.display_, (99, 104, 107), (self.ESM[0], self.ESM[1], 600, 500)
        )
        pygame.draw.rect(
            self.display_, (99, 104, 107), (self.ESM[0] + 650, self.ESM[1], 250, 75)
        )
        self.display_.blit(self.img[0], (self.screen_size[0] - 275, 0))

        # affichage des textes
        self.display_.blit(self.texts[4], (self.ESM[0] + 10, self.ESM[1] + 70))
        self.display_.blit(self.texts[5], (self.ESM[0] + 10, self.ESM[1] + 270))

        self.display_.blit(self.texts[0], (self.ESM[0] + 10, self.ESM[1] + 10))
        self.display_.blit(self.texts[1], (self.ESM[0] + 50, self.ESM[1] + 110))
        self.display_.blit(self.texts[2], (self.ESM[0] + 50, self.ESM[1] + 160))
        self.display_.blit(self.texts[3], (self.ESM[0] + 50, self.ESM[1] + 210))
        self.display_.blit(self.texts[6], (self.ESM[0] + 50, self.ESM[1] + 300))
        self.display_.blit(self.texts[7], (self.ESM[0] + 50, self.ESM[1] + 350))
        self.display_.blit(self.texts[0], (self.ESM[0] + 10, self.ESM[1] + 10))

        self.manager.update(time_delta)
        self.manager.draw_ui(self.display_)

    def event(self, isTest=False):
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
                    if event.ui_element == self.buttons[1]:
                        if self.text_input[0].get_text() == "":
                            self.texts[0] = self.font.render(
                                "Game Name", True, (255, 0, 0)
                            )
                        else:
                            self.playing = True

            self.manager.process_events(event)
        return self

    def get_playing(self):
        return self.playing
