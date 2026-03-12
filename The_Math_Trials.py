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


#load images (character and backgrounds)
bg_img = pygame.image.load('img/sky.png')
sun_img = pygame.image.load('img/sun.png')


#creating loop so the game keeps running
run = True
while run == True:

    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (100, 100))
#adding a way to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
