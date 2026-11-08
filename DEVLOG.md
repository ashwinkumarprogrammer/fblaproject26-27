# Dev Log

## Phase 1: Skeleton
**Built:** A 1280x720 window, a game loop at 60 FPS, ESC to quit (checked in the main loop so it works on every screen), a blank placeholder screen ("state"), `resource_path()` for PyInstaller, and `requirements.txt`.

**Tools and why:** Python 3.12 and pygame-ce (required by our rules). We run the game from source with `python main.py` so there is no build step to break.

**Could be improved:** Add a real state manager (switch between screens) in Phase 3 when the title screen arrives.
