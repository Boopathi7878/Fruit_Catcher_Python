import pygame
import os

class Basket:
    def _init_(self, width, height):
        self.image = pygame.image.load(os.path.join("assets", "basket.png"))
        self.image = pygame.transform.scale(self.image, (80, 50))
        self.x = width // 2
        self.y = height - 60
        self.speed = 10
        self.width = width

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < self.width - 80:
            self.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
