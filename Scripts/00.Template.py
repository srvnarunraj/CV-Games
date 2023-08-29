import pygame
# Initialize
pygame.init()

# Create Window/Display
width, height = 1280,720
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("My game")

# Initialize clock for FPS
fps = 120
clock = pygame.time.Clock()

# Main Loop
start = True
while start:
    for event in pygame.event.get():
         if event.type ==pygame.QUIT:
             start = False
             pygame.quit()

    # Apply Logic

    window.fill((255,255,255))

    pygame.display.update()
    clock.tick(fps)

