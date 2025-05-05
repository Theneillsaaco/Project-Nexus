import pygame

from AppSetting import BATTLE_BOX_HEIGHT, BATTLE_BOX_Y, BATTLE_BOX_WIDTH


class BattleMenu:
    def __init__(self, options, font, spacing = 40):
        self.options = options
        self.font = font
        self.selected_index = 0
        self.spacing = spacing

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                self.selected_index = (self.selected_index + 1) % len(self.options)
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                self.selected_index = (self.selected_index - 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected_index]
        return None

    def draw(self, screen):
        menu_y = BATTLE_BOX_Y + BATTLE_BOX_HEIGHT + 60

        rendered_texts = []
        total_width = 0
        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected_index else (255, 255, 255)
            text_surface = self.font.render(option, True, color)
            rendered_texts.append(text_surface)
            total_width += text_surface.get_width()
            if i < len(self.options) - 1:
                total_width += self.spacing

        start_x = (screen.get_width() - total_width) // 2

        x = start_x
        for i, surface in enumerate(rendered_texts):
            screen.blit(surface, (x, menu_y))
            if i == self.selected_index:
                # Arrow under selected option
                arrow = self.font.render("^", True, (255, 255, 0))
                arrow_x = x + (surface.get_width() - arrow.get_width()) // 2
                arrow_y = menu_y + surface.get_height() + 5
                screen.blit(arrow, (arrow_x, arrow_y))
            x += surface.get_width() + self.spacing