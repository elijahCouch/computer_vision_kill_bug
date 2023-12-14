import pygame

WINDOW_NAME = "FLOSSIE"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 2000, 1200

FPS = 90
DRAW_FPS = True

BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
MOSQUITOS_SIZES = (50, 38)
MOSQUITO_SIZE_RANDOMIZE = (1,2)
BEE_SIZES = (50, 50)
BEE_SIZE_RANDOMIZE = (1.2, 1.5)

DRAW_HITBOX = False # will draw all the hitbox


ANIMATION_SPEED = 0.08

GAME_DURATION = 600000
MOSQUITOS_SPAWN_TIME = 1
MOSQUITOS_MOVE_SPEED = {"min": 1, "max": 5}



COLORS = {"title": (38, 61, 39), "score": (38, 61, 39), "timer": (38, 61, 39),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)}}


MUSIC_VOLUME = 0.16
SOUNDS_VOLUME = 1

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
