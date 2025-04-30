import pygame
from Entities.Player import Player
from Entities.Enemy import Enemy
from States.Battles.BattleSlime import BattleSlime
from Ui.HUD import HUD


class ExplorationState:
    def __init__(self, scene_manager, screen):
        self.scene_manager = scene_manager
        self.screen = screen
        self.player = Player(100, 400)
        self.enemy = Enemy(600, 400)
        self.platforms = [pygame.Rect(0, 500, 800, 100)]  # suelo
        self.hud = HUD(self.player)

    def handle_event(self, event):
        self.player.handle_event(event)

    def update(self, dt):
        self.player.update(dt, self.platforms)

        if self.player.rect.colliderect(self.enemy.rect) and not self.player.invulnerable:
            self.scene_manager.push(BattleSlime(self.scene_manager, self.screen))

    def draw(self):
        self.screen.fill((30, 30, 30))
        for platform in self.platforms:
            pygame.draw.rect(self.screen, (100, 100, 100), platform)
        self.enemy.draw(self.screen)
        self.player.draw(self.screen)
        self.hud.draw(self.screen)