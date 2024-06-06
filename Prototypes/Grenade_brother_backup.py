# The author of this file is Declan Lewis. Made 5th of February 2024.
# Tutorial on this if i want to use keyboard things were added on top of the tutorial
# My first backup, i made this when i was stuck in my main project.

import pygame

pygame.init()

SCREEN_WIDTH = (800)
SCREEN_HEIGHT = (600)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player1 = pygame.Rect((150,500,50,50))
player2 = pygame.Rect((650,500,50,50))
ball = pygame.Rect((400,300,10,10))
edge_left = pygame.Rect((20, 20, 20, 560))
edge_right = pygame.Rect((760, 20, 20, 560))
bottom = pygame.Rect((20, 560, 760, 20))

jump = True
run = True
while run:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (225, 0, 0), player1)
    pygame.draw.rect(screen, (0, 0, 225), player2)
    pygame.draw.rect(screen, (0, 225, 0), ball)
    pygame.draw.rect(screen, (255, 255, 255), edge_left)
    pygame.draw.rect(screen, (255, 255, 255), edge_right)
    pygame.draw.rect(screen, (255, 255, 255), bottom)

    key = pygame.key.get_pressed()
    if jump and key[pygame.K_a] == True:
        player1.move_ip(-5, 0)
    elif jump and key[pygame.K_d] == True:
        player1.move_ip(5, 0)

    if jump and key[pygame.K_LEFT] == True:
        player2.move_ip(-5, 0)
    elif jump and key[pygame.K_RIGHT] == True:
        player2.move_ip(5, 0)

    if jump and key[pygame.K_w] == True:
        player1.move_ip(0, -5)
        jump = False

    elif jump == False:
        player1.move_ip(0, 5)
        jump = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

