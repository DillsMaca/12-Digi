
# Importing modules to start pygame
import pygame
from pygame.locals import *

pygame.init()

# Defining variables
screen_width = 1000
screen_height = 1000

#creating game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Number Trials")

#define game variables
tile_size = 200


#load images (character and backgrounds)
bg_img = pygame.image.load('img/sky.png')
# Scale image to fill the screen dimensions
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))

def draw_grid():
    for line in range(0, 6):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


#class World():
    #def __init__(self, data):

    #load images
    #platform_img = pygame.image.load("img/platform.png")

world_data = [
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 1],
]
#creating loop so the game keeps running
run = True
while run: # == True:

    draw_grid()
    # adding a way to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        screen.blit(bg_img, (0, 0))

    pygame.display.update()
pygame.quit()


