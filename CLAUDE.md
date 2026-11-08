# Marvin Ridge Cricket Academy: Road to the Championship

FBLA 2026-2027 Computer Game & Simulation Programming (topic: "Road to the Championship").
Read `PLAN.md` for the full design and the build phases.

## Who we are
Two high school beginners. Ashwin codes on a Mac, Yuvan on Windows. We must explain every file to judges in a 3-minute Q&A, so code must be easy to read.

## Hard rules (never break)
1. Python 3.12 + `pygame-ce` only (imported as `import pygame`). No other game engines or extra libraries. `pyinstaller` is allowed for the final build.
2. Pressing ESC at any time instantly closes the game. The ESC check lives in the main loop and works on every screen.
3. Title screen has three buttons: **Play**, **Instructions**, **Quit**.
4. Five matches, getting harder, ending in the state final. Choices (training, events, tactics) change match results.
5. Every function and logic block gets heavy, beginner-friendly comments that say what it does and why. Use plain words.
6. Clear, descriptive variable names (`team_morale`, not `tm`).
7. Modular code: UI, match logic, game data and screens in separate files (see folder layout in `PLAN.md`).
8. Works on macOS and Windows. Use `os.path`/`pathlib`, never absolute paths, and load every file through `resource_path()` so the PyInstaller .exe works.
9. Offline only. No network calls. No audio or video through external speakers; sound comes from the laptop.
10. Original work only. No real student names, no logos. Every font, sound or image we use is listed in `CREDITS.md` with source and license.

## How to work with us
- Do **one phase at a time** from `PLAN.md`. When it is done, stop, tell us exactly how to run and test it, and wait.
- Do not change files outside the current phase without asking.
- After each phase, add an entry to `DEVLOG.md`: what we built, which tools we used and why, what could be improved. This feeds the judges' Implementation score.
- If we say "explain", explain in simple words with a real-life comparison.
- Do not run `git push`. We use GitHub Desktop.
- Keep each file short enough to read in a few minutes. Prefer simple code over clever code.
