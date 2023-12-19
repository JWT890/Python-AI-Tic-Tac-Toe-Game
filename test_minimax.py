import unittest
from game import minimax, check_winner, get_empty_cells, is_board_full, get_best_move

class TestTicTacToe(unittest.TestCase):

    def test_check_winner_row_win(self):
        board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(check_winner(board, 'X'))

    def test_check_winner_col_win(self):
        board = [[' ', ' ', ' '], ['X', 'X', ' '], [' ', ' ', 'X']]
        self.assertTrue(check_winner(board, 'X'))

    def test_check_winner_diag_win(self):
        board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertTrue(check_winner(board, 'X'))

    def test_check_winner_no_win(self):
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertFalse(check_winner(board, 'X'))

    def test_get_empty_cells(self):
        board = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        expected = [(0, 0), (1, 1), (2, 2)]
        self.assertEqual(get_empty_cells(board), expected)

    def test_is_board_full(self):
        board = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(is_board_full(board))

        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', 'X']]
        self.assertFalse(is_board_full(board))

    def test_get_best_move(self):
        board = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        expected = (0, 0)
        self.assertEqual(get_best_move(board), expected)

    def test_minimax_maximizing_player(self):
        board = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        expected = 0
        self.assertEqual(minimax(board, 0, True), expected)

    def test_minimax_minimizing_player(self):
        board = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        expected = -1
        self.assertEqual(minimax(board, 0, False), expected)

if __name__ == '__main__':
    unittest.main()