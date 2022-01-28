import pygame


class CheatCode:
    def __init__(self, screen, game, w=400, h=35):
        self.color = pygame.Color("gold3")
        self.color_active = pygame.Color("gold3")
        self.color_inactive = pygame.Color("dimgray")
        self.text = ""
        self.font = pygame.font.Font(None, 32)
        self.text_rect = self.font.render(self.text, True, self.color_active)
        self.active = False
        self.game = game
        self.screen = screen
        self.pos = (screen.get_width() // 2 - 200, screen.get_height() // 2 + 200)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], w, h)

    def execute_cheat(self, action):
        if action == "NINJALUI":
            self.game.players[0]._wood += 10000
            self.game.players[0]._food += 10000
            self.game.players[0]._gold += 10000
            self.game.players[0]._stone += 10000
        elif action == "COINAGE":
            self.game.players[0]._gold += 1000
        elif action == "PEPPERONI PIZZA":
            self.game.players[0]._food += 1000
        elif action == "QUARRY":
            self.game.players[0]._stone += 1000
        elif action == "WOODSTOCK":
            self.game.players[0]._wood += 1000

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # USER CLICK ON THE TEXT BOX
            if self.rect.collidepoint(event.pos):
                self.active = True  # Toggle the active variable
                self.color = self.color_active
            else:
                self.active = False
                self.color = self.color_inactive
        if self.active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.execute_cheat(self.text)
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    pass
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
