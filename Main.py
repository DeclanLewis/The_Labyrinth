# The author of this file is Declan Lewis. Made 15th of december 2023.
# This software will be distributed with a GNU lesser general public license
# Pygame also uses this GNU lesser general public license
import pygame
from Resources import rooms
import random
import webbrowser

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
white = (255, 255, 255)
black = (0, 0, 0)
trapped_chance = 0.005
trapped = False
stuck_in_trap = 5
remove_trap = 1
death_counter = 0
font = pygame.font.SysFont("Times New Roman", 50)
font2 = pygame.font.SysFont("Times New Roman", 30)
open_tutorial = 0



# game loop
run= True
current_room = "main"
rooms[current_room].play_speech()

while run:
    # Check for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update current room and plays the necessary music
    destination = rooms[current_room].get_next_room()

    if destination and destination == "main2":
        if open_tutorial < 1:
            open_tutorial = open_tutorial + 1
            webbrowser.open("https://www.youtube.com/watch?v=gMq55u-2vWs")



    if destination and not destination == "main":
        current_room = destination
        rooms[current_room].start_music()
        rooms[current_room].play_speech()

    # check for death screen, and returns the player back to the main menu
    if destination == "main" and destination:
        open_tutorial = 0
        current_room = destination
        rooms[current_room].start_music()
        death = pygame.mixer.Sound("Sounds/Death.mp3")
        death.play()
        fade()
        death_counter = death_counter + 1
    # This will have a chance to trap the player causing them to die in trapped rooms.
    if random.random() < trapped_chance and current_room == "lab":
        print("trapped")
        stuck_in_trap = stuck_in_trap + 20
        trapped = True
    if random.random() < trapped_chance and current_room == "bunker hatch room":
        print("trapped")
        stuck_in_trap = stuck_in_trap + 20
        trapped = True
    if random.random() < trapped_chance and current_room == "":
        print("trapped")
        stuck_in_trap = stuck_in_trap + 20
        trapped = True
    while trapped:
        while stuck_in_trap >10:
            open_tutorial = 0
            current_room = "main"
            rooms[current_room].start_music()
            death = pygame.mixer.Sound("Sounds/Death.mp3")
            death.play()
            fade()
            stuck_in_trap = stuck_in_trap - 20
            remove_trap = remove_trap + 1
            if remove_trap == 2:
                death_counter = death_counter + 1
                remove_trap = remove_trap - 1
                trapped = False


    # Draws the current room to the screen
    rooms[current_room].draw(screen)

    if current_room == "main" or current_room == "main2":
        text1 = font.render("Times died:" + str(death_counter), 1, white)
        text2 = font2.render("This game is best played with sound", 1, white)
        screen.blit(text1, (900, 100))
        screen.blit(text2, (50, 650))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()