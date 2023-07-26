import pygame
pygame.init()
Width = 700
Height = 500
plane_1 = 0
plane_2 = 150
background_1 = 0
background_2 = 0
text_color = (255,255,255)
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("game")
icon = pygame.image.load("ari.png")
background = pygame.image.load("9.jpg")
sound_game = pygame.mixer.Sound("buon.mp3")
font = pygame.font.SysFont('javanesetext', 30)
player_image = pygame.image.load("14.gif")

def plane():
    screen.blit(player_image, (plane_1, plane_2))
tuong = True

while tuong:
    screen.blit(background, (background_1,background_2))
    text = font.render('Hello world',True , text_color)
    pygame.display.set_icon(icon)
    screen.blit(text,(285,-10))
    pygame.mixer.Sound.play(sound_game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tuong = False
    plane()
    pygame.display.update()
    
    

   

