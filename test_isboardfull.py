import unittest
from game import is_board_full


class TestTicTacToe(unittest.TestCase):

    def test_board_is_full(self):
        board = [['X', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', 'X']]
        self.assertTrue(is_board_full(board))

    def test_board_is_not_full(self):
        board = [['X', ' ', ' '],
                 [' ', 'O', ' '],
                 [' ', ' ', ' ']]
        self.assertFalse(is_board_full(board))


if __name__ == '__main__':
    unittest.main()