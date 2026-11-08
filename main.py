# main.py
# This is the file you run: `python main.py`
# It opens the window and runs the game loop. The loop repeats until we quit.

import sys
import pygame

import settings
from states.blank_state import BlankState


def main():
    # Start pygame and make the window.
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption(settings.WINDOW_TITLE)
    clock = pygame.time.Clock()

    # The "current state" is the screen being shown right now.
    # To change screens later, we just swap this variable.
    current_state = BlankState()

    is_running = True
    while is_running:
        # 1. Look at everything the player did since the last frame.
        for event in pygame.event.get():
            # Closing the window with the X button quits.
            if event.type == pygame.QUIT:
                is_running = False
            # ESC quits instantly. The check is here in the main loop,
            # so it works on every screen (hard rule #2).
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                is_running = False
            else:
                # Anything else goes to the current screen to handle.
                current_state.handle_event(event)

        # 2. Let the screen update, then 3. paint it.
        current_state.update()
        current_state.draw(screen)
        pygame.display.flip()  # show the finished frame

        # Wait so we run at about 60 frames per second.
        clock.tick(settings.FRAMES_PER_SECOND)

    pygame.quit()
    sys.exit()


main()
