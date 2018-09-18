import pygame
import time

display_width = 800
display_height = 800


class ghost(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('ghost.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.left = x
        self.born = time.time()

    def update(self):
        if self.born + 5 <= time.time():
            self.kill()
            del self
