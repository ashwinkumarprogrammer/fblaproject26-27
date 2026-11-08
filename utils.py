# utils.py
# Small helper functions that many files use.

import os
import sys


def resource_path(relative_path):
    """Return the real location of a game file (sound, font, image).

    Why we need this: when the game is a normal Python script, files are
    next to our code. When it is packed into a PyInstaller .exe, files are
    unpacked into a temporary folder, and PyInstaller tells us where in
    sys._MEIPASS. This function works in both cases, on Mac and Windows.
    """
    # sys._MEIPASS only exists inside a PyInstaller build. If it is missing,
    # we are running normally, so we use the folder this file is in.
    base_folder = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_folder, relative_path)
