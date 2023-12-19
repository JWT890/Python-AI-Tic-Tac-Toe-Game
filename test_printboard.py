import unittest
from game import print_board

class TestPrintBoard(unittest.TestCase):
    def test_print_board(self):
        board = [['X', 'O', ' '], [' ', 'X', 'O'], ['O', ' ', 'X']]
        expected_output = """
---------
 | X | O |  |
---------
 |  | X | O |
---------
 | O |  | X |
---------
"""

if __name__ == '__main__':
    unittest.main()