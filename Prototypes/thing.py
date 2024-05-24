class Room:
    def __init__(self, image, Door1, Door1_height, Door1_width, Door2, Door2_height, Door2_width, Door3, Door3_height, Door3_width):
        self.BG = pygame.image.load(image)
        self.BG = pygame.transform.scale(self.BG, (1280, 720))
        self.Door1 = pygame.image.load(Door1)
        self.Door1 = pygame.transform.scale(self.Door1,  (Door1_height, Door1_width))
        self.Door2 = pygame.image.load(Door2)
        self.Door2 = pygame.transform.scale(self.Door2, (Door2_height, Door2_width))
        self.Door3 = pygame.image.load(Door3)
        self.Door3 = pygame.transform.scale(self.Door3, (Door3_height, Door3_width))
    def draw(self, screen):
        screen.blit(self.BG, (0, 0))


