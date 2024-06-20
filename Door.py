# The author of this file is Declan Lewis. Made 16th of February 2024.
# This software will be distributed with a GNU lesser general public license
# Pygame also uses this GNU lesser general public license

# The library I use to help run the game.
import pygame

class Door:
    def __init__(self, x, y, image, destination, x_transform, y_transform, new_x, new_y):
        # Class initialisation
        self.img = pygame.image.load(image)
        self.img = pygame.transform.scale(self.img,(x_transform, y_transform))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.destination = destination
        self.clicked = False
        self.new_x = new_x
        self.new_y = new_y
        self.old_x = x_transform
        self.old_y = y_transform
        self.rect.topleft = ((((new_x - x_transform)/2) + x), (((new_y - y_transform)/2) + y))
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))
        # gets mouse position
        pos = pygame.mouse.get_pos()

        # check's if mouse is on door
        if self.rect.collidepoint(pos):
            # This will increase the size of the button from the centre
            self.rect.topleft = ((self.x - ((self.new_x - self.old_x) / 2)), ((self. y - (self.new_y - self.old_y) / 2)))
            self.img = pygame.transform.scale(self.img, (self.new_x, self.new_y))

            # sets value to true to load up new room
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
        # Resets self.clicked back to False
        if not pygame.mouse.get_pressed()[0]:
                self.clicked = False

        # Resets the size of the door back to its original
        if not self.rect.collidepoint(pos):
            self.rect.topleft = (self.x, self.y)
            self.img = pygame.transform.scale(self.img, (self.old_x, self.old_y))