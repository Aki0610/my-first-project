import pygame
pygame.init()
x = 600
y = 600

scrn = pygame.display.set_mode((x,y))

pygame.display.set_caption('image')

imp = pygame.image.load("C:\\Users\\Karuna\\Projects\\spaceship.png").convert_alpha()

scrn.blit(imp,(0,0))

pygame.display.flip()
status =  True
while(status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False

pygame.quit()
