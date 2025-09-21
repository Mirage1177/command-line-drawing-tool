# command-line-drawing-tool

A lightweight drawing application built with Pygame that lets you create shapes using typed commands in the terminal. Designed for simplicity, responsiveness, and extensibility — no GUI required.

## Features

- 🖌️ Draw lines, circles, and polygons with custom size and color
- 💬 Command-driven interface — type instructions like `draw line 10 10 100 100`
- 🧠 Simple command registry for easy extension
- 💾 Save your drawing as `draw.png` with `end drawing`
- 🧼 Clean and minimal codebase — no threading or external libraries

## Commands

| Command            | Description                                  | Example                            |
|--------------------|----------------------------------------------|------------------------------------|
| `change size N`    | Set line thickness to `N`                    | `change size 3`                    |
| `change color R G B` | Set drawing color (RGB values 0–255)       | `change color 255 0 0`             |
| `draw line x1 y1 x2 y2` | Draw a line from `(x1, y1)` to `(x2, y2)` | `draw line 10 10 100 100`          |
| `draw circle x y r` | Draw a circle at `(x, y)` with radius `r`   | `draw circle 150 150 40`           |
| `draw polygon x1 y1 x2 y2 ...` | Draw a polygon with given vertices | `draw polygon 50 50 100 50 75 100` |
| `end drawing`      | Save the canvas to `draw.png` and exit       | `end drawing`                      |

## How to Run

1. Make sure you have Python and Pygame installed:
```bash
pip install pygame
```
2.Run the script in a terminal (not inside the Pygame window):
```bash
python draw.py
```
Type commands directly into the terminal. The Pygame window will stay open and update as you draw.
you can see the result of your work at the draw.png that you created with 'end drawing' command.
   ```bash
   pip install pygame
