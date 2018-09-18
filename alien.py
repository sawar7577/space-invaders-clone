import pygame
import random
import time

display_width = 800
display_height = 800


class alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('alien.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = random.randint(0, 1) * display_height / 8
        self.rect.left = random.randint(0, 7) * display_width / 8
        self.born = time.time()

    def update(self):
        if self.born + 8 <= time.time():
            self.kill()
            del self
