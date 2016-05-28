import pygame
import globals


def update_display_mode():
    if(globals.fullscreen):
        # if fullscreen is True
        globals.window = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT), pygame.FULLSCREEN)
    else:
        # if fullscreen is False
        globals.window = globals.pygame.display.set_mode(
            (globals.WIDTH, globals.HEIGHT))


def toggle_fullscreen():
    # flip the global fullscreen boolean
    globals.fullscreen = not globals.fullscreen
    # update the display mode, which will apply our toggle
    update_display_mode()
