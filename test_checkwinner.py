import unittest
from game import check_winner

class testcheckwinner(unittest.TestCase):
        # Returns True if a player has three in a row horizontally
    def test_horizontal_winner(self):
        board = [['X', 'X', 'X'],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]
        result = check_winner(board, 'X')
        self.assertTrue(result)

        # Returns True if a player has three in a row vertically
    def test_vertical_winner(self):
        board = [['X', ' ', ' '],
                 ['X', ' ', ' '],
                 ['X', ' ', ' ']]
        result = check_winner(board, 'X')
        self.assertTrue(result)

        # Returns True if a player has three in a row diagonally from top left to bottom right
    def test_diagonal_winner(self):
        board = [['X', ' ', ' '],
                 [' ', 'X', ' '],
                 [' ', ' ', 'X']]
        result = check_winner(board, 'X')
        self.assertTrue(result)

        # Returns False if the board is empty
    def test_empty_board(self):
        board = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]
        result = check_winner(board, 'X')
        self.assertFalse(result)

        # Returns False if the board has only one player's mark
    def test_single_mark(self):
        board = [['X', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]
        result = check_winner(board, 'X')
        self.assertFalse(result)

        # Returns False if the board has two different player's marks in a row/column/diagonal
    def test_two_marks(self):
        board = [['X', 'O', 'X'],
                 [' ', 'O', ' '],
                 [' ', 'O', 'X']]
        result = check_winner(board, 'X')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()