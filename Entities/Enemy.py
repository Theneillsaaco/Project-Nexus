import pygame
import pygame.draw

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill((255, 60, 60))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.vx = 0
        self.vy = 0
        self.speed = 100  # Velocidad base del enemigo

        self.max_hp = 100
        self.hp = self.max_hp

    def update(self, dt):
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        print("Enemigo derrotado")
        self.kill()  # Quita el sprite del grupo

    def ai_behavior(self, player):
        if player.rect.x < self.rect.x:
            self.vx = -self.speed
        else:
            self.vx = self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Ejemplo de uso (fuera de la clase):

# Crear grupo de enemigos
enemies = pygame.sprite.Group()
enemies.add(Enemy(100, 200))

# En tu bucle principal de juego:
# enemies.update(dt)
# enemies.draw(screen)


