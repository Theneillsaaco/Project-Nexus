import pygame
from AppSetting import (
    PLAYER_MAX_HEALTH,
    BATTLE_BOX_Y,
    BATTLE_BOX_HEIGHT,
    BATTLE_BOX_X,
)


class HUD:
    def __init__(self, player):
        self.player = player

    def draw(self, screen):
        bar_x = BATTLE_BOX_X + 50
        bar_y = BATTLE_BOX_Y + BATTLE_BOX_HEIGHT + 20
        bar_width = 200
        bar_height = 20
        fill = (self.player.health / PLAYER_MAX_HEALTH) * bar_width

        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, fill, bar_height))
