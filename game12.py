import pygame
pygame.init()

text_color = (24,71,133)
text2_color = (223,0,41)

Width = 1330
Height = 700

background_1 = 0
background_2 = 0
background_3 = 1230
background_4 = 0
background_5 = 2660
background_6 = 0

launch_1 = 1150
launch_2 = 630
player_1 = 0 # vị trí tên lửa
ufo_1 = 0
ufo_2 = 0
flag_1 = 1090
flag_2 = 570
flag_vietnam_1 = 225
flag_vietnam_2 = 480
home_1 = 100
home_2 = 500
skyscraper_1 = 0
skyscraper_2 = 400
hospital_1 = 0
hospital_2 = 500
mausoleum_1 = 200
mausoleum_2 = 500
tower_1 = 0
tower_2 = 640
hotel_1 = 200
hotel_2 = 635
motel_1 = 200
motel_2 = 400
telecom_1 = 100
telecom_2 = 400
car_1 = 0
car_2 = 580
oto_1 = 100
oto_2 = 580
yellow_1 = 200
yellow_2 = 580
silver_1 = 100
silver_2 = 650
nui_1 = 450
nui_2 = 430
mountain_1 = 450
mountain_2 = 495
mountain2_1 = 450
mountain2_2 = 300
airport_1 = 325
airport_2 = 573
electric_1 = 290
electric_2 = 500
dien_1 = 370
dien_2 = 500
elec_1 = 445
elec_2 = 500
wire_1 = 410
wire_2 = 483
wire2_1 = 330
wire2_2 = 483
street_1 = 0
street_2 = 610
duong_1 = 30
duong_2 = 610
duong_di_1 = 60
duong_di_2 = 610
street1_1 = 90
street1_2 = 610
street2_1 = 120
street2_2 = 610
street3_1 = 150
street3_2 = 610
street4_1 = 180
street4_2 = 610
street5_1 = 210
street5_2 = 610
street6_1 = 240
street6_2 = 610
street7_1 = 270
street7_2 = 610
street8_1 = 300
street8_2 = 610
street9_1 = 330
street9_2 = 610
street10_1 = 360
street10_2 = 610
street11_1 = 60
street11_2 = 680
street12_1 = 90
street12_2 = 680
street13_1 = 120
street13_2 = 680
street14_1 = 150
street14_2 = 680
street15_1 = 180
street15_2 = 680
street16_1 = 210
street16_2 = 680
street17_1 = 240
street17_2 = 680
street18_1 = 270
street18_2 = 680
street19_1 = 300
street19_2 = 680
tree_1 = 700
tree_2 = 635
tree2_1 = 700
tree2_2 = 570
tree3_1 = 700
tree3_2 = 440
tree4_1 = 800
tree4_2 = 440
tree5_1 = 800
tree5_2 = 570
tree6_1 = 800
tree6_2 = 635
tree7_1 = 630
tree7_2 = 505
tree8_1 = 720
tree8_2 = 505
tree9_1 = 800
tree9_2 = 505
tree10_1 = 400
tree10_2 = 570
people1_1 = 40
people1_2 = 470
people2_1 = 70
people2_2 = 470
people3_1 = 100
people3_2 = 470
people4_1 = 10
people4_2 = 550
people5_1 = 30
people5_2 = 550
people6_1 = 50
people6_2 = 550
people7_1 = 80
people7_2 = 550
people8_1 = 100
people8_2 = 550
people9_1 = 120
people9_2 = 550
people10_1 = 140
people10_2 = 550
people11_1 = 160
people11_2 = 550
cloud_1 = 50
cloud_2 = 250
cloud2_1 = 200
cloud2_2 = 250
cloud3_1 = 350
cloud3_2 = 250
sun_1 = 100
sun_2 = 150
moon_1 = 1330
moon_2 = 100
station_1 = 1050
station_2 = 630
rada_1 = 950
rada_2 = 550
satellite_1 = 950
satellite_2 = 630
plane_1 = 50
plane_2 = 320
vetinh_1 = 1330
vetinh_2 = 70
vetinh2_1 = 1230
vetinh2_2 = 70
traffic_1 = 0
traffic_2 = 590
traffic2_1 = 150
traffic2_2 = 590
traffic3_1 = 300
traffic3_2 = 590
speedometer_1 = 1060
speedometer_2 = 500
thermometer_1 = 10
thermometer_2 = 0
clock_1 = 1060
clock_2 = 460
clock_3 = 13
clock_4 = 40

rocket_1 = 0 # vị trí của đạn
rocket_2 = 600
rocket1_change = 10 # tốc độ bắn ngang của đạn (nếu có)
rocket2_change = 3 # tốc độ bắn lên của đạn
rocket_state = True
# nếu là True thì (hack game) auto bắn k cần nhấn space


screen = pygame.display.set_mode((Width, Height))
background_image = pygame.image.load("anh.png")
background_image2 = pygame.image.load("night1.jpg")
background_image3 = pygame.image.load("anh.png")

pygame.display.set_caption("The universe")
icon = pygame.image.load("launch.png")
font = pygame.font.SysFont('javanesetext', 20)
font2 = pygame.font.SysFont('javanesetext', 30)
font3 = pygame.font.SysFont("javanesetext", 25)
font4 = pygame.font.SysFont("sans", 23)
font5 = pygame.font.SysFont("sans", 20)

sound_game = pygame.mixer.Sound("vippro33.mp3")
sound2_game = pygame.mixer.Sound("vippro33.mp3")

launchers_image = pygame.image.load("station space.png")
ufo_image = pygame.image.load("ufo2.png")
flag_image = pygame.image.load("flag_vietnam.png")
flag_vietnam_image = pygame.image.load("lovevietnam.png")
home_image = pygame.image.load("home.png")
skyscraper_image = pygame.image.load("skyscraper.png")
hospital_image = pygame.image.load("hospital.png")
mausoleum_image = pygame.image.load("mausoleum.png")
tower_image = pygame.image.load("tower.png")
hotel_image = pygame.image.load("hotel.png")
motel_image = pygame.image.load("building.png")
telecom_image = pygame.image.load("telecommunication.png")
car_image = pygame.image.load("car.png")
oto_image = pygame.image.load("car1.png")
yellow_image = pygame.image.load("car3.png")
silver_image = pygame.image.load("car2.png")
nui_image = pygame.image.load("nui2.png")
mountain_image = pygame.image.load("nui.png")
mountain2_image = pygame.image.load("nui.png")
airport_image = pygame.image.load("airport.png")
electric_image = pygame.image.load("electric.png")
dien_image = pygame.image.load("electric.png")
elec_image = pygame.image.load("electric.png")
wire_image = pygame.image.load("wire.png")
wire2_image = pygame.image.load("wire.png")
street_image = pygame.image.load("street2.png")
duong_image = pygame.image.load("street2.png")
duong_di_image = pygame.image.load("street2.png")
street1_image = pygame.image.load("street2.png")
street2_image = pygame.image.load("street2.png")
street3_image = pygame.image.load("street2.png")
street4_image = pygame.image.load("street2.png")
street5_image = pygame.image.load("street2.png")
street6_image = pygame.image.load("street2.png")
street7_image = pygame.image.load("street2.png")
street8_image = pygame.image.load("street2.png")
street9_image = pygame.image.load("street2.png")
street10_image = pygame.image.load("street2.png")
street11_image = pygame.image.load("street2.png")
street12_image = pygame.image.load("street2.png")
street13_image = pygame.image.load("street2.png")
street14_image = pygame.image.load("street2.png")
street15_image = pygame.image.load("street2.png")
street16_image = pygame.image.load("street2.png")
street17_image = pygame.image.load("street2.png")
street18_image = pygame.image.load("street2.png")
street19_image = pygame.image.load("street2.png")
tree_image = pygame.image.load("tree.png")
tree2_image = pygame.image.load("tree.png")
tree3_image = pygame.image.load("tree.png")
tree4_image = pygame.image.load("tree.png")
tree5_image = pygame.image.load("tree.png")
tree6_image = pygame.image.load("tree.png")
tree7_image = pygame.image.load("forest.png")
tree8_image = pygame.image.load("forest.png")
tree9_image = pygame.image.load("forest.png")
tree10_image = pygame.image.load("tree.png")
people1_image = pygame.image.load("people.png")
people2_image = pygame.image.load("people.png")
people3_image = pygame.image.load("people.png")
people4_image = pygame.image.load("people.png")
people5_image = pygame.image.load("people.png")
people6_image = pygame.image.load("people.png")
people7_image = pygame.image.load("people.png")
people8_image = pygame.image.load("people.png")
people9_image = pygame.image.load("people.png")
people10_image = pygame.image.load("people.png")
people11_image = pygame.image.load("people.png")
cloud_image = pygame.image.load("cloud.png")
cloud2_image = pygame.image.load("cloud.png")
cloud3_image = pygame.image.load("cloud.png")
sun_image = pygame.image.load("sunny.png")
moon_image = pygame.image.load("moon.png")
station_image = pygame.image.load("launch.png")
rada_image = pygame.image.load("rada.png")
satellite_image = pygame.image.load("satellite.png")
plane_image = pygame.image.load("planevietnam.png")
vetinh_image = pygame.image.load("vetinh.png")
vetinh2_image = pygame.image.load("vetinh2.png")
traffic_image = pygame.image.load("light.png")
traffic2_image = pygame.image.load("light.png")
traffic3_image = pygame.image.load("light.png")
speedomater_image = pygame.image.load("speedometer.png")
thermometer_image = pygame.image.load("hot.png")
clock_image = pygame.image.load("clock2.png")
clock_image2 = pygame.image.load("clock3.png")

rocket_image = pygame.image.load("rocket2.png")


def background2(x, y):
    screen.blit(background_image2, (x,y))
def background3(x, y):
    screen.blit(background_image3, (x,y))

def launch(x, y): # tạo hàm launch để thêm tên lửa vào game 
    screen.blit(launchers_image, (x, y)) # được truyền vào biến x, y

def fire_rocket(x, y): # tạo hàm fire_rocket để thêm tên đạn vào game
    global rocket_state
    rocket_state = True # True nên (line 73) if rocket_state is True:
    screen.blit(rocket_image, (x+10, y+-20))# tọa độ của đạn với tên lửa
def ufo(x, y):
    screen.blit(ufo_image, (x, y))

def flag(x, y):
    screen.blit(flag_image, (x, y))
def flag_vietnam(x, y):
    screen.blit(flag_vietnam_image, (x, y))

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

def telecom(x, y):
    screen.blit(telecom_image ,(x, y))

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

def mountain2(x, y):
    screen.blit(mountain2_image, (x, y))

def airport(x, y):
    screen.blit(airport_image, (x, y))

def electric(x, y):
    screen.blit(electric_image, (x, y))

def elec(x, y):
    screen.blit(elec_image, (x, y))

def dien(x, y):
    screen.blit(dien_image, (x, y))

def wire(x, y):
    screen.blit(wire_image, (x, y))

def wire2(x, y):
    screen.blit(wire2_image, (x, y))

def street(x, y):
    screen.blit(street_image, (x, y))

def duong(x, y):
    screen.blit(duong_image, (x, y))

def duong_di(x, y):
    screen.blit(duong_di_image, (x, y))

def street1(x, y):
    screen.blit(street1_image, (x, y))

def street2(x, y):
    screen.blit(street2_image, (x, y))

def street3(x, y):
    screen.blit(street3_image, (x, y))

def street4(x, y):
    screen.blit(street4_image, (x, y))

def street5(x, y):
    screen.blit(street5_image, (x, y))

def street6(x, y):
    screen.blit(street6_image, (x, y))

def street7(x, y):
    screen.blit(street7_image, (x, y))

def street8(x, y):
    screen.blit(street8_image, (x, y))

def street9(x, y):
    screen.blit(street9_image, (x, y))

def street10(x, y):
    screen.blit(street10_image, (x, y))

def street11(x, y):
    screen.blit(street11_image, (x, y))

def street12(x, y):
    screen.blit(street12_image, (x, y))

def street13(x, y):
    screen.blit(street13_image, (x, y))

def street14(x, y):
    screen.blit(street14_image, (x, y))

def street15(x, y):
    screen.blit(street15_image, (x, y))

def street16(x, y):
    screen.blit(street16_image, (x, y))

def street17(x, y):
    screen.blit(street17_image, (x, y))

def street18(x, y):
    screen.blit(street18_image, (x, y))

def street19(x, y):
    screen.blit(street19_image, (x, y))

def tree(x, y):
    screen.blit(tree_image, (x, y))

def tree2(x, y):
    screen.blit(tree2_image, (x, y))

def tree3(x, y):
    screen.blit(tree3_image, (x, y))

def tree4(x, y):
    screen.blit(tree4_image, (x, y))

def tree5(x, y):
    screen.blit(tree5_image, (x, y))

def tree6(x, y):
    screen.blit(tree6_image, (x, y))

def tree7(x, y):
    screen.blit(tree7_image, (x, y))

def tree8(x, y):
    screen.blit(tree8_image, (x, y))

def tree9(x, y):
    screen.blit(tree9_image, (x, y))

def tree10(x, y):
    screen.blit(tree10_image, (x+-8, y))

def people1(x, y):
    screen.blit(people1_image, (x, y))
def people2(x, y):
    screen.blit(people2_image, (x, y))
def people3(x, y):
    screen.blit(people3_image, (x, y))
def people4(x, y):
    screen.blit(people4_image, (x, y))
def people5(x, y):
    screen.blit(people5_image, (x, y))
def people6(x, y):
    screen.blit(people6_image, (x, y))
def people7(x, y):
    screen.blit(people7_image, (x, y))
def people8(x, y):
    screen.blit(people8_image, (x, y))
def people9(x, y):
    screen.blit(people9_image, (x, y))
def people10(x, y):
    screen.blit(people10_image, (x, y))
def people11(x, y):
    screen.blit(people11_image, (x, y))

def cloud(x ,y):
    screen.blit(cloud_image, (x, y))
def cloud1(x ,y):
    screen.blit(cloud2_image, (x, y))
def cloud2(x ,y):
    screen.blit(cloud3_image, (x, y))

def sun(x, y):
    screen.blit(sun_image, (x, y))
def moon(x, y):
    screen.blit(moon_image, (x, y))

def station(x, y):
    screen.blit(station_image, (x, y))

def rada(x, y):
    screen.blit(rada_image, (x, y))

def satellite(x, y):
    screen.blit(satellite_image ,(x, y))

def plane(x, y):
    screen.blit(plane_image, (x, y))

def vetinh(x, y):
    screen.blit(vetinh_image, (x,y))
def vetinh2(x, y):
    screen.blit(vetinh2_image, (x,y))

def traffic(x, y):
    screen.blit(traffic_image, (x, y))
def traffic2(x, y):
    screen.blit(traffic2_image, (x, y))
def traffic3(x, y):
    screen.blit(traffic3_image, (x, y))

def speedometer(x,y):
    screen.blit(speedomater_image, (x, y))

def thermometer(x, y):
    screen.blit(thermometer_image, (x, y))

def clock(x, y):
    screen.blit(clock_image, (x, y))
def clock2(x, y):
    screen.blit(clock_image2, (x, y))


tuong = True

while tuong: # vòng lặp
    pygame.mixer.Sound.play(sound2_game)

    screen.blit(background_image, (background_1,background_2))
    text = font.render('km/m : '+str(plane_1*10),True,text_color)
    text_2 = font2.render("Hello Universe", True, text_color)
    text_3 = font3.render("27°C", True, text2_color)
    text_4 = font4.render("7h00pm", True, text2_color)
    text_5 = font5.render("max speed 13300km/4m", True, text_color)

    pygame.display.set_icon(icon)
    screen.blit(text, (1100,500))
    screen.blit(text_2, (550,-10))
    screen.blit(text_3, (45,-10))
    screen.blit(text_4, (50,43))
    screen.blit(text_5, (1100,465))

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
        rocket_2 = 600 # vị trí tên lửa bắn lên
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
    plane_1 += 4
    if plane_1 + 0 > Width:
            plane_1 = Height - 700
    print(plane_1)
    
    car_1 += 4
    if car_1 + 750 > Width:
            car_1 = Height - 700
    oto_1 += 4
    if oto_1 + 750 > Width:
            oto_1 = Height - 700
    yellow_1 += 4
    if yellow_1 + 800 > Width:
            yellow_1 = Height - 700
    silver_1 += 4
    if silver_1 + 950 > Width:
            silver_1 = Height - 650
    sun_1 += 0.4
    if sun_1 + 950> Width:
            sun_1 = Height - 1500
    moon_1 -= 0.8
    if moon_1 + 0 > Width:
            moon_1 = Height - 700
    cloud_1 += 0.4
    if cloud_1 + 980 > Width:
            cloud_1 = Height - 1600
    cloud2_1 += 0.4
    if cloud2_1 + 875 > Width:
            cloud2_1 = Height - 1600
    cloud3_1 += 0.4
    if cloud3_1 + 765 > Width:
            cloud3_1 = Height - 1600
    
    
    vetinh_1 -= 0.8
    if vetinh_1 + 0 > Width:
            vetinh_1 = Height - 300
    vetinh2_1 -= 0.8
    if vetinh2_1 + 0 > Width:
            vetinh2_1 = Height - 300

    background_3 -= 1
    if background_3 + 0 > Width:
            background_3 = Height - 700
    background_5 -= 1
    if background_5 + 0 > Width:
            background_5 = Height - 700

    clock2(clock_3, clock_4)
    clock(clock_1,clock_2)
    thermometer(thermometer_1,thermometer_2)
    speedometer(speedometer_1,speedometer_2)
    #background3(background_5,background_6)
    #background2(background_3, background_4)
    launch(launch_1, launch_2)# cho tên lửa vô game
    ufo(ufo_1, ufo_2)
    flag(flag_1, flag_2)
    flag_vietnam(flag_vietnam_1, flag_vietnam_2)
    home(home_1, home_2)
    skyscraper(skyscraper_1, skyscraper_2)
    hospital(hospital_1, hospital_2)
    mausoleum(mausoleum_1, mausoleum_2)
    tower(tower_1, tower_2)
    hotel(hotel_1, hotel_2)
    motel(motel_1, motel_2)
    telecom(telecom_1, telecom_2)
    street(street_1, street_2)
    duong(duong_1, duong_2)
    duong_di(duong_di_1, duong_di_2)
    street1(street1_1, street1_2)
    street2(street2_1, street2_2)
    street3(street3_1, street3_2)
    street4(street4_1, street4_2)
    street5(street5_1, street5_2)
    street6(street6_1, street6_2)
    street7(street7_1, street7_2)
    street8(street8_1, street8_2)
    street9(street9_1, street9_2)
    street10(street10_1, street10_2)
    street11(street11_1, street11_2)
    street12(street12_1, street12_2)
    street13(street13_1, street13_2)
    street14(street14_1, street14_2)
    street15(street15_1, street15_2)
    street16(street16_1, street16_2)
    street17(street17_1, street17_2)
    street18(street18_1, street18_2)
    street19(street19_1, street18_2)

    car(car_1, car_2)
    oto(oto_1, oto_2)
    yellow(yellow_1, yellow_2)
    silver(silver_1, silver_2)

    mountain2(mountain2_1, mountain2_2)
    tree7(tree7_1, tree7_2)
    nui(nui_1, nui_2)
    mountain(mountain_1, mountain_2)

    tree10(tree10_1, tree10_2)
    airport(airport_1, airport_2)
    electric(electric_1, electric_2)
    wire(wire_1, wire_2)
    wire2(wire2_1, wire2_2)
    elec(elec_1, elec_2)
    dien(dien_1, dien_2)
    tree(tree_1, tree_2)
    tree2(tree2_1, tree2_2)
    tree3(tree3_1, tree3_2)
    tree4(tree4_1, tree4_2)
    tree5(tree5_1, tree5_2)
    tree6(tree6_1, tree6_2)
    tree8(tree8_1, tree8_2)
    tree9(tree9_1, tree9_2)

    people1(people1_1, people1_2)
    people2(people2_1, people2_2)
    people3(people3_1, people3_2)
    people4(people4_1, people4_2)
    people5(people5_1, people5_2)
    people6(people6_1, people6_2)
    people7(people7_1, people7_2)
    people8(people8_1, people8_2)
    people9(people9_1, people9_2)
    people10(people10_1, people10_2)
    people11(people11_1, people11_2)

    cloud(cloud_1, cloud_2)
    cloud1(cloud2_1, cloud2_2)
    cloud2(cloud3_1, cloud3_2)

    sun(sun_1, sun_2)
    moon(moon_1, moon_2)
    station(station_1, station_2)
    rada(rada_1, rada_2)
    satellite(satellite_1, satellite_2)
    plane(plane_1, plane_2)

    vetinh(vetinh_1, vetinh_2)
    vetinh2(vetinh2_1, vetinh2_2)
    traffic(traffic_1, traffic_2)
    traffic2(traffic2_1, traffic2_2)
    traffic3(traffic3_1, traffic3_2)

# nếu in ra fire_rocket(launch_1, rocket_2) ở cuối
# thì tên lửa đè lên 2 backgrounnd và bắn liên tục lên
# còn khi fire_rocket(launch_1, rocket_2) được in dưới
# dòng 576 thì tên lửa bị 2 background đè lên nên k thấy 
# khi đó nhấn space mới thấy tên lửa bắn

    pygame.display.update()
pygame.quit()
     # đang trong vòng lặp
