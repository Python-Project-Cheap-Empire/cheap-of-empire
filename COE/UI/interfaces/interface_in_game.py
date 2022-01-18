import pygame
from pygame.locals import QUIT
import pygame_gui
from COE.map.map import Map


class GameMenu:
    def __init__(self, display_, manager, cheat_code):
        self.display_ = display_
        self.menu_passed = False
        self.screen_size = pygame.display.get_surface().get_size()
        self.width = self.screen_size[0]
        self.height = self.screen_size[1]
        self.manager = manager
        self.manager_menu = pygame_gui.UIManager(self.screen_size)
        self.ESM = (self.screen_size[0] / 2 - 300, self.screen_size[0] / 2 - 500)
        self.buttons = [
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((0, 20), (100, 50)),
                text="Menu",
                manager=self.manager,
                visible=1,
            ),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 250, self.ESM[1] + 400), (100, 50)
                ),
                text="Exit",
                manager=self.manager,
                visible=0,
            ),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 250, self.ESM[1] + 50), (100, 50)
                ),
                text="Resume",
                manager=self.manager,
                visible=0,
            ),
        ]
        self.cheat_code = cheat_code
        self.pause = False
        self.clock = pygame.time.Clock()

    def draw_pos(self, game, static):
        x, y = Map.screen_to_map(
            pygame.mouse.get_pos(),
            game.camera.x_offset,
            game.camera.y_offset,
            static.half_width_cells_size,
            static.half_height_cells_size,
        )

        x, y = int(x), int(y)
        pos = f"{x}, {y}"
        mpos = pygame.mouse.get_pos()
        self.draw_text(
            pos,
            25,
            (255, 0, 0),
            (mpos[0] + 20, mpos[1]),
        )

    def draw_fps(self, fps):
        self.draw_text(
            f"fps={round(fps)}",
            25,
            (255, 0, 0),
            (self.width - 100, 100),
        )

    def draw(self):
        s = pygame.Surface((self.width, self.height))
        s.set_alpha(128)
        s.fill((0, 0, 0))
        pygame.draw.rect(
            self.display_, (99, 104, 107), (self.ESM[0], self.ESM[1], 600, 500)
        )
        self.display_.blit(s, (0, 0))

    def draw_ressources(self, game):
        self.draw_text(
            str(game.players[0]._wood),
            15,
            (255, 255, 255),
            (35, 0),
        )
        self.draw_text(
            str(game.players[0]._food),
            15,
            (255, 255, 255),
            (185, 0),
        )
        self.draw_text(
            str(game.players[0]._gold),
            15,
            (255, 255, 255),
            (335, 0),
        )
        self.draw_text(
            str(game.players[0]._stone),
            15,
            (255, 255, 255),
            (485, 0),
        )

    def draw_text(self, format, size, color, positions):
        myfont = pygame.font.SysFont("Comic Sans MS", size)
        textsurface = myfont.render(format, False, color)
        self.display_.blit(textsurface, positions)

    def event(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if self.pause and event.ui_element == self.buttons[1]:
                    return False
                if self.pause and event.ui_element == self.buttons[2]:
                    self.pause = False
                    self.visibility_pause()
                if event.ui_element == self.buttons[0]:
                    self.pause = not self.pause
                    self.visibility_pause()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.pause = not self.pause
                self.visibility_pause()
        self.cheat_code.event(event)
        self.manager.process_events(event)
        return True

    def visibility_pause(self):
        self.buttons[1].visible = int(not self.buttons[1].visible)
        self.buttons[2].visible = int(not self.buttons[2].visible)
