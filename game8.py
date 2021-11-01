import pygame, sys
from pygame.locals import*
pygame.init()

Width = 800
Height = 600
background_1 = 0
background_2 = 0
mario_1 = 100
mario_2 = 100
size_mario_1 = 100
size_mario_2 = 100


screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("game")
background = pygame.image.load("11.jpg")
mario_image = pygame.image.load("mario.gif")
mario_image = pygame.transform.scale(mario_image,(size_mario_1, size_mario_2))

def mario(x,y):
    screen.blit(mario_image, (x, y))
tuong = True
while tuong:

    screen.blit(background, (background_1,background_2))

    for event in pygame.event.get():
        if event.type == QUIT:
            tuong = False
            pygame.quit()
            sys.exit()

    mario(mario_1, mario_2)
    pygame.display.update()
