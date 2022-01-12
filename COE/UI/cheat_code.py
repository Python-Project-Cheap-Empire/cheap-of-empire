import pygame
import os

COLOR_INACTIVE = pygame.Color("dimgray")
COLOR_ACTIVE = pygame.Color("gold3")
os.environ["RESSOURCE"] = ""


class CheatCode:
    def __init__(
        self,
        screen,
        x,
        y,
        w=400,
        h=35,
    ):
        self.pos = (x // 2 - 200, y // 2 + 200)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], w, h)
        self.color = COLOR_INACTIVE
        self.text = ""
        self.screen = screen
        self.font = pygame.font.Font(None, 32)
        self.text_rect = self.font.render(self.text, True, self.color)
        self.active = False
        self.ressource = ""

    def process_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # USER CLICK ON THE TEXT BOX
            if self.rect.collidepoint(event.pos):
                self.active = not self.active  # Toggle the active variable
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.text == "COINAGE":
                        self.ressource = "GOLD"
                    if self.text == "PEPPERONI PIZZA":
                        self.ressource = "FOOD"
                    if self.text == "QUARRY":
                        self.ressource = "STONE"
                    if self.text == "WOODSTOCK":
                        self.ressource = "WOOD"
                    # assign to the evironment's value
                    if self.ressource != "":
                        os.environ["RESSOURCE"] = self.ressource
                        self.ressource = ""
                    print(self.text)
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.text_rect = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(400, self.text_rect.get_width() + 10)
        self.rect.w = width

    def draw(self):
        self.screen.blit(self.text_rect, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(self.screen, self.color, self.rect, 2)
