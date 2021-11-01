import pygame

class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(sheet, frame, ngang, doc, scale, colour):
		image = pygame.Surface((ngang, doc)).convert_alpha()
		image.blit(sheet, (0,0), ((frame*ngang),0, ngang,doc))
		image = pygame.transform.scale(image, (ngang*scale, doc*scale))
		image.set_colorkey(colour)
		
		return image