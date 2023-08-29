import pygame

pygame.init()

width, height = 1280,720
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("My game")
fps =60
clock = pygame.time.Clock()

start = True
while start:
    for event in pygame.event.get():
         if event.type ==pygame.QUIT:
             start = False
             pygame.quit()
    red,green,blue,white = (255,0,0),(0,255,0),(0,0,255),(255,255,255)
    window.fill((white))
    # Shapes
    pygame.draw.polygon(window,red,((491,100),(788,100),(937,357),
                                    (788,614),(491,614),(342,357)))
    pygame.draw.circle(window,green,(640,360),200)
    pygame.draw.line(window,blue,(468,392),(812,392),10)
    pygame.draw.rect(window,blue,(468,307,345,70),border_radius=5)

    # Display
    pygame.display.update()
    clock.tick(fps)
