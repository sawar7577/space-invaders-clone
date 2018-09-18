import pygame
import time


class missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.left = x
