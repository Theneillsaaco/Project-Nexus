import pygame
from AppSetting import GAMENAME, DISPLAYRADIO

# pygame setup
pygame.init()
screen = pygame.display.set_mode(DISPLAYRADIO)
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption(GAMENAME)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()