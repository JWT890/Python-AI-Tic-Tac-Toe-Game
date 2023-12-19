import unittest
from game import get_empty_cells

class TestGetEmptyCells(unittest.TestCase):

    def test_empty_cells(self):
        board = [['X', 'O', ' '], [' ', ' ', ' '], [' ', ' ', 'O']]
        expected_cells = [(0, 0), (1, 1), (2, 2)]
        actual_cells = get_empty_cells(board)
        self.assertEqual(expected_cells, actual_cells)

    def test_non_empty_cells(self):
        board = [['X', 'O', 'X'], [' ', ' ', ' '], [' ', ' ', 'O']]
        expected_cells = []
        actual_cells = get_empty_cells(board)
        self.assertEqual(expected_cells, actual_cells)

    def test_no_empty_cells(self):
        board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['X', 'O', 'X']]
        expected_cells = []
        actual_cells = get_empty_cells(board)
        self.assertEqual(expected_cells, actual_cells)

    def test_all_cells_occupied(self):
        board = [['X', 'O', 'X'], ['X', 'O', ' '], ['X', 'O', 'O']]
        expected_cells = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 0), (1, 2), (2, 0)]
        actual_cells = get_empty_cells(board)
        self.assertEqual(expected_cells, actual_cells)

if __name__ == '__main__':
    unittest.main()