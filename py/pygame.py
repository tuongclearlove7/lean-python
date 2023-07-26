import pygame
import array as arr
import random
pygame.init()

width = 1200
height = 600
clock = pygame.time.Clock()
window = (width,height)
win = pygame.display.set_mode(window)
backGround = pygame.image.load('space_background.png')
icon = pygame.image.load('space_ship.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('SPACE_____INVADER')
game_run = True
life = 3
heart = pygame.image.load('heart.png')

space_ship = pygame.image.load('space_ship(64).png')
shipX = 500
shipY = 500
velShipX = 0
slideX = False
velShipY = 0
slideY = False
speed_ship = 10

lazer = pygame.image.load('lazer.png')
lazerX = arr.array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
lazerY = arr.array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
speed_lazer = 10
num_of_lazer = -1
speed_shot = 0
count_lazer = 0
fire = False

ufo = pygame.image.load('ufo.png')
ufoX = arr.array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
ufoY = arr.array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
speed_ufo = 2
num_of_ufo = -1
count_ufo = 0
count_shot = arr.array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

def lazerMove():
    global num_of_lazer,lazerY,lazerX
    for i in range(0,num_of_lazer+1):
        lazerY[i] -= speed_lazer
def checkOutLazer():
    global lazerY,num_of_lazer
    if lazerY[0] < -8:
        for i in range(0,num_of_lazer):
            lazerY[i] = lazerY[i+1]
            lazerX[i] = lazerX[i+1]
        if num_of_lazer >0:
            num_of_lazer -= 1
        else: num_of_lazer = 0
def ufoMove():
    global ufoY,num_of_ufo
    for i in range(0,num_of_ufo+1):
        ufoY[i] += speed_ufo
def ufoCheckOut():
    global ufoX,ufoY,num_of_ufo,life
    if ufoY[0] > height:
        for i in range(0,num_of_ufo):
            ufoY[i]=ufoY[i+1]
            ufoX[i]=ufoX[i+1]
        num_of_ufo -= 1
        life -= 1
def ufoCheckTouch_lazer():
    global lazerX,lazerY,ufoX,ufoY,num_of_ufo,num_of_lazer
    for i in range(0,num_of_ufo+1):
        for j in range(0,num_of_lazer+1):
            if lazerY[j]>ufoY[i] and lazerY[j]<ufoY[i]+48 and lazerX[j]>ufoX[i] and lazerX[j]<ufoX[i]+64:
                count_shot[i]+=1
                for k in range(0,num_of_lazer):
                    lazerY[k] = lazerY[k+1]
                    lazerX[k] = lazerX[k+1]
                if num_of_lazer >0:
                    num_of_lazer -= 1
                else: num_of_lazer = 0
    for i in range(0,num_of_ufo):
        if count_shot[i]>=10:
            for j in range(i,num_of_ufo):
                count_shot[j] = count_shot[j+1]
            for j in range(i,num_of_ufo):
                ufoY[j]=ufoY[j+1]
                ufoX[j]=ufoX[j+1]
            num_of_ufo -= 1   
def ufoCheckTouch_lose():
    global shipX,shipY,num_of_ufo,ufoX,ufoY,life
    for i in range(0,num_of_ufo+1):
        if (ufoX[i]>shipX and ufoX[i]<shipX+64 and ufoY[i]>shipY and ufoY[i]<shipY+64) or (ufoX[i]+64>shipX and ufoX[i]+64<shipX+64 and ufoY[i]+64>shipY and ufoY[i]+64<shipY+64):
            for j in range(i,num_of_ufo):
                ufoY[j]=ufoY[j+1]
                ufoX[j]=ufoX[j+1]
            num_of_ufo -= 1
            life -= 1
def Inputkey():
    global game_run
    global velShipX,velShipY
    global lazerX,lazerY,num_of_lazer,speed_shot,fire
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if ((event.key == pygame.K_w) or (event.key == pygame.K_UP)):
                velShipY = -speed_ship
            if ((event.key == pygame.K_s) or (event.key == pygame.K_DOWN)):
                velShipY = speed_ship
            if (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                velShipX = -speed_ship
            if (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                velShipX = speed_ship
            if event.key == pygame.K_SPACE:
                speed_shot = 1
                fire = True

        if event.type == pygame.KEYUP:
            if  (event.key == pygame.K_a) or (event.key == pygame.K_LEFT) or (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                velShipX = 0
            if (event.key == pygame.K_w) or (event.key == pygame.K_UP) or (event.key == pygame.K_s) or (event.key == pygame.K_DOWN):
                velShipY = 0
            if event.key == pygame.K_SPACE:
                speed_shot = 0
def Logic():
    global shipX,shipY,velShipY,velShipX
    shipX += velShipX
    shipY += velShipY
    if shipX < 0:
        shipX = 0
    if shipX > width-64:
        shipX = width-64
    if shipY < 0:
        shipY = 0
    if shipY > height-64:
        shipY = height-64

    global speed_shot,num_of_lazer,lazerX,lazerY,count_lazer
    if speed_shot == 1 and count_lazer >= 4:
        num_of_lazer += speed_shot
        lazerX[num_of_lazer] = shipX + 28
        lazerY[num_of_lazer] = shipY - 20
        count_lazer = 0
    else: count_lazer +=1
    lazerMove()
    checkOutLazer()

    global speed_ufo,num_of_ufo,count_ufo
    if count_ufo>=100:
        num_of_ufo+=1
        ufoX[num_of_ufo] = random.randint(0,width-64)
        ufoY[num_of_ufo] = -64
        count_ufo = 0
        count_shot[num_of_ufo] = 0
    else: count_ufo+=1
    ufoMove()
    ufoCheckOut()
    ufoCheckTouch_lazer()
    ufoCheckTouch_lose()
    if life < 1:
        pygame.quit()

def Draw():
    win.blit(space_ship,(shipX,shipY))
    if fire:
        for i in range(0,num_of_lazer+1):
            win.blit(lazer,(lazerX[i],lazerY[i]))
    for i in range(0,num_of_ufo+1):
        win.blit(ufo,(ufoX[i],ufoY[i]))
    for i in range(1,life+1):
        win.blit(heart,(i*35,5))

while game_run:
    win.blit(backGround,(0,0))
    Inputkey()
    Logic()
    Draw()
    pygame.display.update()
    clock.tick(60)