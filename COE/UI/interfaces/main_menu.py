import pygame
from pygame.locals import QUIT
import pygame_gui


class MainMenu:
    def __init__(self, display_):
        self.display_ = display_
        self.menu_passed = False
        self.screen_size = pygame.display.get_surface().get_size()
        self.width = self.screen_size[0]
        self.height = self.screen_size[1]
        self.manager = pygame_gui.UIManager(self.screen_size)
        self.buttons = [
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.width / 2 - 200, self.height / 2 + 200),
                    (400, 100),
                ),
                text="QUIT",
                manager=self.manager,
            ),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.width / 2 - 200, self.height / 2 + 50),
                    (400, 100),
                ),
                text="OPTIONS",
                manager=self.manager,
            ),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.width / 2 - 200, self.height / 2 - 100),
                    (400, 100),
                ),
                text="PLAY",
                manager=self.manager,
            ),
        ]
        self.img = [
            pygame.image.load("COE/UI/interfaces/images/background_menu.png").convert()
        ]
        self.img[0] = pygame.transform.scale(self.img[0], (500, 331))
        self.clock = pygame.time.Clock()
        self.loop = True

    def display(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.display_.fill(0x000)
        self.display_.blit(self.img[0], (self.width / 2 - 250, 0))
        self.manager.update(time_delta)
        self.manager.draw_ui(self.display_)

    def event(self, isTest=False):
        for event in pygame.event.get():
            if (
                event.type == pygame.MOUSEBUTTONUP
            ):  # or MOUSEBUTTONDOWN depending on what you want.
                print(event.pos)
            if event.type == QUIT:  # Stop the game if the QUIT button is clicked on
                self.loop = False
            if isTest or event.type == pygame.USEREVENT:
                if isTest or event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                    if isTest or event.ui_element == self.buttons[0]:
                        self.loop = False
                    elif isTest or event.ui_element == self.buttons[2]:
                        self.menu_passed = True
            self.manager.process_events(event)
        if not self.loop:
            return None
        return self


# pour qslhb
