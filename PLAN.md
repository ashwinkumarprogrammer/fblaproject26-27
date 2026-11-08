# PLAN: Marvin Ridge Cricket Academy: Road to the Championship

Build order is at the bottom. Rules are in `CLAUDE.md`.

## 1. Concept
The player is head coach of the Marvin Ridge High School cricket team. Over one season they recruit and train players, manage morale, fitness and money, survive random events, and choose tactics in each match to win the state championship. Everything is button-driven (no real-time reflex gameplay).

## 2. Season structure
| Phase | Details |
|---|---|
| Preseason | Pick 2 recruits from 5 tryout candidates (limited budget) to join 4 core players |
| Weeks 1-3 (league) | vs Weddington, Ardrey Kell, Providence. Need 2 wins of 3 to make the playoffs. League record sets seed (a small home bonus) |
| Week 4 | Semifinal vs Myers Park (single elimination) |
| Week 5 | State Final vs Green Level (single elimination) |

Opponent teams are fictionalized: no logos, no real students. Each week flows: **Management menu -> Random event -> Scouting + lineup -> Match -> Result**.

Opponent ratings (starting values, tune later): Weddington 45, Ardrey Kell 55, Providence 65, Myers Park 72, Green Level 80.

### Endings (6)
Champion, Runner-Up, Semifinal Exit, Missed Playoffs, Dynasty (champion with morale > 80 and budget > $500), Fired (morale reaches 0). Each has its own screen plus a season report card (score and charts of player growth).

## 3. Data
- **Team:** `team_morale` (0-100), `team_fitness` (0-100), `team_budget` ($0-1000, start $500), `season_score`
- **Player:** `name` (fictional), `role`, `batting`, `bowling`, `fielding` (1-100), `form` (cold / normal / hot), `hidden_potential` (revealed by scouting)
- **Squad:** 4 core players (Opening Batsman, Spin Bowler, Fast Bowler, All-Rounder) + 2 recruits, bench up to 8. Six play each match.
- **Opponent:** `team_rating`, `strength` (e.g. bat-heavy, spin-weak), `pitch_type`

## 4. Weekly management (3 Training Points per week)
| Action | Effect |
|---|---|
| Net Practice (pick player + skill) | +5 to that skill, -5 fitness |
| Gym Conditioning | +10 fitness, -2 morale |
| Team Bonding | +10 morale, -$50 |
| Scout Opponent | -$100, reveals weakness and pitch type |
| Scout Talent | -$200, reveals a player's potential or adds a bench recruit |
| Fundraiser | +$150, -3 morale |
| Physio / Rest | restore fitness, fix minor injury, -$75 |

Fitness below 40 applies a stat penalty in matches. Morale acts as a "clutch" modifier in the last 2 overs. Winning a match earns a sponsor bonus.

## 5. Random events (one per week, no repeats)
Each has 2-3 choices with trade-offs; some have a risk roll. Start with 12: star player injured, rival poaches a player, rainy week, sponsor offer, viral highlight, exam week, equipment breaks, captain conflict, heat wave, parent fundraiser, local news feature, controversial umpire call. Store them in `data/events_data.py` as plain Python lists so a teammate can add events without touching logic.

## 6. Match engine
5 overs per innings (30 balls), 5 wickets. Both innings are played. Pitch type (spin-friendly / pace-friendly / flat) comes from the scouting report. Pre-match: choose the batting order (top 6) and bat-or-bowl.

**Batting, each ball:** choose Defensive, Balanced or Aggressive. Starting outcome probabilities (%), to tune with the simulator:

| Shot | Dot | 1 | 2 | 4 | 6 | Wicket |
|---|---|---|---|---|---|---|
| Defensive | 40 | 35 | 15 | 5 | 2 | 3 |
| Balanced | 25 | 30 | 12 | 16 | 8 | 9 |
| Aggressive | 18 | 15 | 5 | 24 | 20 | 18 |

The batter's edge over the bowler (rating difference, adjusted by form, fitness and pitch) shifts a few percentage points from dots and wickets toward boundaries, or the reverse.

**Bowling, each over:** choose a bowler (max 2 overs each) and an approach: Attack, Contain, or Pitch Plan (rewarded when it matches the pitch and the opponent's weakness). Fielding rating lowers opponent runs.

**Coach tools, once per match:** Timeout (temporary morale boost) and Powerplay (boundaries more likely for one over).

**Commentary:** one generated text line per ball.

All outcome math lives in one function, `resolve_ball(...)`, in `logic/match_engine.py`, so it can be tested and tuned alone.

## 7. Look, sound, accessibility
- Window 1280x720. One color palette and one font family everywhere. A consistent pixel-style look drawn with Pygame shapes and small hand-made sprites (no copyrighted art).
- Screens: title, instructions, recruit, weekly menu, event, pre-match, match, result, season end.
- Sound effects (CC0 only) for click, bat hit, crowd, win, lose. A mute button on every screen.
- Accessibility: colorblind-safe palette, high-contrast text, font-size toggle, keyboard shortcuts (1/2/3 for tactics), hover and click feedback on every button.
- Instructions screen explains the rules, states that opponents are fictional, and every button has a short tooltip.

## 8. Folder layout
```
main.py                # game loop, state manager, ESC check
settings.py            # constants, colors, screen size
game_state.py          # Team, Player, Opponent classes
utils.py               # resource_path()
states/                # title, instructions, recruit, weekly_menu, event, prematch, match, result, season_end
logic/                 # match_engine, training, events, recruiting, opponents
ui/                    # button, panel, text helpers, theme
data/                  # events_data, names, opponents_data
tools/simulate.py      # runs 1000 seasons to balance difficulty
assets/                # sounds, fonts
CREDITS.md  DEVLOG.md  README.md  requirements.txt
```

## 9. Build phases (do one at a time; stop after each)
1. **Skeleton:** window, state manager, ESC listener, `resource_path()`, `requirements.txt`. *Done when:* a blank window opens and ESC closes it on Mac and Windows.
2. **UI toolkit:** Button, Panel, text drawing, theme colors, hover and click feedback. *Done when:* a demo screen shows working buttons.
3. **Title + Instructions:** Play / Instructions / Quit. *Done when:* every button works and Quit exits.
4. **Data models:** Team, Player, Opponent, starting squad, opponent list. *Done when:* a test script prints the squad.
5. **Recruiting:** preseason tryouts with budget. *Done when:* picking 2 recruits updates squad and budget.
6. **Weekly management:** 3 training points, all actions, stat changes. *Done when:* actions change the numbers correctly.
7. **Random events:** 12 events, choices, effects. *Done when:* a different event shows each week.
8. **Match engine (no UI):** `resolve_ball`, innings simulation, opponent AI, coach tools. *Done when:* a text-only test plays a full match.
9. **Match screens:** pre-match setup, ball-by-ball UI, scoreboard, commentary. *Done when:* a full match is playable with the mouse and 1/2/3 keys.
10. **Season flow + endings:** league, playoffs, 6 endings, report card. *Done when:* all 6 endings can be reached.
11. **Art and sound:** field, player cards, animations, effects, mute. *Done when:* the look is consistent and `CREDITS.md` is complete.
12. **Accessibility + settings:** palette, font size, shortcuts. *Done when:* the settings screen works.
13. **Balance simulator:** `tools/simulate.py`. *Target:* about 55% season wins with sensible play, about 10% with random clicks.
14. **Windows build (on Yuvan's PC):** PyInstaller one-file .exe, tested with Wi-Fi off on a different computer.
15. **Docs:** finish `README.md`, `DEVLOG.md`, `CREDITS.md`.

Must-have: phases 1-10 and 14. Polish: 11-13.

## 10. FBLA rubric checklist
- Concept covers recruit, develop, practices, resources, morale, unexpected challenges, strategy
- Rules clear in the Instructions screen
- Multiple outcomes (6 endings) and a challenge that is winnable
- Innovation: scouting + pitch plan, clutch morale, commentary, balance simulator
- Implementation can be explained: tools, why we chose them, evaluation, future improvements (`DEVLOG.md`)
- Graphics and audio consistent and documented
- Title screen, accessible controls, intuitive buttons
- Fully offline, runs on one laptop
