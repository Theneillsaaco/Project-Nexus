from time import sleep
import pygame.draw
import pygame
from AppSetting import (
    INVULNERABLETIMER,
    ENEMYSLIME_DAMAGE,
    BATTLE_BOX_X,
    BATTLE_BOX_Y,
    BATTLE_BOX_WIDTH,
)
from States.Battles.Core.Battle import BattleState

class BattleSlime(BattleState):
    def __init__(self, scene_manager, screen, hud):
        super().__init__(scene_manager, screen, hud)
        self.invulnerable = False
        self.invuln_timer = 0
        self.projectiles = []

    def update_logic(self, dt):
        for proj in self.projectiles:
            proj.y += 200 * dt
        self.projectiles = [p for p in self.projectiles if p.y < 580]

        for p in self.projectiles:
            if self.player_rect.colliderect(p):
                self.apply_damage(ENEMYSLIME_DAMAGE)

        if self.invulnerable:
            self.invuln_timer -= dt
            if self.invuln_timer <= 0:
                self.invulnerable = False

        if self.timer > 5:
            self.finished = True

    def start_enemy_turn(self):
        # projectiles del slime
        self.projectiles = [pygame.Rect(
            BATTLE_BOX_X + 30 + i * 50,
            BATTLE_BOX_Y + 10,
            10, 10
        ) for i in range(5)]

    def draw_enemy_attack(self):
        pygame.draw.rect(self.screen, (255, 255, 0), self.player_rect)
        for proj in self.projectiles:
            pygame.draw.rect(self.screen, (255, 0, 0), proj)

    def draw_enemy(self):
        slime_width = 50
        slime_height = 50

        x = BATTLE_BOX_X + (BATTLE_BOX_WIDTH - slime_width) // 2
        y = BATTLE_BOX_Y - slime_height - 20

        slime_rect = pygame.Rect(x, y, slime_width, slime_height)
        pygame.draw.ellipse(self.screen, (0, 200, 0), slime_rect)

        """slime_rect = pygame.Rect(300, 100, 50,50)
        pygame.draw.ellipse(self.screen, (0, 200, 0), slime_rect)"""
