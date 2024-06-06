# The author of this file is Declan Lewis. Made 15th of december 2023.
# Watched a tutorial on some of this to understand how it works create some myself
# This software will be distributed with a GNU lesser general public license
# Pygame also uses this GNU lesser general public license
# This was an early start to my game figuring out how the game will work

import pygame

pygame.init()

class Button:
    def __init__(self, x, y):
         self.img=B_img
         self.rect=self.img.get_rect()
         self.rect.topleft=(x,y)
         self.clicked=False

    def draw(self):
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked=True
                print("Click")
                if not pygame.mouse.get_pressed()[0]:
                    self.clicked=False

        window.blit(self.img ,(self.rect.x, self.rect.y))

class Button2:
    def __init__(self, x, y):
        self.img=B2_img
        self.rect=self.img.get_rect()
        self.rect.topleft=(x,y)
        self.clicked = False

    def draw(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked=True
                print("Clicked")
                if not pygame.mouse.get_pressed()[0]:
                    self.clicked=False

        window.blit(self.img,(self.rect.x, self.rect.y))

class background:
    def __init__(self, x, y):
        self.img=Background_img
        self.rect=self.img.get_rect()
        self.rect.topleft=(x,y)

    def draw(self):
        window.blit(self.img, (self.rect.x, self.rect.y))

class Door:
    def __init__(self, x, y):
        self.img=D_img
        self.rect=self.img.get_rect()
        self.rect.topleft=(x,y)
        self.clicked = False

    def draw(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                print("Clicky")
                if not pygame.mouse.get_pressed()[0]:
                    self.clicked = False
        window.blit(self.img, (self.rect.x, self.rect.y))


class Background2:

    def __init__(self, x, y):
        self.img = Background2_img
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        window.blit(self.img, (self.rect.x, self.rect.y))



clock=pygame.time.Clock()
FPS=30
white=(255,255,255)
width = 1000
height = 800
window=pygame.display.set_mode((width, height))

B_img=pygame.image.load("download.jpeg")
B_img=pygame.transform.scale(B_img, (100, 100))
B2_img=pygame.image.load("download.jpeg")
B2_img=pygame.transform.scale(B2_img, (100, 100))
Background_img=pygame.image.load("../Images/Backgrounds/StartRoom.jpg")
Background_img=pygame.transform.scale(Background_img, (1000, 800))
D_img=pygame.image.load("../Door2.png")
D_img=pygame.transform.scale(D_img, (70, 80))
Background2_img=pygame.image.load("../Images/Backgrounds/Background_2.jpg")
Background2_img=pygame.transform.scale(Background2_img, (1000, 800))


B=Button(800,400)
B2=Button2(200,50)
Back=Background_img
D = Door(590, 340)
Back2 = Background2_img

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.blit(Back, (0, 0))
    if D.rect.collidepoint(590, 340) == True:
        D.draw()

    if D.clicked == True:
        window.blit(Back2, (0, 0))
        B2.draw()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
