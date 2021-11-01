import pygame
pygame.init()

Width = 1000
Height = 600
background = (50,50,50)
white = (0,0,0)

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("game")
sprite_image = pygame.image.load("mario.gif").convert_alpha()

def get_image(sheet, ngang, doc, scale,colour):
	image = pygame.Surface((ngang,doc)).convert_alpha()
	image.blit(sheet,(0,0),(0,0,ngang, doc))
	image = pygame.transform.scale(image,(ngang*scale,doc*scale))
	image.set_colorkey(colour)

	return image

frame_0 = get_image(sprite_image,200,200,1,white)

tuong = True
while tuong:
	
	screen.fill(background)
	screen.blit(frame_0, (0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			tuong = False

	pygame.display.update()
pygame.quit()