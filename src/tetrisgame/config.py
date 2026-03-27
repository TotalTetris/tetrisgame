"""Configuration File"""


class Shapes:
    """Store the shapes of the Tetrominos."""

    I = [
        "....",
        "XXXX",
        "....",
        "....",
    ]
    J = [
        "....",
        ".X..",
        ".XXX",
        "....",
    ]
    L = [
        "....",
        "...X",
        ".XXX",
        "....",
    ]
    O = [
        "....",
        ".XX.",
        ".XX.",
        "....",
    ]
    S = [
        "....",
        ".XX.",
        "XX..",
        "....",
    ]
    Z = [
        "....",
        "XX..",
        ".XX.",
        "....",
    ]
    T = [
        "....",
        ".X..",
        "XXX.",
        "....",
    ]

    SHAPES = [
        I, J, L, O, S, Z, T
    ]


class Colors:
    """Store color values."""

    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    PURPLE = (160, 32, 240)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (40, 40, 40)

    COLORS = [
        CYAN, BLUE, ORANGE, YELLOW, GREEN, RED, PURPLE
    ]


class Text:
    """Store text for the game."""

    CAPTION = "Tetris"
    GAME_OVER = "Game Over"
    RESTART_MESSAGE = "Press R to restart"

    @staticmethod
    def score(score: int | float):
        """Returns the score format."""
        return f"Score: {score}"


class Constants:
    """Store game constants."""

    COLS = 10
    ROWS = 20
    BLOCK_SIZE = 30

    FALL_INTERVAL = 500  # milliseconds

    GAME_FONT = "monospace"
