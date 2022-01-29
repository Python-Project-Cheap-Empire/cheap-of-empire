import time
import pygame
from pygame.locals import QUIT
import pygame_gui
from COE.map.map import Map

# importer la classe static pour les images
from COE.contents.static.static import Static

import os

script_dir = os.path.dirname(os.path.abspath(__file__))


class GameMenu:
    def __init__(self, display_, manager, cheat_code, timer):
        self.display_ = display_
        self.menu_passed = False
        self.static = Static()
        self.screen_size = pygame.display.get_surface().get_size()
        self.width = self.screen_size[0]
        self.height = self.screen_size[1]
        self.manager = manager
        self.manager_menu = pygame_gui.UIManager(self.screen_size)
        self.ESM = (self.screen_size[0] / 2 - 300, self.screen_size[0] / 2 - 500)
        self.timer = timer
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
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.ESM[0] + 250, self.ESM[1] + 300), (100, 50)
                ),
                text="Save",
                manager=self.manager,
                visible=0,
            ),
        ]
        self.buttons[0].visible = 0
        self.multicateur = (
            1 if self.width // 2 > 1000 else ((self.width * (3 / 8)) / (1000))
        )
        self.mul_pannelmenu = (self.width * (4 / 8)) / 502
        self.mul_pannelaction = (107 * self.mul_pannelmenu) / 343
        self.imgs_panel = [
            pygame.transform.scale(
                self.static.image_cache["resourcecivpanel_04"],
                (1000 * self.multicateur, 105 * self.multicateur),
            ),
            pygame.transform.scale(
                self.static.image_cache["menucivpanel_04"],
                (502 * self.mul_pannelmenu, 107 * self.mul_pannelmenu),
            ),
            pygame.transform.scale(
                self.static.image_cache["actioncivpanel_04"],
                (674 * self.mul_pannelaction, 343 * self.mul_pannelaction),
            ),
        ]
        self.imgs_icon = [
            # icon du bois
            pygame.transform.scale(
                self.static.image_cache["resourceicons_18"],
                (62 * self.multicateur, 62 * self.multicateur),
            ),
            # icon de la nouriture
            pygame.transform.scale(
                self.static.image_cache["resourceicons_03"],
                (62 * self.multicateur, 62 * self.multicateur),
            ),
            # icon de l'or
            pygame.transform.scale(
                self.static.image_cache["resourceicons_06"],
                (62 * self.multicateur, 62 * self.multicateur),
            ),
            # icon de pierre
            pygame.transform.scale(
                self.static.image_cache["resourceicons_15"],
                (62 * self.multicateur, 62 * self.multicateur),
            ),
            # icon du tipi
            pygame.transform.scale(
                self.static.image_cache["resourceicons_12"],
                (62 * self.multicateur, 62 * self.multicateur),
            ),
            # icon player
            pygame.transform.scale(
                self.static.image_cache["ui_uniticons_01"],
                (62 * self.mul_pannelmenu, 62 * self.mul_pannelmenu),
            ),
        ]
        self.cheat_code = cheat_code
        self.pause = False
        self.clock = pygame.time.Clock()
        self.saved = False

    def draw_pos(self, game, static):
        x, y = Map.screen_to_map(
            pygame.mouse.get_pos(),
            game.camera.x_offset,
            game.camera.y_offset,
            self.static.half_width_cells_size,
            self.static.half_height_cells_size,
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

    def draw_selection_rectangle(self, rectangle):
        if rectangle:
            rectangleCorners = [
                rectangle.topleft,
                rectangle.topright,
                rectangle.bottomright,
                rectangle.bottomleft,
            ]
            pygame.draw.lines(self.display_, (255, 255, 255), True, rectangleCorners, 1)

    def draw_fps(self, fps):
        self.draw_text(
            f"fps={round(fps)}",
            int(25 * self.multicateur),
            (0, 255, 0),
            (0, 0),
        )

    def draw_shortcuts(self, speed):
        self.draw_text(f"F4 | speed: {speed}", 30, (0, 255, 0), (self.width - 300, 0))

    def draw(self):
        s = pygame.Surface((self.width, self.height))
        s.set_alpha(128)
        s.fill((0, 0, 0))
        pygame.draw.rect(
            self.display_, (99, 104, 107), (self.ESM[0], self.ESM[1], 600, 500)
        )
        self.display_.blit(s, (0, 0))

    def draw_ressources(self, game):
        font_size = int(35 * self.multicateur)
        top_pannel = ((105 * self.multicateur) / 2) - (
            (font_size * self.multicateur) / 2
        )
        partition_pannel = (1000 * self.multicateur - (30 * self.multicateur * 2)) / 5
        self.draw_text(
            str(game.players[0]._wood),
            font_size,
            (255, 255, 255),
            (
                partition_pannel * 0
                + (30 * self.multicateur)
                + (67 * self.multicateur),
                top_pannel,
            ),
        )
        self.draw_text(
            str(game.players[0]._food),
            font_size,
            (255, 255, 255),
            (
                partition_pannel * 1
                + (30 * self.multicateur)
                + (67 * self.multicateur),
                top_pannel,
            ),
        )
        self.draw_text(
            str(game.players[0]._gold),
            font_size,
            (255, 255, 255),
            (
                partition_pannel * 2
                + (30 * self.multicateur)
                + (67 * self.multicateur),
                top_pannel,
            ),
        )
        self.draw_text(
            str(game.players[0]._stone),
            font_size,
            (255, 255, 255),
            (
                partition_pannel * 3
                + (30 * self.multicateur)
                + (67 * self.multicateur),
                top_pannel,
            ),
        )
        self.draw_text(
            "?",
            font_size,
            (255, 255, 255),
            (
                partition_pannel * 4
                + (30 * self.multicateur)
                + (67 * self.multicateur),
                top_pannel,
            ),
        )

    def draw_text(self, format, size, color, positions):
        myfont = pygame.font.SysFont(None, size)
        textsurface = myfont.render(format, True, color)
        self.display_.blit(textsurface, positions)

    def display(self, game):
        self.display_.blit(self.imgs_panel[0], (0, 0))  # panel ressources
        top_pannel = ((105 * self.multicateur) / 2) - ((62 * self.multicateur) / 2)
        partition_pannel = (1000 * self.multicateur - (30 * self.multicateur * 2)) / 5
        self.display_.blit(
            self.imgs_icon[0],
            (partition_pannel * 0 + (30 * self.multicateur), top_pannel),
        )  # wood
        self.display_.blit(
            self.imgs_icon[1],
            (partition_pannel * 1 + (30 * self.multicateur), top_pannel),
        )  # food
        self.display_.blit(
            self.imgs_icon[2],
            (partition_pannel * 2 + (30 * self.multicateur), top_pannel),
        )  # gold
        self.display_.blit(
            self.imgs_icon[3],
            (partition_pannel * 3 + (30 * self.multicateur), top_pannel),
        )  # stone
        self.display_.blit(
            self.imgs_icon[4],
            (partition_pannel * 4 + (30 * self.multicateur), top_pannel),
        )  # tipi
        self.draw_ressources(game)

    def draw_entity(self, entity):
        top_pannel_y = self.height - (self.mul_pannelmenu * 107)
        top_pannel_x = self.width / 2 - (self.mul_pannelmenu * 502 / 2)
        self.display_.blit(self.imgs_panel[1], (top_pannel_x, top_pannel_y))
        self.display_.blit(self.imgs_panel[2], (0, top_pannel_y))
        self.display_.blit(
            self.imgs_icon[5],
            (
                top_pannel_x + (40 * self.mul_pannelmenu),
                top_pannel_y + (15 * self.mul_pannelmenu),
            ),
        )
        self.draw_text(
            entity.name,
            20,
            (255, 255, 255),
            (
                top_pannel_x + (502 * self.mul_pannelmenu / 2),
                top_pannel_y + (15 * self.mul_pannelmenu),
            ),
        )
        self.draw_text(
            str(entity.hp) + " / ?",
            20,
            (255, 255, 255),
            (
                top_pannel_x + (55 * self.mul_pannelmenu),
                top_pannel_y + (15 * self.mul_pannelmenu) + (62 * self.mul_pannelmenu),
            ),
        )

    def event(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if self.pause and event.ui_element == self.buttons[1]:
                    return False
                if self.pause and event.ui_element == self.buttons[2]:
                    self.timer.prev_time = time.time()
                    self.pause = False
                    self.visibility_pause()
                if self.pause and event.ui_element == self.buttons[3]:
                    self.saved = True
                if event.ui_element == self.buttons[0]:
                    self.timer.prev_time = time.time()
                    self.pause = not self.pause
                    self.visibility_pause()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.timer.prev_time = time.time()
                self.pause = not self.pause
                self.visibility_pause()
        self.cheat_code.event(event)
        self.manager.process_events(event)
        return True

    def visibility_pause(self):
        self.buttons[1].visible = int(not self.buttons[1].visible)
        self.buttons[2].visible = int(not self.buttons[2].visible)
        self.buttons[3].visible = int(not self.buttons[3].visible)
