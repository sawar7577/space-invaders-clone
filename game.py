import pygame
import random
import os
import time
from alien import *
from ghost import *
from missile import *
from bullet import *
from bomb import *
from player import *

display_width = 800
display_height = 800
fps = 60

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("my game")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
running = True

# Groups
players = pygame.sprite.Group()
missiles = pygame.sprite.Group()
ghosts = pygame.sprite.Group()
aliens = pygame.sprite.Group()

player = Player()
players.add(player)
a = alien()
aliens.add(a)
t = time.time()
deaths = 0


while running:
    clock.tick(fps)
    x_change = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = - display_width / 8

            elif event.key == pygame.K_d:
                x_change = display_width / 8

            elif event.key == pygame.K_s:
                mis = bullet(player.rect.left, player.rect.top)
                missiles.add(mis)

            elif event.key == pygame.K_SPACE:
                mis = bomb(player.rect.left, player.rect.top)
                missiles.add(mis)

            elif event.key == pygame.K_q:
                running = False

    player.update(x_change)
    if t + 10 <= time.time():
        a = alien()
        t = time.time()
        aliens.add(a)

    for goli in missiles:
        try:
            if type(goli) is bullet:
                if goli.rect.bottom <= a.rect.bottom and goli.rect.left == a.rect.left:
                    b = ghost(a.rect.left, a.rect.bottom)
                    ghosts.add(b)
                    a.kill()
                    del a
                    goli.kill()
                    deaths += 1
                    break

            elif goli.rect.bottom == a.rect.bottom and goli.rect.left == a.rect.left:
                a.kill()
                del a
                goli.kill()
                deaths += 1
                break
        except:
            pass

    screen.fill(BLACK)
    ghosts.update()
    missiles.update()
    aliens.update()

    players.draw(screen)
    missiles.draw(screen)
    ghosts.draw(screen)
    aliens.draw(screen)

    text = font.render("Score: " + str(deaths), True, WHITE)
    screen.blit(text, [10, 10])
    pygame.display.flip()

pygame.quit()
