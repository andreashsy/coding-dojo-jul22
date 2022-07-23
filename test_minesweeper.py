from multiprocessing.sharedctypes import Value
from minesweeper import return_board, find_neighbour
import pytest

def test_can_initialise_return_board_function():
    assert return_board

def test_return_board_returns_correct_values():
    assert return_board([3, 2], [['.', '*', '.'], ['.', '.', '.']]) == [['1', '*', '1'], ['1', '1', '1']]


def test_can_initialise_find_neighbour_function():
    assert find_neighbour

def test_find_neighbour_incomplete_matrix_throws_error():
    with pytest.raises(ValueError):
        find_neighbour([['.'],['.', '.']], 0, 0)

def test_find_neighbour_row_out_of_bounds_throws_error():
    with pytest.raises(ValueError):
        find_neighbour([['.', '.'],['.', '.']], 5, 0)
# TODO: add min, max for row, cols

def test_find_neighbour_returns_correct_value():
    assert find_neighbour([['*', '.'],['.', '*']], 0, 1) == 2
    assert find_neighbour([['*', '.'],['.', '*']], 1, 0) == 2
    assert find_neighbour([['*', '.'],['.', '*']], 0, 0) == '*'
    assert find_neighbour([['*', '.'],['.', '*']], 1, 1) == '*'

