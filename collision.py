import pygame
def check_collisions(basket, fruit_bomb_gen, score):
    basket_rect = basket.get_rect()
    for entity in fruit_bomb_gen.entities[:]:
        entity_rect = pygame.Rect(entity["x"], entity["y"], entity["img"].get_width(), entity["img"].get_height())
        if basket_rect.colliderect(entity_rect):
            if entity["type"] == "bomb":
                score.update(-10)
            elif entity["type"] == "powerup":
                score.time_bonus(5)  # Bonus time
            else:
                score.update(10)
            fruit_bomb_gen.entities.remove(entity)
