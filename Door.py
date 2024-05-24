import pygame
class Door:
    def __init__(self, x, y, image, destination, x_transform, y_transform, new_x, new_y):
        # Class initialisation
        self.img = pygame.image.load(image)
        self.img = pygame.transform.smoothscale(self.img, (x_transform, y_transform))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.destination = destination
        self.clicked = False
        self.new_x = new_x
        self.new_y = new_y
        self.old_x = x_transform
        self.old_y = y_transform

    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))
        # gets mouse position
        pos = pygame.mouse.get_pos()

        # check's if mouse is on door
        if self.rect.collidepoint(pos):
            self.img = pygame.transform.smoothscale(self.img, (self.new_x, self.new_y))
            self.img = pygame.transform.scale(self.img, (self.new_x, self.new_y))
            # sets value to true to load up new room
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
        if not pygame.mouse.get_pressed()[0]:
                self.clicked = False

        if not self.rect.collidepoint(pos):
            self.img = pygame.transform.smoothscale(self.img, (self.old_x, self.old_y))







