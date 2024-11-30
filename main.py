import pygame
from basket import Basket
from fruit_bomb_generator import FruitBombGenerator
from collision import check_collisions
from game_timer import GameTimer
from score import Score
import os

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Catcher Pro")

# Colors
BLACK = (0, 0, 0)

# Initialize game components
basket = Basket(WIDTH, HEIGHT)
fruit_bomb_gen = FruitBombGenerator(WIDTH, HEIGHT)
timer = GameTimer(60)  # 60 seconds
score = Score()

clock = pygame.time.Clock()
running = True

# Game Loop
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Basket movement
    basket.move()

    # Generate and move entities
    fruit_bomb_gen.generate_entities()
    fruit_bomb_gen.move_entities()

    # Collision detection
    check_collisions(basket, fruit_bomb_gen, score)

    # Timer update
    if timer.update():
        running = False  # End game when timer reaches zero

    # Draw everything
    basket.draw(screen)
    fruit_bomb_gen.draw_entities(screen)
    score.display(screen)
    timer.display(screen, WIDTH)

    # Update display
    pygame.display.flip()
    clock.tick(30)

# End screen
screen.fill(BLACK)
score.display_final(screen, WIDTH, HEIGHT)
pygame.display.flip()
pygame.time.delay(3000)
pygame.quit()