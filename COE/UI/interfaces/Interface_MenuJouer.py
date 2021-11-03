import pygame
from pygame.locals import *
import pygame_gui


class MenuJouer:
    def __init__(self, fenetre_):
        self.fenetre = fenetre_
        self.screen_size = pygame.display.get_surface().get_size()
        self.manager = pygame_gui.UIManager(self.screen_size)
        self.ESM = (self.screen_size[0] / 2 - 450, self.screen_size[0] / 2 - 400)
        self.bouttons = [
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
            pygame.image.load("COE/UI/interfaces/images/fond_menu.png").convert()
        ]
        self.img[0] = pygame.transform.scale(self.img[0], (300, 199))
        self.clock = pygame.time.Clock()

    def display(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.fenetre.fill(0x000)
        pygame.draw.rect(
            self.fenetre, (99, 104, 107), (self.ESM[0], self.ESM[1], 600, 500)
        )
        pygame.draw.rect(
            self.fenetre, (99, 104, 107), (self.ESM[0] + 650, self.ESM[1], 250, 151)
        )
        self.fenetre.blit(self.img[0], (self.screen_size[0] - 275, 0))
        self.manager.update(time_delta)
        self.manager.draw_ui(self.fenetre)

    def event(self, isTest=False):
        for event in pygame.event.get():
            if event.type == QUIT:  # stopper le programme si on click sur la crois
                self.loop = False
            if isTest or event.type == pygame.USEREVENT:
                if isTest or event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if isTest or event.ui_element == self.bouttons[0]:
                        from COE.UI.interfaces.Interface_MenuPrincipale import (
                            MenuPrincipale,
                        )

                        return MenuPrincipale(self.fenetre)

                    if isTest or event.ui_element == self.bouttons[1]:
                        from COE.UI.interfaces.Interface_MenuNewGame import (
                            MenuNewGame,
                        )

                        return MenuNewGame(self.fenetre)

                    if isTest or event.ui_element == self.bouttons[2]:
                        from COE.UI.interfaces.Interface_MenuMultiplayers import (
                            MenuMulti,
                        )

                        return MenuMulti(self.fenetre)

            self.manager.process_events(event)
        return self
