import math
import sys
import numpy as np
import pygame
from pygame.locals import *

#Set up pygame
pygame.init()

#Set up the window
screen = pygame.display.set_mode((500, 500), 0 , 32)
pygame.display.set_caption('POV Simulator')

#Set up the colors
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)


def rotate(point, cx, cy, angle):
    px, py = point
    angle = math.radians(angle)
    s = math.sin(angle)
    c = math.cos(angle)
    # // translate point back to origin:
    px -= cx
    py -= cy

    # // rotate point
    xnew = px * c - py * s
    ynew = px * s + py * c

    # // translate point back:
    px = xnew + cx
    py = ynew + cy
    return px, py


colors = []

image = pygame.image.load('image.png')
pixels_array = pygame.PixelArray(image)
pixels = np.array(pixels_array)
pixels_array.close()


angle = 0

cx = 250
cy = 250 

sx = 10
gap = 5

step_size = 30
speed = 360 / step_size


leds = [RED] * 20

positions = [None] * len(leds)
x = 250
for i, c in enumerate(leds):
    positions[i] = [x, cy]
    x += sx + gap


surf = pygame.Surface((500, 500))
surf.set_alpha(128)
rect = surf.get_rect(center=(cx, cy))

clock = pygame.time.Clock()

#Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    angle = (angle + step_size) % 360 + 5

    # screen.blit(image, (0, 0))

    surf.fill(WHITE)
    surf.set_alpha(200)

    for i, c in enumerate(leds):
        x, y = rotate(positions[i], cx, cy, angle)
        x, y = int(x), int(y)
        if x < 500 and y < 500 and x > 0 and y > 0:
            pass
            color = image.get_at((x, y))
            # color = RED
            pygame.draw.circle(surf, color, (x, y), 7, 0)

    screen.blit(surf, rect)

    pygame.draw.circle(screen, WHITE, (cx, cy), 3, 0)

    #Draw the window onto the screen
    pygame.display.flip()

    print(clock.get_fps())
    clock.tick(60)
