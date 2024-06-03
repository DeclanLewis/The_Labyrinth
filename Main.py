# The author of this file is Declan Lewis. Made 15th of december 2023.
# This software will be distributed with a GNU lesser general public license
# Pygame also uses this GNU lesser general public license
import pygame
from Resources import rooms
import random
from Door import Door


# fading this fades the screen to black overtime.
def fade():
    fade = pygame.Surface(screen_size)
    fade.fill(black)
    for alpha in range(0, 600):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        death_text = pygame.image.load("Images/Death_text.png")
        screen.blit(death_text, (440, 260))
    pygame.display.update()


#Startup
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("The Labyrinth (I did this cuz dom forced me too)")
fps = 60
screen_size = (1280, 720)
screen = pygame.display.set_mode((1280, 720))
black = (0, 0, 0)
trapped_chance = 0.01
trapped = False
stuck_in_trap = 5
remove_trap = 1
current_room = "main"
# TRAPPED: notifies the player they have been trapped.
trapped_button = Door(440, 260, "images/Trapped.png", current_room, 400, 200, 450, 225)

# game loop
run= True
death_counter = 0
# previous_room = "start"
rooms[current_room].play_speech()

while run:
    # Check for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update current room and plays the necessary music
    destination = rooms[current_room].get_next_room()
    if destination and not destination == "main":
        current_room = destination
        rooms[current_room].start_music()
        rooms[current_room].play_speech()

    # check for death screen, and returns the player back to the main menu
    if destination == "main" and destination:
        current_room = destination
        rooms[current_room].start_music()
        death = pygame.mixer.Sound("Sounds/Death.mp3")
        death.play()
        fade()
        death_counter = death_counter + 1
        print(death_counter)
    # This will have a chance to trap the player causing them to die.
    if random.random() < trapped_chance:
        print("trapped")
        stuck_in_trap = stuck_in_trap + 20
        trapped = True
    else:
        trapped = False
    while trapped:
        trapped_button.draw(screen)
        if destination:
            trapped = False
        pygame.display.update()

    # Draws the current room to the screen
    rooms[current_room].draw(screen)



    pygame.display.flip()
    clock.tick(fps)

pygame.quit()