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

bullet_1 = 0 # vị trí của đạn
bullet_2 = 370
bullet1_change = 0 # tốc độ bắn ngang của đạn (nếu có)
bullet2_change = 3 # tốc độ bắn lên của đạn
bullet_state = "start" 
# nếu là True thì auto bắn k cần nhấn space

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("game")
icon = pygame.image.load("ari.png")
background = pygame.image.load("9.jpg")
font = pygame.font.SysFont('javanesetext', 30)
player_image = pygame.image.load("rocket.png")
bullet_image = pygame.image.load("bullet.png")

def rocket(x, y): # tạo hàm rocket để thêm tên lửa vào game 
    screen.blit(player_image, (x, y)) # được truyền vào biến x, y

def fire_bullet(x, y): # tạo hàm fire_bullet để thêm tên đạn vào game
    global bullet_state
    bullet_state = True # True nên (line 73) if bullet_state is True:
    screen.blit(bullet_image, (x+15, y+10))# tọa độ của đạn với tên lửa

tuong = True

while tuong: # vòng lặp 
    
    screen.blit(background, (background_1,background_2))
    text = font.render('Hello world',True , text_color)
    pygame.display.set_icon(icon)
    screen.blit(text,(390,-10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tuong = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1 = -5
                # tốc độ bay sang trái của tên lửa
            if event.key == pygame.K_RIGHT:
                player_1 = 5
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
        bullet_state = "start"
    # nếu là True thì auto bắn k cần nhấn space
    if bullet_state is True:
        fire_bullet(rocket_1, bullet_2)
        bullet_2 -= bullet2_change 

    rocket(rocket_1, rocket_2)# cho tên lửa vô game
    pygame.display.update()
    print("game đang chạy") # đang trong vòng lặp 

