import pygame
from pygame.locals import *
import pygame_gui
from COE.UI.interfaces.Interface_MenuOptions import MenuOptions
from COE.UI.interfaces.Interface_MenuJouer import MenuJouer


class MenuPrincipale:
    def __init__(self, fenetre_):
        self.fenetre = fenetre_
        self.screen_size = pygame.display.get_surface().get_size()
        self.manager = pygame_gui.UIManager(self.screen_size)
        self.bouttons = [
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.screen_size[0] / 2 - 200, self.screen_size[1] / 2 + 200),
                    (400, 100),
                ),
                text="QUITTER",
                manager=self.manager,
            ),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.screen_size[0] / 2 - 200, self.screen_size[1] / 2 + 50),
                    (400, 100),
                ),
                text="OPTIONS",
                manager=self.manager,
            ),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.screen_size[0] / 2 - 200, self.screen_size[1] / 2 - 100),
                    (400, 100),
                ),
                text="JOUER",
                manager=self.manager,
            ),
        ]
        self.img = [
            pygame.image.load("COE/UI/interfaces/images/fond_menu.png").convert()
        ]
        self.img[0] = pygame.transform.scale(self.img[0], (500, 331))
        self.clock = pygame.time.Clock()
        self.loop = True

    def display(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.fenetre.fill(0x000)
        self.fenetre.blit(self.img[0], (self.screen_size[0] / 2 - 250, 0))
        self.manager.update(time_delta)
        self.manager.draw_ui(self.fenetre)

    def event(self, isTest=False):
        for event in pygame.event.get():
            if event.type == QUIT:  # stopper le programme si on click sur la crois
                self.loop = False
            if isTest or event.type == pygame.USEREVENT:
                if isTest or event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if isTest or event.ui_element == self.bouttons[0]:
                        self.loop = False
                    if isTest or event.ui_element == self.bouttons[1]:
                        return MenuOptions(self.fenetre)
                    if isTest or event.ui_element == self.bouttons[2]:
                        return MenuJouer(self.fenetre)

            self.manager.process_events(event)
        if not self.loop:
            return None
        return self
