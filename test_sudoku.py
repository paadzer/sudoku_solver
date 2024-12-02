import unittest
from sudoku import solve_sudoku

class TestSudokuSolver(unittest.TestCase):
    def test_valid_puzzle_1(self):
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        solved = solve_sudoku(board)
        self.assertIsNotNone(solved)  # checks if the board is solved, not None
        self.assertEqual(len(solved), 9)  # check if the board still has 9 rows
        self.assertTrue(all(len(row) == 9 for row in solved))  # check all rows have 9 columns

    def test_invalid_input_size(self):
        # testing a board that is not 9x9
        board = [[0]*10]*10  # 10x10 grid
        with self.assertRaises(ValueError):
            solve_sudoku(board)

    def test_invalid_input_numbers(self):
        # testing a board with invalid numbers (e.g -1 or 10)
        board = [[-1]*9]*9
        with self.assertRaises(ValueError):
            solve_sudoku(board)

    def test_unsolvable_puzzle(self):
        # unsolvable puzzle
        board = [
            [5, 1, 6, 8, 4, 9, 7, 3, 2],
            [3, 2, 7, 6, 1, 5, 4, 8, 9],
            [8, 9, 4, 2, 3, 7, 5, 1, 6],
            [1, 5, 3, 4, 6, 8, 9, 2, 7],
            [4, 7, 2, 5, 9, 1, 3, 6, 8],
            [9, 6, 8, 3, 7, 2, 1, 5, 4],
            [2, 8, 9, 7, 5, 3, 6, 4, 1],
            [6, 3, 5, 1, 8, 4, 2, 9, 7],
            [7, 4, 1, 9, 2, 6, 8, 3, 5]  
        ]
        with self.assertRaises(ValueError):
            solve_sudoku(board)

    def test_empty_puzzle(self):
        # empty Sudoku board
        board = [[0]*9]*9
        solved = solve_sudoku(board)
        self.assertIsNotNone(solved)
        self.assertTrue(all(all(num != 0 for num in row) for row in solved))  # check if all cells are filled

    def test_almost_complete_puzzle(self):
        # puzzle that is nearly complete
        board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]  
        ]
        board[8][8] = 0  # make the last cell empty
        solved = solve_sudoku(board)
        self.assertIsNotNone(solved)
        self.assertEqual(solved[8][8], 9)  # verify that the last cell is filled correctly

if __name__ == '__main__':
    unittest.main()
