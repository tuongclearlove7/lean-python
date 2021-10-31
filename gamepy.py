import pygame
pygame.init()
width = 700
height = 500
background_color = (192,192,192)
text_color = (255,255,255)
background_1 = 0
background_2 = 0
air_1 = 5
air_2 = 150
pygame.display.set_caption('Game')
screen=pygame.display.set_mode((width, height))
font = pygame.font.SysFont('javanesetext', 20)
background = pygame.image.load("11.jpg")
sound_game = pygame.mixer.Sound("xedap.mp3")
air = pygame.image.load("14.png")
tuong = True
while tuong:
    screen.fill(background_color)
    screen.blit(background, (background_1,background_2))
    pygame.mixer.Sound.play(sound_game)
    text = font.render('Hello world',True , text_color)
    screen.blit(text,(310,-5))
    screen.blit(air,(air_1, air_2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tuong = False
    pygame.display.flip()
pygame.quit() 

	