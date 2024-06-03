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
    def __init__(self, image1, x, y, new_x, new_y):
        self.img = pygame.image.load(image1)
        self.img = pygame.transform.smoothscale(self.img, (new_x, new_y))
        self.x = x
        self.y = y
        self.new_x = new_x  
        self.new_y = new_y
        self.state = False
        self. clicked = False


    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))





        while stuck_in_trap >10:
            current_room = "main"
            rooms[current_room].start_music()
            death = pygame.mixer.Sound("Sounds/Death.mp3")
            death.play()
            fade()
            stuck_in_trap = stuck_in_trap - 20
            remove_trap = remove_trap + 1
            if remove_trap == 2:
                death_counter = death_counter + 1
                print(death_counter)
                remove_trap = remove_trap - 1
                trapped = False
