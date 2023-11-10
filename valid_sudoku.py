from typing import List

# Valid Sudoku (Medium)
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

def valid_square(board, offx=0, offy=0):
    bitmask = 0x0
    for i in range(3):
        for j in range(3):
            value = board[offx * 3 + i][offy * 3 + j]
            if value == '.':
                continue
            elif bitmask & 1 << int(value):
                return False
            bitmask |= 1 << int(value)

    return True

# n = sudoku board row/col length
# Time complexity: O(nˆ2) - we iterate over each cell thrice and do O(1) operation
# Space complexity: O(1) - we use only single bitmask
def isValidSudoku(board: List[List[str]]) -> bool:
    rows, cols = len(board), len(board[0])

    # Verify each row O(k)
    for i in range(rows):
        bitmask = 0x0
        for value in board[i]:
            if value == '.':
                continue
            elif bitmask & 1 << int(value):
                return False
            bitmask |= 1 << int(value)

    # Verify each column
    for j in range(cols):
        bitmask = 0x0
        for i in range(rows):
            value = board[i][j]
            if value == '.':
                continue
            elif bitmask & 1 << int(value):
                return False
            bitmask |= 1 << int(value)

    # Verify each sudoku square
    for i in range(3):
        for j in range(3):
            if not valid_square(board, offx=i, offy=j):
                return False

    return True



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
    res = isValidSudoku(board)
    assert res == True

    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]
    res = isValidSudoku(board)
    assert res == False
