import pygame
import abc
from AppSetting import (
    INVULNERABLETIMER,
    BATTLE_BOX_WIDTH,
    BATTLE_BOX_X, PLAYER_SIZE,
    BATTLE_BOX_Y,
    BATTLE_BOX_HEIGHT
)
from States.Battles.Core.BattleMenu import BattleMenu


class BattleState(abc.ABC):
    def __init__(self, scene_manager, screen, hud):
        self.scene_manager = scene_manager
        self.screen = screen
        self.hud = hud

        self.font = pygame.font.SysFont("Arial", 32)
        self.timer = 0
        self.finished = False

        self.phase = "menu"
        self.menu = BattleMenu(["FIGHT", "ACT", "ITEM", "MERCY"], self.font)

        self.enemy_turn_started = False

        self.player_rect = pygame.Rect(
            BATTLE_BOX_X + BATTLE_BOX_WIDTH // 2,
            BATTLE_BOX_Y + BATTLE_BOX_HEIGHT // 2,
            PLAYER_SIZE, PLAYER_SIZE
        )

    def handle_event(self, event):
        if self.phase == "menu":
            action = self.menu.handle_event(event)
            if action:
                self.handle_menu_selection(action)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.finished:
                self.scene_manager.pop()

        """if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.finished:
                self.scene_manager.pop()"""

    def handle_menu_selection(self, action):
        if action == "FIGHT":
            # Implementacion de la subfase de ataque
            print("FIGHT seleccionado")
            self.phase = "enemy_turn" # Salta al turno del enemigo
        elif action == "ACT":
            print("ACT seleccionado")
            self.phase = "enemy_turn"
        elif action == "ITEM":
            print("ITEM seleccionado")
            self.phase = "enemy_turn"
        elif action == "MERCY":
            print("MERCY seleccionado")
            self.phase = "enemy_turn"

    def handle_player_movement(self, dt):
        keys = pygame.key.get_pressed()
        speed = 150
        dx = dy = 0

        # Keys del movimiento
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= speed * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += speed * dt
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= speed * dt
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += speed * dt

        self.player_rect.x += int(dx)
        self.player_rect.y += int(dy)

        # Limiter del area de combate
        self.player_rect.clamp_ip(pygame.Rect(BATTLE_BOX_X,
                                              BATTLE_BOX_Y,
                                              BATTLE_BOX_WIDTH,
                                              BATTLE_BOX_HEIGHT))

    def update(self, dt):
        if self.phase == "enemy_turn":
            if not self.enemy_turn_started:
                self.start_enemy_turn()
                self.enemy_turn_started = True

            self.timer += dt
            self.handle_player_movement(dt)
            self.update_logic(dt)

            if self.finished:
                self.phase = "menu"
                self.timer = 0
                self.finished = False
                self.enemy_turn_started = False


    def apply_damage(self, amount):
        if not self.invulnerable:
            self.hud.player.health -= amount
            self.invulnerable = True
            self.invuln_timer = INVULNERABLETIMER

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (255, 255, 255), (BATTLE_BOX_X, BATTLE_BOX_Y,
                                                        BATTLE_BOX_WIDTH, BATTLE_BOX_HEIGHT), 2)
        pygame.draw.rect(self.screen, (255, 255, 0), self.player_rect)

        self.draw_enemy()
        self.draw_enemy_attack()

        if self.hud:
            self.hud.draw(self.screen)

        if self.phase == "menu":
            self.menu.draw(self.screen)

    @abc.abstractmethod
    def start_enemy_turn(self):
        """ Logica del turno del enemigo"""

    @abc.abstractmethod
    def update_logic(self, dt):
        """ Logica de combate especifica del enemigo"""
        pass

    @abc.abstractmethod
    def draw_enemy (self):
        """ Dibuja el enemigo"""

    @abc.abstractmethod
    def draw_enemy_attack(self):
        """ Dibuja patron de ataque del enemigo"""
