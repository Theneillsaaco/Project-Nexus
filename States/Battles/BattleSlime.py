import pygame.draw
import pygame

from States.Battles.Core.Battle import BattleState


class BattleSlime(BattleState):
    def __init__(self, scene_manager, screen):
        super().__init__(scene_manager, screen)
        self.box_x = 250
        self.box_y = 480
        self.player_rect = pygame.Rect(370, 530, 20, 20)
        self.projectiles = [pygame.Rect(250 + i * 40, 480, 10, 10) for i in range(5)]

    def update_logic(self, dt):
        for proj in self.projectiles:
            proj.y += 200 * dt
        self.projectiles = [p for p in self.projectiles if p.y < 580]

        for p in self.projectiles:
            if self.player_rect.colliderect(p):
                print("Golpeado!")

        if self.timer > 5:
            self.finished = True

    def draw_enemy_attack(self):
        pygame.draw.rect(self.screen, (255, 255, 0), self.player_rect)
        for proj in self.projectiles:
            pygame.draw.rect(self.screen, (255, 0, 0), proj)