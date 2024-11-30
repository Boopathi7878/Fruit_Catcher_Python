import pygame

class Score:
    def _init_(self):
        self.score = 0

    def update(self, points):
        self.score += points

    def display(self, screen):
        font = pygame.font.Font(None, 36)
        label = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(label, (10, 10))

    def display_final(self, screen, width, height):
        font = pygame.font.Font(None, 50)
        label = font.render(f"Final Score: {self.score}", True, (0, 255, 0))
        screen.blit(label, (width // 2 - 100, height // 2 - 20))
