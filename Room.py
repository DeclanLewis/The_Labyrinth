# The author of this file is Declan Lewis. Made 16th of February 2024.
# This software will be distributed with a GNU lesser general public license
# Pygame also uses this GNU lesser general public license

import pygame

class Room:
    def __init__(self, image, list_of_doors, music, speech):

        # Class initialisation
        self.BG = pygame.image.load(image)
        self.BG = pygame.transform.smoothscale(self.BG, (1280, 720))
        self.doors = list_of_doors
        self.music = music
        pygame.mixer.init()
        self.speech = speech

    def draw(self, screen):

        # Draws the room and doors to the screen
        screen.blit(self.BG, (0, 0))
        for door in self.doors:
            door.draw(screen)

    def start_music(self):
        # stops than starts the music from the given resource file
        pygame.mixer.stop()
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)
        return True

    def play_speech(self):
        # plays the speech given from the resources file
        speech = pygame.mixer.Sound(self.speech)
        speech.stop()
        speech.play()
        return True

    def stop_speech(self):
        # stops the speech given from the resources file
        speech = pygame.mixer.Sound(self.speech)
        speech.stop()

    def get_next_room(self):

        # a loop to get the correct amount of doors and return what doors
        for door in self.doors:
            if door.clicked:
                door.clicked = False
                return door.destination
        return None