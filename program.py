import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Snake settings
BLOCK_SIZE = 20
SPEED = 10

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 30)


# Score display
def show_score(score):
    text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )
    screen.blit(text, (10, 10))


# Draw snake
def draw_snake(snake):
    for x, y in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            [x, y, BLOCK_SIZE, BLOCK_SIZE]
        )


# Main game function
def game():

    game_over = False
    close_game = False

    x = WIDTH // 2
    y = HEIGHT // 2

    x_change = 0
    y_change = 0

    snake = []
    snake_length = 1


    # Food position
    food_x = random.randrange(
        0,
        WIDTH - BLOCK_SIZE,
        BLOCK_SIZE
    )

    food_y = random.randrange(
        0,
        HEIGHT - BLOCK_SIZE,
        BLOCK_SIZE
    )


    while not game_over:

        while close_game:

            screen.fill(BLACK)

            msg = font.render(
                "Game Over! C=Restart Q=Quit",
                True,
                RED
            )

            screen.blit(
                msg,
                (100, HEIGHT//2)
            )

            show_score(snake_length - 1)

            pygame.display.update()


            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    # Restart
                    if event.key == pygame.K_c:
                        game()

                    # Quit
                    if event.key == pygame.K_q:
                        game_over = True
                        close_game = False


        # Events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0

                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0

                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0

                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0


        # Boundary collision
        if (
            x >= WIDTH or
            x < 0 or
            y >= HEIGHT or
            y < 0
        ):
            close_game = True


        x += x_change
        y += y_change


        screen.fill(BLACK)


        # Draw food
        pygame.draw.rect(
            screen,
            RED,
            [
                food_x,
                food_y,
                BLOCK_SIZE,
                BLOCK_SIZE
            ]
        )


        # Snake head
        head = []
        head.append(x)
        head.append(y)

        snake.append(head)


        if len(snake) > snake_length:
            del snake[0]


        # Self collision
        for part in snake[:-1]:
            if part == head:
                close_game = True


        draw_snake(snake)

        show_score(snake_length - 1)


        pygame.display.update()


        # Food eaten
        if x == food_x and y == food_y:

            food_x = random.randrange(
                0,
                WIDTH - BLOCK_SIZE,
                BLOCK_SIZE
            )

            food_y = random.randrange(
                0,
                HEIGHT - BLOCK_SIZE,
                BLOCK_SIZE
            )

            snake_length += 1


        clock.tick(SPEED)


    pygame.quit()
    quit()


# Start game
game()