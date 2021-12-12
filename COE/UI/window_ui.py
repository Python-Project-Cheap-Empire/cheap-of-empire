import pygame
from pygame.locals import FULLSCREEN
from COE.UI.interfaces.main_menu import MainMenu
from COE.map.map import Map


class Window:
    width, height = 0, 0

    def __init__(self, width=0, height=0):
        pygame.init()  # pygame init
        self.display = pygame.display.set_mode(
            (width, height), FULLSCREEN
        )  # window init
        self.clock = pygame.time.Clock()
        self.loop = True
        self.menu = MainMenu(self.display)
        self.width, self.height = (
            Window.width,
            Window.height,
        ) = pygame.display.get_window_size()

    def quit(self):
        pygame.quit()
        return None

    def show(self, map, camera, scaled_blocks, isTest=False):
        self.clock.tick(60)
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        # <<<<<<< HEAD
        if not self.menu.menu_passed:
            self.menu.display()
            self.menu = self.menu.event(isTest)
            if self.menu is None:
                self.loop = False
        else:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    res = Map.screen_to_map(
                        (event.pos[0], event.pos[1]), camera.x_offset, camera.y_offset
                    )
                    print(res[0], res[1])
            camera.update()
            map.draw_map(self, camera, scaled_blocks)
        # =======
        # self.menu.display()
        # self.menu = self.menu.event(isTest)
        # if self.menu is None:
        #     self.loop = False
        pygame.display.update()

    def get_loop(self):
        return self.loop
