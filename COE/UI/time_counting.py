import pygame
import time


class time_counting:
    def __init__(self, time_):
        self.font = pygame.font.Font(None, 25)
        self.frame_rate = 60
        self.time = time_
        self.prev_time = time.time()

    def update(self, game_speed):
        now = time.time()
        dt = now - self.prev_time
        self.total_seconds = self.time.frame_count // self.frame_rate
        self.time.m = self.total_seconds // 60
        self.time.s = self.total_seconds % 60
        self.time.h = self.total_seconds // 3600
        self.time.frame_count += round(dt * 60 * game_speed)
        self.prev_time = now

    def draw_time(self, screen):

        output_string = "{0:02}:{1:02}:{2:02}".format(
            self.time.h, self.time.m, self.time.s
        )
        text = self.font.render(output_string, True, (255, 255, 255))
        screen.blit(text, [10, 80])
