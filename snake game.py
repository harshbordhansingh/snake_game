import pygame
import random

pygame.init()

# colours
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 128, 0)
screen_width = 900
screen_height = 600

# generating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# game title
pygame.display.set_caption("Snakes With Me")
pygame.display.update()

# game specific variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0

food_x = random.randint(20, screen_width / 2)
food_y = random.randint(20, screen_height / 2)
food_size = 20
snake_size = 30
init_velocity = 5
score = 0
fps = 60
snake_list = []
snake_length = 1

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0
            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0
            if event.key == pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x = 0

    snake_x += velocity_x
    snake_y += velocity_y

    if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:
        score += 1
        food_x = random.randint(20, screen_width / 2)
        food_y = random.randint(20, screen_height / 2)
        snake_length += 3
    gameWindow.fill(white)
    text_screen("Score :" + str(score * 10), green, 5, 5)

    pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])

    head = [snake_x, snake_y]
    snake_list.append(head)
    if len(snake_list) > snake_length:
        del snake_list[0]
    plot_snake(gameWindow, black, snake_list, snake_size)
    clock.tick(fps)
    pygame.display.update()
pygame.quit()
quit()
