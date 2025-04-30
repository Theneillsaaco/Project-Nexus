import pygame
from AppSetting import PLAYER_MAX_HEALTH


class HUD:
    def __init__(self, player):
        self.player = player
        self.bar_width = 200
        self.bar_height = 20
        self.pos = (20, 20)

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), (*self.pos, self.bar_width, self.bar_height))
        pygame.draw.rect(screen, (255, 0, 0), (*self.pos, self.bar_width, self.bar_height))
        current_width = int(self.bar_width * self.player.health / PLAYER_MAX_HEALTH)
        pygame.draw.rect(screen, (0, 255, 0), (*self.pos, current_width, self.bar_height))