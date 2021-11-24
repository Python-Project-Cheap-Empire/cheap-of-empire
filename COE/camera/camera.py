import pygame


class Camera:  # pragma: no cover
    def __init__(self, window):
        self.x_offset = 0
        self.y_offset = 0
        self.speed = 20
        self.width = window[0]
        self.height = window[1]

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        # x movement
        if mouse_pos[0] > self.width * 0.95:
            self.x_offset -= self.speed
        elif mouse_pos[0] < self.width * 0.05:
            self.x_offset += self.speed

        # y movement
        if mouse_pos[1] > self.height * 0.95:
            self.y_offset -= self.speed
        elif mouse_pos[1] < self.height * 0.05:
            self.y_offset += self.speed
