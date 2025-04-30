import pygame
import abc
from AppSetting import INVULNERABLETIMER

class BattleState(abc.ABC):
    def __init__(self, scene_manager, screen):
        self.scene_manager = scene_manager
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 32)
        self.timer = 0
        self.finished = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.finished:
                self.scene_manager.pop()
                previous_state = self.scene_manager.scenes[-1]
                previous_state.player.invulnerable = True
                previous_state.player.invuln_timer = INVULNERABLETIMER

    def update(self, dt):
        self.timer += dt
        self.update_logic(dt)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_ui()
        self.draw_enemy_attack()

        if self.finished:
            text = self.font.render("Pulsa Enter para salir", True, (255, 255, 255))
            self.screen.blit(text, (220, 550))

    @abc.abstractmethod
    def updaye_logic(self, dt):
        """ Logica de combate especifica del enemigo"""
        pass

    @abc.abstractmethod
    def draw_enemy_attack(self):
        """ Dibuja patron de ataque del enemigo"""

    def draw_ui(self):
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(250, 480, 300, 100), 2)


