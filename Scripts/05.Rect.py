"""
Rect

    Can detect Collisions
    Can access x and y points

    Two ways of creating a rect
    1. pygame.Rect(x, y, width, height)
    2. surface.get_rect()  # creates rect around a surface/image
"""

# Import
import pygame

# Initialize
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")

# Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

# Load Images
imgBackground = pygame.image.load("../Resources/img.png").convert()
imgBalloonRed = pygame.image.load("../Resources/img2.png").convert_alpha()

# Transform Images
imgBackground = pygame.transform.smoothscale(imgBackground,(width,height))
imgBalloonRed = pygame.transform.smoothscale(imgBalloonRed,(100,200))

# Rect
rectBalloon = imgBalloonRed.get_rect()

# Main loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
    rectBalloon.x += 2

    window.blit(imgBackground, (0, 0))
    pygame.draw.rect(window, (0, 255, 0), rectBalloon)
    window.blit(imgBalloonRed, rectBalloon)

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)