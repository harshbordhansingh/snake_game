import pygame
pygame.init()

# creating window screen
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game")

# declaring variables
exit_game = False
game_over = False

# creating a loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("you have pressed the right key")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("you have pressed left arrow key")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("you have pressed up arrow key")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    print("you have pressed down arrow key")
pygame.quit()
quit()