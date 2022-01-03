import pygame


class time_counting:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 25)
        self.frame_count = 0
        self.frame_rate = 60
        self.start_time = 0
        self.clock = pygame.time.Clock()

    def draw_time(self, screen):
        self.total_seconds = self.frame_count // self.frame_rate
        self.minutes = self.total_seconds // 60
        self.seconds = self.total_seconds % 60
        self.hours = self.total_seconds // 3600
        output_string = "{0:02}:{1:02}:{2:02}".format(
            self.hours, self.minutes, self.seconds
        )
        text = self.font.render(output_string, True, (255, 255, 255))
        screen.blit(text, [10, 80])  # position
        self.frame_count += 1

        self.clock.tick(self.frame_rate)
