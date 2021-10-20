import pygame
from pygame.locals import *
import pygame_gui


class MenuOptions:
    def __init__(self, fenetre_):
        self.fenetre = fenetre_
        self.screen_size = pygame.display.get_surface().get_size()
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
            pygame_gui.elements.ui_button.UIButton(
                relative_rect=pygame.Rect(
                    (self.screen_size[0] / 2, self.screen_size[1] / 2),
                    (100, 50),
                ),
                text="q",
                manager=self.manager,
            ),
        ]
        self.img = [
            pygame.image.load("COE/UI/interfaces/images/fond_menu.png").convert()
        ]
        self.img[0] = pygame.transform.scale(self.img[0], (300, 199))
        self.clock = pygame.time.Clock()
        self.currante_key = ""

    def display(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.fenetre.fill(0x000)
        self.fenetre.blit(self.img[0], (self.screen_size[0] - 275, 0))
        self.manager.update(time_delta)
        self.manager.draw_ui(self.fenetre)

    def event(self, isTest=False):
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:
                for button in self.bouttons:
                    if button.text == "press key":
                        button.set_text(self.currante_key)
                        button.rebuild()

            # recuperations des touches du clavier appuyers
            if event.type == KEYDOWN:
                # assigner la touche apuyer boutton qui a etais selectionner
                for button in self.bouttons:
                    if button.text == "press key":
                        button.set_text(chr(event.key))
                        button.rebuild()

            # stopper le programme si on click sur la crois
            if event.type == QUIT:
                self.loop = False

            # evennement des bouttons
            if isTest or event.type == pygame.USEREVENT:
                if isTest or event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    # si le boutton selectionner et back
                    if isTest or event.ui_element == self.bouttons[0]:
                        from COE.UI.interfaces.Interface_MenuPrincipale import (
                            MenuPrincipale,
                        )

                        # on retourne sur le menu principale
                        return MenuPrincipale(self.fenetre)

                    # action pour le boutton de choix de touche
                    if isTest or event.ui_element == self.bouttons[1]:
                        if self.bouttons[1].text != "press key":
                            self.currante_key = self.bouttons[1].text
                            self.bouttons[1].set_text("press key")
                            self.bouttons[1].rebuild()
                        else:
                            self.bouttons[1].set_text(self.currante_key)
                            self.bouttons[1].rebuild()
                            self.currante_key = ""

            self.manager.process_events(event)
        return self
