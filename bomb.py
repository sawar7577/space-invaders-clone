import pygame
import time
from missile import *

display_width = 800
display_height = 800
fps = 60


class bomb(missile):
    def __init__(self, x, y):
        self.image = pygame.image.load('bomb.png').convert_alpha()
        super().__init__(x, y)

    def update(self):
        self.rect.top -= (display_height / 8) / fps
        if self.rect.bottom <= 0:
            self.kill()
