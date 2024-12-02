def solve_sudoku(board):
    """
    Solves a Sudoku puzzle and returns the solution or None if unsolvable.
    
    Args:
    board (list of list of int): The Sudoku board represented as a 9x9 grid of integers.
                                 Empty cells are represented by 0s.
    
    Returns:
    list of list of int or None: The solved Sudoku board, or None if unsolvable.
    """
    def is_valid(row, col, num):
        for x in range(9):
            if board[row][x] == num or board[x][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(row, col, num):
                            board[row][col] = num
                            if solve():
                                return True
                            board[row][col] = 0
                    return False
        return True

    if not solve():
        return None  # Instead of raising an error, return None
    return board
