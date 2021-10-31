from time import sleep
Clearlove = '''┌─────────────────────────────────────────────┐
│          Invite you to play my game         │
├─────────────────────────────────────────────┤
│            [+] Publish 27/10/2021           │
│            [+] By Clearlove7                │
├─────────────────────────────────────────────┤
│                 Game : Plane                │
└─────────────────────────────────────────────┘'''
for c in Clearlove:
    print(c, end="", flush=True)
    sleep(0.001)
print()
print("game đang khởi động vui lòng hãy chờ 1 vài giây")
sleep(1)
cowndown = range(10,110, +10)
for i in range(len(cowndown)):
    print("                       Loading...: ",cowndown[i], end = "")
    print("%")
    sleep(0.2) #Tốc độ loading khi bắt đầu xử lý loading 10 -> 100%    

import pygame, sys
from pygame.locals import *
pygame.init()
background_1 = 0
background_2 = 0
Width = 800
Height = 500
text_color = (255,255,255)
speed = 200
# Xác định speed : tốc độ di chuyển của máy bay 

fpsClock = pygame.time.Clock()
icon = pygame.image.load("plane.png")
screen = pygame.display.set_mode((Width,Height))
background = pygame.image.load("11.jpg")
pygame.display.set_caption('Game move')
font = pygame.font.SysFont('javanesetext', 30)
sound_game = pygame.mixer.Sound("buon.mp3")
class my_plane():
    def __init__(self): #biến face được truyền vào self
        self.Fly = 0 # left Vị trí của máy bay
         
        self.Surface = pygame.image.load('14.png')
    # Tạo biến face và thêm hình chiếc máy bay vào

    def draw(self): # Hàm dùng để vẽ máy bay
        screen.blit(self.Surface, (self.Fly, 150))# top, below
    # Vị trí của máy bay
    
    def update(self, Fly_left, Fly_right): 
    # Hàm dùng để thay đổi vị trí máy bay
        if Fly_left == True:
            self.Fly -= 2 # tốc độ bắt đầu của máy bay

        if Fly_right == True:
            self.Fly += 2 # tốc độ bắt đầu của máy bay

        if self.Fly + 0 > Width:
            self.Fly = Height - 700 
            # vị trí bắt đầu bay của máy bay

plane = my_plane()
Fly_left = False
Fly_right = False

while True: #vòng lặp
    screen.blit(background, (background_1,background_2))
    text = font.render('Welcome My Game',True , text_color)
    screen.blit(text,(270,-15))# in ra chữ trên chương trình game
    pygame.display.set_icon(icon)
    pygame.mixer.Sound.play(sound_game)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
       
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                Fly_left = True
            if event.key == K_RIGHT:
                Fly_right = True
        
        if event.type == KEYUP:
            if event.key == K_LEFT:
                Fly_left = False
            if event.key == K_RIGHT:
                Fly_right = False
    plane.draw()
    plane.update(Fly_left, Fly_right)

    pygame.display.update()
    fpsClock.tick(speed)
    print('game đang chạy') 