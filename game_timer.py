import pygame

class GameTimer:
    def _init_(self, duration):
        self.duration = duration
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        elapsed_time = (pygame.time.get_ticks() - self.start_ticks) / 1000
        return max(0, self.duration - elapsed_time) <= 0

    def display(self, screen, width):
        font = pygame.font.Font(None, 36)
        remaining_time = max(0, self.duration - (pygame.time.get_ticks() - self.start_ticks) / 1000)
        label = font.render(f"Time: {int(remaining_time)}s", True, (255, 255, 255))
        screen.blit(label, (width - 150, 10))