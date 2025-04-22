import pygame
from AppSetting import GAMENAME, DISPLAYRADIO
from Core.Scene_Manager import SceneManager
from States.Exploration import ExplorationState

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode(DISPLAYRADIO)
    pygame.display.set_caption(GAMENAME)
    clock = pygame.time.Clock()
    dt = 0

    scene_manager = SceneManager()
    scene_manager.push(ExplorationState(scene_manager, screen))

    running = True
    while running:
        # limits FPS to 60
        dt = clock.tick(60) / 1000
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                scene_manager.handle_event(event)

        # RENDER YOUR GAME HERE
        scene_manager.update(dt)
        scene_manager.draw()

        # flip() the display to put your work on screen
        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()