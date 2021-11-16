import pygame
from pygame.locals import *
from COE.UI.interfaces.Interface_MenuPrincipale import MenuPrincipale


class Fenetre:
    def __init__(self):
        pygame.init()  # initialisation de pygame
        self.fenetre = pygame.display.set_mode(
            (0, 0), FULLSCREEN
        )  # creation d'une fenetre
        self.clock = pygame.time.Clock()
        self.screen_size = pygame.display.get_surface().get_size()
        self.loop = True
        self.menu = MenuPrincipale(self.fenetre)

    def quitter(self):
        pygame.quit()
        return None

    def display(self, isTest=False):
        self.clock.tick(100)
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        self.menu.display()
        self.menu = self.menu.event(isTest)
        if self.menu is None:
            self.loop = False
        pygame.display.flip()

    def get_loop(self):
        return self.loop
