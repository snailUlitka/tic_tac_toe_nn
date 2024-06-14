# TODO: Write doc here
import pytest
from app.tic_tac_toe import TicTacToe, Figure


def test_empty_board():
    game = TicTacToe()
    assert not game.check_win()


def test_row_win():
    game = TicTacToe()
    game.game_field[0, 0] = Figure.CROSS
    game.game_field[0, 1] = Figure.CROSS
    game.game_field[0, 2] = Figure.CROSS
    assert game.check_win()


def test_column_win():
    game = TicTacToe()
    game.game_field[0, 0] = Figure.ZERO
    game.game_field[1, 0] = Figure.ZERO
    game.game_field[2, 0] = Figure.ZERO
    assert game.check_win()


def test_diagonal_win():
    game = TicTacToe()
    game.game_field[0, 0] = Figure.CROSS
    game.game_field[1, 1] = Figure.CROSS
    game.game_field[2, 2] = Figure.CROSS
    assert game.check_win()


def test_inverse_diagonal_win():
    game = TicTacToe()
    game.game_field[0, 2] = Figure.ZERO
    game.game_field[1, 1] = Figure.ZERO
    game.game_field[2, 0] = Figure.ZERO
    assert game.check_win()


def test_no_win_mixed_figures():
    game = TicTacToe()
    game.game_field[0, 0] = Figure.CROSS
    game.game_field[0, 1] = Figure.ZERO
    game.game_field[0, 2] = Figure.CROSS
    game.game_field[1, 0] = Figure.ZERO
    game.game_field[1, 1] = Figure.CROSS
    game.game_field[1, 2] = Figure.ZERO
    assert not game.check_win()
