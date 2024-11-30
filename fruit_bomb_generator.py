import pygame
import random
import os

class FruitBombGenerator:
    def _init_(self, width, height):
        self.fruit_imgs = [
            pygame.image.load(os.path.join("assets", f"fruit{i}.png")).convert_alpha()
            for i in range(1, 4)
        ]
        self.bomb_img = pygame.image.load(os.path.join("assets", "bomb.png")).convert_alpha()
        self.powerup_img = pygame.image.load(os.path.join("assets", "powerup.png")).convert_alpha()
        self.width = width
        self.height = height
        self.entities = []

    def generate_entities(self):
        if random.randint(1, 30) == 1:
            self.entities.append({"type": "fruit", "img": random.choice(self.fruit_imgs), "x": random.randint(0, self.width - 40), "y": 0})
        if random.randint(1, 50) == 1:
            self.entities.append({"type": "bomb", "img": self.bomb_img, "x": random.randint(0, self.width - 40), "y": 0})
        if random.randint(1, 200) == 1:
            self.entities.append({"type": "powerup", "img": self.powerup_img, "x": random.randint(0, self.width - 30), "y": 0})

    def move_entities(self):
        for entity in self.entities:
            entity["y"] += 5 if entity["type"] == "fruit" else 7

    def draw_entities(self, screen):
        for entity in self.entities:
            screen.blit(entity["img"], (entity["x"], entity["y"]))
