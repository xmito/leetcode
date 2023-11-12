from typing import List

# Sudoku Solver (Hard)
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.

# Time complexity: n!ˆn - n is fixed == 9 and we have 9! permutations for each row
# Space complexity: O(n) - we have bitmask for each row, column and square
def solveSudoku(board: List[List[str]]) -> None:
    def solve(board, x, y):
        
        # Find first position with missing value
        while x < 9 and y < 9 and board[x][y] != '.':
            x += y // 8
            y = (y + 1) % 9

        # Base case, we have solution
        if x == 9:
            return True

        sq_x, sq_y = x // 3, y // 3
        mask = row_mask[x] | col_mask[y] | sq_mask[sq_x][sq_y]
        mask = ~mask & (2**10 - 1)
        for value in range(1, 10):
            if 1 << value & mask:
                board[x][y] = str(value)
                row_mask[x] |= 1 << value
                col_mask[y] |= 1 << value
                sq_mask[sq_x][sq_y] |= 1 << value

                if solve(board, x, y):
                    return True

                board[x][y] = '.'
                row_mask[x] &= ~(1 << value)
                col_mask[y] &= ~(1 << value)
                sq_mask[sq_x][sq_y] &= ~(1 << value)

        # No value can be placed at this position
        return False

    row_mask = [0] * 9
    col_mask = [0] * 9
    sq_mask = [[0] * 3 for _ in range(3)]

    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue

            row_mask[i] |= 1 << int(board[i][j])
            col_mask[j] |= 1 << int(board[i][j])

            sq_x, sq_y = i // 3, j // 3
            sq_mask[sq_x][sq_y] |= 1 << int(board[i][j])
        
    return solve(board, 0, 0)



if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]
    solveSudoku(board)
    for line in board:
        print(line)

    assert board == [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"],
    ]
