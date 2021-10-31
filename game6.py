import pygame
pygame.init()

text_color = (255,255,255)
Width = 1320
Height = 600
background_1 = 0
background_2 = 0
launch_1 = 1050
launch_2 = 530
player_1 = 0 # vị trí tên lửa
ufo_1 = 0
ufo_2 = 0
flag_1 = 950
flag_2 = 530
home_1 = 100
home_2 = 400
skyscraper_1 = 0
skyscraper_2 = 300
hospital_1 = 0
hospital_2 = 400
mausoleum_1 = 200
mausoleum_2 = 400
tower_1 = 0
tower_2 = 530
hotel_1 = 200
hotel_2 = 530
motel_1 = 200
motel_2 = 300
car_1 = 0
car_2 = 470
oto_1 = 100
oto_2 = 470
yellow_1 = 200
yellow_2 = 470
silver_1 = 100
silver_2 = 550
nui_1 = 450
nui_2 = 230
mountain_1 = 450
mountain_2 = 390
airport_1 = 310
airport_2 = 465
electric_1 = 300
electric_2 = 365
dien_1 = 380
dien_2 = 365
street_1 = 0
street_2 = 500
rocket_1 = 0 # vị trí của đạn
rocket_2 = 370
rocket1_change = 10 # tốc độ bắn ngang của đạn (nếu có)
rocket2_change = 2 # tốc độ bắn lên của đạn
rocket_state = True
# nếu là True thì (hack game) auto bắn k cần nhấn space

screen = pygame.display.set_mode((Width, Height))
background_image = pygame.image.load("11.jpg")
pygame.display.set_caption("The universe")
icon = pygame.image.load("launch.png")
font = pygame.font.SysFont('javanesetext', 30)
launchers_image = pygame.image.load("launch.png")
ufo_image = pygame.image.load("ufo.png")
flag_image = pygame.image.load("flag_vietnam.png")
home_image = pygame.image.load("home.png")
skyscraper_image = pygame.image.load("skyscraper.png")
hospital_image = pygame.image.load("hospital.png")
mausoleum_image = pygame.image.load("mausoleum.png")
tower_image = pygame.image.load("tower.png")
hotel_image = pygame.image.load("hotel.png")
motel_image = pygame.image.load("building.png")
car_image = pygame.image.load("car.png")
oto_image = pygame.image.load("car1.png")
yellow_image = pygame.image.load("car3.png")
silver_image = pygame.image.load("car2.png")
nui_image = pygame.image.load("nui2.png")
mountain_image = pygame.image.load("nui.png")
airport_image = pygame.image.load("airport.png")
electric_image = pygame.image.load("electric.png")
dien_image = pygame.image.load("electric.png")
street_image = pygame.image.load("street2.png")
rocket_image = pygame.image.load("startup.png")


def launch(x, y): # tạo hàm launch để thêm tên lửa vào game 
    screen.blit(launchers_image, (x, y)) # được truyền vào biến x, y

def fire_rocket(x, y): # tạo hàm fire_rocket để thêm tên đạn vào game
    global rocket_state
    rocket_state = True # True nên (line 73) if rocket_state is True:
    screen.blit(rocket_image, (x+-5, y+-20))# tọa độ của đạn với tên lửa
def ufo(x, y):
    screen.blit(ufo_image, (x, y))

def flag(x, y):
    screen.blit(flag_image, (x, y))

def home(x, y):
    screen.blit(home_image, (x, y))

def skyscraper(x, y):
    screen.blit(skyscraper_image, (x, y))

def hospital(x, y):
    screen.blit(hospital_image, (x, y))

def mausoleum(x, y):
    screen.blit(mausoleum_image ,(x, y))

def tower(x, y):
    screen.blit(tower_image ,(x, y))

def hotel(x, y):
    screen.blit(hotel_image ,(x, y))

def motel(x, y):
    screen.blit(motel_image ,(x, y))

def car(x, y):
    screen.blit(car_image, (x, y))

def oto(x, y):
    screen.blit(oto_image, (x, y))

def yellow(x, y):
    screen.blit(yellow_image, (x, y))

def silver(x, y):
    screen.blit(silver_image, (x, y))

def nui(x,y):
    screen.blit(nui_image, (x, y))

def mountain(x, y):
    screen.blit(mountain_image, (x, y))

def airport(x, y):
    screen.blit(airport_image, (x, y))

def electric(x, y):
    screen.blit(electric_image, (x, y))

def dien(x, y):
    screen.blit(dien_image, (x, y))

def street(x, y):
    screen.blit(street_image, (x, y))




tuong = True

while tuong: # vòng lặp 
    
    screen.blit(background_image, (background_1,background_2))
    text = font.render('Hello Universe',True , text_color)
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
                fire_rocket(launch_1, rocket_2)

        if event.type == pygame.KEYUP: # xác định vị trí muốn dừng của tên lửa
            if event.key == pygame.K_LEFT:
                player_1 = 0 
            if event.key == pygame.K_RIGHT:
                player_1 = 0

    launch_1 += player_1
    if launch_1 <= -15:
        launch_1 = -15
#vị trí lề trái game mà tên lửa bay tới và đứng lại
    elif launch_1 >= 1260:
        launch_1 = 1260
#vị trí lề phải game mà tên lửa bay tới và đứng lại
    
    if rocket_2 <= 0:
        rocket_2 = 530 # vị trí tên lửa bắn lên
        rocket_state = True
    # nếu là True thì auto bắn k cần nhấn space
    if rocket_state is True:
        fire_rocket(launch_1, rocket_2)
        rocket_2 -= rocket2_change
    if rocket_2 <= 0:
        rocket_2 = 0

    elif rocket_2 >= 850:
        rocket_2 = 850
    #vị trí lề trái game mà tên lửa bay tới và đứng lại

    ufo_1 += 4 # tốc độ bay sang phải của ufo
    if ufo_1 + 0 > Width:# vị trí bắt đầu bay của ufo_1 bay sang phải
            ufo_1 = Height - 700 
            # vị trí xuất hiện của ufo khi bay hết lề

    launch(launch_1, launch_2)# cho tên lửa vô game
    ufo(ufo_1, ufo_2)
    flag(flag_1, flag_2)
    home(home_1, home_2)
    skyscraper(skyscraper_1, skyscraper_2)
    hospital(hospital_1, hospital_2)
    mausoleum(mausoleum_1, mausoleum_2)
    tower(tower_1, tower_2)
    hotel(hotel_1, hotel_2)
    motel(motel_1, motel_2)
    street(street_1, street_2)
    car(car_1, car_2)
    oto(oto_1, oto_2)
    yellow(yellow_1, yellow_2)
    silver(silver_1, silver_2)
    nui(nui_1, nui_2)
    mountain(mountain_1,mountain_2)
    airport(airport_1, airport_2)
    electric(electric_1, electric_2)
    dien(dien_1, dien_2)
    
    pygame.display.update()
     # đang trong vòng lặp