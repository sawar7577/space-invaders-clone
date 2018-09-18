import pygame
import random
import os
import time

display_width = 800
display_height = 800


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('rocket.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = display_height
        self.rect.left = 0

    def update(self, x_change):
        self.rect.left += x_change
        if self.rect.left >= display_width:
            self.rect.left = display_width - display_width / 8
        if self.rect.left + display_width / 8 <= 0:
            self.rect.left = 0
