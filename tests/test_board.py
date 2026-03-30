import numpy as np
import pytest

from src.tetrisgame.config import (Constants)
from src.tetrisgame.board import Board


@pytest.fixture
def arbitrary_board():
    """Create an arbitrary/fictitious board for testing."""
    return Board(Constants.COLS, Constants.ROWS, Constants.BLOCK_SIZE)


def test_clear_lines_board(arbitrary_board):
    """Tests if the clearing the lines of the board functions."""
    board_1 = arbitrary_board
    board_2 = arbitrary_board.clear_lines()
    assert board_1 != board_2


@pytest.mark.parametrize(
    "columns, rows, block_sizes",
    [
        (15, 30, 40),
        (50, 40, 3),
        (1000, 1000, 10)
    ]
)
def test_different_boards(columns, rows, block_sizes, arbitrary_board):
    """Test the creation of boards with various parameters."""
    board = Board(columns, rows, block_sizes)
    assert type(arbitrary_board.grid) == type(board.grid)
