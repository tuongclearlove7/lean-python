import pygame
pygame.init()
screen=pygame.display.set_mode((1000,600))
pygame.display.set_caption('dinosaur TUONG')
WHITE=(255,255,255)
RED=(255,0,0)
background_x=0
background_y=0
dinosaur_x=0
dinosaur_y=210
tree_x=950
tree_y=400
x_velocity=3
y_velocity=5
score=0
font=pygame.font.SysFont('san',40)
font1=pygame.font.SysFont('san',60)
background=pygame.image.load('background.jpg')
dinosaur=pygame.image.load('dinosaur.png')
tree=pygame.image.load('tree.png')
sound1=pygame.mixer.Sound('tick.wav')
sound2=pygame.mixer.Sound('te.wav')
clock=pygame.time.Clock()
jump=False
pausing=False
running=True
while running:
	clock.tick(60)
	screen.fill(WHITE)
	background1_rect=screen.blit(background,(background_x,background_y))
	background2_rect=screen.blit(background,(background_x+600,background_y))
	dinosaur_rect=screen.blit(dinosaur,(dinosaur_x,dinosaur_y))
	tree_rect=screen.blit(tree,(tree_x,tree_y))
	score_txt=font.render("Score:"+str(score),True,RED)
	screen.blit(score_txt,(5,5))
	background_x-=x_velocity
	if background_x+600<=0:
		background_x=0
	tree_x-=y_velocity*3/2
	if tree_x<=-40:
		tree_x=950
		score+=1
	if 210>=dinosaur_y>=40:
		if jump==True:
			dinosaur_y-=y_velocity
	else:
		jump=False
	if dinosaur_y<210:
		if jump==False:
			dinosaur_y+=y_velocity

	if dinosaur_rect.colliderect(tree_rect):
		pygame.mixer.Sound.play(sound2)
		pausing=True
		gameover_txt=font1.render("GAME OVER",True,RED)
		screen.blit(score_txt,(200,200))
		x_velocity=0
		y_velocity=0
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_SPACE:
				if dinosaur_y==210:
					pygame.mixer.Sound.play(sound1)
					jump=True
				if pausing:
					background_x=0
					background_y=0
					x_velocity =3
					y_velocity =5
					dinosaur_x=0
					dinosaur_y=210
					tree_x=950
					tree_y=400
					x_vilocity=3
					y_velocity=7
					score=0
					pausing=False

	
	pygame.display.flip()
pygame.quit()


	