import pygame
import settings
import entity
import os

class Player(entity.Entity):
    def __init__(self):
        image_path = os.path.abspath("/Users/sateya2022/Desktop/bibo8/images/cars/car_purple.png")
        super().__init__(60, 0.5, image_path, settings.SPEED * 4)
        self.rect.center = (settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 100)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.MOVEMENT_SPEED, 0)
        if pressed[pygame.K_RIGHT] and self.rect.right < settings.SCREEN_WIDTH:
            self.rect.move_ip(self.MOVEMENT_SPEED, 0)
