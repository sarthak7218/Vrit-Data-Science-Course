import pygame
import time

# Initialize Pygame
pygame.init()

# Set the width and height of the game window
window_width = 800
window_height = 600

# Set the colors (RGB format)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set the clock to control the game's FPS (Frames Per Second)
clock = pygame.time.Clock()

# Set the size of the snake's segments and the speed of the snake
segment_size = 20
snake_speed = 20

# Define the font for displaying the game over message
font_style = pygame.font.SysFont(None, 50)

# Define a function to display the game over message
def display_game_over_message():
    message = font_style.render("Game Over!", True, red)
    window.blit(message, [window_width/2 - 100, window_height/2])

# Define the main game loop
def game_loop():
    game_over = False
    game_exit = False

    # Initial position of the snake
    x1 = window_width / 2
    y1 = window_height / 2

    # Movement of the snake
    x1_change = 0
    y1_change = 0

    # Main game loop
    while not game_exit:
        while game_over:
            window.fill(black)
            display_game_over_message()
            pygame.display.update()

            # Wait for the player to press any key to restart the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -segment_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = segment_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -segment_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = segment_size
                    x1_change = 0

        # Check if the snake hits the boundaries of the window
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, white, [x1, y1, segment_size, segment_size])
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()


 