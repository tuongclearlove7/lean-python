import pygame
pygame.init()
Width = 900
Height = 500
rocket_1 = 430
rocket_2 = 420
background_1 = 0
background_2 = 0
text_color = (255,255,255)
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("The universe")
icon = pygame.image.load("rocket.png")
background = pygame.image.load("11.jpg")
sound_game = pygame.mixer.Sound("buon.mp3")
font = pygame.font.SysFont('javanesetext', 30)
rocket_image = pygame.image.load("rocket.png")

def rocket():
    screen.blit(rocket_image, (rocket_1, rocket_2))
tuong = True

while tuong:
    rocket_2 -= 0.15
    screen.blit(background, (background_1,background_2))
    text = font.render('Hello world',True , text_color)
    pygame.display.set_icon(icon)
    screen.blit(text,(390,-10))
    pygame.mixer.Sound.play(sound_game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tuong = False
    
    if rocket_2 <= 0:
        rocket_2 = 0

    elif rocket_2 >= 850:
        rocket_2 = 850
    #vị trí lề trái game mà tên lửa bay tới và đứng lại
    
    rocket()
    pygame.display.update()
    print("The universe is running")
    