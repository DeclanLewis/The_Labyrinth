import pygame
from Resources import rooms


# fading this fades the screen to black overtime.
def fade():
    fade = pygame.Surface((1280, 720))
    fade.fill(black)
    for alpha in range(0, 600):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        death_text = pygame.image.load("Images/Death_text.png")
        screen.blit(death_text, (440, 260))
    if range == 600:
        pygame.display.update()

#Startup
pygame.init()
clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode((1280, 720))
black = (0, 0, 0)

# game loop
run= True
current_room = "main"
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

    # Draws the current room to the screen
    rooms[current_room].draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()