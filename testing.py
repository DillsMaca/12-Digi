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


