# states/blank_state.py
# A "state" is one screen of the game (title, match, result...).
# This blank one is only a placeholder so we can see the window works.
# Later phases will add real screens in this folder.

import settings


class BlankState:
    def handle_event(self, event):
        """Called for every key press or mouse click. Blank screen ignores them."""
        pass

    def update(self):
        """Called once per frame to move things. Nothing to move yet."""
        pass

    def draw(self, screen):
        """Called once per frame to paint the screen."""
        screen.fill(settings.COLOR_BACKGROUND)
