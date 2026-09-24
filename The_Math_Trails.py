
# Importing modules to start pygame
# Importing modules to start pygame
"""import pygame
from pygame.locals import *

print("hello world")

pygame.init()

game_clock = pygame.time.Clock()
fps = 60
# Defining variables
screen_width = 1000
screen_height = 1000

#creating game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Number Trials")

#define game variables
tile_size = 50

#font for menu text
font = pygame.font.SysFont('Times Roman', 40)

#game state: "menu" or "game"
game_state = "menu"

#load images (character and backgrounds)
bg_img = pygame.image.load('img/sky.png')
# Scale image to fill the screen dimensions
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))

#start button setup
button_width = 200
button_height = 60
start_button = pygame.Rect(
    (screen_width // 2) - (button_width // 2),
    (screen_height // 2) - (button_height // 2),
    button_width,
    button_height
)




def draw_menu():
    screen.blit(bg_img, (0, 0))
    pygame.draw.rect(screen, (50, 150, 50), start_button)
    pygame.draw.rect(screen, (255, 255, 255), start_button, 3)
    text_surf = font.render("Start", True, (255, 255, 255))
    text_rect = text_surf.get_rect(center=start_button.center)
    screen.blit(text_surf, text_rect)

#def draw_grid():
    #for line in range(0, 20):
        #pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        #pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'img/guy{num}.png')
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0


    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5

        #get key presses
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.jumped == False:
            self.vel_y = -15
            self.jumped = True
        if not key[pygame.K_UP]:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            self.counter = 0
            self.index = 0
            #self.image = self.images_left[self.index]
            
        #handle animation

        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y


         #check for collision
        for tile in world.tile_list:
            img, img_rect = tile
            if player.rect.colliderect(img_rect):
                self.tile_list.remove(tile)


            #check for collision in x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0

            #check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #check if below the ground (jumping)
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                #check if above the ground (falling)
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0



         #update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0




        #draw player onto screen
        screen.blit(self.image , self.rect)
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)


class World():
    def __init__(self, data):
        self.tile_list = []

        # This line must be indented (pushed to the right)
        # Use an underscore instead of a dot for the variable name
        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grass.png')
        blob_img = pygame.image.load('img/blob.png')
        coin_img = pygame.image.load('img/coin.png')


        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(coin_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    blob = Enemy(col_count * tile_size, row_count * tile_size)
                    blob_group.add(blob)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('img/blob.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

#2d list representing the tile map spatial layout
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
player = Player(100, screen_height - 130)

blob_group = pygame.sprite.Group()

world = World(world_data)

#creating loop so the game keeps running
run = True
while run:

    game_clock.tick(fps)

    if game_state == "menu":
        draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    game_state = "game"

    elif game_state == "game":
        screen.blit(bg_img, (0, 0))

        world.draw()

        player.update()

        #draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.display.update()

pygame.quit()"""

# Importing modules to start pygame
import pygame
from pygame.locals import *
import random

print("hello world")

pygame.init()

game_clock = pygame.time.Clock()
fps = 60
# Defining variables
screen_width = 1000
screen_height = 1000

# creating game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Number Trials")

# define game variables
tile_size = 50

# font for menu text
font = pygame.font.SysFont('Times Roman', 40)

# game state: "menu" or "game"
game_state = "menu"
target_number = 0
user_input = ""

# load images (character and backgrounds)
bg_img = pygame.image.load('img/sky.png')
# Scale image to fill the screen dimensions
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))

# start button setup
button_width = 200
button_height = 60
start_button = pygame.Rect(
    (screen_width // 2) - (button_width // 2),
    (screen_height // 2) - (button_height // 2),
    button_width,
    button_height
)


def draw_menu():
    screen.blit(bg_img, (0, 0))
    pygame.draw.rect(screen, (50, 150, 50), start_button)
    pygame.draw.rect(screen, (255, 255, 255), start_button, 3)
    text_surf = font.render("Start", True, (255, 255, 255))
    text_rect = text_surf.get_rect(center=start_button.center)
    screen.blit(text_surf, text_rect)


class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'img/guy{num}.png')
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.score = 0  # Added tracking for coins picked up

    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5

        # get key presses
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.jumped == False:
            self.vel_y = -15
            self.jumped = True
        if not key[pygame.K_UP]:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            self.counter = 0
            self.index = 0

        # handle animation
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        # add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # --- NEW: SEPARATE COIN PICKUP LOGIC ---
        # Look through a slice copy [:] of the coin list so removal doesn't break the loop
        for tile in world.coin_list[:]:
            img, img_rect = tile
            if self.rect.colliderect(img_rect):
                world.coin_list.remove(tile)
                self.score += 1
                print(f"Coins collected: {self.score}")

                #make the end user choose a random number
                global game_state, target_number, user_input
                target_number = random.randint(1, 100)
                user_input = ""
                game_state = "quiz"


        # --- SOLID TILE BLOCK COLLISION ---
        for tile in world.tile_list:
            img, img_rect = tile
            # check for collision in x direction
            if img_rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0

            # check for collision in y direction
            if img_rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground (jumping)
                if self.vel_y < 0:
                    dy = img_rect.bottom - self.rect.top
                    self.vel_y = 0
                # check if above the ground (falling)
                elif self.vel_y >= 0:
                    dy = img_rect.top - self.rect.bottom
                    self.vel_y = 0

        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0

        # draw player onto screen
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)


class World():
    def __init__(self, data):
        self.tile_list = []
        self.coin_list = []  # Separate list so coins don't act like solid walls

        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grass.png')
        coin_img = pygame.image.load('img/coin.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tile_list.append((img, img_rect))
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tile_list.append((img, img_rect))
                if tile == 4:
                    img = pygame.transform.scale(coin_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.coin_list.append((img, img_rect))  # Save to coin_list
                if tile == 3:
                    blob = Enemy(col_count * tile_size, row_count * tile_size)
                    blob_group.add(blob)
                col_count += 1
            row_count += 1

    def draw(self):
        # Draw solid tiles
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1]) # Fixed: added indexing
            pygame.draw.rect(screen, (255, 255, 255), tile[1], 2) # Fixed: added indexing

        # Draw interactive coins
        for coin in self.coin_list:
            screen.blit(coin[0], coin[1]) # Fixed: added indexing


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/blob.png')  # Changed from self.img to self.image for group compliance
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# 2d list representing the tile map spatial layout
world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

player = Player(100, screen_height - 130)
blob_group = pygame.sprite.Group()
world = World(world_data)

# creating loop so the game keeps running
run = True
while run:

    game_clock.tick(fps)

    if game_state == "menu":
        draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    game_state = "game"
    elif game_state == "game":
        screen.blit(bg_img, (0, 0))
        world.draw()
        blob_group.draw(screen)
        player.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    elif game_state == "quiz":
        draw_quiz()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                # If they hit Backspace, delete the last character
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]

                # If they hit Enter, check if they are right
                elif event.key == pygame.K_RETURN:
                    if user_input == str(target_number):
                        player.score += 1  # Award point only after solving!
                        game_state = "game"  # Go back to platforming

                # Check if the pressed key is a number (0-9)
                elif event.unicode.isdigit():
                    user_input += event.unicode


        # --- MOVE THIS COMPLETELY OUTSIDE THE WHILE LOOP ---
        def draw_quiz():
            screen.blit(bg_img, (0, 0))  # background
            prompt_text = font.render(f"Type a random number 1 - 100: {target_number}", True, (255, 255, 255))
            prompt_rect = prompt_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
            screen.blit(prompt_text, prompt_rect)  # Fixed: changed input_text to prompt_text

            # Fixed: Added missing comma after True
            input_text = font.render(f"Your Answer: {user_input}", True, (255, 255, 0))
            input_rect = input_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
            screen.blit(input_text, input_rect)

            # Guidance text
            help_text = font.render("Press ENTER to submit", True, (200, 200, 200))
            help_rect = help_text.get_rect(center=(screen_width // 2, screen_height // 2 + 150))
            screen.blit(help_text, help_rect)


        screen.blit(help_text, help_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    game_state = "game"

    elif game_state == "game":
        screen.blit(bg_img, (0, 0))
        world.draw()
        blob_group.draw(screen)
        player.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    elif game_state == "quiz":
        # Simply call the function here! It will draw everything we set up above.
        draw_quiz()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]

                elif event.key == pygame.K_RETURN:
                    if user_input == str(target_number):
                        player.score += 1
                        game_state = "game"

                elif event.unicode.isdigit():
                    user_input += event.unicode

    pygame.display.update()

    pygame.quit()

    pygame.display.update()

pygame.quit()

"""import pygame
from pygame.locals import *

pygame.init()

game_clock = pygame.time.Clock()
fps = 60
# Defining variables
screen_width = 1000
screen_height = 1000

#creating game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Number Trials")

#define game variables
tile_size = 50


#load images (character and backgrounds)
bg_img = pygame.image.load('img/sky.png')
# Scale image to fill the screen dimensions
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))

#def draw_grid():
    #for line in range(0, 20):
        #pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        #pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'img/guy{num}.png')
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0


    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5

        #get key presses
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.jumped == False:
            self.vel_y = -15
            self.jumped = True
        if not key[pygame.K_UP]:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            self.counter = 0
            self.index = 0
            #self.image = self.images_left[self.index]


        #handle animation

        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]


        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y


         #check for collision
        for tile in world.tile_list:
            #check for collision in x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0

            #check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #check if below the ground (jumping)
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                #check if above the ground (falling)
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0



         #update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0




        #draw player onto screen
        screen.blit(self.image , self.rect)
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)


class World():
    def __init__(self, data):
        self.tile_list = []

        # This line must be indented (pushed to the right)
        # Use an underscore instead of a dot for the variable name
        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grass.png')
        blob_img = pygame.image.load('img/blob.png')


        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    blob = Enemy(col_count * tile_size, row_count * tile_size)
                    blob_group.add(blob)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('img/blob.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y


world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
player = Player(100, screen_height - 130)

blob_group = pygame.sprite.Group()

world = World(world_data)
#creating loop so the game keeps running
run = True
while run: # == True:

    game_clock.tick(fps)

    screen.blit(bg_img, (0, 0))

    world.draw()

    player.update()

    #draw_grid()


    # adding a way to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()
pygame.quit()"""




