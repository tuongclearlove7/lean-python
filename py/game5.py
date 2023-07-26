import pygame
pygame.init()

text_color = (255,255,255)
Width = 900
Height = 500
background_1 = 0
background_2 = 0
rocket_1 = 430
rocket_2 = 420
player_1 = 0 # vị trí tên lửa
ufo_1 = 0
ufo_2 = 0
bullet_1 = 0 # vị trí của đạn
bullet_2 = 370
bullet1_change = 10 # tốc độ bắn ngang của đạn (nếu có)
bullet2_change = 1 # tốc độ bắn lên của đạn
bullet_state = "shoot"
# nếu là True thì (hack game) auto bắn k cần nhấn space

screen = pygame.display.set_mode((Width, Height))
background_image = pygame.image.load("11.jpg")
pygame.display.set_caption("game")
icon = pygame.image.load("rocket.png")
font = pygame.font.SysFont('javanesetext', 30)
player_image = pygame.image.load("rocket.png")
ufo_image = pygame.image.load("ufo.png")
bullet_image = pygame.image.load("bullet.png")


def ufo(x, y):
    screen.blit(ufo_image, (x, y))

def rocket(x, y): # tạo hàm rocket để thêm tên lửa vào game 
    screen.blit(player_image, (x, y)) # được truyền vào biến x, y

def fire_bullet(x, y): # tạo hàm fire_bullet để thêm tên đạn vào game
    global bullet_state
    bullet_state = True # True nên (line 73) if bullet_state is True:
    screen.blit(bullet_image, (x+16, y+10))# tọa độ của đạn với tên lửa

tuong = True

while tuong: # vòng lặp 
    
    screen.blit(background_image, (background_1,background_2))
    text = font.render('Hello world',True , text_color)
    pygame.display.set_icon(icon)
    screen.blit(text,(390,-10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tuong = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1 = -2
                # tốc độ bay sang trái của tên lửa
            if event.key == pygame.K_RIGHT:
                player_1 = 2
                # tốc độ bay sang phải của tên lửa
            if event.key == pygame.K_SPACE:
                fire_bullet(rocket_1, bullet_2)

        if event.type == pygame.KEYUP: # xác định vị trí muốn dừng của tên lửa
            if event.key == pygame.K_LEFT:
                player_1 = 0 
            if event.key == pygame.K_RIGHT:
                player_1 = 0

    rocket_1 += player_1
    if rocket_1 <= -15:
        rocket_1 = -15
#vị trí lề trái game mà tên lửa bay tới và đứng lại
    elif rocket_1 >= 850:
        rocket_1 = 850
#vị trí lề phải game mà tên lửa bay tới và đứng lại
    
    if bullet_2 <= 0:
        bullet_2 = 400
        bullet_state = "shoot"
    # nếu là True thì auto bắn k cần nhấn space
    if bullet_state is True:
        fire_bullet(rocket_1, bullet_2)
        bullet_2 -= bullet2_change

    ufo_1 += 0.3 # tốc độ bay sang phải của ufo
    if ufo_1 + 0 > Width:# vị trí bắt đầu bay của ufo_1 bay sang phải
            ufo_1 = Height - 700 
            # vị trí xuất hiện của ufo khi bay hết lề

    rocket(rocket_1, rocket_2)# cho tên lửa vô game
    ufo(ufo_1, ufo_2)
    pygame.display.update()
    print("game đang chạy") # đang trong vòng lặp