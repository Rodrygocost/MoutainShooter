import sys
from code.Const import C_WHITE, WIND_HEIGHT, FPS_HEIGHT

import pygame
from pygame import Surface

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            # Evento de saída
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()

            clock.tick(60)


            # printed text
            self.level_text(
                text_size=14,
                text=f'FPS: {clock.get_fps():.0f}',
                text_color=C_WHITE,
                text_pos=(10, FPS_HEIGHT - 35)
            )


        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
            pygame.font.init()
            text_font = pygame.font.SysFont('Lucida Sans Typewriter', text_size)
            text_surf = text_font.render(text, True, text_color).convert_alpha()
            text_rect = text_surf.get_rect(topleft=text_pos)
            self.window.blit(text_surf, text_rect)
            pygame.display.flip()
