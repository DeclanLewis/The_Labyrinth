# The author of this file is Declan Lewis. Made 5th of June 2024.
# This software will be distributed with a GNU lesser general public license
# Pygame also uses this GNU lesser general public license
# the purpose of this was to test for to make a label class worked out for a function to be better

import pygame

pygame.init()
white = (255, 255, 255)
screen = pygame.display.set_mode((1280, 720))
death_counter = 0
font = pygame.font.SysFont("Times New Roman", 50)
text1 = font.render("Times died:"+ str(death_counter), True, white)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(text1, (900, 100))
    pygame.display.flip()

pygame.quit()