import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)

# Set game window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Set up the display
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Create clock object
clock = pygame.time.Clock()

# Define fonts
font_style = pygame.font.SysFont(None, 35)

def message(msg, color, y_displace=0):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [WINDOW_WIDTH // 6, WINDOW_HEIGHT // 3 + y_displace])

def game_loop():
    # Initial game conditions
    game_over = False
    game_close = False

    # Snake initial position and size
    x = WINDOW_WIDTH // 2
    y = WINDOW_HEIGHT // 2
    x_change = 0
    y_change = 0
    snake_list = []
    snake_length = 1

    # Initial food position
    food_x = round(random.randrange(0, WINDOW_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, WINDOW_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    # Main game loop
    while not game_over:

        # Display game over options
        while game_close:
            game_window.fill(BLACK)
            message("Game Over!", RED, -50)
            message("Press P to Play Again", WHITE, 0)
            message("Press Q to Quit", WHITE, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        # Handle keypresses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = SNAKE_BLOCK
                    x_change = 0

        # Update snake's position
        if x >= WINDOW_WIDTH or x < 0 or y >= WINDOW_HEIGHT or y < 0:
            game_close = True
        x += x_change
        y += y_change

        # Refresh game window
        game_window.fill(BLACK)

        # Draw food
        pygame.draw.rect(game_window, GREEN, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

        # Update snake's head and body
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw snake
        for segment in snake_list:
            pygame.draw.rect(game_window, WHITE, [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])

        # Update display
        pygame.display.update()

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WINDOW_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            food_y = round(random.randrange(0, WINDOW_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            snake_length += 1

        # Control the speed of the snake
        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Start the game
game_loop()


