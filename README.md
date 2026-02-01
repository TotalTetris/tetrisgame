# tetrisgame

This is a TetrisGame

A simple, modular implementation of the classic **Tetris** game written in Python.  
The project focuses on clear separation of responsibilities between game logic, board representation, and rendering, making it suitable for learning, extension, and experimentation.

---

## Project Structure

```text
tetrisgame/
├─ src/
│  └─ tetrisgame/
│     ├─ __init__.py        
│     ├─ main.py            
│     ├─ board.py           
│     ├─ cubes.py           
│     └─ config.py
└─ README.md                
```

---

## Core Design

The game is structured around three main concepts:

### 1. Cube (`cubes.py`)
- The smallest unit of the game board.
- Each cube has:
  - A grid coordinate `(x, y)`
  - A color (default: black, meaning empty)
  - A lock state for collision detection
- Cubes are reused to represent both empty cells and occupied blocks.

### 2. Board (`board.py`)
- The board is a 2D grid composed of `Cube` objects.
- Responsibilities:
  - Managing the game grid
  - Detecting collisions and boundaries
  - Clearing completed lines
  - Rendering the fixed (locked) blocks

### 3. Game Loop (`main.py`)
- Controls overall game flow.
- Responsibilities:
  - Spawning and updating the current falling piece
  - Handling user input (movement, rotation, hard drop)
  - Automatic falling based on time
  - Locking pieces and triggering line clears
  - Calling draw functions to render the game state

---

## Configuration (`config.py`)

All global constants are defined in one place, such as:
- Board width and height
- Cube size
- Colors
- Screen dimensions
- Timing parameters (fall speed, delays)

This makes the game easy to tune without touching core logic.

---

## Key Features

- Modular, readable code structure
- Clear separation between data (cube/board) and control (game loop)
- Line clearing and collision detection
- Automatic falling and hard drop mechanics
- Easily extendable (scoring, next piece preview, hold piece, etc.)

---

## How to Run

1. Ensure you have Python 3 installed.
2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Run the game from the package directory:
   ```bash
   cd src/tetrisgame
   python main.py
   ```

---

## What's Next?

- Add a start screen.
- Add pause/resume.
- Add a preview for the next piece.
- Add speed up with time.
- ......

