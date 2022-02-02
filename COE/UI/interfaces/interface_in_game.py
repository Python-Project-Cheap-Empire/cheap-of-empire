import time
from COE.contents.building.barrack import Barrack
from COE.contents.building.house import House
import pygame
from pygame.locals import QUIT
import pygame_gui
from COE.contents.building.building import Building
from COE.contents.building.military_building import MilitaryBuilding
from COE.contents.building.town_center import TownCenter
from COE.contents.unit.villager import Villager
from COE.map.map import Map

# importer la classe static pour les images
from COE.contents.static.static import Static

import os

script_dir = os.path.dirname(os.path.abspath(__file__))


class GameMenu:
    def __init__(self, display_, manager, cheat_code, timer, static):
        self.display_ = display_
        self.menu_passed = False
        self.static = static
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
                    (self.ESM[0] + 250, self.ESM[1] + 150), (100, 50)
                ),
                text="Save",
                manager=self.manager,
                visible=0,
            ),
        ]
        self.buttons[0].visible = 0
        self.static.multiplicateur = (
            1 if self.width // 2 > 1000 else ((self.width * (3 / 8)) / (1000))
        )
        self.font_size = int(35 * self.static.multiplicateur)
        self.top_panel = ((105 * self.static.multiplicateur) / 2) - (
            (self.font_size * self.static.multiplicateur) / 2
        )
        self.partition_panel = (
            1000 * self.static.multiplicateur - (30 * self.static.multiplicateur * 2)
        ) / 5
        self.static.mul_menu_panel = (self.width * (4 / 8)) / 502
        self.static.mul_action_panel = (107 * self.static.mul_menu_panel) / 343
        self.top_x_panel = self.width / 2 - (self.static.mul_menu_panel * 502 / 2)
        self.top_y_panel = self.height - (self.static.mul_menu_panel * 107)
        self.top_panel = ((105 * self.static.multiplicateur) / 2) - (
            (62 * self.static.multiplicateur) / 2
        )
        self.partition_panel = (
            1000 * self.static.multiplicateur - (30 * self.static.multiplicateur * 2)
        ) / 5
        self.static.scaled_UI_imgs = {
            "resource_panel": [
                pygame.transform.scale(
                    self.static.image_cache["resourcecivpanel_04"],
                    (
                        1000 * self.static.multiplicateur,
                        105 * self.static.multiplicateur,
                    ),
                ),
                (0, 0),
            ],
            "menu_panel": [
                pygame.transform.scale(
                    self.static.image_cache["menucivpanel_04"],
                    (
                        502 * self.static.mul_menu_panel,
                        107 * self.static.mul_menu_panel,
                    ),
                ),
                (
                    self.width / 2 - (self.static.mul_menu_panel * 502 / 2),
                    self.height - (self.static.mul_menu_panel * 107),
                ),
            ],
            "action_panel": [
                pygame.transform.scale(
                    self.static.image_cache["actioncivpanel_04"],
                    (
                        674 * self.static.mul_action_panel,
                        343 * self.static.mul_action_panel,
                    ),
                ),
                (0, self.height - (self.static.mul_menu_panel * 107)),
            ],
            # icon du bois
            "wood": [
                pygame.transform.scale(
                    self.static.image_cache["resourceicons_18"],
                    (62 * self.static.multiplicateur, 62 * self.static.multiplicateur),
                ),
                (
                    self.partition_panel * 0 + (30 * self.static.multiplicateur),
                    self.top_panel,
                ),
            ],
            # icon de la nouriture
            "food": [
                pygame.transform.scale(
                    self.static.image_cache["resourceicons_03"],
                    (62 * self.static.multiplicateur, 62 * self.static.multiplicateur),
                ),
                (
                    self.partition_panel * 1 + (30 * self.static.multiplicateur),
                    self.top_panel,
                ),
            ],
            # icon de l'or
            "gold": [
                pygame.transform.scale(
                    self.static.image_cache["resourceicons_06"],
                    (62 * self.static.multiplicateur, 62 * self.static.multiplicateur),
                ),
                (
                    self.partition_panel * 2 + (30 * self.static.multiplicateur),
                    self.top_panel,
                ),
            ],
            # icon de pierre
            "stone": [
                pygame.transform.scale(
                    self.static.image_cache["resourceicons_15"],
                    (62 * self.static.multiplicateur, 62 * self.static.multiplicateur),
                ),
                (
                    self.partition_panel * 3 + (30 * self.static.multiplicateur),
                    self.top_panel,
                ),
            ],
            # icon du tipi
            "tipi": [
                pygame.transform.scale(
                    self.static.image_cache["resourceicons_12"],
                    (62 * self.static.multiplicateur, 62 * self.static.multiplicateur),
                ),
                (
                    self.partition_panel * 4 + (30 * self.static.multiplicateur),
                    self.top_panel,
                ),
            ],
            # icon player
            "villager": [
                pygame.transform.scale(
                    self.static.image_cache["ui_uniticons_01"],
                    (50 * self.static.mul_menu_panel, 50 * self.static.mul_menu_panel),
                ),
                (
                    self.top_x_panel + (40 * self.static.mul_menu_panel),
                    self.top_y_panel + (20 * self.static.mul_menu_panel),
                ),
            ],
            "clubman": [
                pygame.transform.scale(
                    self.static.image_cache["ui_uniticons_03"],
                    (50 * self.static.mul_menu_panel, 50 * self.static.mul_menu_panel),
                ),
                (200, (self.height - (self.static.mul_menu_panel * 107)) + 20),
            ],
            "buildings": {
                "house": [
                    pygame.transform.scale(
                        self.static.image_cache["ui_buildinghouse"],
                        (
                            100 * self.static.mul_action_panel,
                            100 * self.static.mul_action_panel,
                        ),
                    ),
                    (200, (self.height - (self.static.mul_menu_panel * 107)) + 20),
                ],
                "barrack": [
                    pygame.transform.scale(
                        self.static.image_cache["ui_buildingbarrack"],
                        (
                            100 * self.static.mul_action_panel,
                            100 * self.static.mul_action_panel,
                        ),
                    ),
                    (275, (self.height - (self.static.mul_menu_panel * 107)) + 20),
                ],
            },
        }

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
            int(40 * self.static.multiplicateur),
            (0, 255, 0),
            (self.width - 100, 0),
        )

    def draw_shortcuts(self, speed):
        self.draw_text(
            f"F4 | speed: {speed}",
            int(40 * self.static.multiplicateur),
            (0, 255, 0),
            (self.width - 300, 0),
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
            self.font_size,
            (255, 255, 255),
            (
                self.partition_panel * 0
                + (30 * self.static.multiplicateur)
                + (67 * self.static.multiplicateur),
                self.top_panel,
            ),
        )
        self.draw_text(
            str(game.players[0]._food),
            self.font_size,
            (255, 255, 255),
            (
                self.partition_panel * 1
                + (30 * self.static.multiplicateur)
                + (67 * self.static.multiplicateur),
                self.top_panel,
            ),
        )
        self.draw_text(
            str(game.players[0]._gold),
            self.font_size,
            (255, 255, 255),
            (
                self.partition_panel * 2
                + (30 * self.static.multiplicateur)
                + (67 * self.static.multiplicateur),
                self.top_panel,
            ),
        )
        self.draw_text(
            str(game.players[0]._stone),
            self.font_size,
            (255, 255, 255),
            (
                self.partition_panel * 3
                + (30 * self.static.multiplicateur)
                + (67 * self.static.multiplicateur),
                self.top_panel,
            ),
        )
        nb_house = 0
        for building in game.players[0].buildings:
            if isinstance(building, House):
                if building.is_master:
                    if building.construction_percent == 100:
                        nb_house += 1
        self.draw_text(
            f"{len(game.players[0].units)}/{5+(5*nb_house)}",
            self.font_size,
            (255, 255, 255),
            (
                self.partition_panel * 4
                + (30 * self.static.multiplicateur)
                + (67 * self.static.multiplicateur),
                self.top_panel,
            ),
        )

    def draw_text(self, format, size, color, positions):
        myfont = pygame.font.SysFont(None, size)
        textsurface = myfont.render(format, True, color)
        self.display_.blit(textsurface, positions)

    def display(self, game):
        self.display_.blit(
            self.static.scaled_UI_imgs["resource_panel"][0],
            self.static.scaled_UI_imgs["resource_panel"][1],
        )  # panel ressources
        self.display_.blit(
            self.static.scaled_UI_imgs["wood"][0],
            self.static.scaled_UI_imgs["wood"][1],
        )  # wood
        self.display_.blit(
            self.static.scaled_UI_imgs["food"][0],
            self.static.scaled_UI_imgs["food"][1],
        )  # food
        self.display_.blit(
            self.static.scaled_UI_imgs["gold"][0],
            self.static.scaled_UI_imgs["gold"][1],
        )  # gold
        self.display_.blit(
            self.static.scaled_UI_imgs["stone"][0],
            self.static.scaled_UI_imgs["stone"][1],
        )  # stone
        self.display_.blit(
            self.static.scaled_UI_imgs["tipi"][0],
            self.static.scaled_UI_imgs["tipi"][1],
        )  # tipi
        self.draw_ressources(game)

    def draw_entity(self, selected_entities):
        entity_ = None
        for entity in selected_entities:
            if isinstance(entity, Villager) or isinstance(entity, Building):
                # entity_ = entity
                self.display_.blit(
                    self.static.scaled_UI_imgs["menu_panel"][0],
                    self.static.scaled_UI_imgs["menu_panel"][1],
                )

                if entity.player._is_human:
                    self.display_.blit(
                        self.static.scaled_UI_imgs["action_panel"][0],
                        self.static.scaled_UI_imgs["action_panel"][1],
                    )
                    break

        for entity in selected_entities:
            if isinstance(entity, Villager):
                self.display_.blit(
                    self.static.scaled_UI_imgs["villager"][0],
                    self.static.scaled_UI_imgs["villager"][1],
                )
                entity_ = entity
                if entity.player._is_human:
                    self.display_.blit(
                        self.static.scaled_UI_imgs["buildings"]["house"][0],
                        self.static.scaled_UI_imgs["buildings"]["house"][1],
                    )
                    self.display_.blit(
                        self.static.scaled_UI_imgs["buildings"]["barrack"][0],
                        self.static.scaled_UI_imgs["buildings"]["barrack"][1],
                    )

                    break

        if not entity_:
            for entity in selected_entities:
                if isinstance(entity, TownCenter):
                    entity_ = entity
                    if entity.player._is_human:
                        self.display_.blit(
                            self.static.scaled_UI_imgs["villager"][0],
                            (
                                self.top_x_panel + (50 * self.static.mul_menu_panel),
                                self.top_y_panel + (25 * self.static.mul_menu_panel),
                            ),
                        )
                        break

        if not entity_:
            # print("no entity")
            for entity in selected_entities:
                if isinstance(entity, Barrack):
                    entity_ = entity
                    if entity.player._is_human:
                        self.display_.blit(
                            self.static.scaled_UI_imgs["clubman"][0],
                            self.static.scaled_UI_imgs["clubman"][1],
                        )
                        # entity_ = entity
                        break

        if not entity_:
            for entity in selected_entities:
                if isinstance(selected_entities[0], Building):
                    self.display_.blit(
                        self.static.scaled_UI_imgs["buildings"][
                            selected_entities[0].name.lower()
                        ][0],
                        (
                            self.top_x_panel + (50 * self.static.mul_menu_panel),
                            self.top_y_panel + (25 * self.static.mul_menu_panel),
                        ),
                    )
                    entity_ = entity
                    break

        if entity_:
            self.draw_text(
                entity_.name,
                20,
                (255, 255, 255),
                (
                    self.top_x_panel + (502 * self.static.mul_menu_panel / 2),
                    self.top_y_panel + (15 * self.static.mul_menu_panel),
                ),
            )
            self.draw_text(
                f"{entity_.hp}/{entity_.max_hp}",
                20,
                (255, 255, 255),
                (
                    self.top_x_panel + (55 * self.static.mul_menu_panel),
                    self.top_y_panel
                    + (15 * self.static.mul_menu_panel)
                    + (62 * self.static.mul_menu_panel),
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
