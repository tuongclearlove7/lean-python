import pygame
pygame.init()

text_color = (255,255,255)
Width = 500
Height = 500
background_1 = 0
background_2 = 0
character_1 = 400
character_2 = 200
player_1 = 0 # vị trí character
player_2 = 0
size_character_1 = 100
size_character_2 = 100
FPS = 1000000


screen = pygame.display.set_mode((Width, Height))
fpsClock  = pygame.time.Clock()
pygame.display.set_caption("game")
icon = pygame.image.load("clearlove7.png")
background = pygame.image.load("clearlove7.png")
font = pygame.font.SysFont('javanesetext', 30)
font2 = pygame.font.SysFont('javanesetext',30)
character_image = pygame.image.load("dude.gif")
character_image = pygame.transform.scale(character_image,(size_character_1, size_character_2))

def character(x, y): # tạo hàm character để thêm nhân vật vào game 
    screen.blit(character_image, (x, y)) # được truyền vào biến x, y

tuong = True

while tuong: # vòng lặp 
    
    screen.blit(background, (background_1,background_2))
    text = font.render('Hello world',True , text_color)

    pygame.display.set_icon(icon)
    screen.blit(text,(180,-10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tuong = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1 = -1
                print('left')
                # tốc độ bắt đầu đi sang trái của nhân vật
            if event.key == pygame.K_RIGHT:
                player_1 = 1
                print("right")
                # tốc độ bắt đầu đi sang phải của nhân vật
            if event.key == pygame.K_UP:
                player_2 = -1
                print("up")
            # tốc độ bắt đầu đi lên của nhân vật
            if event.key == pygame.K_DOWN:
                player_2 = 1
                print("down")
            # tốc độ bắt đầu đi xuống của nhân vật
            

        if event.type == pygame.KEYUP: # xác định vị trí muốn dừng của tên lửa
            if event.key == pygame.K_LEFT:
                player_1 = 0
            if event.key == pygame.K_RIGHT:
                player_1 = 0
            if event.key == pygame.K_DOWN:
                player_2 = 0
            if event.key == pygame.K_UP:
                player_2 = 0
            

    character_1 += player_1
    if character_1 <= -12:
        character_1 = -12
#vị trí lề trái game mà nhân vật đi tới và đứng lại
    elif character_1 >= 840:
        character_1 = 840
#vị trí lề phải game mà nhân vật đi tới và đứng lại

    character_2 += player_2
    if character_2 <= -15:
        character_2 = -15
#vị trí lề trên game mà nhân vật đi tới và đứng lại
    elif character_2 >= 415:
        character_2 = 415
#vị trí lề dưới game mà nhân vật đi tới và đứng lại



    character(character_1, character_2)# cho nhân vật vô game
    print(character_1,character_2)
    fpsClock.tick(FPS)
    pygame.display.update()

    # đang trong vòng lặp 


    