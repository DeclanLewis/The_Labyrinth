import pygame


    for generator in self.generator:
        generator.draw(screen)


    def generator_pop_up(self):

        for generator in self.generator:
            if generator.clicked:
                generator.clicked = False
                return generator.test
        return None


class Generator():
    def __init__(self, image1, x, y, new_x, new_y, state):
        self.img = pygame.image.load(image1)
        self.img = pygame.transform.smoothscale(self.img, (new_x, new_y))
        self.x = x
        self.y = y
        self.new_x = new_x
        self.new_y = new_y
        self.state = state
        self. clicked = False


    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))






