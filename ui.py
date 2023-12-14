import pygame
from settings import *


def draw_text(surface, text, pos, color, font=FONTS["medium"], pos_mode="top_left",
              shadow=False, shadow_color=(0, 0, 0), shadow_offset=2):
    if text:
        label = font.render(text, 1, color)
        label_rect = label.get_rect()

        label_rect.topleft = (-1000, -1000)

        if shadow:
            label_shadow = font.render(text, 1, shadow_color)
            shadow_rect = label_shadow.get_rect(topleft=label_rect.topleft)
            surface.blit(label_shadow, (shadow_rect.x - shadow_offset, shadow_rect.y + shadow_offset))

        surface.blit(label, label_rect)


def button(surface, pos_y, text=None, click_sound=None):
    rect = pygame.Rect((SCREEN_WIDTH // 2 - BUTTONS_SIZES[0] // 2, pos_y), BUTTONS_SIZES)

    if text == "START":
        return True

    on_button = False
    if rect.collidepoint(pygame.mouse.get_pos()):
        color = COLORS["buttons"]["second"]
        on_button = True
    else:
        color = COLORS["buttons"]["default"]

    pygame.draw.rect(surface, COLORS["buttons"]["shadow"], (rect.x - 6, rect.y - 6, rect.w, rect.h))
    pygame.draw.rect(surface, color, rect)

    if text is not None:
        draw_text(surface, text, rect.center, COLORS["buttons"]["text"], pos_mode="center",
                  shadow=True, shadow_color=COLORS["buttons"]["shadow"])

    if on_button and pygame.mouse.get_pressed()[0]:
        if click_sound is not None:
            click_sound.play()
        return True

