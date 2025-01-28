import pygame
import random
import time

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 102)
PURPLE = (138, 43, 226)

# Define display width and height
WIDTH = 800
HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Quirky Snake Game')

# Set the clock
clock = pygame.time.Clock()

# Define snake block size
snake_block = 20
snake_speed = 15

# Font for messages
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, YELLOW)
    screen.blit(value, [0, 0])

def gameLoop():
    game_over = False
    game_close = False

    # Initial snake position
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    # Initial snake movement
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_List = []
    Length_of_snake = 1

    # Random position for the food
    foodx = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # If snake hits the wall
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)

        # Draw food
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])

        # Snake body movement
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # If snake collides with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw snake
        for block in snake_List:
            pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

        your_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        # Control the snake speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
