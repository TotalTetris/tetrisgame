# Game constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
COLUMNS = SCREEN_WIDTH // BLOCK_SIZE
ROWS = SCREEN_HEIGHT // BLOCK_SIZE
FPS = 60

# Colors (R, G, B)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)


class Colors:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]


def index_to_colour(colour_index) -> tuple[int, int, int]:
    """Converts index to RGB tuple."""

    colours = {
        0: BLACK,
        1: GRAY,
        2: WHITE,
        3: CYAN,
        4: BLUE,
        5: ORANGE,
        6: YELLOW,
        7: GREEN,
        8: PURPLE,
        9: RED
    }

    return colours[colour_index]


def colour_to_index(colour) -> int:
    """Converts RGB tuple to index."""

    colours = {
        BLACK: 0,
        GRAY: 1,
        WHITE: 2,
        CYAN: 3,
        BLUE: 4,
        ORANGE: 5,
        YELLOW: 6,
        GREEN: 7,
        PURPLE: 8,
        RED: 9
    }

    return colours[colour]
