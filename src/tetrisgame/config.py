"""TODO"""

SHAPES = [
    # I
    [
        "....",
        "XXXX",
        "....",
        "....",
    ],
    # J
    [
        "....",
        ".X..",
        ".XXX",
        "....",
    ],
    # L
    [
        "....",
        "...X",
        ".XXX",
        "....",
    ],
    # O
    [
        "....",
        ".XX.",
        ".XX.",
        "....",
    ],
    # S
    [
        "....",
        ".XX.",
        "XX..",
        "....",
    ],
    # Z
    [
        "....",
        "XX..",
        ".XX.",
        "....",
    ],
    # T
    [
        "....",
        ".X..",
        "XXX.",
        "....",
    ],
]


# TODO: this could be a class
class Colors:
    """Store color values."""

    WHITE = (255, 255, 255)
    ...


class Text:
    """Store displayed text."""

    SCORE_TEMPLATE = "Score: {score}"
    GAME_OVER = "Game Over"


COLORS = [
    (0, 255, 255),  # I - cyan
    (0, 0, 255),  # J - blue
    (255, 165, 0),  # L - orange
    (255, 255, 0),  # O - yellow
    (0, 255, 0),  # S - green
    (255, 0, 0),  # Z - red
    (160, 32, 240),  # T - purple
]
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)

COLS = 10
ROWS = 20
BLOCK_SIZE = 30

FALL_INTERVAL = 500  # milliseconds
