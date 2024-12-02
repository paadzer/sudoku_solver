def solve_sudoku(board):
    """
    Solves a Sudoku puzzle and returns the solution or raises ValueError if unsolvable or invalid input.

    Args:
    board (list of list of int): The Sudoku board represented as a 9x9 grid of integers.
                                 Empty cells are represented by 0s.

    Returns:
    list of list of int or None: The solved Sudoku board, or raises ValueError if unsolvable or invalid input.
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

    def is_initial_board_valid():
        # Check for duplicates in rows, columns, and 3x3 grids
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != 0:
                    board[row][col] = 0  # Temporarily clear the cell
                    if not is_valid(row, col, num):
                        return False
                    board[row][col] = num  # Restore the cell
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

    # Input validation
    if len(board) != 9 or any(len(row) != 9 for row in board):
        raise ValueError("Invalid board size")
    if any(num not in range(10) for row in board for num in row):
        raise ValueError("Invalid number in board")
    if not is_initial_board_valid():
        raise ValueError("Invalid initial board configuration")

    if not solve():
        raise ValueError("Puzzle is unsolvable")
    return board
