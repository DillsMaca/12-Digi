import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 400))

def start_the_game():
    # Function to start your actual game logic
    print("Game started!")

menu = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=400
)

menu.add.text_input('Name: ', default='John Doe', maxchar=10)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)



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





"""class World():
    def __init__(self, data):

    #load images
    platform_x.png_img = os.path.join("img", "platform_x.png")"""

class World():
    def __init__(self, data):
        # This line must be indented (pushed to the right)
        # Use an underscore instead of a dot for the variable name
        path = os.path.join("img", "platform_x.png")
        self.platform_x_img = pygame.image.load(path)
