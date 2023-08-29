import pygame

pygame.init()

width, height = 1280,720
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("My game")
fps =60
clock = pygame.time.Clock()

# Load images
bgimg = pygame.image.load("../Resources/img.png").convert()
balloonimg = pygame.image.load("../Resources/img2.png").convert_alpha()
# Scale the image to fit the window
bgimg = pygame.transform.scale(bgimg, (width, height))

# balloonimg = pygame.transform.rotozoom(balloonimg,90,0.3)
balloonimg = pygame.transform.smoothscale(balloonimg,(100,200))

start = True
while start:
    for event in pygame.event.get():
         if event.type ==pygame.QUIT:
             start = False
             pygame.quit()

    window.blit(bgimg,(0,0))
    window.blit(balloonimg,(110,110))

    pygame.display.update()
    clock.tick(fps)

