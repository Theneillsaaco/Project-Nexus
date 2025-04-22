import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 60)
        self.color = (0, 200, 255)
        self.velocity = pygame.Vector2(0, 0)
        self.on_ground = False
        self.invulnerable = False
        self.invuln_timer = 0
        self.visible = True # para el parpadeo

    def handle_event(self, event):
        pass # El movimiento se maneja por estado de teclado

    def update(self, dt, platforms):
        keys = pygame.key.get_pressed()

        # Movimiento lateteral
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity.x = -200
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity.x = 200
        else:
            self.velocity.x = 0

        # Salto
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]
                or keys[pygame.K_UP]) and self.on_ground:
            self.velocity.y = -400

        # gravedad
        self.velocity.y += 1000 * dt

        # Movimiento horizontal y colisiones
        self.rect.x += int(self.velocity.x * dt)
        self.check_collisions(platforms, horizontal = True)

        # Movimiento vertical y colisiones
        self.rect.y += int(self.velocity.y * dt)
        self.on_ground = False
        self.check_collisions(platforms, horizontal = False)

        # Inmunidad temporal tras combate
        if self.invulnerable:
            self.invuln_timer -= dt

            # Hacer parpadear cada 0.1 segundos
            self.visible = int(self.invuln_timer * 10) % 2 == 0
            if self.invuln_timer <= 0:
                self.invulnerable = False
                self.visible = True


    def check_collisions(self, platforms, horizontal):
        for platform in platforms:
            if self.rect.colliderect(platform):
                if horizontal:
                    if self.velocity.x > 0:
                        self.rect.right = platform.left
                    elif self.velocity.x < 0:
                        self.rect.left = platform.right
                else:
                    if self.velocity.y > 0:
                        self.rect.bottom = platform.top
                        self.velocity.y = 0
                        self.on_ground = True
                    elif self.velocity.y < 0:
                        self.rect.top = platform.bottom
                        self.velocity.y = 0

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.color, self.rect)