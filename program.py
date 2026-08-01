import pygame
import random
import os

pygame.init()

# Screen
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Professional Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 30)

BLOCK = 20


# High Score
def get_high_score():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as f:
            return int(f.read())
    return 0


def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))


# Text Display
def text(msg, color, x, y):
    value = font.render(msg, True, color)
    screen.blit(value, (x, y))


# Draw Snake
def draw_snake(snake):
    for x, y in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            [x, y, BLOCK, BLOCK]
        )


# Start Menu
def menu():

    while True:

        screen.fill(BLACK)

        text(
            "SNAKE GAME",
            GREEN,
            210,
            80
        )

        text(
            "Press ENTER to Start",
            WHITE,
            150,
            170
        )

        text(
            "Press Q to Exit",
            WHITE,
            180,
            220
        )

        pygame.display.update()


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    return

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()



# Choose Level
def choose_level():

    while True:

        screen.fill(BLACK)

        text(
            "Choose Level",
            BLUE,
            200,
            80
        )

        text(
            "1 Easy",
            WHITE,
            220,
            150
        )

        text(
            "2 Medium",
            WHITE,
            220,
            200
        )

        text(
            "3 Hard",
            WHITE,
            220,
            250
        )

        pygame.display.update()


        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    return 5

                if event.key == pygame.K_2:
                    return 10

                if event.key == pygame.K_3:
                    return 20



# Main Game
def game(speed):

    x = WIDTH//2
    y = HEIGHT//2

    dx = 0
    dy = 0


    snake = []
    length = 1


    food_x = random.randrange(
        0,
        WIDTH-BLOCK,
        BLOCK
    )

    food_y = random.randrange(
        0,
        HEIGHT-BLOCK,
        BLOCK
    )


    pause = False

    high_score = get_high_score()


    running = True


    while running:


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_LEFT:
                    dx = -BLOCK
                    dy = 0


                elif event.key == pygame.K_RIGHT:
                    dx = BLOCK
                    dy = 0


                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -BLOCK


                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = BLOCK


                elif event.key == pygame.K_SPACE:
                    pause = not pause



        if pause:
            text(
                "PAUSED",
                BLUE,
                250,
                180
            )

            pygame.display.update()
            continue



        x += dx
        y += dy



        # Wall Collision
        if (
            x < 0 or
            x >= WIDTH or
            y < 0 or
            y >= HEIGHT
        ):
            break



        screen.fill(BLACK)



        pygame.draw.rect(
            screen,
            RED,
            [
                food_x,
                food_y,
                BLOCK,
                BLOCK
            ]
        )



        head = [x,y]

        snake.append(head)


        if len(snake) > length:
            snake.pop(0)



        # Self Collision
        if head in snake[:-1]:
            break



        draw_snake(snake)



        score = length-1


        text(
            "Score: "+str(score),
            WHITE,
            10,
            10
        )


        text(
            "High: "+str(high_score),
            WHITE,
            400,
            10
        )


        pygame.display.update()



        # Eat Food
        if x == food_x and y == food_y:

            length += 1

            if score > high_score:
                save_high_score(score)


            food_x = random.randrange(
                0,
                WIDTH-BLOCK,
                BLOCK
            )

            food_y = random.randrange(
                0,
                HEIGHT-BLOCK,
                BLOCK
            )


        clock.tick(speed)



    # Game Over
    screen.fill(BLACK)

    text(
        "GAME OVER",
        RED,
        220,
        150
    )

    text(
        "Press R Restart",
        WHITE,
        180,
        220
    )

    pygame.display.update()



    while True:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    game(speed)

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()



# Start Program

menu()

level_speed = choose_level()

game(level_speed)