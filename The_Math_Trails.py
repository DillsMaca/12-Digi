"""
import pygame
import pygame_menu
# Initialize Pygame
pygame.init()
# Screen dimensions
WIDTH = 1080
HEIGHT = 1920
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #
pygame.display.set_caption("The Number Trials")

# Colours (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# I will define more colours when I need it

# This controls the framerate and helps with concistency over all devices
clock = pygame.time.Clock()
FPS = 60

# Font setup
font = pygame.font.SysFont(None, 40)

# game state value
game_state = "START_SCREEN"

"""
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

#creating loop so the game keeps running
run = True
while run == True:
#adding a way to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
    pygame.display.update()
pygame.quit()