import pygame

class BattleState:
    def __init__(self, scene_manager, screen):
        self.scene_manager = scene_manager
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 40)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                print("Saliendo del combate")
                self.scene_manager.pop()
                previous_state = self.scene_manager.scenes[-1]
                previous_state.player.invulnerable = True
                previous_state.player.invuln_timer = 5.0

    def update(self, dt):
        pass

    def draw(self):
        self.screen.fill((150, 0, 0))
        text = self.font.render("Modo Batalla - Pulsa Enter para salir", True, (255, 255, 255))
        self.screen.blit(text, (100, 280))