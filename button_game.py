import sys,pygame
pygame.init()

background_x=0
background_y=0
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("BUTTON")
star_image = pygame.image.load("star.png").convert_alpha()
exit_image = pygame.image.load("exit.png").convert_alpha()
background_image = pygame.image.load("10.png")
def background(x, y):
    screen.blit(background_image,(x, y))
class button(): # lớp nút
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.click = False
    
    def draw(self):
        action = False
        position = pygame.mouse.get_pos()

        position = pygame.mouse.get_pos()
        #print(position)
        if self.rect.collidepoint(position):
            #print("hover")
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                action = True
                #print("click")
        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
star_button = button(80,200, star_image, 0.5)
exit_button = button(300,200, exit_image, 0.5)

tuong = True
while tuong:
        screen.fill((255,255,255))
        background(background_x,background_y)
        if star_button.draw():
            print("star")
        if exit_button.draw():
            tuong = 0
            print("exit")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tuong = 0
                pygame.quit()
                sys.exit()
        pygame.display.update()
