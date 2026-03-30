import pytest

from random import randint
from src.tetrisgame.board import Board
from src.tetrisgame.config import (Shapes, Colors, Constants)
from src.tetrisgame.tetromino import (Tetromino)


@pytest.fixture
def arbitrary_board():
    """Create an arbitrary/fictitious board for testing."""
    return Board(Constants.COLS, Constants.ROWS, Constants.BLOCK_SIZE)


@pytest.fixture
def tetromino_dummy(arbitrary_board):
    """Create a dummy tetromino on the arbitrary board."""
    return Tetromino(shape=Shapes.I, color=Colors.RED, board=arbitrary_board)


def test_tetromino_creation(tetromino_dummy):
    """Tests that the creation of the tetromino is done correctly."""
    assert tetromino_dummy.shape == Shapes.I
    assert tetromino_dummy.color == Colors.RED


def test_tetromino_rotation(tetromino_dummy, arbitrary_board):
    """Tests that the rotated Tetromino is not the same as the original."""
    original_tetromino = tetromino_dummy.shape
    tetromino_dummy.rotate(arbitrary_board)
    rotated_tetromino = tetromino_dummy.shape

    assert rotated_tetromino != original_tetromino


def test_tetromino_move(tetromino_dummy, arbitrary_board):
    """Tests that the moved Tetromino is not in the same position on the board as an original tetromino."""
    original_x = tetromino_dummy.x
    original_y = tetromino_dummy.y
    tetromino_dummy.move(dx=randint(2, 5), dy=randint(2, 7), board=arbitrary_board)
    new_x = tetromino_dummy.x
    new_y = tetromino_dummy.y
    assert original_x != new_x
    assert original_y != new_y


@pytest.mark.parametrize("shape", [Shapes.I, Shapes.J, Shapes.L, Shapes.O])
def test_all_shapes(shape, arbitrary_board):
    """Tests the initialization of multiple shapes."""
    tetromino = Tetromino(shape=shape, color=Colors.RED, board=arbitrary_board)
    assert tetromino.shape == shape
