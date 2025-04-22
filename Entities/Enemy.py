import pygame

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 60)
        self.color = (255, 60, 60)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)