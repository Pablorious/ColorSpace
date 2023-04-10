import random
import pygame
import math
from math import sqrt, pow
pygame.init()
screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)

running = True

def random_color(l_min,l_max):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    l = sqrt(0.299 * pow((r/255),2) + 0.587 * pow((g/255),2) + 0.114 * pow((b/255),2))
    while l < l_min or l > l_max:
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        l = sqrt(0.299 * pow((r/255),2) + 0.587 * pow((g/255),2) + 0.114 * pow((b/255),2))
    return (r,g,b)

def random_pos(canvas):
    return (random.randint(0,canvas.get_width()),random.randint(0,canvas.get_height()))

def add_stars(canvas):
    for i in range(0,200):
        size = pow(random.randint(0,8),0.33333)
        if size == 0:
            screen.set_at(random_pos(screen),random_color(0.1,0.4))
        else:
            pygame.draw.circle(screen, random_color(0.1+size/5,0.4+size/5),random_pos(screen),size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                add_stars(screen)
            if event.key == pygame.K_s:
                pygame.image.save(screen, "starsurf.png")
            if event.key == pygame.K_c:
                screen.fill((0,0,0))
    pygame.display.update()


